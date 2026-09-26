#!/usr/bin/env python3
"""Keep neutral observer and execution-authority services alive."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from v2r_inventory import atomic_json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "status" / "reset"
PYTHON = os.environ.get("RSD_PYTHON", sys.executable)
MONITOR_SESSION = "rsd-monitor"
ORCHESTRATOR_SESSION = "rsd-orchestrator"


def read(path: Path, default=None):
    try:
        return json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return default


def has_session(name: str) -> bool:
    return subprocess.run(["tmux", "has-session", "-t", name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0


def start(name: str, command: str) -> None:
    if not has_session(name):
        subprocess.Popen(["tmux", "new-session", "-d", "-s", name, command], start_new_session=True)


def cycle() -> None:
    now = dt.datetime.now(dt.timezone.utc)
    start(MONITOR_SESSION, f"cd {ROOT} && exec {PYTHON} scripts/v2r_unified_monitor.py --interval 90")
    start(ORCHESTRATOR_SESSION, f"cd {ROOT} && exec {PYTHON} scripts/v2r_orchestrator.py --interval 60")
    atomic_json(OUT / "watchdog_health.json", {
        "schema_version": "rsd.watchdog_health.1",
        "status": "RUNNING",
        "timestamp": now.isoformat(),
        "pid": os.getpid(),
        "service": "rsd-watchdog",
        "monitor_session": MONITOR_SESSION,
        "orchestrator_session": ORCHESTRATOR_SESSION,
        "monitor_session_alive": has_session(MONITOR_SESSION),
        "orchestrator_session_alive": has_session(ORCHESTRATOR_SESSION),
        "monitor_health": read(OUT / "monitor_health.json", {}),
        "orchestrator_health": read(OUT / "orchestrator_health.json", {}),
    })


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--interval", type=int, default=120)
    parser.add_argument("--once", action="store_true")
    args = parser.parse_args()
    while True:
        try:
            cycle()
        except Exception as error:
            atomic_json(OUT / "watchdog_health.json", {"status": "DEGRADED_RETRY", "timestamp": dt.datetime.now(dt.timezone.utc).isoformat(), "error": str(error)})
        if args.once:
            break
        time.sleep(max(60, args.interval))


if __name__ == "__main__":
    main()
