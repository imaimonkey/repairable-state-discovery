#!/bin/bash
#SBATCH --job-name=repair_phase1
#SBATCH --output=/home/kimhj/repairable-state-discovery/logs/protocol_phase1_%j.out
#SBATCH --error=/home/kimhj/repairable-state-discovery/logs/protocol_phase1_%j.err
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=96G
#SBATCH --time=9999:00:00
#SBATCH --nodelist=devbox

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

find_repo_root() {
  local start_dir="$1"
  local dir="$start_dir"
  local remaining=8
  while ((remaining > 0)); do
    if [[ -f "$dir/pyproject.toml" && -d "$dir/repairable_diffusion" ]]; then
      echo "$dir"
      return 0
    fi
    local parent
    parent="$(cd -- "$dir/.." && pwd)"
    [[ "$parent" == "$dir" ]] && break
    dir="$parent"
    remaining=$((remaining - 1))
  done
  return 1
}

abs_path() {
  local value="$1"
  if [[ "$value" = /* ]]; then
    echo "$value"
  else
    echo "$ROOT_DIR/$value"
  fi
}

has_hf_token() {
  [[ -n "${HF_TOKEN:-}" || -n "${HUGGINGFACE_HUB_TOKEN:-}" || -n "${HUGGING_FACE_HUB_TOKEN:-}" ]]
}

load_hf_token_from_file() {
  local token_file="${HOME}/.secrets/hf_token"
  if has_hf_token; then
    return 0
  fi
  if [[ -f "$token_file" ]]; then
    local token
    token="$(tr -d '\r\n' < "$token_file")"
    if [[ -n "$token" ]]; then
      export HF_TOKEN="$token"
      export HUGGINGFACE_HUB_TOKEN="$token"
      export HUGGING_FACE_HUB_TOKEN="$token"
    fi
  fi
}

ROOT_CANDIDATE="${SLURM_SUBMIT_DIR:-$SCRIPT_DIR}"
ROOT_DIR="$(find_repo_root "$ROOT_CANDIDATE")" || {
  echo "Could not locate repo root from '$ROOT_CANDIDATE'."
  exit 1
}
cd "$ROOT_DIR"

mkdir -p "$ROOT_DIR/logs" "$ROOT_DIR/results" "$ROOT_DIR/repairable_diffusion/outputs/runs"

if [[ -f .venv/bin/activate ]]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
elif [[ -f /home/kimhj/provenance-decompositon/.venv/bin/activate ]]; then
  # shellcheck disable=SC1091
  source /home/kimhj/provenance-decompositon/.venv/bin/activate
fi

load_hf_token_from_file

PYTHON_BIN="$(command -v python || command -v python3 || true)"
if [[ -z "$PYTHON_BIN" ]]; then
  echo "python not found on PATH"
  exit 1
fi

PROTOCOL_PATH="${PROTOCOL_PATH:-repairable_diffusion/configs/protocol_phase1.yaml}"
PROTOCOL_FAMILIES="${PROTOCOL_FAMILIES:-}"
PROTOCOL_RUN_NAMES="${PROTOCOL_RUN_NAMES:-}"
HF_HOME="${HF_HOME:-$ROOT_DIR/.hf_home}"
HF_HUB_CACHE="${HF_HUB_CACHE:-$HF_HOME/hub}"

PROTOCOL_PATH_ABS="$(abs_path "$PROTOCOL_PATH")"
if [[ ! -f "$PROTOCOL_PATH_ABS" ]]; then
  echo "Protocol file not found: $PROTOCOL_PATH_ABS"
  exit 1
fi
mkdir -p "$HF_HOME" "$HF_HUB_CACHE"
export HF_HOME HF_HUB_CACHE

if [[ ! -d /home/kimhj/rfba ]]; then
  echo "Required backend root missing: /home/kimhj/rfba"
  exit 1
fi

if [[ ! -d /home/kimhj/difffusion-sampling-exp-benchmark-playground/Dream ]]; then
  echo "Required Dream backend root missing: /home/kimhj/difffusion-sampling-exp-benchmark-playground/Dream"
  exit 1
fi

echo "=========================================="
echo "Repairable State Discovery Protocol"
echo "Protocol:      $PROTOCOL_PATH_ABS"
echo "Families:      ${PROTOCOL_FAMILIES:-<all>}"
echo "Run names:     ${PROTOCOL_RUN_NAMES:-<all>}"
echo "HF_HOME:       $HF_HOME"
echo "HF_HUB_CACHE:  $HF_HUB_CACHE"
if has_hf_token; then
  echo "HF token:      present"
else
  echo "HF token:      missing"
fi
echo "Job ID:        ${SLURM_JOB_ID:-local}"
echo "Host:          $(hostname)"
echo "=========================================="

CMD=(
  "$PYTHON_BIN" -m repairable_diffusion.src.run_protocol
  --protocol "$PROTOCOL_PATH_ABS"
)

if [[ -n "$PROTOCOL_FAMILIES" ]]; then
  CMD+=(--families "$PROTOCOL_FAMILIES")
fi
if [[ -n "$PROTOCOL_RUN_NAMES" ]]; then
  CMD+=(--run-names "$PROTOCOL_RUN_NAMES")
fi

"${CMD[@]}"
