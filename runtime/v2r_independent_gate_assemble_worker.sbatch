#!/usr/bin/env bash
set -euo pipefail

: "${V2R_GATE_ROOT:?}"
: "${V2R_TASK:?}"
: "${V2R_PY:?}"
: "${V2R_EXEC_ROOT:?}"
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

# The dependency guarantees that R2 exited successfully.  Assemble the exact
# server-local reports atomically only after they exist; all shards write the
# same canonical bytes and therefore bind to one gate hash.
"$V2R_PY" - "$V2R_GATE_ROOT" "$V2R_TASK" "$V2R_GATES" <<'PY'
import json, os, sys, tempfile
from pathlib import Path
root, task, destination = sys.argv[1:]
base = Path(root) / "outputs" / "v2r_reference" / f"gate-78fe5d7-llada-{task}"
reports = {stage: json.loads((base / stage / "gate_report.json").read_text()) for stage in ("R0", "R1", "R2")}
if any(row.get("status") != "PASS" for row in reports.values()):
    raise SystemExit("SERVER_LOCAL_GATE_CHAIN_NOT_PASS")
data = json.dumps(reports, sort_keys=True, separators=(",", ":")) + "\n"
path = Path(destination)
path.parent.mkdir(parents=True, exist_ok=True)
fd, temp = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
with os.fdopen(fd, "w", encoding="utf-8") as handle:
    handle.write(data)
    handle.flush()
    os.fsync(handle.fileno())
os.replace(temp, path)
PY

exec "$V2R_PY" "$V2R_EXEC_ROOT/scripts/v2r_worker.py" \
  --manifest "$V2R_MANIFEST" \
  --shard "$V2R_SHARD" \
  --run-dir "$V2R_RUN_DIR" \
  --gates "$V2R_GATES"
