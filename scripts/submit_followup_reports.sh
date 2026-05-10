#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd -- "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT_DIR"

mkdir -p "$ROOT_DIR/logs"

AGGREGATE_MEM="${AGGREGATE_MEM:-8G}"
AGGREGATE_NODE="${AGGREGATE_NODE:-devbox}"
SBATCH_NODE_ARGS=()
if [[ -n "$AGGREGATE_NODE" ]]; then
  SBATCH_NODE_ARGS=(--nodelist="$AGGREGATE_NODE")
fi

AFTER_JOB_ID="${AFTER_JOB_ID:-${1:-}}"
if [[ -z "$AFTER_JOB_ID" ]]; then
  echo "usage: AFTER_JOB_ID=<job_id> bash scripts/submit_followup_reports.sh"
  echo "   or: bash scripts/submit_followup_reports.sh <job_id>"
  echo "optional: AGGREGATE_MEM=8G AGGREGATE_NODE=devbox"
  exit 1
fi

FINAL_JOB_ID="$(
  sbatch --parsable \
    --dependency="afterok:${AFTER_JOB_ID}" \
    --job-name=repair_final_aggregate \
    --mem="$AGGREGATE_MEM" \
    "${SBATCH_NODE_ARGS[@]}" \
    --output="$ROOT_DIR/logs/final_aggregate_%j.out" \
    --error="$ROOT_DIR/logs/final_aggregate_%j.err" \
    "$ROOT_DIR/scripts/build_final_report.sh"
)"
echo "Submitted final aggregate job: $FINAL_JOB_ID"

SUBMISSION_JOB_ID="$(
  sbatch --parsable \
    --dependency="afterok:${FINAL_JOB_ID}" \
    --job-name=repair_submission_aggregate \
    --mem="$AGGREGATE_MEM" \
    "${SBATCH_NODE_ARGS[@]}" \
    --output="$ROOT_DIR/logs/submission_aggregate_%j.out" \
    --error="$ROOT_DIR/logs/submission_aggregate_%j.err" \
    "$ROOT_DIR/scripts/build_submission_report.sh"
)"
echo "Submitted submission aggregate job: $SUBMISSION_JOB_ID"
echo "Follow-up reports chained after job: $AFTER_JOB_ID"
