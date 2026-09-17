#!/bin/bash
# Synchronize one node-local run directory to an artifact collector.
# Usage: sync_run_artifacts.sh RUN_DIR DEST_HOST DEST_ROOT [RUN_NAME]
set -euo pipefail

RUN_DIR="${1:-}"
DEST_HOST="${2:-}"
DEST_ROOT="${3:-}"
RUN_NAME="${4:-$(basename "${RUN_DIR:-}")}"

if [[ -z "$RUN_DIR" || -z "$DEST_HOST" || -z "$DEST_ROOT" ]]; then
  echo "usage: $0 RUN_DIR DEST_HOST DEST_ROOT [RUN_NAME]" >&2
  exit 2
fi
if [[ ! -d "$RUN_DIR" ]]; then
  echo "run directory does not exist: $RUN_DIR" >&2
  exit 1
fi
if ! command -v rsync >/dev/null 2>&1 || ! command -v ssh >/dev/null 2>&1; then
  echo "rsync and ssh are required" >&2
  exit 1
fi

for value in "$DEST_HOST" "$DEST_ROOT" "$RUN_NAME"; do
  if [[ "$value" == *[!A-Za-z0-9_./:@-]* ]]; then
    echo "unsafe destination or run name: $value" >&2
    exit 2
  fi
done

DEST_DIR="${DEST_ROOT%/}/$RUN_NAME"
SSH_OPTS="${SYNC_SSH_OPTS:--o BatchMode=yes}"
RSYNC_SSH="ssh $SSH_OPTS"

if ssh $SSH_OPTS -- "$DEST_HOST" "test -f '$DEST_DIR/.sync_complete'"; then
  echo "[sync] already complete: $DEST_HOST:$DEST_DIR"
  exit 0
fi

ssh $SSH_OPTS -- "$DEST_HOST" "mkdir -p '$DEST_DIR'"
rsync -a --partial --append-verify \
  -e "$RSYNC_SSH" \
  "$RUN_DIR/" "$DEST_HOST:$DEST_DIR/"

required_files=(report.json trajectories.pkl oracle_repair.json repair_predictor.json)
if [[ -n "${SYNC_REQUIRED_FILES:-}" ]]; then
  IFS=',' read -r -a required_files <<< "$SYNC_REQUIRED_FILES"
fi
for required in "${required_files[@]}"; do
  if ! ssh $SSH_OPTS -- "$DEST_HOST" "test -f '$DEST_DIR/$required'"; then
    echo "[sync] missing required artifact: $DEST_HOST:$DEST_DIR/$required" >&2
    exit 1
  fi
done

ssh $SSH_OPTS -- "$DEST_HOST" \
  "printf '%s\\n' 'synced_at='\"\$(date -Is)\" 'source_host='\"\$(hostname)\" > '$DEST_DIR/.sync_complete'"
echo "[sync] complete: $DEST_HOST:$DEST_DIR"
