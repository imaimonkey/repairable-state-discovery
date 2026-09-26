#!/usr/bin/env python3
"""Explicit, storage-gated launch for an authorized scientific task.

This module never infers authorization from queue state. Phase 2A leaves every
task unauthorized, so importing or calling this module cannot start a run
without an explicit task flag and a fresh storage/GPU audit.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import shlex
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYTHON = os.environ.get("RSD_PYTHON", "/data/kimhj/llada8b_basic/.venv/bin/python")
RUNTIME = Path(os.environ.get("RSD_RUNTIME_ROOT", "/var/tmp/repairable-state-discovery/runtime"))
MIN_RESERVED_BYTES = 200 * 1024**3
MIN_INODE_FRACTION = 0.10
FORBIDDEN_IDENTIFIERS = ("iclr", "naacl", "acl", "emnlp", "conference", "submission", "deadline")


def storage_gate(path: str | Path, projected: int = 2 * 1024**3) -> dict:
    location = Path(path)
    location.mkdir(parents=True, exist_ok=True)
    stat = os.statvfs(location)
    available = stat.f_bavail * stat.f_frsize
    used = (stat.f_blocks - stat.f_bfree) * stat.f_frsize
    inode_fraction = stat.f_favail / stat.f_files if stat.f_files else 0.0
    required = max(MIN_RESERVED_BYTES, 3 * projected)
    if used / (used + available) >= 0.95:
        raise RuntimeError("STORAGE_GATE_FAILED: filesystem usage is at or above 95%")
    if available < required:
        raise RuntimeError(f"STORAGE_GATE_FAILED: {available} < required {required} bytes")
    if inode_fraction < MIN_INODE_FRACTION:
        raise RuntimeError("STORAGE_GATE_FAILED: inode margin below 10%")
    return {
        "available_bytes": available,
        "required_reserved_bytes": required,
        "projected_bytes": projected,
        "usage_fraction": used / (used + available),
        "free_inode_fraction": inode_fraction,
    }


def command(task: dict) -> list[str]:
    return [
        PYTHON,
        str(Path(task["execution_worktree"]) / "scripts" / "v2r_reference_gate.py"),
        "--backbone", task["backbone"],
        "--task", task["task"],
        "--stage", task["stage"],
        "--output", task["output"],
        "--source-cache", "/var/tmp/repairable-state-discovery/upstream",
        "--model-cache", task.get("model_cache", "/var/tmp/repairable-state-discovery/model-cache"),
        "--execution-sha", task["execution_git_sha"],
    ]


def environment() -> dict[str, str]:
    return {
        "HF_DATASETS_CACHE": "/var/tmp/repairable-state-discovery/datasets",
        "HF_MODULES_CACHE": "/var/tmp/repairable-state-discovery/modules",
        "HF_HUB_CACHE": "/var/tmp/repairable-state-discovery/hub",
        "OMP_NUM_THREADS": "4",
        "TOKENIZERS_PARALLELISM": "false",
        "PYTHONDONTWRITEBYTECODE": "1",
    }


def audit_prepared_registries() -> dict:
    owners = {}
    count = 0
    root = Path("/var/tmp/repairable-state-discovery/outputs/v2r_reference")
    for path in root.glob("gate-*/*/seed_registry.json"):
        registry = json.loads(path.read_text())
        for row in registry["records"]:
            key = (registry["scope"], row["group_id"])
            if row["seed"] in owners and owners[row["seed"]] != key:
                raise RuntimeError("UNINTENDED_CROSS_JOB_SEED_COLLISION")
            owners[row["seed"]] = key
            count += 1
    if not count:
        raise RuntimeError("NO_PREPARED_SEED_REGISTRIES")
    return {"context_count": count, "unique_seed_count": len(owners), "unintended_collisions": 0}


def _neutral_name(task_id: str) -> str:
    name = "rsd-" + "".join(char if char.isalnum() or char in "-_" else "-" for char in task_id.lower())
    if any(token in name for token in FORBIDDEN_IDENTIFIERS):
        raise ValueError("NON_NEUTRAL_TASK_IDENTIFIER")
    return name[:80]


def submit(task: dict, inventory: dict, dry_run: bool = False) -> dict:
    if not task.get("execution_authorized", False):
        raise RuntimeError("EXECUTION_AUTHORIZATION_REQUIRED")
    if task.get("purpose") not in {"reference_gate", "scientific_validation"}:
        raise RuntimeError("UNSUPPORTED_TASK_PURPOSE")
    if task.get("server") != "server3":
        raise RuntimeError("Remote execution requires an independently verified deployment")
    node = inventory["servers"][task["server"]]
    if not node.get("observed") or not node.get("idle_gpu_candidates"):
        raise RuntimeError("NO_OBSERVED_IDLE_GPU")
    checked = dt.datetime.fromisoformat(inventory["timestamp"])
    if (dt.datetime.now(dt.timezone.utc) - checked).total_seconds() > 300:
        raise RuntimeError("INVENTORY_TOO_OLD")
    storage = storage_gate(task["output"], int(task.get("projected_bytes", 2 * 1024**3)))
    seed_audit = audit_prepared_registries()
    prepared = Path(task["output"]) / task["stage"] / "prepared.json"
    if not prepared.is_file():
        raise RuntimeError("CPU_SEED_PREPARATION_REQUIRED")
    prep = json.loads(prepared.read_text())
    if prep["execution_git_sha"] != task["execution_git_sha"]:
        raise RuntimeError("PREPARED_SHA_MISMATCH")
    repo = Path(task["execution_worktree"])
    if subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip() != task["execution_git_sha"]:
        raise RuntimeError("IMMUTABLE_SHA_MISMATCH")
    if subprocess.run(["git", "diff", "--quiet"], cwd=repo).returncode:
        raise RuntimeError("DIRTY_EXECUTION_TREE")
    precheck = "import subprocess; p=subprocess.run(['nvidia-smi','--query-compute-apps=pid','--format=csv,noheader'],capture_output=True,text=True); assert p.returncode==0 and not p.stdout.strip(), 'CONFLICTING_GPU_PROCESS'"
    lines = ["#!/usr/bin/env bash", "set -euo pipefail", f"cd {shlex.quote(str(repo))}"]
    lines += [f"export {key}={shlex.quote(value)}" for key, value in environment().items()]
    lines += [shlex.join([PYTHON, "-c", precheck]), "exec " + shlex.join(command(task))]
    script = RUNTIME / (task["id"] + ".sbatch")
    script.parent.mkdir(parents=True, exist_ok=True)
    script.write_text("\n".join(lines) + "\n")
    logdir = Path(task["output"]) / task["stage"]
    logdir.mkdir(parents=True, exist_ok=True)
    neutral = _neutral_name(task["id"])
    args = [
        "sbatch", "--parsable", "--partition=gpu", "--qos=lab_gpu_s3", "--nodelist=ubuntu",
        "--gres=gpu:h200:1", "--cpus-per-task=4", "--mem=48G", "--time=" + task.get("walltime", "04:00:00"),
        "--job-name=" + neutral, "--chdir=" + str(repo),
        "--output=" + str(logdir / "rsd-%j.out"), "--error=" + str(logdir / "rsd-%j.err"), str(script),
    ]
    if any(any(token in value.lower() for token in FORBIDDEN_IDENTIFIERS) for value in args):
        raise RuntimeError("NON_NEUTRAL_SLURM_METADATA")
    if dry_run:
        return {"command": args, "storage": storage, "seed_audit": seed_audit}
    result = subprocess.run(args, text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    job = result.stdout.strip().split(";")[0]
    if not job.isdigit():
        raise RuntimeError("INVALID_JOB_ID " + result.stdout)
    return {
        "job_id": job,
        "started_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "storage": storage,
        "script": str(script),
        "slurm_args": args,
        "seed_audit": seed_audit,
        "command_sha256": hashlib.sha256("\0".join(args).encode()).hexdigest(),
    }
