from __future__ import annotations

import gc
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import torch

from repairable_diffusion.src.utils.io import load_yaml, save_json
from repairable_diffusion.src.v2.backends import create_v2_backend
from repairable_diffusion.src.v2.contracts import deterministic_branch_seed, validate_contract_dict
from repairable_diffusion.src.v2.task_adapters import create_task_adapter


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "repairable_diffusion/configs/v2/measurement_contract.yaml"
PROFILES = ROOT / "repairable_diffusion/configs/model_profiles.yaml"
READINESS = ROOT / "results/v2_measurement/readiness/backend_validation.json"

VALIDATION_CONFIGS = [
    ROOT / "repairable_diffusion/configs/v2/runs/full_math500_llada.yaml",
    ROOT / "repairable_diffusion/configs/v2/runs/full_math500_dream.yaml",
]


def _git_sha() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def _profile(name: str) -> dict[str, Any]:
    payload = load_yaml(PROFILES)
    return dict(payload["models"][name]["backend"])


def _validation_item(adapter: Any, dataset_cfg: dict[str, Any]) -> dict[str, Any]:
    cfg = dict(dataset_cfg)
    cfg["limit"] = 1
    cfg["sample_seed"] = 424242
    return adapter.load_records(cfg)[0]


def _selected_snapshots(record: dict[str, Any]) -> list[dict[str, Any]]:
    rows = [
        step for step in record["steps"]
        if step.get("snapshot") is not None and float(step.get("masked_ratio", 0.0)) > 0.0
    ]
    if not rows:
        raise RuntimeError("no nonterminal snapshot available for replay validation")
    if len(rows) == 1:
        return rows
    return [rows[0], rows[len(rows) // 2]]


def _validate_one(config_path: Path, contract: dict[str, Any]) -> dict[str, Any]:
    cfg = load_yaml(config_path)
    adapter = create_task_adapter(cfg["dataset"])
    backend = create_v2_backend(_profile(str(cfg["model_profile"])), adapter)
    item = _validation_item(adapter, cfg["dataset"])
    generation_cfg = dict(cfg["generation"])
    generation_cfg["trajectories_per_item"] = 1
    record = backend.generate_trajectory_v2(item, 0, generation_cfg)

    operator_cfg = dict(contract["canonical_operator"])
    operator_cfg["anchor_confidence_threshold"] = float(cfg.get("operator", {}).get("anchor_confidence_threshold", 0.80))
    operator_cfg.update(cfg.get("operator", {}))
    root_seed = int(cfg.get("probe", {}).get("root_seed", 2027))

    checks = []
    for step in _selected_snapshots(record):
        snapshot = step["snapshot"]
        branch_seed = deterministic_branch_seed(
            root_seed=root_seed,
            item_id=int(record["item_id"]),
            trajectory_id=int(record["trajectory_id"]),
            step_index=int(step["step_index"]),
            branch_index=0,
            stage="localization",
        )
        exact = backend.run_operator_branch(
            item,
            snapshot,
            generation_cfg,
            operator_cfg,
            operator_id="native_continuation",
            branch_seed=branch_seed,
        )
        exact_match = exact.get("final_text") == record.get("final_text") and exact.get("final_answer") == record.get("final_answer")
        if not exact_match:
            raise RuntimeError(
                f"native replay mismatch backend={backend.backend_type} step={step['step_index']}"
            )

        stochastic_a = backend.run_operator_branch(
            item,
            snapshot,
            generation_cfg,
            operator_cfg,
            operator_id="matched_stochastic_continuation",
            branch_seed=branch_seed,
        )
        stochastic_b = backend.run_operator_branch(
            item,
            snapshot,
            generation_cfg,
            operator_cfg,
            operator_id="matched_stochastic_continuation",
            branch_seed=branch_seed,
        )
        same_seed_match = (
            stochastic_a.get("final_text") == stochastic_b.get("final_text")
            and stochastic_a.get("final_answer") == stochastic_b.get("final_answer")
            and stochastic_a.get("compute") == stochastic_b.get("compute")
        )
        if not same_seed_match:
            raise RuntimeError(
                f"same-seed continuation is not reproducible backend={backend.backend_type} step={step['step_index']}"
            )
        if int(stochastic_a.get("compute", {}).get("nfe", -1)) < 0:
            raise RuntimeError("negative/missing NFE in continuation validation")

        checks.append(
            {
                "step_index": int(step["step_index"]),
                "native_exact_replay": True,
                "same_seed_reproducible": True,
                "native_nfe": int(exact.get("compute", {}).get("nfe", 0)),
                "stochastic_nfe": int(stochastic_a.get("compute", {}).get("nfe", 0)),
            }
        )

    result = {
        "config": str(config_path.relative_to(ROOT)),
        "model_profile": cfg["model_profile"],
        "backend_type": backend.backend_type,
        "item_id": int(record["item_id"]),
        "checks": checks,
        "status": "PASS",
    }
    del backend
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    return result


def main() -> None:
    if not torch.cuda.is_available():
        raise SystemExit("V2 backend replay validation requires a CUDA worker")
    contract = load_yaml(CONTRACT)
    validate_contract_dict(contract)
    rows = []
    for path in VALIDATION_CONFIGS:
        print(f"[v2 validation] {path.relative_to(ROOT)}")
        rows.append(_validate_one(path, contract))
    payload = {
        "status": "PASS",
        "git_sha": _git_sha(),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "rows": rows,
    }
    READINESS.parent.mkdir(parents=True, exist_ok=True)
    save_json(READINESS, payload)
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
