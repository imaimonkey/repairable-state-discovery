#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd -- "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT_DIR"

mkdir -p "$ROOT_DIR/logs"

submit_protocol() {
  local protocol_path="$1"
  PROTOCOL_PATH="$protocol_path" sbatch --parsable scripts/run_protocol_repairability_final.sh
}

MATH500_JOB_ID="$(submit_protocol repairable_diffusion/configs/final/protocol_math500_final.yaml)"
echo "Submitted MATH-500 main protocol: $MATH500_JOB_ID"

GSM8K_JOB_ID="$(submit_protocol repairable_diffusion/configs/final/protocol_gsm8k_final.yaml)"
echo "Submitted GSM8K main protocol: $GSM8K_JOB_ID"

ROBUSTNESS_JOB_ID="$(submit_protocol repairable_diffusion/configs/final/protocol_math500_submission_robustness.yaml)"
echo "Submitted MATH-500 robustness protocol: $ROBUSTNESS_JOB_ID"

AGGREGATE_JOB_ID="$(
  sbatch --parsable \
    --dependency="afterok:${MATH500_JOB_ID}:${GSM8K_JOB_ID}:${ROBUSTNESS_JOB_ID}" \
    --job-name=repair_submission_aggregate \
    --output="$ROOT_DIR/logs/submission_aggregate_%j.out" \
    --error="$ROOT_DIR/logs/submission_aggregate_%j.err" \
    --wrap="cd '$ROOT_DIR' && bash scripts/build_submission_report.sh"
)"
echo "Submitted submission aggregate job: $AGGREGATE_JOB_ID"
echo "Submission-ready suite chained successfully."
