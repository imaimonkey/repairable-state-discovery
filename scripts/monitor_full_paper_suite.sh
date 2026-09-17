#!/bin/bash
# Durable Slurm-side monitor for a submitted full-paper job chain.
# It keeps running independently of the Codex/SSH session and records state
# transitions for jobs across all configured Slurm nodes.
set -euo pipefail

JOB_SPEC="${FULL_PAPER_JOB_IDS:-${1:-}}"
INTERVAL="${FULL_PAPER_MONITOR_INTERVAL:-60}"

if [[ -z "$JOB_SPEC" ]]; then
  echo "usage: $0 JOB_ID[,JOB_ID...]" >&2
  exit 2
fi

IFS=',:' read -r -a JOB_IDS <<< "$JOB_SPEC"
if (( ${#JOB_IDS[@]} == 0 )); then
  echo "no job ids supplied" >&2
  exit 2
fi

job_csv="$(IFS=,; echo "${JOB_IDS[*]}")"
echo "[monitor] jobs: $job_csv"
echo "[monitor] host: $(hostname)"
echo "[monitor] interval: ${INTERVAL}s"

while true; do
  date -Is
  squeue -h -j "$job_csv" -o '%i %u %j %T %M %R' || true

  pending_or_running=0
  bad_jobs=()
  for job_id in "${JOB_IDS[@]}"; do
    state="$(sacct -X -n -P -j "$job_id" -o State 2>/dev/null | awk 'NF {print $1; exit}')"
    case "$state" in
      COMPLETED)
        ;;
      PENDING|RUNNING|CONFIGURING|COMPLETING|SUSPENDED|RESIZING|REQUEUED|REQUEUE_FED|REQUEUE_HOLD|SPECIAL_EXIT)
        pending_or_running=1
        ;;
      CANCELLED*|FAILED|TIMEOUT|OUT_OF_MEMORY|NODE_FAIL|BOOT_FAIL|DEADLINE|PREEMPTED|OOM|"")
        bad_jobs+=("$job_id:${state:-UNKNOWN}")
        ;;
      *)
        pending_or_running=1
        ;;
    esac
  done

  if (( ${#bad_jobs[@]} > 0 )); then
    echo "[monitor] terminal failures: ${bad_jobs[*]}" >&2
    exit 1
  fi
  if (( pending_or_running == 0 )); then
    echo "[monitor] all jobs completed successfully"
    exit 0
  fi
  sleep "$INTERVAL"
done
