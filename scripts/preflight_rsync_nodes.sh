#!/bin/bash
# Check whether independent nodes are ready for rsync-based execution.
# Usage: preflight_rsync_nodes.sh HOST [HOST ...]
set -u

SSH_OPTS="${SYNC_SSH_OPTS:--o BatchMode=yes -o ConnectTimeout=5}"
if (( $# == 0 )); then
  echo "usage: $0 HOST [HOST ...]" >&2
  exit 2
fi

failed=0
for host in "$@"; do
  echo "=== $host ==="
  if ! output="$(ssh $SSH_OPTS -- "$host" 'set -u; printf "host=%s\\n" "$(hostname)"; printf "home=%s\\n" "$HOME"; command -v rsync; command -v sbatch; command -v squeue; df -h . | tail -n 1' 2>&1)"; then
    echo "$output"
    echo "STATUS=BLOCKED_SSH"
    failed=1
    continue
  fi
  echo "$output"
  if ssh $SSH_OPTS -- "$host" 'test -x /home/kimhj/llada8b_basic/.venv/bin/python || test -x /data/kimhj/llada8b_basic/.venv/bin/python' >/dev/null 2>&1; then
    echo "python_runtime=found"
  else
    echo "python_runtime=MISSING"
    failed=1
  fi
  if ssh $SSH_OPTS -- "$host" 'test -d /home/kimhj/.cache/huggingface || test -d /data/kimhj/.cache/huggingface' >/dev/null 2>&1; then
    echo "huggingface_cache=found"
  else
    echo "huggingface_cache=MISSING"
    failed=1
  fi
  if ssh $SSH_OPTS -- "$host" 'test -d /home/kimhj/rfba || test -d /data/kimhj/rfba || test -d /home/kimhj/Rethinking-Fixed-Block-Assumptions-in-Diffusion-Language-Model-Decoding || test -d /data/kimhj/Rethinking-Fixed-Block-Assumptions-in-Diffusion-Language-Model-Decoding' >/dev/null 2>&1; then
    echo "rfba_checkout=found"
  else
    echo "rfba_checkout=MISSING"
    failed=1
  fi
done

if (( failed )); then
  exit 1
fi
