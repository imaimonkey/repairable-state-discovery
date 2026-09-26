#!/usr/bin/env python3
"""Write neutral scientific-runtime status; never writes derived release state."""
from __future__ import annotations

import csv
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from v2r_inventory import atomic_json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "status" / "reset"
HISTORICAL_ANCESTOR = "0dd161c8cf4bf3e7dbe4042234a0954950ce870e"
PREFERRED_SOURCE = "78fe5d7c1829b67d1bb1416b7205edfa647bb2fa"


def read(path: Path, default=None):
    try:
        return json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return default


def source_sha() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return "UNKNOWN"


def write_status(queue: dict, health: dict) -> dict:
    OUT.mkdir(parents=True, exist_ok=True)
    now = dt.datetime.now(dt.timezone.utc)
    gates: dict[str, dict] = {}
    artifacts = []
    for task in queue.get("tasks", []):
        report_path = Path(task["output"]) / task["stage"] / "gate_report.json"
        report = read(report_path)
        key = f"{task.get('backbone', 'unknown')}_{task.get('task', 'unknown')}"
        gates.setdefault(key, {})[task["stage"]] = {
            "status": report.get("status") if report else task.get("status", "NOT_RUN"),
            "path": str(report_path),
            "job_id": task.get("job_id"),
            "error": report.get("error") if report else task.get("error"),
        }
        if report:
            artifacts.append({
                "kind": "gate_report",
                "path": str(report_path),
                "execution_sha": task.get("execution_git_sha"),
                "status": report.get("status"),
            })

    active = [
        task["id"] for task in queue.get("tasks", [])
        if task.get("status") in {"RUNNING", "SUBMITTED", "PENDING"}
    ]
    current = {
        "schema_version": "rsd.canonical_status.1",
        "timestamp": now.isoformat(),
        "runtime_mode": "NEUTRAL_SCIENTIFIC_RUNTIME",
        "execution_authority": "orchestrator",
        "observation_authority": "slurm_scheduler",
        "historical_ancestor_sha": HISTORICAL_ANCESTOR,
        "preferred_scientific_source_sha": PREFERRED_SOURCE,
        "development_sha": source_sha(),
        "active_tasks": active,
        "gate_status": gates,
        "storage_gate": {
            "raw_execution_allowed": False,
            "minimum_reserved_free_bytes": 200 * 1024**3,
            "minimum_free_inode_fraction": 0.10,
            "formula": "max(200 GiB, 3x projected maximum single-shard raw output)",
        },
        "scientific_execution": "NOT_AUTHORIZED_IN_PHASE_2A",
        "artifacts": artifacts,
    }
    atomic_json(OUT / "canonical_status.json", current)
    atomic_json(OUT / "gate_status.json", gates)
    atomic_json(OUT / "artifact_index.json", {"timestamp": now.isoformat(), "artifacts": artifacts})
    atomic_json(OUT / "orchestrator_health.json", health)
    atomic_json(OUT / "aggregate_status.json", {
        "status": "WAITING_FOR_AUTHORIZED_EXECUTION",
        "sealed_reference_runs": [],
        "source_sha": PREFERRED_SOURCE,
    })
    atomic_json(OUT / "provenance_status.json", {
        "historical_ancestor_sha": HISTORICAL_ANCESTOR,
        "preferred_scientific_source_sha": PREFERRED_SOURCE,
        "execution_worktrees_immutable": True,
        "raw_execution_authorized": False,
    })
    plan = {
        "timestamp": now.isoformat(),
        "output_policy": "approved filesystem required before raw execution",
        "minimum_reserved_free_bytes": 200 * 1024**3,
        "minimum_free_inode_fraction": 0.10,
        "raw_execution_allowed": False,
    }
    atomic_json(OUT / "resource_plan.json", plan)
    with (OUT / "shard_matrix.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["id", "backbone", "task", "stage", "priority", "status", "job_id", "execution_git_sha"])
        writer.writeheader()
        for task in queue.get("tasks", []):
            writer.writerow({key: task.get(key) for key in writer.fieldnames})
    with (OUT / "progress_history.jsonl").open("a") as handle:
        handle.write(json.dumps({"timestamp": now.isoformat(), "active_tasks": active}, sort_keys=True) + "\n")
    return current
