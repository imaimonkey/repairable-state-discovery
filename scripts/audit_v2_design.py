from __future__ import annotations

import argparse
from pathlib import Path

from repairable_diffusion.src.utils.io import load_yaml
from repairable_diffusion.src.v2.contracts import validate_contract_dict


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONTRACT = ROOT / "repairable_diffusion/configs/v2/measurement_contract.yaml"

REQUIRED_DESIGN_FILES = [
    ROOT / "docs/v2_scientific_contract.md",
    ROOT / "repairable_diffusion/configs/v2/measurement_contract.yaml",
    ROOT / "repairable_diffusion/src/v2/contracts.py",
    ROOT / "repairable_diffusion/src/v2/metrics.py",
    ROOT / "repairable_diffusion/src/v2/oof.py",
    ROOT / "repairable_diffusion/src/v2/provenance.py",
]

# Execution readiness is intentionally stricter than design readiness. The V2
# design is frozen before the scientific backend refactor is declared runnable.
REQUIRED_EXECUTION_FILES = [
    ROOT / "repairable_diffusion/src/v2/task_adapters.py",
    ROOT / "repairable_diffusion/src/v2/backends.py",
    ROOT / "repairable_diffusion/src/v2/run_measurement.py",
    ROOT / "scripts/run_v2_suite.sh",
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


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--contract", default=str(DEFAULT_CONTRACT))
    ap.add_argument("--mode", choices=["design", "execution"], default="design")
    args = ap.parse_args()

    contract_path = Path(args.contract)
    errors: list[str] = []
    try:
        cfg = load_yaml(contract_path)
        validate_contract_dict(cfg)
    except Exception as exc:  # deliberate audit boundary
        errors.append(f"contract invalid: {exc}")

    missing_design = _missing(REQUIRED_DESIGN_FILES)
    errors.extend(f"missing design file: {path}" for path in missing_design)

    if args.mode == "execution":
        missing_execution = _missing(REQUIRED_EXECUTION_FILES)
        errors.extend(f"missing execution file: {path}" for path in missing_execution)
        present_tests = _execution_test_names()
        for name in sorted(REQUIRED_TEST_NAMES - present_tests):
            errors.append(f"missing scientific readiness test: {name}")

    print(f"mode: {args.mode}")
    print(f"contract: {contract_path}")
    if errors:
        print("\nNOT READY")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    if args.mode == "design":
        print("\nDESIGN READY")
        print("V2 scientific contract is frozen; this does not imply execution readiness.")
    else:
        print("\nEXECUTION STRUCTURE READY")
        print("Run the scientific test suite before submitting full-scale GPU jobs.")


if __name__ == "__main__":
    main()
