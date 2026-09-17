#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd -- "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT_DIR"

if [[ -z "${PYTHON_BIN:-}" ]]; then
  if [[ -x "$ROOT_DIR/.venv/bin/python" ]]; then
    PYTHON_BIN="$ROOT_DIR/.venv/bin/python"
  elif [[ -x /home/kimhj/llada8b_basic/.venv/bin/python ]]; then
    PYTHON_BIN=/home/kimhj/llada8b_basic/.venv/bin/python
  else
    PYTHON_BIN="$(command -v python || command -v python3 || true)"
  fi
fi
if [[ -z "$PYTHON_BIN" ]]; then
  echo "python not found on PATH" >&2
  exit 1
fi

usage() {
  cat <<'EOF'
Usage: bash scripts/full_paper_pipeline.sh <preflight|submit|status|finalize>

preflight  Validate that all canonical full-split protocol configs are paper-safe.
submit     Run preflight and submit/reuse all missing benchmark-complete Slurm jobs.
status     Report which required protocol reports and final artifacts exist.
finalize   Rebuild the canonical aggregate/extended outputs, run strict final audit,
           and write results/full_paper_manifest.json.
EOF
}

cmd="${1:-status}"
case "$cmd" in
  preflight)
    "$PYTHON_BIN" scripts/audit_full_paper_ready.py --mode preflight
    ;;
  submit)
    "$PYTHON_BIN" scripts/audit_full_paper_ready.py --mode preflight
    bash scripts/submit_benchmark_complete_suite.sh
    ;;
  status)
    "$PYTHON_BIN" scripts/audit_full_paper_ready.py --mode status
    ;;
  finalize)
    bash scripts/build_benchmark_complete_report.sh
    "$PYTHON_BIN" scripts/audit_full_paper_ready.py --mode final --write-manifest
    ;;
  -h|--help|help)
    usage
    ;;
  *)
    usage >&2
    exit 2
    ;;
esac
