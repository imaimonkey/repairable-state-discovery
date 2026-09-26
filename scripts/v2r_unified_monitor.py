#!/usr/bin/env python3
"""Read-only neutral observation of scheduler, GPU, filesystem, and artifacts."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import time
from pathlib import Path

from v2r_inventory import atomic_json, collect

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "status" / "reset"


def read(path: Path, default=None):
    try:
        return json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return default


def reconcile() -> dict:
    now = dt.datetime.now(dt.timezone.utc)
    inventory = collect(OUT)
    jobs = read(OUT / "job_inventory.json", {}) or {}
    queue = read(OUT / "orchestrator_queue.json", {"tasks": []}) or {"tasks": []}
    orchestrator = read(OUT / "orchestrator_health.json", {}) or {}
    previous = read(OUT / "canonical_status.json", {}) or {}
    previous_ids = set(previous.get("active_tasks", []))
    observed_ids = {str(job.get("job_id")) for job in jobs.get("active_or_pending", [])}
    drift = []
    for job in jobs.get("active_or_pending", []):
        job_id = str(job.get("job_id"))
        if previous_ids and job_id not in previous_ids:
            drift.append({"type": "MONITOR_DRIFT", "message": f"Scheduler job {job_id} is not in the previous canonical status snapshot.", "job_id": job_id})
    missing = sorted(previous_ids - observed_ids) if previous_ids else []
    if missing:
        drift.append({"type": "MONITOR_DRIFT", "message": "Previously active task is absent from the current scheduler listing.", "job_ids": missing})
    digest = hashlib.sha256(json.dumps(drift, sort_keys=True).encode()).hexdigest()
    old_drift = read(OUT / "monitor_last_drift.json", {}) or {}
    if drift and old_drift.get("digest") != digest:
        with (OUT / "event_history.jsonl").open("a") as handle:
            for item in drift:
                handle.write(json.dumps({"timestamp": now.isoformat(), "event": "MONITOR_DRIFT", **item}, sort_keys=True) + "\n")
    atomic_json(OUT / "monitor_last_drift.json", {"timestamp": now.isoformat(), "digest": digest, "alerts": drift})

    servers = inventory.get("servers", {})
    atomic_json(OUT / "gpu_inventory.json", {
        "timestamp": now.isoformat(),
        "servers": {
            key: {
                "node": value.get("node"),
                "observed": value.get("observed"),
                "gpus": value.get("gpus", []),
                "gpu_processes": value.get("gpu_processes", {}),
                "slurm_node": value.get("slurm_node"),
            }
            for key, value in servers.items()
        },
    })
    unified = {
        "schema_version": "rsd.monitor.1",
        "timestamp": now.isoformat(),
        "source_of_truth": ["Slurm scheduler", "GPU/process observation", "filesystem observation", "artifact manifests"],
        "slurm_jobs": jobs,
        "inventory_summary": inventory.get("job_inventory_summary", {}),
        "servers": servers,
        "orchestrator": orchestrator,
        "queue": queue,
        "integrity_alerts": drift,
        "execution_allowed": bool(queue.get("execution_authorized")),
    }
    atomic_json(OUT / "unified_status.json", unified)
    atomic_json(OUT / "monitor_health.json", {
        "schema_version": "rsd.monitor_health.1",
        "status": "RUNNING",
        "timestamp": now.isoformat(),
        "pid": os.getpid(),
        "service": "rsd-monitor",
        "poll_interval_seconds": 90,
        "scheduler_authoritative": True,
        "execution_authority": "rsd-orchestrator",
        "integrity_alert_count": len(drift),
    })
    lines = [
        now.isoformat(),
        "RUNTIME MODE: NEUTRAL SCIENTIFIC OBSERVATION",
        "SOURCE OF TRUTH: SLURM SCHEDULER",
        "EXECUTION AUTHORITY: rsd-orchestrator",
        "",
        "MONITOR DRIFT",
    ]
    lines += [f"{item['type']}: {item['message']}" for item in drift] or ["None in current reconciliation."]
    lines += ["", "ACTIVE USER JOBS"]
    active = jobs.get("active_or_pending", [])
    lines += [f"{job.get('job_id')} {job.get('job_name')} {job.get('state')} {job.get('node_list')} {job.get('classification')}" for job in active] or ["None"]
    for name, server in servers.items():
        lines += ["", name.upper(), f"observed={server.get('observed')} idle_gpu_candidates={server.get('idle_gpu_candidates')} safe_filesystems={server.get('safe_filesystem_candidates')}"]
    lines += ["", "STORAGE GATE", "Raw scientific execution is disabled until an approved filesystem reservation and inode margin are recorded."]
    lines += ["", "ORCHESTRATOR", f"status={orchestrator.get('status')} service={orchestrator.get('service')} heartbeat={orchestrator.get('timestamp')}"]
    (OUT / "attention_required.md").write_text("\n".join(lines) + "\n")
    return unified


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--interval", type=int, default=90)
    args = parser.parse_args()
    while True:
        try:
            reconcile()
        except Exception as error:
            atomic_json(OUT / "monitor_health.json", {"status": "DEGRADED_RETRY", "timestamp": dt.datetime.now(dt.timezone.utc).isoformat(), "pid": os.getpid(), "error": str(error)})
        if args.once:
            break
        time.sleep(max(30, args.interval))


if __name__ == "__main__":
    main()
