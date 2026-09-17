#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd -- "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT_DIR"

mkdir -p "$ROOT_DIR/logs"

PROTOCOL_NODE="${PROTOCOL_NODE:-$(hostname)}"
AGGREGATE_NODE="${AGGREGATE_NODE:-$PROTOCOL_NODE}"
MAX_PARALLEL_GPUS="${MAX_PARALLEL_GPUS:-4}"
AGGREGATE_MEM="${AGGREGATE_MEM:-8G}"
PYTHON_BIN="${PYTHON_BIN:-/home/kimhj/llada8b_basic/.venv/bin/python}"
HF_HOME="${HF_HOME:-/data/kimhj/.cache/huggingface}"
RFBA_ROOT="${RFBA_ROOT:-/home/kimhj/Rethinking-Fixed-Block-Assumptions-in-Diffusion-Language-Model-Decoding}"

if ! command -v sbatch >/dev/null 2>&1 || ! command -v squeue >/dev/null 2>&1; then
  echo "Slurm sbatch/squeue are required for benchmark-complete submission" >&2
  exit 1
fi
if ! scontrol show node "$PROTOCOL_NODE" >/dev/null 2>&1; then
  echo "Unknown Slurm node: $PROTOCOL_NODE" >&2
  exit 1
fi
gpu_count="$(scontrol show node "$PROTOCOL_NODE" | sed -n 's/.*CfgTRES=.*gres\/gpu=\([0-9][0-9]*\).*/\1/p' | head -n1)"
if [[ -n "$gpu_count" && "$MAX_PARALLEL_GPUS" -gt "$gpu_count" ]]; then
  echo "MAX_PARALLEL_GPUS=$MAX_PARALLEL_GPUS exceeds $PROTOCOL_NODE GPU count=$gpu_count" >&2
  exit 1
fi

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

check_run() {
  local family="$1"
  local run_name="$2"
  if [[ "$family" == "diffusion" ]]; then
    [[ -f "$ROOT_DIR/repairable_diffusion/outputs/runs/$run_name/report.json" ]] \
      && jq -e '.dataset and .selection_eval' "$ROOT_DIR/repairable_diffusion/outputs/runs/$run_name/report.json" >/dev/null
  else
    [[ -f "$ROOT_DIR/repairable_diffusion/outputs/runs/$run_name/ar_baseline_summary.json" ]] \
      && jq -e '.pass_at_1 != null and .pass_at_k != null' "$ROOT_DIR/repairable_diffusion/outputs/runs/$run_name/ar_baseline_summary.json" >/dev/null
  fi
}

find_existing_jobs() {
  local job_name="$1"
  squeue \
    --noheader \
    --user="${USER:-$(id -un)}" \
    --name="$job_name" \
    --states=PENDING,RUNNING,CONFIGURING,COMPLETING \
    --format="%A" \
    | awk 'NF'
}

submit_run_if_missing() {
  local label="$1"
  local job_name="$2"
  local protocol="$3"
  local run_name="$4"
  local family="$5"
  if check_run "$family" "$run_name"; then
    echo "[skip] $label run already complete: $run_name" >&2
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
    PROTOCOL_RUN_NAMES="$run_name" \
    PROTOCOL_FAMILIES="$family" \
    PROTOCOL_WRITE_REPORT=false \
    RFBA_ROOT="$RFBA_ROOT" \
    HF_HOME="$HF_HOME" \
    PYTHON_BIN="$PYTHON_BIN" \
      sbatch --parsable \
        --job-name="$job_name" \
        --nodelist="$PROTOCOL_NODE" \
        --output="$ROOT_DIR/logs/${job_name}_%j.out" \
        --error="$ROOT_DIR/logs/${job_name}_%j.err" \
        --export="ALL,PROTOCOL_PATH=$protocol,PROTOCOL_RUN_NAMES=$run_name,PROTOCOL_FAMILIES=$family,PROTOCOL_WRITE_REPORT=false,RFBA_ROOT=$RFBA_ROOT,HF_HOME=$HF_HOME,PYTHON_BIN=$PYTHON_BIN" \
        scripts/run_protocol_repairability_final.sh
  )"
  echo "[submit] $label run=$run_name gpu=1 node=$PROTOCOL_NODE job=$job_id" >&2
  echo "$job_id"
}

submit_protocol() {
  local label="$1"
  local report="$2"
  local expected_diffusion="$3"
  local expected_ar="$4"
  shift 4
  local protocol="$1"
  shift

  if check_report "$report" "$expected_diffusion" "$expected_ar"; then
    echo "[skip] $label protocol report already complete: $report" >&2
    echo ""
    return 0
  fi

  local run_jobs=()
  while (( "$#" )); do
    local run_name="$1"
    local family="$2"
    local job_name="$3"
    shift 3
    local maybe_job
    maybe_job="$(submit_run_if_missing "$label" "$job_name" "$protocol" "$run_name" "$family")"
    [[ -n "$maybe_job" ]] && run_jobs+=("$maybe_job")
  done

  local aggregate_job_name="repair_bm_aggregate_${label//[^a-zA-Z0-9]/_}"
  local existing_aggregate
  existing_aggregate="$(find_existing_jobs "$aggregate_job_name" | paste -sd: -)"
  if [[ -n "$existing_aggregate" ]]; then
    echo "[wait] $label protocol aggregation already queued/running as $existing_aggregate" >&2
    echo "$existing_aggregate"
    return 0
  fi

  local aggregate_args=(
    --job-name="$aggregate_job_name"
    --mem="$AGGREGATE_MEM"
    --nodelist="$AGGREGATE_NODE"
    --export="ALL,REPAIRABLE_ROOT=$ROOT_DIR,PROTOCOL_PATH=$protocol,PYTHON_BIN=$PYTHON_BIN"
    --output="$ROOT_DIR/logs/${aggregate_job_name}_%j.out"
    --error="$ROOT_DIR/logs/${aggregate_job_name}_%j.err"
  )
  if (( ${#run_jobs[@]} > 0 )); then
    local dep
    dep="$(IFS=:; echo "${run_jobs[*]}")"
    aggregate_args=(--dependency="afterok:${dep}" "${aggregate_args[@]}")
  fi
  local aggregate_id
  aggregate_id="$(sbatch --parsable "${aggregate_args[@]}" scripts/aggregate_protocol_report.sh)"
  echo "[submit] $label protocol aggregation job=$aggregate_id after=${run_jobs[*]:-none}" >&2
  echo "$aggregate_id"
}

protocol_jobs=()

maybe_job="$(submit_protocol math500_full \
  results/generated_configs/protocol_math500_full_report.json 1 2 \
  repairable_diffusion/configs/final/protocol_math500_full.yaml \
  math500_full_llada8b_fast diffusion repair_bm_math500_full_diffusion \
  math500_full_ar_qwen25_7b ar repair_bm_math500_full_qwen \
  math500_full_ar_llama31_8b ar repair_bm_math500_full_llama)"
[[ -n "$maybe_job" ]] && protocol_jobs+=("$maybe_job")

maybe_job="$(submit_protocol gsm8k_full \
  results/generated_configs/protocol_gsm8k_full_report.json 1 2 \
  repairable_diffusion/configs/final/protocol_gsm8k_full.yaml \
  gsm8k_full_llada8b_fast diffusion repair_bm_gsm8k_full_diffusion \
  gsm8k_full_ar_qwen25_7b ar repair_bm_gsm8k_full_qwen \
  gsm8k_full_ar_llama31_8b ar repair_bm_gsm8k_full_llama)"
[[ -n "$maybe_job" ]] && protocol_jobs+=("$maybe_job")

maybe_job="$(submit_protocol math500_full_robustness \
  results/generated_configs/protocol_math500_full_robustness_report.json 3 0 \
  repairable_diffusion/configs/final/protocol_math500_full_robustness.yaml \
  math500_full_seed29_llada8b_fast diffusion repair_bm_math500_seed29 \
  math500_full_stride16_llada8b_fast diffusion repair_bm_math500_stride16 \
  math500_full_branch2_llada8b_fast diffusion repair_bm_math500_branch2)"
[[ -n "$maybe_job" ]] && protocol_jobs+=("$maybe_job")

maybe_job="$(submit_protocol math500_full_seed_repeats \
  results/generated_configs/protocol_math500_full_seed_repeats_report.json 2 0 \
  repairable_diffusion/configs/final/protocol_math500_full_seed_repeats.yaml \
  math500_full_seed41_llada8b_fast diffusion repair_bm_math500_seed41 \
  math500_full_seed53_llada8b_fast diffusion repair_bm_math500_seed53)"
[[ -n "$maybe_job" ]] && protocol_jobs+=("$maybe_job")

maybe_job="$(submit_protocol gsm8k_full_seed_repeats \
  results/generated_configs/protocol_gsm8k_full_seed_repeats_report.json 2 0 \
  repairable_diffusion/configs/final/protocol_gsm8k_full_seed_repeats.yaml \
  gsm8k_full_seed29_llada8b_fast diffusion repair_bm_gsm8k_seed29 \
  gsm8k_full_seed41_llada8b_fast diffusion repair_bm_gsm8k_seed41)"
[[ -n "$maybe_job" ]] && protocol_jobs+=("$maybe_job")

maybe_job="$(submit_protocol math500_full_dream_backbone \
  results/generated_configs/protocol_math500_full_dream_backbone_report.json 1 0 \
  repairable_diffusion/configs/final/protocol_math500_full_dream_backbone.yaml \
  math500_full_dream_v0_instruct_7b diffusion repair_bm_math500_dream)"
[[ -n "$maybe_job" ]] && protocol_jobs+=("$maybe_job")

maybe_job="$(submit_protocol gsm8k_full_dream_backbone \
  results/generated_configs/protocol_gsm8k_full_dream_backbone_report.json 1 0 \
  repairable_diffusion/configs/final/protocol_gsm8k_full_dream_backbone.yaml \
  gsm8k_full_dream_v0_instruct_7b diffusion repair_bm_gsm8k_dream)"
[[ -n "$maybe_job" ]] && protocol_jobs+=("$maybe_job")

benchmark_outputs_complete() {
  local aggregate="$ROOT_DIR/results/benchmark_complete_reports/aggregate_report.json"
  local extended="$ROOT_DIR/results/benchmark_extended_analysis/extended_repair_analysis.json"
  [[ -f "$aggregate" && -f "$extended" ]] && jq -e \
    '((.diffusion_rows | length) == 11) and ((.ar_rows | length) == 4)' \
    "$aggregate" >/dev/null
}

if benchmark_outputs_complete; then
  echo "benchmark complete job: already complete"
  exit 0
fi

existing_benchmark="$(find_existing_jobs repair_benchmark_complete | paste -sd: -)"
if [[ -n "$existing_benchmark" ]]; then
  echo "benchmark complete job: $existing_benchmark"
  exit 0
fi

aggregate_args=(
  --job-name=repair_benchmark_complete
  --mem="$AGGREGATE_MEM"
  --nodelist="$AGGREGATE_NODE"
  --export="ALL,REPAIRABLE_ROOT=$ROOT_DIR,PYTHON_BIN=$PYTHON_BIN"
  --output="$ROOT_DIR/logs/benchmark_complete_%j.out"
  --error="$ROOT_DIR/logs/benchmark_complete_%j.err"
)
if (( ${#protocol_jobs[@]} > 0 )); then
  dep="$(IFS=:; echo "${protocol_jobs[*]}")"
  aggregate_args=(--dependency="afterok:${dep}" "${aggregate_args[@]}")
fi

BENCHMARK_JOB_ID="$(sbatch --parsable "${aggregate_args[@]}" scripts/build_benchmark_complete_report.sh)"
echo "protocol aggregation jobs: ${protocol_jobs[*]:-none}"
echo "benchmark complete job: $BENCHMARK_JOB_ID"
