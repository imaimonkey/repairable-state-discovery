from __future__ import annotations

import argparse
import json
import pickle
import subprocess
from pathlib import Path
from typing import Any

from repairable_diffusion.src.utils.io import load_yaml, save_json
from repairable_diffusion.src.v2.backends import DREAM_NATIVE_SOURCE_REPOSITORY, DREAM_NATIVE_SOURCE_REVISION, V2_BACKEND_VERSION
from repairable_diffusion.src.v2.contracts import DECODER_STATE_SCHEMA_VERSION, assert_disjoint
from repairable_diffusion.src.v2.provenance import config_sha256, scientific_fingerprint, sha256_file


ROOT = Path(__file__).resolve().parents[1]
RUNS_ROOT = ROOT / "repairable_diffusion/configs/v2/runs"
OUTPUT_ROOT = ROOT / "repairable_diffusion/outputs/v2_measurement"
CONTRACT = load_yaml(ROOT / "repairable_diffusion/configs/v2/measurement_contract.yaml")


def _git_sha() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def _seed_hash(seeds: list[int]) -> str:
    return config_sha256({"seeds": sorted(set(int(x) for x in seeds))})


def seal(config_path: Path) -> dict[str, Any]:
    cfg = load_yaml(config_path)
    run_name = str(cfg["run_name"])
    run_dir = OUTPUT_ROOT / run_name
    report_path = run_dir / "report.json"
    run_manifest_path = run_dir / "run_manifest.json"
    branches_path = run_dir / "probe_branches.jsonl"
    trajectories_path = run_dir / "trajectories.pkl"
    required = [report_path, run_manifest_path, branches_path, trajectories_path]
    missing = [str(x) for x in required if not x.is_file()]
    if missing:
        raise RuntimeError(f"cannot seal incomplete V2 run {run_name}; missing={missing}")

    report = json.loads(report_path.read_text(encoding="utf-8"))
    run_manifest = json.loads(run_manifest_path.read_text(encoding="utf-8"))
    current_sha = _git_sha()
    if report.get("git_sha") != current_sha or run_manifest.get("git_sha") != current_sha:
        raise RuntimeError(
            f"refusing to seal run from another code revision: run={run_name} "
            f"report={report.get('git_sha')} manifest={run_manifest.get('git_sha')} current={current_sha}"
        )
    if report.get("v1_artifacts_substituted") is not False:
        raise RuntimeError(f"run {run_name} does not explicitly reject V1 substitution")

    with trajectories_path.open("rb") as fh:
        trajectory_payload = pickle.load(fh)
    records = trajectory_payload.get("records", [])
    item_ids = sorted({int(r["item_id"]) for r in records})
    actual_subset_hash = config_sha256({"item_ids": item_ids})

    branches = _read_jsonl(branches_path)
    loc_seeds = [int(r["branch_seed"]) for r in branches if r.get("stage") == "localization"]
    confirm_seeds = [int(r["branch_seed"]) for r in branches if r.get("stage") == "confirmation"]
    assert_disjoint(loc_seeds, confirm_seeds)
    operators = sorted({str(r["operator_id"]) for r in branches})

    base = dict(run_manifest.get("base_provenance") or {})
    required_provenance = {
        "git_sha": current_sha,
        "config_sha256": str(report["config_sha256"]),
        "model_id": base.get("model_id"),
        "model_revision": base.get("model_revision", "default"),
        "dataset_id": base.get("dataset_id"),
        "dataset_revision": base.get("dataset_revision", "default"),
        "dataset_split": base.get("dataset_split"),
        "subset_hash": actual_subset_hash,
        "task_adapter_version": base.get("task_adapter_version"),
        "trajectory_bank_hash": str(report["trajectory_bank_hash"]),
        "decoder_state_schema_version": DECODER_STATE_SCHEMA_VERSION,
        "operator_id": "probe_bank_multi_operator",
        "operator_version": V2_BACKEND_VERSION,
        "localization_seed_hash": _seed_hash(loc_seeds),
        "confirmation_seed_hash": _seed_hash(confirm_seeds),
        "evaluator_id": base.get("evaluator_id"),
        "evaluator_version": base.get("evaluator_version"),
    }
    missing_fields = [key for key in CONTRACT["provenance"]["required_fields"] if required_provenance.get(key) in (None, "")]
    if missing_fields:
        raise RuntimeError(f"missing required provenance for {run_name}: {missing_fields}")

    artifact_paths = [
        report_path,
        run_manifest_path,
        branches_path,
        trajectories_path,
        run_dir / "state_values.jsonl",
        run_dir / "selector_confirmation.csv",
        run_dir / "existence.csv",
        run_dir / "fresh_sampling.jsonl",
    ]
    artifacts = {
        str(path.relative_to(run_dir)): sha256_file(path)
        for path in artifact_paths
        if path.is_file()
    }
    payload = {
        "status": "SEALED",
        "run_name": run_name,
        "required_provenance": required_provenance,
        "scientific_fingerprint": scientific_fingerprint(required_provenance),
        "operators": operators,
        "localization_seed_count": len(set(loc_seeds)),
        "confirmation_seed_count": len(set(confirm_seeds)),
        "item_count": len(item_ids),
        "artifacts": artifacts,
        "core_label": CONTRACT["operator_controls"].get("core_label"),
        "core_source_revision": CONTRACT["operator_controls"].get("core_source_revision"),
        "v1_artifacts_substituted": False,
        "dream_native_sampler_reference": ({"repository": DREAM_NATIVE_SOURCE_REPOSITORY, "revision": DREAM_NATIVE_SOURCE_REVISION, "algorithm": "origin"} if str(cfg.get("model_profile", "")).startswith("dream_") else None),
    }
    save_json(run_dir / "scientific_provenance.json", payload)
    return payload


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config")
    ap.add_argument("--all-completed", action="store_true")
    args = ap.parse_args()
    if bool(args.config) == bool(args.all_completed):
        raise SystemExit("specify exactly one of --config or --all-completed")

    if args.config:
        configs = [Path(args.config)]
    else:
        configs = sorted(RUNS_ROOT.glob("*.yaml"))

    sealed = []
    skipped = []
    for path in configs:
        cfg = load_yaml(path)
        run_dir = OUTPUT_ROOT / str(cfg["run_name"])
        if not (run_dir / "report.json").is_file():
            if args.all_completed:
                skipped.append(str(cfg["run_name"]))
                continue
            raise RuntimeError(f"run is incomplete: {cfg['run_name']}")
        result = seal(path)
        sealed.append(result["run_name"])
        print(f"sealed {result['run_name']} -> {run_dir / 'scientific_provenance.json'}")
    print(json.dumps({"sealed": sealed, "skipped_incomplete": skipped}, indent=2))


if __name__ == "__main__":
    main()
