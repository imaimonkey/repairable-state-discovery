from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from repairable_diffusion.src.utils.io import load_yaml
from repairable_diffusion.src.v2.contracts import validate_contract_dict
from repairable_diffusion.src.v2.provenance import config_sha256


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONTRACT = ROOT / "repairable_diffusion/configs/v2/measurement_contract.yaml"
DEFAULT_OUTPUT = ROOT / "results/v2_measurement/design_manifest.json"


def _git_sha() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--contract", default=str(DEFAULT_CONTRACT))
    ap.add_argument("--output", default=str(DEFAULT_OUTPUT))
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    contract_path = Path(args.contract)
    cfg = load_yaml(contract_path)
    validate_contract_dict(cfg)

    output = Path(args.output)
    if output.exists() and not args.force:
        raise SystemExit(f"refusing to overwrite frozen V2 manifest without --force: {output}")

    payload = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "design_frozen_execution_not_implied",
        "contract_version": cfg["version"],
        "artifact_namespace": cfg["artifact_namespace"],
        "git_sha": _git_sha(),
        "contract_path": str(contract_path.relative_to(ROOT)),
        "contract_sha256": config_sha256(cfg),
        "scientific_contract": "docs/v2_scientific_contract.md",
        "paper_structure": "docs/v2_paper_structure.md",
        "implementation_request": "docs/CODEX_V2_IMPLEMENTATION_REQUEST.md",
        "readiness_gates": cfg["readiness_gates"],
        "v1_artifacts_are_historical_only": True,
        "v2_output_namespace": "results/v2_measurement",
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"frozen V2 design manifest: {output}")
    print(f"git_sha: {payload['git_sha']}")
    print(f"contract_sha256: {payload['contract_sha256']}")


if __name__ == "__main__":
    main()
