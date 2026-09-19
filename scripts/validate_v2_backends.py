from __future__ import annotations

import argparse
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
from repairable_diffusion.src.v2.replay import replay_dream_next_state, replay_llada_next_state
from repairable_diffusion.src.v2.task_adapters import create_task_adapter


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "repairable_diffusion/configs/v2/measurement_contract.yaml"
PROFILES = ROOT / "repairable_diffusion/configs/model_profiles.yaml"
READINESS_ROOT = ROOT / "results/v2_measurement/readiness"
VALIDATION_CONFIGS = {
    "llada": ROOT / "repairable_diffusion/configs/v2/runs/full_math500_llada.yaml",
    "dream": ROOT / "repairable_diffusion/configs/v2/runs/full_math500_dream.yaml",
}


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


def _selected_transition_pairs(record: dict[str, Any]) -> list[tuple[dict[str, Any], dict[str, Any]]]:
    steps = record["steps"]
    pairs: list[tuple[dict[str, Any], dict[str, Any]]] = []
    for idx in range(len(steps) - 1):
        current = steps[idx]
        nxt = steps[idx + 1]
        if current.get("snapshot") is None or nxt.get("snapshot") is None:
            continue
        if float(current.get("masked_ratio", 0.0)) <= 0.0:
            continue
        pairs.append((current, nxt))
    if not pairs:
        raise RuntimeError("no nonterminal adjacent snapshot pair available for transition replay validation")
    if len(pairs) == 1:
        return pairs
    # Validate an early and a mid/late transition so block/phase state is exercised.
    selected = [pairs[0], pairs[len(pairs) // 2]]
    if selected[0][0]["step_index"] == selected[1][0]["step_index"]:
        return [selected[0]]
    return selected


def _assert_next_state_replay(backend: Any, current: dict[str, Any], nxt: dict[str, Any], generation_cfg: dict[str, Any]) -> None:
    snapshot = current["snapshot"]
    expected = nxt["snapshot"]
    if backend.backend_type == "rfba_llada_v2":
        replayed = replay_llada_next_state(backend, snapshot, generation_cfg)
        if replayed["full_token_ids"] != expected["full_token_ids"]:
            raise RuntimeError(
                f"LLaDA next-state replay mismatch step={current['step_index']}->{nxt['step_index']}"
            )
        if int(replayed["block_index"]) != int(expected["block_index"]):
            raise RuntimeError("LLaDA replay block_index mismatch")
        if int(replayed["step_in_block"]) != int(expected["step_in_block"]):
            raise RuntimeError("LLaDA replay step_in_block mismatch")
        return
    if backend.backend_type == "dream_v2":
        replayed = replay_dream_next_state(backend, snapshot, generation_cfg)
        if replayed["full_token_ids"] != expected["full_token_ids"]:
            raise RuntimeError(
                f"Dream next-state replay mismatch step={current['step_index']}->{nxt['step_index']}"
            )
        return
    raise RuntimeError(f"unsupported backend in transition replay validator: {backend.backend_type}")


def _validate_one(config_path: Path, contract: dict[str, Any]) -> dict[str, Any]:
    cfg = load_yaml(config_path)
    adapter = create_task_adapter(cfg["dataset"])
    backend = create_v2_backend(_profile(str(cfg["model_profile"])), adapter)
    item = _validation_item(adapter, cfg["dataset"])
    generation_cfg = dict(cfg["generation"])
    generation_cfg["trajectories_per_item"] = 1
    # Validation only: save every native state so x_t -> x_{t+1} can be
    # compared directly. This does not alter any scientific full-run config.
    generation_cfg["checkpoint_stride"] = 1
    record = backend.generate_trajectory_v2(item, 0, generation_cfg)

    operator_cfg = dict(contract["canonical_operator"])
    operator_cfg["anchor_confidence_threshold"] = float(
        cfg.get("operator", {}).get("anchor_confidence_threshold", 0.80)
    )
    operator_cfg.update(cfg.get("operator", {}))
    root_seed = int(cfg.get("probe", {}).get("root_seed", 2027))

    terminal_intervention_check = None
    if backend.backend_type == "dream_v2":
        final_step = record["steps"][-1]
        final_snapshot = final_step.get("snapshot")
        if final_snapshot is None:
            raise RuntimeError("Dream terminal snapshot missing from validation trajectory")
        terminal_seed = deterministic_branch_seed(
            root_seed=root_seed,
            item_id=int(record["item_id"]),
            trajectory_id=int(record["trajectory_id"]),
            step_index=int(final_step["step_index"]),
            branch_index=0,
            stage="localization",
        )
        terminal = backend.run_operator_branch(
            item,
            final_snapshot,
            generation_cfg,
            operator_cfg,
            operator_id="low_confidence_remask_v2",
            branch_seed=terminal_seed,
        )
        if terminal.get("applicable", True):
            raise RuntimeError("Dream terminal snapshot incorrectly accepts a repair intervention")
        if terminal.get("metadata", {}).get("reason") != "no_remaining_native_schedule":
            raise RuntimeError("Dream terminal intervention did not report exhausted native schedule")
        terminal_intervention_check = True

    checks = []
    for step, next_step in _selected_transition_pairs(record):
        snapshot = step["snapshot"]
        _assert_next_state_replay(backend, step, next_step, generation_cfg)

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
        exact_match = (
            exact.get("final_text") == record.get("final_text")
            and exact.get("final_answer") == record.get("final_answer")
        )
        if not exact_match:
            raise RuntimeError(
                f"native final replay mismatch backend={backend.backend_type} step={step['step_index']}"
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
                "next_step_index": int(next_step["step_index"]),
                "next_state_exact_replay": True,
                "native_final_exact_replay": True,
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
        "terminal_intervention_inapplicable": terminal_intervention_check,
        "status": "PASS",
    }
    del backend
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend", choices=["llada", "dream", "all"], default="all")
    args = ap.parse_args()
    if not torch.cuda.is_available():
        raise SystemExit("V2 backend replay validation requires a CUDA worker")
    contract = load_yaml(CONTRACT)
    validate_contract_dict(contract)
    names = ["llada", "dream"] if args.backend == "all" else [args.backend]
    rows = []
    for name in names:
        path = VALIDATION_CONFIGS[name]
        print(f"[v2 validation:{name}] {path.relative_to(ROOT)}")
        rows.append(_validate_one(path, contract))
    payload = {
        "status": "PASS",
        "git_sha": _git_sha(),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "backends": names,
        "rows": rows,
    }
    READINESS_ROOT.mkdir(parents=True, exist_ok=True)
    for name in names:
        backend_type = "rfba_llada_v2" if name == "llada" else "dream_v2"
        row_payload = {
            "status": "PASS",
            "git_sha": payload["git_sha"],
            "generated_at_utc": payload["generated_at_utc"],
            "backends": [name],
            "rows": [row for row in rows if row["backend_type"] == backend_type],
        }
        save_json(READINESS_ROOT / f"backend_validation_{name}.json", row_payload)
    if args.backend == "all":
        save_json(READINESS_ROOT / "backend_validation.json", payload)
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
