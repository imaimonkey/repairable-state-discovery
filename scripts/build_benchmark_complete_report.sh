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
  echo "python not found on PATH" >&2
  exit 1
fi

OUTPUT_DIR="${OUTPUT_DIR:-$ROOT_DIR/results/benchmark_complete_reports}"
EXTENDED_DIR="${EXTENDED_DIR:-$ROOT_DIR/results/benchmark_extended_analysis}"
BOOTSTRAP="${BOOTSTRAP:-1000}"

required_reports=(
  "$ROOT_DIR/results/generated_configs/protocol_math500_full_report.json"
  "$ROOT_DIR/results/generated_configs/protocol_gsm8k_full_report.json"
  "$ROOT_DIR/results/generated_configs/protocol_math500_full_robustness_report.json"
  "$ROOT_DIR/results/generated_configs/protocol_math500_full_seed_repeats_report.json"
  "$ROOT_DIR/results/generated_configs/protocol_gsm8k_full_seed_repeats_report.json"
  "$ROOT_DIR/results/generated_configs/protocol_math500_full_dream_backbone_report.json"
  "$ROOT_DIR/results/generated_configs/protocol_gsm8k_full_dream_backbone_report.json"
)

for path in "${required_reports[@]}"; do
  if [[ ! -f "$path" ]]; then
    echo "missing required benchmark-complete protocol report: $path" >&2
    exit 1
  fi
done

aggregate_args=()
for path in "${required_reports[@]}"; do
  aggregate_args+=(--protocol-report "$path")
done

"$PYTHON_BIN" -m repairable_diffusion.src.analysis.aggregate_runs \
  "${aggregate_args[@]}" \
  --output-dir "$OUTPUT_DIR"

"$PYTHON_BIN" -m repairable_diffusion.src.analysis.render_tables \
  --aggregate-report "$OUTPUT_DIR/aggregate_report.json" \
  --output-dir "$OUTPUT_DIR/tables"

"$PYTHON_BIN" -m repairable_diffusion.src.analysis.export_figure_data \
  --aggregate-report "$OUTPUT_DIR/aggregate_report.json" \
  --output-dir "$OUTPUT_DIR/figure_data"

mapfile -t run_dirs < <(
  "$PYTHON_BIN" - "$OUTPUT_DIR/aggregate_report.json" <<'PY'
import json
import sys

with open(sys.argv[1], "r", encoding="utf-8") as fh:
    payload = json.load(fh)
for row in payload.get("diffusion_rows", []):
    print(row["run_dir"])
PY
)

extended_args=()
for run_dir in "${run_dirs[@]}"; do
  if [[ -f "$run_dir/trajectories.pkl" && -f "$run_dir/oracle_repair.json" && -f "$run_dir/repair_predictor.json" ]]; then
    extended_args+=(--run-dir "$run_dir")
  else
    echo "missing run-level artifacts for benchmark extended analysis: $run_dir" >&2
    exit 1
  fi
done

"$PYTHON_BIN" -m repairable_diffusion.src.analysis.extended_repair_analysis \
  "${extended_args[@]}" \
  --output-dir "$EXTENDED_DIR" \
  --bootstrap "$BOOTSTRAP"

"$PYTHON_BIN" -m repairable_diffusion.src.analysis.extract_qualitative_examples \
  "${extended_args[@]}" \
  --output-dir "$EXTENDED_DIR" \
  --max-per-type 3

echo "[benchmark-complete] protocol reports: ${#required_reports[@]}"
echo "[benchmark-complete] diffusion run dirs: ${#run_dirs[@]}"
echo "[benchmark-complete] aggregate: $OUTPUT_DIR"
echo "[benchmark-complete] figure data: $OUTPUT_DIR/figure_data"
echo "[benchmark-complete] extended: $EXTENDED_DIR"
