#!/bin/bash
#SBATCH --job-name=repair_bm_limited
#SBATCH --output=/home/kimhj/repairable-state-discovery/logs/protocol_limited_%A_%a.out
#SBATCH --error=/home/kimhj/repairable-state-discovery/logs/protocol_limited_%A_%a.err
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=30-00:00:00
#SBATCH --nodelist=devbox

set -euo pipefail

if [[ -n "${REPAIRABLE_ROOT:-}" ]]; then
  ROOT_DIR="$REPAIRABLE_ROOT"
elif [[ -n "${SLURM_SUBMIT_DIR:-}" && -f "$SLURM_SUBMIT_DIR/pyproject.toml" ]]; then
  ROOT_DIR="$SLURM_SUBMIT_DIR"
else
  ROOT_DIR="/home/kimhj/repairable-state-discovery"
fi
cd "$ROOT_DIR"

protocols=(
  repairable_diffusion/configs/final/protocol_math500_full.yaml
  repairable_diffusion/configs/final/protocol_gsm8k_full.yaml
  repairable_diffusion/configs/final/protocol_math500_full_robustness.yaml
  repairable_diffusion/configs/final/protocol_math500_full_seed_repeats.yaml
  repairable_diffusion/configs/final/protocol_gsm8k_full_seed_repeats.yaml
  repairable_diffusion/configs/final/protocol_math500_full_dream_backbone.yaml
  repairable_diffusion/configs/final/protocol_gsm8k_full_dream_backbone.yaml
)

reports=(
  results/generated_configs/protocol_math500_full_report.json
  results/generated_configs/protocol_gsm8k_full_report.json
  results/generated_configs/protocol_math500_full_robustness_report.json
  results/generated_configs/protocol_math500_full_seed_repeats_report.json
  results/generated_configs/protocol_gsm8k_full_seed_repeats_report.json
  results/generated_configs/protocol_math500_full_dream_backbone_report.json
  results/generated_configs/protocol_gsm8k_full_dream_backbone_report.json
)

diffusion_counts=(1 1 3 2 2 1 1)
ar_counts=(2 2 0 0 0 0 0)

check_report() {
  local report="$1"
  local expected_diffusion="$2"
  local expected_ar="$3"
  [[ -f "$report" ]] && jq -e \
    --argjson d "$expected_diffusion" \
    --argjson a "$expected_ar" \
    '(.dry_run == false)
     and ((.runs | map(select(.family=="diffusion")) | length) == $d)
     and ((.runs | map(select(.family=="ar")) | length) == $a)' \
    "$report" >/dev/null
}

task_id="${SLURM_ARRAY_TASK_ID:?SLURM_ARRAY_TASK_ID is required}"
if (( task_id < 0 || task_id >= ${#protocols[@]} )); then
  echo "Invalid task id: $task_id" >&2
  exit 2
fi

protocol="${protocols[$task_id]}"
report="${reports[$task_id]}"

if check_report "$report" "${diffusion_counts[$task_id]}" "${ar_counts[$task_id]}"; then
  echo "[skip] report already complete: $report"
  exit 0
fi

echo "[run] task: $task_id"
echo "[run] protocol: $protocol"
echo "[run] report: $report"

export PROTOCOL_PATH="$protocol"
bash "$ROOT_DIR/scripts/run_protocol_repairability_final.sh"
