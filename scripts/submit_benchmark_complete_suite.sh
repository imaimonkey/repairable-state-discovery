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

find_existing_jobs() {
  local job_name="$1"
  if ! command -v squeue >/dev/null 2>&1; then
    return 0
  fi
  squeue \
    --noheader \
    --user="${USER:-$(id -un)}" \
    --name="$job_name" \
    --states=PENDING,RUNNING,CONFIGURING,COMPLETING \
    --format="%A" \
    | awk 'NF'
}

benchmark_outputs_complete() {
  local aggregate="$ROOT_DIR/results/benchmark_complete_reports/aggregate_report.json"
  local extended="$ROOT_DIR/results/benchmark_extended_analysis/extended_repair_analysis.json"
  [[ -f "$aggregate" && -f "$extended" ]] && jq -e \
    '((.diffusion_rows | length) == 11) and ((.ar_rows | length) == 4)' \
    "$aggregate" >/dev/null
}

submit_protocol_if_missing() {
  local label="$1"
  local job_name="$2"
  local protocol="$3"
  local report="$4"
  local expected_diffusion="$5"
  local expected_ar="$6"
  if check_report "$report" "$expected_diffusion" "$expected_ar"; then
    echo "[skip] $label report already complete: $report" >&2
    return 0
  fi
  local existing_jobs
  existing_jobs="$(find_existing_jobs "$job_name" | paste -sd: -)"
  if [[ -n "$existing_jobs" ]]; then
    echo "[wait] $label already queued/running as $existing_jobs" >&2
    echo "$existing_jobs"
    return 0
  fi
  local job_id
  job_id="$(
    PROTOCOL_PATH="$protocol" \
      sbatch --parsable --job-name="$job_name" scripts/run_protocol_repairability_final.sh
  )"
  echo "[submit] $label: $job_id" >&2
  echo "$job_id"
}

missing_jobs=()

maybe_job="$(submit_protocol_if_missing \
  "math500-full" \
  repair_bm_math500_full \
  repairable_diffusion/configs/final/protocol_math500_full.yaml \
  results/generated_configs/protocol_math500_full_report.json \
  1 2)"
[[ -n "$maybe_job" ]] && missing_jobs+=("$maybe_job")

maybe_job="$(submit_protocol_if_missing \
  "gsm8k-full" \
  repair_bm_gsm8k_full \
  repairable_diffusion/configs/final/protocol_gsm8k_full.yaml \
  results/generated_configs/protocol_gsm8k_full_report.json \
  1 2)"
[[ -n "$maybe_job" ]] && missing_jobs+=("$maybe_job")

maybe_job="$(submit_protocol_if_missing \
  "math500-full-robustness" \
  repair_bm_math500_robust \
  repairable_diffusion/configs/final/protocol_math500_full_robustness.yaml \
  results/generated_configs/protocol_math500_full_robustness_report.json \
  3 0)"
[[ -n "$maybe_job" ]] && missing_jobs+=("$maybe_job")

maybe_job="$(submit_protocol_if_missing \
  "math500-full-seed-repeats" \
  repair_bm_math500_seeds \
  repairable_diffusion/configs/final/protocol_math500_full_seed_repeats.yaml \
  results/generated_configs/protocol_math500_full_seed_repeats_report.json \
  2 0)"
[[ -n "$maybe_job" ]] && missing_jobs+=("$maybe_job")

maybe_job="$(submit_protocol_if_missing \
  "gsm8k-full-seed-repeats" \
  repair_bm_gsm8k_seeds \
  repairable_diffusion/configs/final/protocol_gsm8k_full_seed_repeats.yaml \
  results/generated_configs/protocol_gsm8k_full_seed_repeats_report.json \
  2 0)"
[[ -n "$maybe_job" ]] && missing_jobs+=("$maybe_job")

maybe_job="$(submit_protocol_if_missing \
  "math500-full-dream-backbone" \
  repair_bm_math500_dream \
  repairable_diffusion/configs/final/protocol_math500_full_dream_backbone.yaml \
  results/generated_configs/protocol_math500_full_dream_backbone_report.json \
  1 0)"
[[ -n "$maybe_job" ]] && missing_jobs+=("$maybe_job")

maybe_job="$(submit_protocol_if_missing \
  "gsm8k-full-dream-backbone" \
  repair_bm_gsm8k_dream \
  repairable_diffusion/configs/final/protocol_gsm8k_full_dream_backbone.yaml \
  results/generated_configs/protocol_gsm8k_full_dream_backbone_report.json \
  1 0)"
[[ -n "$maybe_job" ]] && missing_jobs+=("$maybe_job")

if benchmark_outputs_complete; then
  echo "missing protocol jobs: ${missing_jobs[*]:-none}"
  echo "benchmark complete job: already complete"
  exit 0
fi

existing_aggregate="$(find_existing_jobs repair_benchmark_complete | paste -sd: -)"
if [[ -n "$existing_aggregate" ]]; then
  echo "missing protocol jobs: ${missing_jobs[*]:-none}"
  echo "benchmark complete job: $existing_aggregate"
  exit 0
fi

aggregate_args=(
  --job-name=repair_benchmark_complete
  --mem="$AGGREGATE_MEM"
  --nodelist="$AGGREGATE_NODE"
  --export=ALL,REPAIRABLE_ROOT="$ROOT_DIR"
  --output="$ROOT_DIR/logs/benchmark_complete_%j.out"
  --error="$ROOT_DIR/logs/benchmark_complete_%j.err"
)

if (( ${#missing_jobs[@]} > 0 )); then
  dep="$(IFS=:; echo "${missing_jobs[*]}")"
  aggregate_args=(--dependency="afterok:${dep}" "${aggregate_args[@]}")
fi

BENCHMARK_JOB_ID="$(
  sbatch --parsable \
    "${aggregate_args[@]}" \
    "$ROOT_DIR/scripts/build_benchmark_complete_report.sh"
)"

echo "missing protocol jobs: ${missing_jobs[*]:-none}"
echo "benchmark complete job: $BENCHMARK_JOB_ID"
