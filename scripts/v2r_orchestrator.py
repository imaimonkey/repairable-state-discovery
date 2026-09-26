#!/usr/bin/env python3
"""Single execution authority for explicitly authorized scientific tasks."""
from __future__ import annotations

import argparse
import datetime as dt
import fcntl
import json
import os
import subprocess
import time
import traceback
from pathlib import Path

from v2r_inventory import atomic_json, collect
from v2r_status import read, write_status
from v2r_submit import command, environment, submit

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "status" / "reset"
RUNTIME = Path(os.environ.get("RSD_RUNTIME_ROOT", "/var/tmp/repairable-state-discovery/runtime"))


def event(name: str, payload: dict) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "event_history.jsonl").open("a") as handle:
        handle.write(json.dumps({"timestamp": dt.datetime.now(dt.timezone.utc).isoformat(), "event": name, **payload}, sort_keys=True) + "\n")


def _slurm_state(job_id: str) -> str:
    result = subprocess.run(
        ["sacct", "-n", "-X", "-P", "-j", job_id, "--format=JobID,State,ExitCode"],
        text=True,
        capture_output=True,
        timeout=15,
    )
    for line in result.stdout.splitlines():
        fields = line.split("|")
        if fields and fields[0] == job_id and len(fields) > 1:
            return fields[1]
    return "UNKNOWN"


def _run_cpu_gate(task: dict) -> bool:
    env = os.environ.copy()
    env.update(environment())
    log = Path(task["output"]) / task["stage"] / "cpu.log"
    log.parent.mkdir(parents=True, exist_ok=True)
    with log.open("a") as handle:
        result = subprocess.run(command(task), cwd=task["execution_worktree"], env=env, stdout=handle, stderr=handle, timeout=240)
    return result.returncode == 0


def cycle() -> bool:
    queue = read(OUT / "orchestrator_queue.json", {"tasks": [], "execution_authorized": False}) or {"tasks": []}
    changed = False
    inventory = read(OUT / "cluster_inventory.json", {}) or {}
    if not inventory or not inventory.get("timestamp"):
        inventory = collect(OUT)
    by_id = {task["id"]: task for task in queue.get("tasks", [])}
    for task in sorted(queue.get("tasks", []), key=lambda value: value.get("priority", 9999)):
        old = task.get("status", "READY")
        report = read(Path(task["output"]) / task["stage"] / "gate_report.json")
        if report and report.get("status") in {"PASS", "NEEDS_REVIEW"}:
            task["status"] = report["status"]
            task["error"] = report.get("error")
        elif task.get("job_id"):
            state = _slurm_state(task["job_id"])
            task["slurm_state"] = state
            if state in {"RUNNING", "PENDING", "CONFIGURING"}:
                task["status"] = state
            elif state != "UNKNOWN":
                task.update(status="NEEDS_REVIEW", error="Terminal scheduler state without PASS: " + state)
        elif task.get("status") in {"READY", "RESOURCE_WAIT", "WAITING_DEPENDENCY", "WAITING_EXECUTION_AUTHORIZATION"}:
            dependencies = [by_id[dependency]["status"] for dependency in task.get("depends_on", [])]
            if not all(status == "PASS" for status in dependencies):
                task["status"] = "WAITING_DEPENDENCY"
            elif not queue.get("execution_authorized") or not task.get("execution_authorized"):
                task["status"] = "WAITING_EXECUTION_AUTHORIZATION"
            elif task.get("stage") == "R1":
                task["status"] = "PASS" if _run_cpu_gate(task) else "NEEDS_REVIEW"
            else:
                try:
                    task.update(submit(task, inventory))
                    task["status"] = "SUBMITTED"
                except RuntimeError as error:
                    task.update(status="RESOURCE_WAIT", error=str(error))
        if task["status"] != old:
            changed = True
            event("TASK_STATE_CHANGE", {"task": task["id"], "old": old, "new": task["status"], "job_id": task.get("job_id"), "error": task.get("error")})
    atomic_json(OUT / "orchestrator_queue.json", queue)
    now = dt.datetime.now(dt.timezone.utc)
    health = {
        "schema_version": "rsd.orchestrator_health.1",
        "timestamp": now.isoformat(),
        "pid": os.getpid(),
        "service": "rsd-orchestrator",
        "status": "RUNNING",
        "execution_authority": True,
        "raw_execution_authorized": bool(queue.get("execution_authorized")),
        "last_error": None,
    }
    write_status(queue, health)
    return changed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--interval", type=int, default=60)
    args = parser.parse_args()
    RUNTIME.mkdir(parents=True, exist_ok=True)
    with (RUNTIME / "orchestrator.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        while True:
            try:
                cycle()
            except Exception as error:
                event("CONTROLLER_ERROR", {"error": str(error), "traceback": traceback.format_exc()})
                atomic_json(OUT / "orchestrator_health.json", {"status": "DEGRADED_RETRY", "pid": os.getpid(), "error": str(error), "timestamp": dt.datetime.now(dt.timezone.utc).isoformat()})
            if args.once:
                break
            time.sleep(max(30, args.interval))


if __name__ == "__main__":
    main()
