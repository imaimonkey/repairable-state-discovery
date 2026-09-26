#!/usr/bin/env python3
"""Create the immutable Generation 3 design-fingerprint manifest."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "status/rsd_ref_v3/design_freeze.json"
FINGERPRINT_FILES = [
    "AGENTS.md",
    "docs/rsd_ref_v3_scientific_contract.md",
    "docs/RSD_REF_V3_TASK_SPEC.md",
    "docs/REFERENCE_TASK_SPEC.md",
    "docs/rsd_ref_v3_sample_size_plan.md",
    "docs/RSD_REF_V3_EXECUTION.md",
    "repairable_diffusion/configs/rsd_ref_v3/measurement_contract.yaml",
    "repairable_diffusion/src/rsd_ref_v3/__init__.py",
    "repairable_diffusion/src/rsd_ref_v3/runtime.py",
    "repairable_diffusion/src/rsd_ref_v3/task_adapters.py",
    "repairable_diffusion/src/rsd_ref_v3/runner.py",
    "repairable_diffusion/src/v2r/schema.py",
    "repairable_diffusion/src/v2r/planning.py",
    "repairable_diffusion/src/v2r/artifacts.py",
    "repairable_diffusion/src/v2r/science.py",
    "scripts/audit_rsd_ref_v3.py",
    "scripts/run_rsd_ref_v3.py",
    "scripts/submit_rsd_ref_v3.py",
    "status/rsd_ref_v3/subsets/selection_policy.json",
    "status/rsd_ref_v3/runtime_templates/storage_plan.template.json",
    "status/rsd_ref_v3/runtime_templates/execution_readiness.template.json",
    "tests/test_rsd_ref_v3_contract.py",
    "tests/test_rsd_ref_v3_runner.py",
]
FINGERPRINT_FILES += [
    str(path.relative_to(ROOT))
    for path in sorted((ROOT / "repairable_diffusion/configs/rsd_ref_v3/runs").glob("*.yaml"))
]
FINGERPRINT_FILES += [
    str(path.relative_to(ROOT))
    for path in sorted((ROOT / "status/rsd_ref_v3/subsets").glob("llada_*.json"))
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--basis-sha", default=None)
    args = parser.parse_args()
    missing = [path for path in FINGERPRINT_FILES if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit(f"missing freeze inputs: {missing}")
    basis_sha = args.basis_sha or subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip()
    if len(basis_sha) != 40:
        raise SystemExit("--basis-sha must be a 40-character git SHA")
    payload = {
        "generation": 3,
        "generation_id": "rsd_ref_v3",
        "status": "FROZEN_BEFORE_CONFIRMATORY_OUTCOMES",
        "freeze_basis_git_sha": basis_sha,
        "canonical_source_parent": "227cbcc99c7edfac83de7f34c452db7defd5bdcb",
        "pilot_results_observed": True,
        "pilot_use": "planning_only",
        "confirmatory_results_observed": False,
        "confirmatory_execution_started": False,
        "files": {path: sha256(ROOT / path) for path in FINGERPRINT_FILES},
    }
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"manifest": str(MANIFEST.relative_to(ROOT)), "freeze_basis_git_sha": basis_sha}, indent=2))


if __name__ == "__main__":
    main()
