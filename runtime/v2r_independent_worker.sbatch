#!/usr/bin/env bash
set -euo pipefail

: "${V2R_EXEC_ROOT:?}"
: "${V2R_PY:?}"
: "${V2R_MANIFEST:?}"
: "${V2R_GATES:?}"
: "${V2R_SHARD:?}"
: "${V2R_RUN_DIR:?}"

cd "$V2R_EXEC_ROOT"
export PYTHONPATH="${V2R_PYTHONPATH:-$V2R_EXEC_ROOT}"
export HF_DATASETS_CACHE="${V2R_DATASETS_CACHE:-/var/tmp/kimhj-v2r-reference/datasets}"
export HF_MODULES_CACHE="${V2R_MODULES_CACHE:-/var/tmp/kimhj-v2r-reference/modules}"
export HF_HUB_CACHE="${V2R_HUB_CACHE:-/var/tmp/kimhj-v2r-reference/hub}"
export HF_HOME="${V2R_HF_HOME:-/var/tmp/kimhj-v2r-independent/hf-home-${SLURMD_NODENAME:-local}}"
export HF_XET_CACHE="${V2R_XET_CACHE:-$HF_HOME/xet}"
export HF_HUB_DISABLE_XET="${V2R_HUB_DISABLE_XET:-1}"
mkdir -p "$HF_HOME" "$HF_XET_CACHE" "$HF_DATASETS_CACHE" "$HF_MODULES_CACHE" "$HF_HUB_CACHE"
export OMP_NUM_THREADS="${OMP_NUM_THREADS:-4}"
export TOKENIZERS_PARALLELISM=false
export PYTHONDONTWRITEBYTECODE=1

exec "$V2R_PY" "$V2R_EXEC_ROOT/scripts/v2r_worker.py" \
  --manifest "$V2R_MANIFEST" \
  --shard "$V2R_SHARD" \
  --run-dir "$V2R_RUN_DIR" \
  --gates "$V2R_GATES"
