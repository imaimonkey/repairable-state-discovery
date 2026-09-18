from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from repairable_diffusion.src.utils.io import load_yaml
from repairable_diffusion.src.v2.contracts import validate_contract_dict


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONTRACT = ROOT / "repairable_diffusion/configs/v2/measurement_contract.yaml"
RESULT_ROOT = ROOT / "results/v2_measurement"
OUTPUT_ROOT = ROOT / "repairable_diffusion/outputs/v2_measurement"

REQUIRED_DESIGN_FILES = [
    ROOT / "AGENTS.md",
    ROOT / "docs/v2_scientific_contract.md",
    ROOT / "docs/CODEX_V2_FINAL_EXECUTION.md",
    ROOT / "docs/CODEX_EXECUTE_NOW.md",
    ROOT / "repairable_diffusion/configs/v2/measurement_contract.yaml",
    ROOT / "repairable_diffusion/src/v2/contracts.py",
    ROOT / "repairable_diffusion/src/v2/metrics.py",
    ROOT / "repairable_diffusion/src/v2/oof.py",
    ROOT / "repairable_diffusion/src/v2/provenance.py",
]

REQUIRED_EXECUTION_FILES = [
    ROOT / "repairable_diffusion/src/v2/task_adapters.py",
    ROOT / "repairable_diffusion/src/v2/backends.py",
    ROOT / "repairable_diffusion/src/v2/replay.py",
    ROOT / "repairable_diffusion/src/v2/run_measurement.py",
    ROOT / "scripts/run_v2_suite.sh",
    ROOT / "scripts/validate_v2_backends.py",
    ROOT / "scripts/submit_v2_suite.py",
    ROOT / "scripts/seal_v2_runs.py",
    ROOT / "scripts/aggregate_v2_results.py",
]

REQUIRED_TEST_NAMES = {
    "test_snapshot_native_replay",
    "test_branch_seed_reproducibility",
    "test_branch_seed_independence",
    "test_fixed_operator_across_branches",
    "test_zero_repair_no_positive_label",
    "test_grouped_oof_no_item_leakage",
    "test_policy_negative_repair_accounting",
    "test_artifact_fingerprint_invalidation",
    "test_task_adapter_evaluator",
    "test_operator_nfe_accounting",
}

PILOT_RUNS = ["v2_pilot_math500_llada", "v2_pilot_gsm8k_llada"]
TIER_A_RUNS = ["v2_math500_llada", "v2_gsm8k_llada"]
FINAL_ARTIFACTS = [
    RESULT_ROOT / "aggregate_report.json",
    RESULT_ROOT / "table1_existence.csv",
    RESULT_ROOT / "table2_mechanisms.csv",
    RESULT_ROOT / "table3_localization.csv",
    RESULT_ROOT / "figure_data/recoverability_landscape.csv",
    RESULT_ROOT / "figure_data/repairability_survival.csv",
    RESULT_ROOT / "figure_data/recovery_harm_compute.csv",
    RESULT_ROOT / "final_execution_manifest.json",
]


def _git_sha() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def _missing(paths: list[Path]) -> list[str]:
    return [str(path.relative_to(ROOT)) for path in paths if not path.is_file() or path.stat().st_size == 0]


def _execution_test_names() -> set[str]:
    names: set[str] = set()
    tests_root = ROOT / "tests"
    if not tests_root.exists():
        return names
    for path in tests_root.glob("test_v2*.py"):
        text = path.read_text(encoding="utf-8")
        for name in REQUIRED_TEST_NAMES:
            if f"def {name}" in text:
                names.add(name)
    return names


def _json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _require_stamp(errors: list[str], path: Path, *, name: str, current_sha: str) -> None:
    if not path.is_file():
        errors.append(f"missing {name}: {path.relative_to(ROOT)}")
        return
    try:
        payload = _json(path)
    except Exception as exc:
        errors.append(f"invalid {name}: {exc}")
        return
    if payload.get("status") != "PASS":
        errors.append(f"{name} is not PASS")
    if payload.get("git_sha") != current_sha:
        errors.append(f"{name} git SHA mismatch: {payload.get('git_sha')} != {current_sha}")


def _require_report(errors: list[str], run_name: str, current_sha: str) -> None:
    path = OUTPUT_ROOT / run_name / "report.json"
    if not path.is_file():
        errors.append(f"missing run report: {run_name}")
        return
    try:
        payload = _json(path)
    except Exception as exc:
        errors.append(f"invalid report {run_name}: {exc}")
        return
    if payload.get("git_sha") != current_sha:
        errors.append(f"run report git SHA mismatch for {run_name}")
    if payload.get("v1_artifacts_substituted") is not False:
        errors.append(f"run report does not reject V1 substitution: {run_name}")


def _require_provenance(errors: list[str], run_name: str, current_sha: str, required_fields: list[str]) -> None:
    path = OUTPUT_ROOT / run_name / "scientific_provenance.json"
    if not path.is_file():
        errors.append(f"missing scientific provenance: {run_name}")
        return
    try:
        payload = _json(path)
    except Exception as exc:
        errors.append(f"invalid scientific provenance {run_name}: {exc}")
        return
    if payload.get("status") != "SEALED":
        errors.append(f"scientific provenance is not SEALED: {run_name}")
    provenance = payload.get("required_provenance") or {}
    if provenance.get("git_sha") != current_sha:
        errors.append(f"scientific provenance git SHA mismatch: {run_name}")
    missing = [field for field in required_fields if provenance.get(field) in (None, "")]
    if missing:
        errors.append(f"scientific provenance missing fields for {run_name}: {missing}")
    if payload.get("v1_artifacts_substituted") is not False:
        errors.append(f"scientific provenance does not reject V1 substitution: {run_name}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--contract", default=str(DEFAULT_CONTRACT))
    ap.add_argument("--mode", choices=["design", "execution", "primary", "dream", "full", "final"], default="design")
    args = ap.parse_args()

    current_sha = _git_sha()
    errors: list[str] = []
    cfg = None
    try:
        cfg = load_yaml(Path(args.contract))
        validate_contract_dict(cfg)
    except Exception as exc:
        errors.append(f"contract invalid: {exc}")

    errors.extend(f"missing design file: {path}" for path in _missing(REQUIRED_DESIGN_FILES))

    if args.mode in {"execution", "primary", "dream", "full", "final"}:
        errors.extend(f"missing execution file: {path}" for path in _missing(REQUIRED_EXECUTION_FILES))
        present_tests = _execution_test_names()
        for name in sorted(REQUIRED_TEST_NAMES - present_tests):
            errors.append(f"missing scientific readiness test: {name}")

    required_fields = list((cfg or {}).get("provenance", {}).get("required_fields", []))
    if args.mode in {"primary", "dream", "full", "final"}:
        _require_stamp(
            errors,
            RESULT_ROOT / "readiness/unit_preflight.json",
            name="unit preflight stamp",
            current_sha=current_sha,
        )

    if args.mode in {"primary", "full", "final"}:
        _require_stamp(
            errors,
            RESULT_ROOT / "readiness/backend_validation_llada.json",
            name="LLaDA backend validation stamp",
            current_sha=current_sha,
        )
        for run_name in PILOT_RUNS:
            _require_report(errors, run_name, current_sha)
            _require_provenance(errors, run_name, current_sha, required_fields)

    if args.mode in {"dream", "full"}:
        _require_stamp(
            errors,
            RESULT_ROOT / "readiness/backend_validation_dream.json",
            name="Dream backend validation stamp",
            current_sha=current_sha,
        )

    if args.mode == "final":
        for run_name in TIER_A_RUNS:
            _require_report(errors, run_name, current_sha)
            _require_provenance(errors, run_name, current_sha, required_fields)
        errors.extend(f"missing final artifact: {path}" for path in _missing(FINAL_ARTIFACTS))
        manifest_path = RESULT_ROOT / "final_execution_manifest.json"
        if manifest_path.is_file():
            manifest = _json(manifest_path)
            if manifest.get("git_sha") != current_sha:
                errors.append("final_execution_manifest git SHA mismatch")
            if manifest.get("v1_results_substituted") is not False:
                errors.append("final manifest does not explicitly forbid V1 substitution")

    print(f"mode: {args.mode}")
    print(f"git_sha: {current_sha}")
    if errors:
        print("\nNOT READY")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    labels = {
        "design": "DESIGN READY",
        "execution": "EXECUTION STRUCTURE READY",
        "primary": "PRIMARY LLADA SUBMISSION READY",
        "dream": "DREAM TRANSFER SUBMISSION READY",
        "full": "FULL MATRIX SUBMISSION READY",
        "final": "FINAL V2 ARTIFACTS READY",
    }
    print(f"\n{labels[args.mode]}")


if __name__ == "__main__":
    main()
