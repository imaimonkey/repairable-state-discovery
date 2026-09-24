#!/usr/bin/env python3
"""Keep the three independent paper variants moving after their gate chains.

The dispatcher only submits work after server-local evidence is present.  It
never imports output between variants and never touches the server3 queue.
"""
from __future__ import annotations

import argparse
import json
import shlex
import subprocess
import time
from argparse import Namespace
from pathlib import Path

from v2r_independent_plan import make_base
from repairable_diffusion.src.v2r.artifacts import atomic_json, read_json

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "status/v2r/independent_variants.json"
SHA = "78fe5d7c1829b67d1bb1416b7205edfa647bb2fa"

VARIANTS = {
    "server1": {"host": "10.0.12.120", "qos": "lab_gpu_s1", "node": "devbox",
                "gres": "gpu:a6000:1", "py": "/home/kimhj/llada8b_basic/.venv/bin/python",
                "pythonpath": "", "exec": "/var/tmp/kimhj-v2r-reference/execution/gates-78fe5d7-s1",
                "source": "/var/tmp/kimhj-v2r-reference/upstream", "model": "/var/tmp/kimhj-v2r-reference/model-cache",
                "gate_root": "/var/tmp/kimhj-v2r-independent/server1", "output_root": "/var/tmp/kimhj-v2r-independent/server1",
                "seconds": 62.0, "task_seconds": {"math500": 62.0, "gsm8k": 94.0}, "target_hours": 2.0},
    "server2": {"host": "10.0.12.121", "qos": "lab_gpu_s2", "node": "server2",
                "gres": "gpu:a6000:1", "py": "/home/kimhj/llada8b_basic/.venv/bin/python",
                "pythonpath": "", "exec": "/var/tmp/kimhj-v2r-reference/execution/gates-78fe5d7-s2",
                "source": "/var/tmp/kimhj-v2r-reference/upstream", "model": "/home/kimhj/.cache/huggingface/hub",
                "gate_root": "/var/tmp/kimhj-v2r-independent/server2", "output_root": "/var/tmp/kimhj-v2r-independent/server2",
                "seconds": 62.0, "task_seconds": {"math500": 62.0, "gsm8k": 94.0}, "target_hours": 2.0},
    "server4": {"host": "10.0.12.163", "qos": "lab_gpu_s4", "node": "server4",
                "gres": "gpu:rtx_pro_6000:1", "py": "/data/kimhj/.local/share/uv/python/cpython-3.11.14-linux-x86_64-gnu/bin/python3.11",
                "pythonpath": "/data/kimhj/llada8b_basic/.venv/lib/python3.11/site-packages", "exec": "/var/tmp/kimhj-v2r-reference/execution/gates-78fe5d7",
                "source": "/var/tmp/kimhj-v2r-reference/upstream", "model": "/var/tmp/kimhj-v2r-reference/model-cache",
                "gate_root": "/var/tmp/kimhj-v2r-independent/server4", "output_root": "/var/tmp/kimhj-v2r-independent/server4",
                "seconds": 26.0, "task_seconds": {"math500": 26.0, "gsm8k": 28.0}, "target_hours": 2.0},
}


def run(command: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, text=True, capture_output=True, check=check)


def ssh(v: dict, command: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return run(["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=8", f"kimhj@{v['host']}", command], check=check)


def remote_json(v: dict, path: str) -> dict | None:
    result = ssh(v, f"test -s {shlex.quote(path)} && cat {shlex.quote(path)}", check=False)
    if result.returncode:
        return None
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return None


def scp_from(v: dict, remote: str, local: Path) -> None:
    local.parent.mkdir(parents=True, exist_ok=True)
    run(["scp", "-q", f"kimhj@{v['host']}:{remote}", str(local)])


def scp_to(v: dict, local: Path, remote: str) -> None:
    run(["scp", "-q", str(local), f"kimhj@{v['host']}:{remote}"])


def gate_reports(v: dict, task: str) -> dict | None:
    result = {}
    gate_dir = f"outputs/v2r_reference/gate-78fe5d7-llada-{task}"
    for stage in ("R0", "R1", "R2"):
        path = f"{v['gate_root']}/{gate_dir}/{stage}/gate_report.json"
        report = remote_json(v, path)
        if report is None:
            return None
        result[stage] = report
    return result


def submit_worker(v: dict, *, name: str, manifest: str, gates: str, shard: int,
                  run_dir: str, dependency: str | None = None) -> str:
    logs = f"{run_dir}/logs"
    ssh(v, f"mkdir -p {shlex.quote(logs)}")
    export = ["ALL", "V2R_HUB_DISABLE_XET=1", f"V2R_EXEC_ROOT={v['exec']}", f"V2R_PY={v['py']}",
              f"V2R_MANIFEST={manifest}", f"V2R_GATES={gates}", f"V2R_SHARD={shard}",
              f"V2R_RUN_DIR={run_dir}", f"V2R_EXECUTION_SHA={SHA}"]
    if v["pythonpath"]:
        export.append(f"V2R_PYTHONPATH={v['pythonpath']}")
    args = ["sbatch", "--parsable", "--partition=gpu", f"--qos={v['qos']}",
            f"--nodelist={v['node']}", f"--gres={v['gres']}", "--cpus-per-task=4",
            "--mem=48G", "--time=04:00:00", f"--job-name={name}",
            f"--chdir={v['exec']}", f"--export={','.join(export)}",
            f"--output={logs}/slurm-%j.out", f"--error={logs}/slurm-%j.err",
            str(ROOT / "runtime/v2r_independent_worker.sbatch")]
    if dependency:
        args.insert(2, f"--dependency={dependency}")
    result = run(args)
    return result.stdout.strip().split(";")[0]


def variant_dir(server: str) -> Path:
    path = ROOT / "status/v2r/independent" / server
    path.mkdir(parents=True, exist_ok=True)
    return path


def summary_status(doc: dict) -> str:
    """Derive the registry summary from the per-task states.

    The original registry retained its bootstrap ``R0_RUNNING`` label after
    the task-local state had advanced.  Keep this summary informational only:
    it must never gate or alter a scientific submission.
    """
    states = [
        state
        for variant in doc.get("variants", {}).values()
        for state in variant.get("task_status", {}).values()
    ]
    if any("ERROR" in state or "FAILED" in state or "BLOCKED" in state for state in states):
        return "ATTENTION_REQUIRED"
    for state in ("DEEP_RUNNING", "DEEP_READY", "BASE_RUNNING", "BASE_QUEUED_AFTER_R2",
                  "R2_RUNNING", "R2_PASS", "R1_RUNNING", "R0_RUNNING"):
        if state in states:
            return state
    return "ACTIVE"


def persist(doc: dict) -> None:
    # This is a status projection, not a scientific input or gate decision.
    doc["status"] = summary_status(doc)
    atomic_json(REGISTRY, doc)


def normalize_entry_paths(server: str, v: dict, entry: dict) -> None:
    """Repair stale status-only paths after a scratch-root migration.

    Existing jobs and scientific artifacts are authoritative.  Earlier
    registry entries for server2/server4 still pointed at /dev/shm even after
    their workers were moved to /var/tmp.  Repoint only the status references
    so future completion/finalization checks observe the artifacts that the
    submitted jobs actually write; never copy, delete, or re-submit data.
    """
    old_root = entry.get("output_root")
    new_root = v["output_root"]
    if old_root and old_root != new_root:
        for section in ("bases", "deeps"):
            for value in entry.get(section, {}).values():
                if not isinstance(value, dict):
                    continue
                for key, item in list(value.items()):
                    if isinstance(item, str):
                        value[key] = item.replace(old_root, new_root)
                    elif isinstance(item, dict):
                        for nested_key, nested_item in list(item.items()):
                            if isinstance(nested_item, str):
                                item[nested_key] = nested_item.replace(old_root, new_root)
    # Always project the configured root, including registries created before
    # the scratch-root migration where the old value may be incomplete.
    entry["output_root"] = new_root
    entry["node"] = v["node"]
    entry["execution_root"] = v["exec"]
    entry["gate_root"] = v["gate_root"]
    entry["model_cache"] = v["model"]


def activate_base(server: str, task: str, v: dict, entry: dict, doc: dict, reports: dict) -> None:
    local_dir = variant_dir(server)
    gates_local = local_dir / f"{task}_gates.json"
    atomic_json(gates_local, reports)
    manifest_local = local_dir / f"{task}_base_manifest.json"
    make_base(Namespace(
        server=server,
        task=task,
        execution_root=v["exec"],
        source_cache="/var/tmp/kimhj-v2r-reference/upstream",
        model_cache=v["model"],
        seconds_per_item=v.get("task_seconds", {}).get(task, v["seconds"]),
        target_shard_hours=v["target_hours"],
        manifest_out=str(manifest_local),
    ))
    manifest = read_json(manifest_local)
    run_root = f"{v['output_root']}/outputs/v2r_reference"
    manifest_remote = f"{run_root}/plans/{manifest['run_id']}.json"
    gates_remote = f"{run_root}/plans/{manifest['run_id']}.gates.json"
    run_dir = f"{run_root}/runs/{manifest['run_id']}"
    ssh(v, f"mkdir -p {shlex.quote(run_root + '/plans')} {shlex.quote(run_root + '/runs')}")
    scp_to(v, manifest_local, manifest_remote)
    scp_to(v, gates_local, gates_remote)
    jobs = []
    for shard in manifest["shards"]:
        jobs.append(submit_worker(v, name=f"v2r-ind-{server}-{task}-base-{shard['shard_id']:03d}",
                                  manifest=manifest_remote, gates=gates_remote,
                                  shard=shard["shard_id"], run_dir=run_dir))
    entry.setdefault("bases", {})[task] = {"manifest": manifest_remote, "gates": gates_remote, "run_dir": run_dir,
                                            "local_manifest": str(manifest_local), "local_gates": str(gates_local),
                                            "jobs": jobs, "shard_count": len(manifest["shards"])}
    entry.setdefault("task_status", {})[task] = "BASE_RUNNING"
    entry["status"] = "ACTIVE_MULTI_TASK"
    persist(doc)


def all_done(v: dict, manifest_path: str, run_dir: str) -> bool:
    manifest = remote_json(v, manifest_path)
    if not manifest:
        return False
    paths = [f"{run_dir}/shards/shard-{row['shard_id']:03d}/DONE.json" for row in manifest["shards"]]
    check = " && ".join(f"test -s {shlex.quote(path)}" for path in paths)
    return ssh(v, check, check=False).returncode == 0


def any_running(job_ids: list[str]) -> bool:
    """Return whether a queued base shard has reached an active Slurm state."""
    if not job_ids:
        return False
    result = run(["squeue", "-h", "-j", ",".join(job_ids), "-o", "%T"], check=False)
    return any(line.strip() == "RUNNING" for line in result.stdout.splitlines())


def finalize_base(server: str, task: str, v: dict, entry: dict, doc: dict) -> None:
    base = entry["bases"][task]
    helper_remote = f"/var/tmp/kimhj-v2r-independent/{server}/v2r_independent_plan.py"
    scp_to(v, ROOT / "runtime/v2r_independent_plan.py", helper_remote)
    deep_parent = f"{v['output_root']}/outputs/v2r_reference/deep/{task}"
    report_remote = f"{deep_parent}/deep_report.json"
    ssh(v, f"mkdir -p {shlex.quote(deep_parent)}")
    command = (
        f"PYTHONPATH={shlex.quote(v['exec'])} {shlex.quote(v['py'])} {shlex.quote(helper_remote)} finalize "
        f"--server {shlex.quote(server)} --execution-root {shlex.quote(v['exec'])} "
        f"--base-manifest {shlex.quote(base['manifest'])} --gates {shlex.quote(base['gates'])} "
        f"--base-run-dir {shlex.quote(base['run_dir'])} --deep-parent {shlex.quote(deep_parent)} "
        f"--report-out {shlex.quote(report_remote)}"
    )
    result = ssh(v, command, check=False)
    if result.returncode:
        entry["status"] = "BASE_MERGE_ERROR"
        entry["error"] = (result.stderr or result.stdout)[-4000:]
        persist(doc)
        return
    report = remote_json(v, report_remote)
    if report is None:
        return
    entry.setdefault("deeps", {})[task] = {"parent": deep_parent, "report": report_remote, "plans": report.get("plans", {})}
    entry.setdefault("task_status", {})[task] = "DEEP_READY"
    entry["status"] = "ACTIVE_MULTI_TASK"
    persist(doc)


def activate_deep(server: str, task: str, v: dict, entry: dict, doc: dict) -> None:
    deep = entry.get("deeps", {}).get(task)
    if not deep or deep.get("jobs"):
        return
    core = deep["plans"].get("core", {})
    temporal = deep["plans"].get("temporal", {})
    if core.get("status") != "READY":
        entry["status"] = "DEEP_BLOCKED"
        persist(doc)
        return
    core_manifest = remote_json(v, core["manifest"])
    if not core_manifest:
        return
    jobs = {}
    for purpose, plan in (("core", core),):
        jobs[purpose] = [submit_worker(v, name=f"v2r-ind-{server}-{task}-{purpose}-{row['shard_id']:03d}",
                                        manifest=plan["manifest"], gates=plan["gates"],
                                        shard=row["shard_id"], run_dir=plan["run_dir"])
                         for row in remote_json(v, plan["manifest"])["shards"]]
    if temporal.get("status") == "READY":
        dependency = "afterok:" + ":".join(jobs["core"])
        jobs["temporal"] = [submit_worker(v, name=f"v2r-ind-{server}-{task}-temporal-{row['shard_id']:03d}",
                                            manifest=temporal["manifest"], gates=temporal["gates"],
                                            shard=row["shard_id"], run_dir=temporal["run_dir"],
                                            dependency=dependency)
                             for row in remote_json(v, temporal["manifest"])["shards"]]
    deep["jobs"] = jobs
    entry.setdefault("task_status", {})[task] = "DEEP_RUNNING"
    entry["status"] = "ACTIVE_MULTI_TASK"
    persist(doc)


def ensure_temporal_replan(server: str, task: str, v: dict, entry: dict, doc: dict) -> None:
    """Recover a resource-only temporal plan without changing scientific inputs.

    Server1's first temporal projection used a conservative 60 GPU-hour
    envelope and correctly refused to freeze 32 items when it estimated 24.
    Once the same base bank is available, use a separately named plan with an
    explicitly recorded 80 GPU-hour envelope.  This remains within the node's
    four-GPU QoS allocation and is submitted after the already queued core
    jobs; no existing core job or plan is rewritten.
    """
    if server != "server1" or task != "math500":
        return
    deep = entry.get("deeps", {}).get(task, {})
    plans = deep.get("plans", {})
    temporal = plans.get("temporal", {})
    jobs = deep.get("jobs", {})
    if temporal.get("status") != "BLOCKED" or jobs.get("temporal"):
        return
    if deep.get("temporal_replan_attempted"):
        return
    deep["temporal_replan_attempted"] = True
    parent = deep.get("parent")
    base = entry.get("bases", {}).get(task, {})
    if not parent or not base.get("manifest") or not base.get("gates") or not base.get("run_dir"):
        entry["status"] = "TEMPORAL_REPLAN_ERROR"
        entry["error"] = "TEMPORAL_REPLAN_MISSING_BASE_BINDING"
        persist(doc)
        return
    helper_remote = f"/var/tmp/kimhj-v2r-independent/{server}/v2r_independent_plan.py"
    scp_to(v, ROOT / "runtime/v2r_independent_plan.py", helper_remote)
    replan_parent = f"{parent}/temporal_replan_v2"
    report_remote = f"{replan_parent}/report.json"
    ssh(v, f"mkdir -p {shlex.quote(replan_parent)}")
    command = (
        f"PYTHONPATH={shlex.quote(v['exec'])} {shlex.quote(v['py'])} {shlex.quote(helper_remote)} "
        f"replan-temporal --server {shlex.quote(server)} --execution-root {shlex.quote(v['exec'])} "
        f"--base-manifest {shlex.quote(base['manifest'])} --gates {shlex.quote(base['gates'])} "
        f"--base-run-dir {shlex.quote(base['run_dir'])} --deep-parent {shlex.quote(replan_parent)} "
        f"--available-gpu-hours 80 --deadline-hours 60 --report-out {shlex.quote(report_remote)}"
    )
    result = ssh(v, command, check=False)
    if result.returncode:
        entry["status"] = "TEMPORAL_REPLAN_ERROR"
        entry["error"] = (result.stderr or result.stdout)[-4000:]
        persist(doc)
        return
    report = remote_json(v, report_remote)
    if not report or report.get("status") != "READY":
        entry["status"] = "TEMPORAL_REPLAN_BLOCKED"
        entry["error"] = json.dumps(report or {"error": "NO_REPLAN_REPORT"})[-4000:]
        persist(doc)
        return
    plan = {key: report[key] for key in ("status", "budget", "manifest", "gates", "run_dir", "selected_n", "shard_count")}
    deep["plans"]["temporal"] = plan
    core_jobs = [str(job) for job in jobs.get("core", [])]
    if not core_jobs:
        entry["status"] = "TEMPORAL_REPLAN_ERROR"
        entry["error"] = "TEMPORAL_REPLAN_MISSING_CORE_JOBS"
        persist(doc)
        return
    manifest = remote_json(v, plan["manifest"])
    if not manifest:
        entry["status"] = "TEMPORAL_REPLAN_ERROR"
        entry["error"] = "TEMPORAL_REPLAN_MISSING_MANIFEST"
        persist(doc)
        return
    dependency = "afterok:" + ":".join(core_jobs)
    temporal_jobs = [submit_worker(
        v, name=f"v2r-ind-{server}-{task}-temporal-v2-{row['shard_id']:03d}",
        manifest=plan["manifest"], gates=plan["gates"], shard=row["shard_id"],
        run_dir=plan["run_dir"], dependency=dependency
    ) for row in manifest["shards"]]
    deep["jobs"]["temporal"] = temporal_jobs
    deep["temporal_replan"] = {
        "status": "SUBMITTED", "available_gpu_hours": 80.0,
        "deadline_hours": 60.0, "dependency": dependency,
        "execution_git_sha": SHA,
    }
    entry.setdefault("task_status", {})[task] = "DEEP_RUNNING"
    entry["status"] = "ACTIVE_MULTI_TASK"
    persist(doc)


def merge_deep(server: str, task: str, v: dict, entry: dict, doc: dict) -> None:
    deep = entry.get("deeps", {}).get(task, {})
    if not deep.get("jobs"):
        return
    helper_remote = f"/var/tmp/kimhj-v2r-independent/{server}/v2r_independent_plan.py"
    merged = deep.setdefault("merged", {})
    for purpose in ("core", "temporal"):
        plan = deep["plans"].get(purpose, {})
        if plan.get("status") != "READY" or purpose in merged:
            continue
        manifest = remote_json(v, plan["manifest"])
        if not manifest or not all_done(v, plan["manifest"], plan["run_dir"]):
            continue
        report = f"{deep['parent']}/{purpose}_merged.json"
        command = (
            f"PYTHONPATH={shlex.quote(v['exec'])} {shlex.quote(v['py'])} {shlex.quote(helper_remote)} merge "
            f"--manifest {shlex.quote(plan['manifest'])} --gates {shlex.quote(plan['gates'])} "
            f"--run-dir {shlex.quote(plan['run_dir'])} --report-out {shlex.quote(report)}"
        )
        result = ssh(v, command, check=False)
        if result.returncode:
            entry.setdefault("task_status", {})[task] = "DEEP_MERGE_ERROR"
            entry["error"] = (result.stderr or result.stdout)[-4000:]
            persist(doc)
            return
        merged[purpose] = report
    if "core" in merged and (deep["plans"].get("temporal", {}).get("status") != "READY" or "temporal" in merged):
        entry.setdefault("task_status", {})[task] = "PAPER_VARIANT_READY"
    persist(doc)


def tick() -> None:
    doc = read_json(REGISTRY)
    for server, v in VARIANTS.items():
        entry = doc["variants"][server]
        normalize_entry_paths(server, v, entry)
        for task in ("math500", "gsm8k"):
            reports = gate_reports(v, task)
            if reports:
                entry.setdefault("gate_status_by_task", {})[task] = {
                    stage: report.get("status") for stage, report in reports.items()
                }
                if not all(report.get("status") == "PASS" for report in reports.values()):
                    last = next((report for report in reports.values() if report.get("status") != "PASS"), None)
                    entry.setdefault("task_status", {})[task] = f"{last.get('gate', 'GATE')}_{last.get('status', 'UNKNOWN')}"
                    persist(doc)
            bases = entry.setdefault("bases", {})
            if reports and all(report.get("status") == "PASS" for report in reports.values()) and task not in bases:
                activate_base(server, task, v, entry, doc, reports)
            base = bases.get(task)
            if (base and reports and all(report.get("status") == "PASS" for report in reports.values())
                    and entry.setdefault("task_status", {}).get(task) in {"R2_RUNNING", "R2_PASS"}):
                entry["task_status"][task] = (
                    "BASE_RUNNING" if any_running([str(job) for job in base.get("jobs", [])])
                    else "BASE_QUEUED_AFTER_R2"
                )
                entry["status"] = "ACTIVE_MULTI_TASK"
                persist(doc)
            if base and entry.setdefault("task_status", {}).get(task) == "BASE_QUEUED_AFTER_R2" \
                    and any_running([str(job) for job in base.get("jobs", [])]):
                entry["task_status"][task] = "BASE_RUNNING"
                entry["status"] = "ACTIVE_MULTI_TASK"
                persist(doc)
            if base and entry.setdefault("task_status", {}).get(task) in {"BASE_RUNNING", "BASE_QUEUED_AFTER_R2"} \
                    and all_done(v, base["manifest"], base["run_dir"]):
                finalize_base(server, task, v, entry, doc)
            if entry.setdefault("task_status", {}).get(task) == "DEEP_READY":
                activate_deep(server, task, v, entry, doc)
            if entry.setdefault("task_status", {}).get(task) == "DEEP_RUNNING":
                ensure_temporal_replan(server, task, v, entry, doc)
                merge_deep(server, task, v, entry, doc)
        # Persist even when this interval only observed a running gate.  This
        # keeps status-only path normalization durable instead of waiting for
        # a later scientific state transition.
        persist(doc)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--interval", type=int, default=90)
    parser.add_argument("--once", action="store_true")
    args = parser.parse_args()
    while True:
        try:
            tick()
        except Exception as exc:
            print(f"independent dispatcher tick failed: {exc!r}", flush=True)
        if args.once:
            return
        time.sleep(max(30, args.interval))


if __name__ == "__main__":
    main()
