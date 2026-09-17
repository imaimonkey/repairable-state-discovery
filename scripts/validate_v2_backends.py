from __future__ import annotations

import argparse
import copy
import json
import subprocess
from pathlib import Path

from repairable_diffusion.src.utils.io import load_yaml
from repairable_diffusion.src.v2.backends import create_v2_backend
from repairable_diffusion.src.v2.replay import replay_dream_next_state, replay_llada_next_state
from repairable_diffusion.src.v2.run_measurement import PROFILES_PATH, _load_profile
from repairable_diffusion.src.v2.task_adapters import MBPPAdapter, create_task_adapter


ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "repairable_diffusion/configs/v2/runs"
OUTPUT = ROOT / "results/v2_measurement/backend_validation.json"


def _git_sha() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def _validation_cfg(path: Path, *, model_profile: str | None = None) -> dict:
    cfg = copy.deepcopy(load_yaml(path))
    if model_profile is not None:
        cfg["model_profile"] = model_profile
    cfg["dataset"]["limit"] = 1
    cfg["dataset"]["sample_seed"] = 987654
    cfg["generation"]["trajectories_per_item"] = 1
    cfg["generation"]["checkpoint_stride"] = 1
    return cfg


def _pair(record: dict) -> tuple[dict, dict]:
    steps = [row for row in record["steps"] if row.get("snapshot")]
    for current, nxt in zip(steps, steps[1:]):
        if int(nxt["step_index"]) == int(current["step_index"]) + 1:
            return current, nxt
    raise RuntimeError("no adjacent saved transition available for replay validation")


def _validate_llada() -> dict:
    cfg = _validation_cfg(RUNS / "pilot_math500_llada.yaml")
    adapter = create_task_adapter(cfg["dataset"])
    items = adapter.load_records(cfg["dataset"])
    backend = create_v2_backend(_load_profile(cfg["model_profile"], PROFILES_PATH), adapter)
    record = backend.generate_trajectory_v2(items[0], 0, cfg["generation"])
    current, nxt = _pair(record)
    replay = replay_llada_next_state(backend, current["snapshot"], cfg["generation"])
    if replay["full_token_ids"] != nxt["snapshot"]["full_token_ids"]:
        raise AssertionError("LLaDA one-step native replay mismatch")
    resumed = backend.continue_from_snapshot(
        items[0], current["snapshot"], cfg["generation"], branch_seed=None, restore_native_rng=True
    )
    if resumed["final_text"] != record["final_text"]:
        raise AssertionError("LLaDA full native replay mismatch")
    return {
        "status": "PASS",
        "validated_step": int(current["step_index"]),
        "next_step": int(nxt["step_index"]),
        "one_step_state_equal": True,
        "full_final_text_equal": True,
    }


def _validate_dream() -> dict:
    cfg = _validation_cfg(RUNS / "full_math500_dream.yaml")
    adapter = create_task_adapter(cfg["dataset"])
    items = adapter.load_records(cfg["dataset"])
    backend = create_v2_backend(_load_profile(cfg["model_profile"], PROFILES_PATH), adapter)
    record = backend.generate_trajectory_v2(items[0], 0, cfg["generation"])
    current, nxt = _pair(record)
    replay = replay_dream_next_state(backend, current["snapshot"], cfg["generation"])
    if replay["full_token_ids"] != nxt["snapshot"]["full_token_ids"]:
        raise AssertionError("Dream one-step token-state replay mismatch")
    if replay["first_conf"] != nxt["snapshot"]["first_conf"]:
        raise AssertionError("Dream one-step first_conf replay mismatch")
    resumed = backend.continue_from_snapshot(
        items[0], current["snapshot"], cfg["generation"], branch_seed=None, restore_native_rng=True
    )
    if resumed["final_text"] != record["final_text"]:
        raise AssertionError("Dream full native replay mismatch")
    return {
        "status": "PASS",
        "validated_step": int(current["step_index"]),
        "next_step": int(nxt["step_index"]),
        "one_step_state_equal": True,
        "first_conf_equal": True,
        "full_final_text_equal": True,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--llada-only", action="store_true")
    ap.add_argument("--dream-only", action="store_true")
    args = ap.parse_args()
    if args.llada_only and args.dream_only:
        raise SystemExit("choose at most one of --llada-only/--dream-only")

    results = {"git_sha": _git_sha(), "status": "PASS"}
    if not args.dream_only:
        results["llada"] = _validate_llada()
    if not args.llada_only:
        results["dream"] = _validate_dream()

    # Safe-code evaluator is a scientific readiness gate even though MBPP itself
    # is a later thin-validation tier.
    MBPPAdapter().executor.self_test()
    results["mbpp_sandbox"] = {"status": "PASS"}

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
