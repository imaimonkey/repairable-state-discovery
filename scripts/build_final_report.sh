#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if [[ -n "${REPAIRABLE_ROOT:-}" ]]; then
  ROOT_DIR="$REPAIRABLE_ROOT"
elif [[ -n "${SLURM_SUBMIT_DIR:-}" && -f "$SLURM_SUBMIT_DIR/pyproject.toml" ]]; then
  ROOT_DIR="$SLURM_SUBMIT_DIR"
else
  ROOT_DIR="$(cd -- "$SCRIPT_DIR/.." && pwd)"
fi
cd "$ROOT_DIR"

if [[ -f .venv/bin/activate ]]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
elif [[ -f /home/kimhj/provenance-decompositon/.venv/bin/activate ]]; then
  # shellcheck disable=SC1091
  source /home/kimhj/provenance-decompositon/.venv/bin/activate
fi

PYTHON_BIN="$(command -v python || command -v python3 || true)"
if [[ -z "$PYTHON_BIN" ]]; then
  echo "python not found on PATH"
  exit 1
fi

OUTPUT_DIR="${OUTPUT_DIR:-$ROOT_DIR/results/final_reports}"
MATH500_REPORT="${MATH500_REPORT:-$ROOT_DIR/results/generated_configs/protocol_math500_final_report.json}"
GSM8K_REPORT="${GSM8K_REPORT:-$ROOT_DIR/results/generated_configs/protocol_gsm8k_final_report.json}"

missing=()
for path in "$MATH500_REPORT" "$GSM8K_REPORT"; do
  if [[ ! -f "$path" ]]; then
    missing+=("$path")
  fi
done

if (( ${#missing[@]} > 0 )); then
  echo "missing protocol report(s) required for build_final_report.sh:" >&2
  for path in "${missing[@]}"; do
    echo "  - $path" >&2
  done
  echo "set MATH500_REPORT/GSM8K_REPORT to alternate report paths or complete the missing protocol runs first." >&2
  exit 1
fi

"$PYTHON_BIN" -m repairable_diffusion.src.analysis.aggregate_runs \
  --protocol-report "$MATH500_REPORT" \
  --protocol-report "$GSM8K_REPORT" \
  --output-dir "$OUTPUT_DIR"

"$PYTHON_BIN" -m repairable_diffusion.src.analysis.render_tables \
  --aggregate-report "$OUTPUT_DIR/aggregate_report.json" \
  --output-dir "$OUTPUT_DIR/tables"
