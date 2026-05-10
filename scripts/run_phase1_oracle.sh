#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd -- "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT_DIR"

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

mkdir -p "$ROOT_DIR/results" "$ROOT_DIR/repairable_diffusion/outputs/runs" "$ROOT_DIR/logs"

if [[ -f .venv/bin/activate ]]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
elif [[ -f /home/kimhj/provenance-decompositon/.venv/bin/activate ]]; then
  # shellcheck disable=SC1091
  source /home/kimhj/provenance-decompositon/.venv/bin/activate
fi

load_hf_token_from_file

CONFIG_PATH="${CONFIG_PATH:-repairable_diffusion/configs/math500_phase1.yaml}"
RUN_DIR="${RUN_DIR:-}"
HF_HOME="${HF_HOME:-$ROOT_DIR/.hf_home}"
HF_HUB_CACHE="${HF_HUB_CACHE:-$HF_HOME/hub}"
PYTHON_BIN="$(command -v python || command -v python3 || true)"

if [[ -z "$PYTHON_BIN" ]]; then
  echo "python not found on PATH"
  exit 1
fi

if [[ ! -f "$CONFIG_PATH" ]]; then
  echo "Config file not found: $CONFIG_PATH"
  exit 1
fi

if [[ ! -d /home/kimhj/rfba ]]; then
  echo "Required backend root missing: /home/kimhj/rfba"
  exit 1
fi

mkdir -p "$HF_HOME" "$HF_HUB_CACHE"
export HF_HOME HF_HUB_CACHE

echo "=========================================="
echo "Repairable State Discovery Phase 1"
echo "Config:      $CONFIG_PATH"
echo "Run Dir:     ${RUN_DIR:-<auto>}"
echo "HF_HOME:     $HF_HOME"
if has_hf_token; then
  echo "HF token:    present"
else
  echo "HF token:    missing"
fi
echo "Host:        $(hostname)"
echo "=========================================="

CMD=(
  "$PYTHON_BIN" -m repairable_diffusion.src.run_pipeline
  --config "$CONFIG_PATH"
)

if [[ -n "$RUN_DIR" ]]; then
  CMD+=(--run-dir "$RUN_DIR")
fi

"${CMD[@]}"
