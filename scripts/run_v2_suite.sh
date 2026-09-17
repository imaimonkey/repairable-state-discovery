#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
PYTHON_BIN="${PYTHON_BIN:-python}"
RESULT_ROOT="$ROOT/results/v2_measurement"
READINESS_ROOT="$RESULT_ROOT/readiness"
mkdir -p "$READINESS_ROOT"

run_cfg() {
  local cfg="$1"
  echo "[v2] running $cfg"
  "$PYTHON_BIN" -m repairable_diffusion.src.v2.run_measurement --config "$cfg"
}

write_preflight_stamp() {
  local sha
  sha="$(git rev-parse HEAD)"
  "$PYTHON_BIN" - "$READINESS_ROOT/unit_preflight.json" "$sha" <<'PY'
import json, sys
from datetime import datetime, timezone
from pathlib import Path
path = Path(sys.argv[1])
payload = {
    "status": "PASS",
    "git_sha": sys.argv[2],
    "generated_at_utc": datetime.now(timezone.utc).isoformat(),
    "commands": [
        "python scripts/audit_v2_design.py --mode execution",
        "python -m compileall -q repairable_diffusion/src/v2 scripts",
        "python -m unittest discover -s tests -p test_v2*.py",
    ],
}
path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(path)
PY
}

case "${1:-}" in
  preflight)
    "$PYTHON_BIN" scripts/audit_v2_design.py --mode execution
    "$PYTHON_BIN" -m compileall -q repairable_diffusion/src/v2 scripts
    "$PYTHON_BIN" -m unittest discover -s tests -p 'test_v2*.py'
    write_preflight_stamp
    ;;

  pilot)
    # Frozen correctness/resource pilots. Their scientific settings must not be
    # changed in response to the observed effect direction.
    run_cfg repairable_diffusion/configs/v2/runs/pilot_math500_llada.yaml
    run_cfg repairable_diffusion/configs/v2/runs/pilot_gsm8k_llada.yaml
    ;;

  full-local)
    # Deadline priority: Tier A first, then backbone transfer, then breadth.
    configs=(
      repairable_diffusion/configs/v2/runs/full_math500_llada.yaml
      repairable_diffusion/configs/v2/runs/full_gsm8k_llada.yaml
      repairable_diffusion/configs/v2/runs/full_math500_dream.yaml
      repairable_diffusion/configs/v2/runs/full_gsm8k_dream.yaml
      repairable_diffusion/configs/v2/runs/full_bbh_logical3_llada.yaml
      repairable_diffusion/configs/v2/runs/full_bbh_logical5_llada.yaml
      repairable_diffusion/configs/v2/runs/full_bbh_logical7_llada.yaml
      repairable_diffusion/configs/v2/runs/full_mbpp_llada.yaml
    )
    for cfg in "${configs[@]}"; do
      run_cfg "$cfg"
    done
    ;;

  aggregate)
    "$PYTHON_BIN" scripts/aggregate_v2_results.py
    ;;

  *)
    cat <<'EOF'
Usage: bash scripts/run_v2_suite.sh {preflight|pilot|full-local|aggregate}

Mandatory order:
  bash scripts/run_v2_suite.sh preflight
  python scripts/validate_v2_backends.py
  bash scripts/run_v2_suite.sh pilot
  python scripts/audit_v2_design.py --mode full
  python scripts/submit_v2_suite.py --tier full --dry-run
  python scripts/submit_v2_suite.py --tier full
EOF
    exit 2
    ;;
esac
