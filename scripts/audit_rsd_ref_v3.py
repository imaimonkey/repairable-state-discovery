#!/usr/bin/env python3
"""Fail-closed design/readiness audit for RSD Generation 3."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Any

from repairable_diffusion.src.utils.io import load_yaml


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "repairable_diffusion/configs/rsd_ref_v3/measurement_contract.yaml"
MANIFEST = ROOT / "status/rsd_ref_v3/design_freeze.json"
CONFIG_ROOT = ROOT / "repairable_diffusion/configs/rsd_ref_v3/runs"
FREEZE_INPUTS = [
    "AGENTS.md",
    "docs/rsd_ref_v3_scientific_contract.md",
    "docs/RSD_REF_V3_TASK_SPEC.md",
    "docs/REFERENCE_TASK_SPEC.md",
    "docs/rsd_ref_v3_sample_size_plan.md",
    "docs/RSD_REF_V3_EXECUTION.md",
    "repairable_diffusion/configs/rsd_ref_v3/measurement_contract.yaml",
    "repairable_diffusion/src/rsd_ref_v3/__init__.py",
    "repairable_diffusion/src/rsd_ref_v3/task_adapters.py",
    "repairable_diffusion/src/rsd_ref_v3/runner.py",
    "repairable_diffusion/src/v2r/schema.py",
    "repairable_diffusion/src/v2r/planning.py",
    "repairable_diffusion/src/v2r/artifacts.py",
    "repairable_diffusion/src/v2r/science.py",
    "scripts/audit_rsd_ref_v3.py",
    "scripts/run_rsd_ref_v3.py",
    "scripts/submit_rsd_ref_v3.py",
    "status/rsd_ref_v3/subsets/selection_policy.json",
    "tests/test_rsd_ref_v3_contract.py",
    "tests/test_rsd_ref_v3_runner.py",
]
FREEZE_INPUTS += [
    str(path.relative_to(ROOT))
    for path in sorted((ROOT / "repairable_diffusion/configs/rsd_ref_v3/runs").glob("*.yaml"))
]
FREEZE_INPUTS += [
    str(path.relative_to(ROOT))
    for path in sorted((ROOT / "status/rsd_ref_v3/subsets").glob("llada_*.json"))
]
EXPECTED_LLaDA_MODEL = "08b83a6feb34df1a6011b80c3c00c7563e963b07"
EXPECTED_MATH_ARCHIVE = "cf44a0c065f23dbb96e3239115758f7442b725776f3dedfa4473821a1c98fe03"
EXPECTED_GSM_ARCHIVE = "5e90449bd5ed9c728dd32fc0c36a21c2cb02fd1fe38cb00fcf5672fcf3dc9378"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_sha() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def check(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def audit_contract(errors: list[str]) -> dict[str, Any] | None:
    if not CONTRACT.is_file():
        errors.append(f"missing contract: {CONTRACT.relative_to(ROOT)}")
        return None
    try:
        cfg = load_yaml(CONTRACT)
    except Exception as exc:
        errors.append(f"invalid contract: {exc}")
        return None
    check(errors, cfg.get("generation_id") == "rsd_ref_v3", "wrong generation_id")
    check(errors, cfg.get("artifact_namespace") == "rsd_ref_v3", "wrong artifact namespace")
    check(errors, cfg.get("status") == "frozen_execution_design", "contract is not frozen")
    check(errors, cfg.get("design_seed") == 314159265, "design seed is not frozen")
    check(errors, cfg.get("confirmatory_results_observed") is False, "confirmatory outcomes must be false")
    check(errors, cfg.get("base_generation", {}).get("trajectories_per_item") == 1, "base bank must be one trajectory per item")
    check(errors, cfg.get("readiness", {}).get("cross_server_equivalence_required_for") == "multi_server_pooling_only", "cross-server gate policy missing")
    tasks = cfg.get("tasks", {})
    math = tasks.get("llada_math", {})
    gsm = tasks.get("llada_gsm8k", {})
    check(errors, math.get("dataset", {}).get("count") == 5000, "LLaDA MATH must be source-native count 5000")
    check(errors, math.get("dataset", {}).get("archive_sha256") == EXPECTED_MATH_ARCHIVE, "MATH archive hash mismatch")
    check(errors, math.get("dataset", {}).get("bridge_is_confirmatory_population") is False, "MATH bridge must be calibration-only")
    check(errors, gsm.get("dataset", {}).get("count") == 1319, "LLaDA GSM8K count mismatch")
    check(errors, gsm.get("dataset", {}).get("archive_sha256") == EXPECTED_GSM_ARCHIVE, "GSM archive hash mismatch")
    check(errors, cfg.get("models", {}).get("llada", {}).get("revision") == EXPECTED_LLaDA_MODEL, "LLaDA model revision is not pinned")
    targets = cfg.get("sample_targets", {})
    check(errors, targets.get("successful_harm_trajectories_per_task") == 128, "successful-harm target is not frozen at 128")
    return cfg


def audit_configs(errors: list[str]) -> None:
    paths = sorted(CONFIG_ROOT.glob("*.yaml"))
    check(errors, len(paths) >= 8, "expected Generation 3 run configs are missing")
    for path in paths:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        check(errors, "limit: 200" not in text and "limit: 200\n" not in text, f"forbidden limit:200 in {rel}")
        try:
            cfg = load_yaml(path)
        except Exception as exc:
            errors.append(f"invalid config {rel}: {exc}")
            continue
        check(errors, cfg.get("generation_id") == "rsd_ref_v3", f"wrong generation in {rel}")
        check(errors, str(cfg.get("run_name", "")).startswith("rsd_ref_v3_"), f"unsafe run name in {rel}")
        roots = cfg.get("paths", {})
        for key in ("outputs_root", "results_root", "status_root"):
            if key in roots:
                check(errors, str(roots[key]).startswith(f"{key.replace('_root', '')}/rsd_ref_v3"), f"old namespace in {rel}:{key}")
        for old_output in ("outputs/v2_measurement", "results/v2_measurement", "status/v2r", "outputs/v2r_reference"):
            check(errors, old_output not in text, f"old artifact namespace in {rel}: {old_output}")


def audit_subsets(errors: list[str]) -> None:
    policy = ROOT / "status/rsd_ref_v3/subsets/selection_policy.json"
    check(errors, policy.is_file(), "missing frozen subset selection policy")
    if policy.is_file():
        payload = json.loads(policy.read_text(encoding="utf-8"))
        check(errors, payload.get("status") == "FROZEN_BEFORE_CONFIRMATORY_OUTCOMES", "subset policy is not frozen")
        check(errors, payload.get("repairability_outcome_used_for_selection") is False, "subset policy leaks repairability outcomes")
        check(errors, payload.get("design_seed") == 314159265, "subset design seed mismatch")
    subset_paths = sorted((ROOT / "status/rsd_ref_v3/subsets").glob("llada_*.json"))
    check(errors, len(subset_paths) == 8, "expected eight predeclared LLaDA subset specs")
    for path in subset_paths:
        payload = json.loads(path.read_text(encoding="utf-8"))
        check(errors, payload.get("status") == "PREDECLARED_AWAITING_BASE_BANK", f"subset not predeclared: {path.name}")
        check(errors, payload.get("item_ids") is None, f"subset outcome IDs already materialized: {path.name}")


def audit_runtime_state(errors: list[str]) -> dict[str, Any] | None:
    readiness = ROOT / "status/rsd_ref_v3/execution_readiness.json"
    storage = ROOT / "status/rsd_ref_v3/storage_plan.json"
    check(errors, readiness.is_file(), "missing execution readiness")
    check(errors, storage.is_file(), "missing storage plan")
    readiness_payload = None
    storage_payload = None
    if readiness.is_file():
        readiness_payload = json.loads(readiness.read_text(encoding="utf-8"))
        check(errors, readiness_payload.get("server1", {}).get("scientific_execution_qualification") == "SCIENTIFIC_EXECUTION_QUALIFIED", "server1 qualification not encoded")
        check(errors, readiness_payload.get("single_server_primary_gate", {}).get("confirmatory_protocol_frozen") is True, "protocol freeze gate not encoded")
    if storage.is_file():
        storage_payload = json.loads(storage.read_text(encoding="utf-8"))
    if readiness_payload is None or storage_payload is None:
        return None
    gate = readiness_payload.get("single_server_primary_gate", {})
    check(errors, gate.get("confirmatory_protocol_frozen") is True, "confirmatory protocol is not frozen")
    check(errors, readiness_payload.get("confirmatory_results_observed") is False, "readiness records confirmatory outcomes")
    if storage_payload.get("status") == "STORAGE_READY":
        approved = storage_payload.get("approved_output_root")
        check(errors, isinstance(approved, str) and "rsd_ref_v3" in Path(approved).parts, "approved output root must use rsd_ref_v3 namespace")
        if isinstance(approved, str):
            location = Path(approved)
            try:
                location.mkdir(parents=True, exist_ok=True)
                stat = os.statvfs(location)
                available = stat.f_bavail * stat.f_frsize
                total = stat.f_blocks * stat.f_frsize
                used_fraction = 1.0 - (available / total if total else 0.0)
                inode_fraction = stat.f_favail / stat.f_files if stat.f_files else 0.0
                check(errors, used_fraction < 0.95, "live filesystem use must remain below 95 percent")
                check(errors, inode_fraction >= 0.10, "live free inode fraction must remain at least 10 percent")
                minimum = int(storage_payload.get("minimum_free_after_run_bytes", 200 * 1024**3))
                check(errors, available >= minimum, "live free bytes are below the reserved post-run minimum")
            except OSError as exc:
                errors.append(f"cannot inspect approved output filesystem: {exc}")
    return {"readiness": readiness_payload, "storage": storage_payload}


def audit_freeze(errors: list[str]) -> None:
    check(errors, MANIFEST.is_file(), "missing status/rsd_ref_v3/design_freeze.json")
    if not MANIFEST.is_file():
        return
    payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
    check(errors, payload.get("status") == "FROZEN_BEFORE_CONFIRMATORY_OUTCOMES", "design freeze status mismatch")
    check(errors, payload.get("generation_id") == "rsd_ref_v3", "design freeze generation mismatch")
    check(errors, payload.get("confirmatory_results_observed") is False, "design freeze observes confirmatory outcomes")
    for rel in FREEZE_INPUTS:
        path = ROOT / rel
        check(errors, path.is_file(), f"missing freeze input: {rel}")
        if path.is_file():
            check(errors, payload.get("files", {}).get(rel) == sha256(path), f"freeze hash mismatch: {rel}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("design", "readiness"), default="design")
    args = parser.parse_args()
    errors: list[str] = []
    audit_contract(errors)
    audit_configs(errors)
    audit_subsets(errors)
    audit_freeze(errors)
    runtime_state = None
    if args.mode == "readiness":
        runtime_state = audit_runtime_state(errors)
        storage = runtime_state["storage"] if runtime_state else {}
        if storage.get("status") != "STORAGE_READY":
            errors.append("readiness mode requires storage_plan.status=STORAGE_READY")
        if storage.get("execution_allowed") is not True:
            errors.append("readiness mode requires storage_plan.execution_allowed=true")
        if not storage.get("approved_output_root") or not storage.get("reservation_id"):
            errors.append("readiness mode requires approved storage reservation metadata")
        gate = (runtime_state or {}).get("readiness", {}).get("single_server_primary_gate", {})
        if gate.get("canonical_source_config_sha_match") is not True:
            errors.append("readiness mode requires canonical_source_config_sha_match=true")
        if gate.get("storage_ready") is not True or gate.get("execution_allowed") is not True:
            errors.append("readiness mode requires open single-server execution gate")
    print(f"mode: {args.mode}")
    print(f"git_sha: {git_sha()}")
    if errors:
        print("\nNOT READY")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    if args.mode == "design":
        print("\nRSD_REF_V3 DESIGN READY; READINESS IS MUTABLE AND EXECUTION REMAINS GATED")
    else:
        print("\nRSD_REF_V3 READINESS READY; EXECUTION GATE OPEN")


if __name__ == "__main__":
    main()
