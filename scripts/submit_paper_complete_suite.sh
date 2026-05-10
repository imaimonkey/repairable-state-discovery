#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd -- "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT_DIR"

mkdir -p "$ROOT_DIR/logs"

AGGREGATE_MEM="${AGGREGATE_MEM:-8G}"
AGGREGATE_NODE="${AGGREGATE_NODE:-devbox}"

check_report() {
  local path="$1"
  local expected_diffusion="$2"
  local expected_ar="$3"
  [[ -f "$path" ]] && jq -e \
    --argjson d "$expected_diffusion" \
    --argjson a "$expected_ar" \
    '(.dry_run == false)
     and ((.runs | map(select(.family=="diffusion")) | length) == $d)
     and ((.runs | map(select(.family=="ar")) | length) == $a)' \
    "$path" >/dev/null
}

submit_protocol_if_missing() {
  local label="$1"
  local protocol="$2"
  local report="$3"
  local expected_diffusion="$4"
  local expected_ar="$5"
  if check_report "$report" "$expected_diffusion" "$expected_ar"; then
    echo "[skip] $label report already complete: $report" >&2
    return 0
  fi
  local job_id
  job_id="$(
    PROTOCOL_PATH="$protocol" \
      sbatch --parsable scripts/run_protocol_repairability_final.sh
  )"
  echo "[submit] $label: $job_id" >&2
  echo "$job_id"
}

missing_jobs=()

maybe_job="$(submit_protocol_if_missing \
  "math500-final" \
  repairable_diffusion/configs/final/protocol_math500_final.yaml \
  results/generated_configs/protocol_math500_final_report.json \
  1 2)"
[[ -n "$maybe_job" ]] && missing_jobs+=("$maybe_job")

maybe_job="$(submit_protocol_if_missing \
  "gsm8k-final" \
  repairable_diffusion/configs/final/protocol_gsm8k_final.yaml \
  results/generated_configs/protocol_gsm8k_final_report.json \
  1 2)"
[[ -n "$maybe_job" ]] && missing_jobs+=("$maybe_job")

maybe_job="$(submit_protocol_if_missing \
  "math500-robustness" \
  repairable_diffusion/configs/final/protocol_math500_submission_robustness.yaml \
  results/generated_configs/protocol_math500_submission_robustness_report.json \
  3 0)"
[[ -n "$maybe_job" ]] && missing_jobs+=("$maybe_job")

maybe_job="$(submit_protocol_if_missing \
  "math500-seed-repeats" \
  repairable_diffusion/configs/final/protocol_math500_seed_repeats.yaml \
  results/generated_configs/protocol_math500_seed_repeats_report.json \
  2 0)"
[[ -n "$maybe_job" ]] && missing_jobs+=("$maybe_job")

maybe_job="$(submit_protocol_if_missing \
  "gsm8k-seed-repeats" \
  repairable_diffusion/configs/final/protocol_gsm8k_seed_repeats.yaml \
  results/generated_configs/protocol_gsm8k_seed_repeats_report.json \
  2 0)"
[[ -n "$maybe_job" ]] && missing_jobs+=("$maybe_job")

maybe_job="$(submit_protocol_if_missing \
  "math500-dream-backbone" \
  repairable_diffusion/configs/final/protocol_math500_dream_backbone.yaml \
  results/generated_configs/protocol_math500_dream_backbone_report.json \
  1 0)"
[[ -n "$maybe_job" ]] && missing_jobs+=("$maybe_job")

maybe_job="$(submit_protocol_if_missing \
  "gsm8k-dream-backbone" \
  repairable_diffusion/configs/final/protocol_gsm8k_dream_backbone.yaml \
  results/generated_configs/protocol_gsm8k_dream_backbone_report.json \
  1 0)"
[[ -n "$maybe_job" ]] && missing_jobs+=("$maybe_job")

aggregate_args=(
  --job-name=repair_paper_complete
  --mem="$AGGREGATE_MEM"
  --nodelist="$AGGREGATE_NODE"
  --export=ALL,REPAIRABLE_ROOT="$ROOT_DIR"
  --output="$ROOT_DIR/logs/paper_complete_%j.out"
  --error="$ROOT_DIR/logs/paper_complete_%j.err"
)

if (( ${#missing_jobs[@]} > 0 )); then
  dep="$(IFS=:; echo "${missing_jobs[*]}")"
  aggregate_args=(--dependency="afterok:${dep}" "${aggregate_args[@]}")
fi

PAPER_JOB_ID="$(
  sbatch --parsable \
    "${aggregate_args[@]}" \
    "$ROOT_DIR/scripts/build_paper_complete_report.sh"
)"

echo "missing protocol jobs: ${missing_jobs[*]:-none}"
echo "paper complete job: $PAPER_JOB_ID"
