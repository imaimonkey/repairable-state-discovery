#!/bin/bash
# Copy the lightweight experiment workspace to an independent Slurm node.
# Large model caches and run artifacts are intentionally excluded.
# Usage: rsync_node_workspace.sh DEST_HOST DEST_ROOT [SOURCE_ROOT]
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_ROOT="${3:-$(cd -- "$SCRIPT_DIR/.." && pwd)}"
DEST_HOST="${1:-}"
DEST_ROOT="${2:-}"

if [[ -z "$DEST_HOST" || -z "$DEST_ROOT" ]]; then
  echo "usage: $0 DEST_HOST DEST_ROOT [SOURCE_ROOT]" >&2
  exit 2
fi
if [[ ! -d "$SOURCE_ROOT/.git" ]]; then
  echo "source is not a git worktree: $SOURCE_ROOT" >&2
  exit 1
fi
if ! command -v rsync >/dev/null 2>&1 || ! command -v ssh >/dev/null 2>&1; then
  echo "rsync and ssh are required" >&2
  exit 1
fi

for value in "$DEST_HOST" "$DEST_ROOT" "$SOURCE_ROOT"; do
  if [[ "$value" == *[!A-Za-z0-9_./:@+-]* ]]; then
    echo "unsafe host/path: $value" >&2
    exit 2
  fi
done

if ! git -C "$SOURCE_ROOT" diff --quiet -- . ':(exclude).codex-goal'; then
  echo "source worktree has tracked changes; commit them before distribution" >&2
  exit 1
fi

commit="$(git -C "$SOURCE_ROOT" rev-parse HEAD)"
remote_workspace="${DEST_ROOT%/}/repairable-state-discovery"
SSH_OPTS="${SYNC_SSH_OPTS:--o BatchMode=yes}"
RSYNC_SSH="ssh $SSH_OPTS"

echo "[workspace] source=$SOURCE_ROOT"
echo "[workspace] commit=$commit"
echo "[workspace] destination=$DEST_HOST:$remote_workspace"

ssh $SSH_OPTS -- "$DEST_HOST" "mkdir -p '$remote_workspace' && command -v rsync >/dev/null"

# Do not use --delete by default: a remote workspace may contain user files.
# Set RSYNC_DELETE=1 only when the destination is a disposable experiment clone.
delete_arg=()
if [[ "${RSYNC_DELETE:-0}" == 1 ]]; then
  delete_arg+=(--delete-delay)
fi

rsync -a --partial --append-verify "${delete_arg[@]}" \
  --exclude='.git/' \
  --exclude='.venv/' \
  --exclude='.codex-goal/' \
  --exclude='logs/' \
  --exclude='repairable_diffusion/outputs/runs/' \
  --exclude='repairable_diffusion/outputs/cache/' \
  --exclude='results/benchmark_complete_reports/' \
  --exclude='results/benchmark_extended_analysis/' \
  -e "$RSYNC_SSH" \
  "$SOURCE_ROOT/" "$DEST_HOST:$remote_workspace/"

ssh $SSH_OPTS -- "$DEST_HOST" \
  "printf '%s\\n' '$commit' > '$remote_workspace/.experiment_commit'"

remote_commit="$(ssh $SSH_OPTS -- "$DEST_HOST" "cat '$remote_workspace/.experiment_commit'")"
if [[ "$remote_commit" != "$commit" ]]; then
  echo "remote commit marker mismatch: $remote_commit != $commit" >&2
  exit 1
fi
echo "[workspace] synchronized successfully"
