#!/bin/bash
# Pull one completed run from an independent Slurm node to the collector.
# Usage: pull_run_artifacts.sh REMOTE_HOST REMOTE_RUN_DIR LOCAL_RUN_ROOT [RUN_NAME] [REQUIRED_FILES]
set -euo pipefail

REMOTE_HOST="${1:-}"
REMOTE_RUN_DIR="${2:-}"
LOCAL_RUN_ROOT="${3:-}"
RUN_NAME="${4:-$(basename "${REMOTE_RUN_DIR:-}")}"
REQUIRED_SPEC="${5:-${SYNC_REQUIRED_FILES:-report.json,trajectories.pkl,oracle_repair.json,repair_predictor.json}}"

if [[ -z "$REMOTE_HOST" || -z "$REMOTE_RUN_DIR" || -z "$LOCAL_RUN_ROOT" || -z "$RUN_NAME" ]]; then
  echo "usage: $0 REMOTE_HOST REMOTE_RUN_DIR LOCAL_RUN_ROOT [RUN_NAME] [REQUIRED_FILES]" >&2
  exit 2
fi
if ! command -v rsync >/dev/null 2>&1 || ! command -v ssh >/dev/null 2>&1; then
  echo "rsync and ssh are required" >&2
  exit 1
fi

for value in "$REMOTE_HOST" "$REMOTE_RUN_DIR" "$LOCAL_RUN_ROOT" "$RUN_NAME" "$REQUIRED_SPEC"; do
  if [[ "$value" == *[!A-Za-z0-9_./,:@+-]* ]]; then
    echo "unsafe host/path/run specification: $value" >&2
    exit 2
  fi
done

IFS=',' read -r -a REQUIRED_FILES <<< "$REQUIRED_SPEC"
if (( ${#REQUIRED_FILES[@]} == 0 )); then
  echo "no required artifacts supplied" >&2
  exit 2
fi

LOCAL_DIR="${LOCAL_RUN_ROOT%/}/$RUN_NAME"
SSH_OPTS="${SYNC_SSH_OPTS:--o BatchMode=yes}"
RSYNC_SSH="ssh $SSH_OPTS"

if [[ -f "$LOCAL_DIR/.sync_complete" ]]; then
  echo "[pull] already complete: $LOCAL_DIR"
  exit 0
fi

ssh $SSH_OPTS -- "$REMOTE_HOST" "test -d '$REMOTE_RUN_DIR'"
for required in "${REQUIRED_FILES[@]}"; do
  if [[ -z "$required" || "$required" == *[!A-Za-z0-9_.-]* ]]; then
    echo "unsafe required artifact: $required" >&2
    exit 2
  fi
  if ! ssh $SSH_OPTS -- "$REMOTE_HOST" "test -f '$REMOTE_RUN_DIR/$required'"; then
    echo "[pull] remote artifact is not complete: $REMOTE_HOST:$REMOTE_RUN_DIR/$required" >&2
    exit 1
  fi
done

mkdir -p "$LOCAL_DIR"
rsync -a --partial --append-verify \
  -e "$RSYNC_SSH" \
  "$REMOTE_HOST:$REMOTE_RUN_DIR/" "$LOCAL_DIR/"

for required in "${REQUIRED_FILES[@]}"; do
  if [[ ! -f "$LOCAL_DIR/$required" ]]; then
    echo "[pull] local artifact is missing: $LOCAL_DIR/$required" >&2
    exit 1
  fi
done

{
  printf 'pulled_at=%s\n' "$(date -Is)"
  printf 'source_host=%s\n' "$REMOTE_HOST"
  printf 'source_dir=%s\n' "$REMOTE_RUN_DIR"
} > "$LOCAL_DIR/.sync_complete"
echo "[pull] complete: $REMOTE_HOST:$REMOTE_RUN_DIR -> $LOCAL_DIR"
