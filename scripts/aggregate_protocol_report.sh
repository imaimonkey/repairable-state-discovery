#!/bin/bash
# CPU-only post-processing job: materialize one complete protocol report from
# the run-level artifacts after all selected GPU jobs have succeeded.
#SBATCH --job-name=repair_protocol_aggregate
#SBATCH --output=/home/kimhj/repairable-state-discovery/logs/protocol_aggregate_%j.out
#SBATCH --error=/home/kimhj/repairable-state-discovery/logs/protocol_aggregate_%j.err
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=24:00:00

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="${REPAIRABLE_ROOT:-$(cd -- "$SCRIPT_DIR/.." && pwd)}"
cd "$ROOT_DIR"

if [[ -f .venv/bin/activate ]]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
fi

if [[ -z "${PYTHON_BIN:-}" ]]; then
  if [[ -x "$ROOT_DIR/.venv/bin/python" ]]; then
    PYTHON_BIN="$ROOT_DIR/.venv/bin/python"
  elif [[ -x /home/kimhj/llada8b_basic/.venv/bin/python ]]; then
    PYTHON_BIN=/home/kimhj/llada8b_basic/.venv/bin/python
  else
    PYTHON_BIN="$(command -v python || command -v python3 || true)"
  fi
fi
if [[ -z "$PYTHON_BIN" ]]; then
  echo "python not found on PATH" >&2
  exit 1
fi
if [[ -z "${PROTOCOL_PATH:-}" ]]; then
  echo "PROTOCOL_PATH is required" >&2
  exit 2
fi

echo "[protocol-aggregate] protocol: $PROTOCOL_PATH"
echo "[protocol-aggregate] host: $(hostname)"
"$PYTHON_BIN" -m repairable_diffusion.src.run_protocol \
  --protocol "$PROTOCOL_PATH" \
  --reuse-only
