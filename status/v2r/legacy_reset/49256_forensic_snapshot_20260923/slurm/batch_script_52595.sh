#!/bin/bash
set -euo pipefail
ROOT=/home/kimhj/repairable-state-discovery-v2-exec
BASE_FORENSIC=/home/kimhj/forensics/v2_50752_confirmation_20260921
OUT=${BASE_FORENSIC}_shard3
mkdir -p "$OUT"
export SHARD_START=26004
export SHARD_END=34672
export PYTHONPATH="$ROOT"
PY=/home/kimhj/llada8b_basic/.venv/bin/python
"$PY" - <<'PY'
from pathlib import Path
src_path = Path('/home/kimhj/forensic_resume_50752.py')
src = src_path.read_text(encoding='utf-8')
base = '/home/kimhj/forensics/v2_50752_confirmation_20260921'
out = base + '_shard3'
src = src.replace('FORENSIC = Path("/home/kimhj/forensics/v2_50752_confirmation_20260921")', f'FORENSIC = Path("{out}")')
src = src.replace('CANDIDATES = FORENSIC / "confirmation_candidates.jsonl"', f'CANDIDATES = Path("{base}/confirmation_candidates.jsonl")')
ns = {'__name__': '__main__', '__file__': str(src_path)}
exec(compile(src, str(src_path), 'exec'), ns, ns)
PY
if [ -f "$OUT/first_failure.json" ]; then
  echo "forensic failure found in shard3" >&2
  exit 42
fi
if ! grep -q '"status": "complete"' "$OUT/shard-00.summary.json" 2>/dev/null; then
  echo "shard3 did not complete" >&2
  exit 43
fi
