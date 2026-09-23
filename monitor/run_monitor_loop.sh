#!/usr/bin/env bash
set -u

ROOT="/data/kimhj/repairable-state-discovery-live-monitor-20260923"
PYTHON="/home/kimhj/llada8b_basic/.venv/bin/python"
RUNTIME="/data/kimhj/.cache/rsd-live-monitor"
LOG="$RUNTIME/monitor.log"
mkdir -p "$RUNTIME"

exec 9>"$RUNTIME/loop.lock"
if ! flock -n 9; then
  printf '%s monitor already running\n' "$(date --iso-8601=seconds)" >> "$LOG"
  exit 0
fi

printf '%s monitor loop started pid=%s\n' "$(date --iso-8601=seconds)" "$$" >> "$LOG"
sleep 1800
while true; do
  if ! RSD_MONITOR_RUNTIME="$RUNTIME" "$PYTHON" "$ROOT/monitor/live_monitor.py" >> "$LOG" 2>&1; then
    printf '%s cycle failed; next cycle will retry\n' "$(date --iso-8601=seconds)" >> "$LOG"
  fi
  sleep 1800
done
