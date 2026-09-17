#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd -- "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT_DIR"

mkdir -p "$ROOT_DIR/logs"

MAX_GPU_JOBS="${MAX_GPU_JOBS:-3}"
PROTOCOL_TIME="${PROTOCOL_TIME:-30-00:00:00}"
AGGREGATE_MEM="${AGGREGATE_MEM:-8G}"
AGGREGATE_NODE="${AGGREGATE_NODE:-devbox}"

if ! [[ "$MAX_GPU_JOBS" =~ ^[1-9][0-9]*$ ]]; then
  echo "MAX_GPU_JOBS must be a positive integer, got: $MAX_GPU_JOBS" >&2
  exit 2
fi

array_job_id="$(
  sbatch --parsable \
    --array="0-6%${MAX_GPU_JOBS}" \
    --time="$PROTOCOL_TIME" \
    --export=ALL,REPAIRABLE_ROOT="$ROOT_DIR" \
    "$ROOT_DIR/scripts/run_benchmark_protocol_array.sh"
)"

aggregate_job_id="$(
  sbatch --parsable \
    --dependency="afterany:${array_job_id}" \
    --job-name=repair_benchmark_complete \
    --mem="$AGGREGATE_MEM" \
    --nodelist="$AGGREGATE_NODE" \
    --export=ALL,REPAIRABLE_ROOT="$ROOT_DIR" \
    --output="$ROOT_DIR/logs/benchmark_complete_%j.out" \
    --error="$ROOT_DIR/logs/benchmark_complete_%j.err" \
    "$ROOT_DIR/scripts/build_benchmark_complete_report.sh"
)"

echo "protocol array job: $array_job_id"
echo "max concurrent protocol jobs: $MAX_GPU_JOBS"
echo "protocol time limit: $PROTOCOL_TIME"
echo "aggregate job: $aggregate_job_id"
