#!/bin/bash
#SBATCH --job-name=repair_final
#SBATCH --output=/home/kimhj/repairable-state-discovery/logs/protocol_final_%j.out
#SBATCH --error=/home/kimhj/repairable-state-discovery/logs/protocol_final_%j.err
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
# 60G is accepted by the 1-GPU memory policy on server2/server4 and remains
# sufficient for the 7B/8B full-paper backends; server3 H200 jobs also fit.
#SBATCH --mem=60G
#SBATCH --time=30-00:00:00

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

detect_required_backends() {
  "$PYTHON_BIN" - "$PROTOCOL_PATH_ABS" "$PROTOCOL_FAMILIES" "$PROTOCOL_RUN_NAMES" <<'PY'
import sys

import yaml


def parse_csv(spec):
    if not spec:
        return set()
    return {part.strip() for part in spec.split(",") if part.strip()}


def allowed(spec, family, allowed_families, allowed_run_names):
    if allowed_families and family not in allowed_families:
        return False
    if allowed_run_names and spec["run_name"] not in allowed_run_names:
        return False
    return True


protocol_path, families_spec, run_names_spec = sys.argv[1:4]
with open(protocol_path, "r", encoding="utf-8") as fh:
    protocol_cfg = yaml.safe_load(fh)
with open(protocol_cfg["profiles_path"], "r", encoding="utf-8") as fh:
    profiles = yaml.safe_load(fh).get("models", {})

allowed_families = parse_csv(families_spec)
allowed_run_names = parse_csv(run_names_spec)
required = set()

if bool(protocol_cfg["protocol"].get("run_diffusion_main", True)):
    for spec in protocol_cfg["protocol"].get("diffusion_runs", []):
        if not allowed(spec, "diffusion", allowed_families, allowed_run_names):
            continue
        backend = profiles.get(spec["model_profile"], {}).get("backend", {})
        backend_type = str(backend.get("type", "")).strip()
        if backend_type:
            required.add(backend_type)

if bool(protocol_cfg["protocol"].get("run_ar_compare", True)):
    for spec in protocol_cfg["protocol"].get("ar_runs", []):
        if not allowed(spec, "ar", allowed_families, allowed_run_names):
            continue
        backend = profiles.get(spec["model_profile"], {}).get("backend", {})
        backend_type = str(backend.get("type", "")).strip()
        if backend_type:
            required.add(backend_type)

for backend_type in sorted(required):
    print(backend_type)
PY
}

# A Slurm submission may originate on a different login node whose absolute
# path is not mounted on the allocated compute node.  Prefer an explicit
# node-local root, then fall back to the submit directory/script location.
ROOT_CANDIDATE="${REPAIRABLE_ROOT:-${SLURM_SUBMIT_DIR:-$SCRIPT_DIR}}"
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

if [[ -z "${PYTHON_BIN:-}" ]]; then
  for candidate in \
    "$ROOT_DIR/.venv/bin/python" \
    "${HOME:-}/llada8b_basic/.venv/bin/python" \
    "${HOME:-}/repo-reconcile/llada8b_basic/.venv/bin/python" \
    /data/kimhj/repo-reconcile/llada8b_basic/.venv/bin/python \
    /home/kimhj/llada8b_basic/.venv/bin/python; do
    if [[ -x "$candidate" ]]; then
      PYTHON_BIN="$candidate"
      break
    fi
  done
  if [[ -z "${PYTHON_BIN:-}" ]]; then
    PYTHON_BIN="$(command -v python || command -v python3 || true)"
  fi
fi
if [[ -z "$PYTHON_BIN" ]]; then
  echo "python not found on PATH"
  exit 1
fi

PROTOCOL_PATH="${PROTOCOL_PATH:-repairable_diffusion/configs/final/protocol_math500_final.yaml}"
PROTOCOL_FAMILIES="${PROTOCOL_FAMILIES:-}"
PROTOCOL_RUN_NAMES="${PROTOCOL_RUN_NAMES:-}"
if [[ -z "${HF_HOME:-}" ]]; then
  for candidate in \
    "${HOME:-}/.cache/huggingface" \
    /data/kimhj/.cache/huggingface \
    /home/kimhj/.cache/huggingface; do
    if [[ -d "$candidate" ]]; then
      HF_HOME="$candidate"
      break
    fi
  done
  HF_HOME="${HF_HOME:-$ROOT_DIR/.hf_home}"
fi
HF_HUB_CACHE="${HF_HUB_CACHE:-$HF_HOME/hub}"

PROTOCOL_PATH_ABS="$(abs_path "$PROTOCOL_PATH")"
if [[ ! -f "$PROTOCOL_PATH_ABS" ]]; then
  echo "Protocol file not found: $PROTOCOL_PATH_ABS"
  exit 1
fi
mkdir -p "$HF_HOME" "$HF_HUB_CACHE"
export HF_HOME HF_HUB_CACHE

REQUIRED_BACKENDS="$(detect_required_backends | tr '\n' ' ')"

if [[ "$REQUIRED_BACKENDS" == *"rfba_llada"* ]]; then
  if [[ -z "${RFBA_ROOT:-}" ]]; then
    for candidate in \
      "${HOME:-}/rfba" \
      "${HOME:-}/repo-reconcile/rfba" \
      /data/kimhj/rfba \
      /home/kimhj/rfba \
      /home/kimhj/Rethinking-Fixed-Block-Assumptions-in-Diffusion-Language-Model-Decoding; do
      if [[ -d "$candidate/decoding/llada" ]]; then
        RFBA_ROOT="$candidate"
        break
      fi
    done
  fi
  if [[ -z "${RFBA_ROOT:-}" || ! -d "$RFBA_ROOT/decoding/llada" ]]; then
    echo "Required LLaDA backend root missing; set RFBA_ROOT to a directory containing decoding/llada" >&2
    exit 1
  fi
  export RFBA_ROOT
fi

if [[ "$REQUIRED_BACKENDS" == *"dream"* ]] && [[ ! -d /home/kimhj/difffusion-sampling-exp-benchmark-playground/Dream ]]; then
  echo "Required Dream backend root missing: /home/kimhj/difffusion-sampling-exp-benchmark-playground/Dream"
  exit 1
fi

echo "=========================================="
echo "Repairability Final Protocol"
echo "Protocol:      $PROTOCOL_PATH_ABS"
echo "Families:      ${PROTOCOL_FAMILIES:-<all>}"
echo "Run names:     ${PROTOCOL_RUN_NAMES:-<all>}"
echo "Backends:      ${REQUIRED_BACKENDS:-<none>}"
echo "HF_HOME:       $HF_HOME"
echo "RFBA_ROOT:     ${RFBA_ROOT:-<not-needed>}"
echo "HF_HUB_CACHE:  $HF_HUB_CACHE"
if has_hf_token; then
  echo "HF token:      present"
else
  echo "HF token:      missing"
fi
echo "Job ID:        ${SLURM_JOB_ID:-local}"
echo "Host:          $(hostname)"
echo "CUDA_VISIBLE_DEVICES: ${CUDA_VISIBLE_DEVICES:-<scheduler-default>}"
echo "SLURM_JOB_GPUS:       ${SLURM_JOB_GPUS:-<unset>}"
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
if [[ "${PROTOCOL_WRITE_REPORT:-true}" != "true" ]]; then
  CMD+=(--no-protocol-report)
fi

"${CMD[@]}"
