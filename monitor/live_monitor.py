#!/usr/bin/env python3
"""Read-only execution/evidence monitor for the frozen V2 experiment.

This module deliberately does not import the scientific package or execute a
scientific analysis. It observes Slurm, remote filesystem metadata, and
already-written result artifacts, then commits only monitoring metadata and
safe compact artifacts to the monitoring branch.
"""

from __future__ import annotations

import csv
import datetime as dt
import fcntl
import hashlib
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LIVE = ROOT / "status" / "live"
RUNTIME = Path(os.environ.get("RSD_MONITOR_RUNTIME", "/data/kimhj/.cache/rsd-live-monitor"))
LOCK_PATH = RUNTIME / "monitor.lock"
PAPER_REPO = Path("/data/kimhj/repairable-state-discovery-iclr-2027")
DEV_REPO = Path("/data/kimhj/repairable-state-discovery")
BASELINE_COMMIT = "c41d6b10ed0c041581cae4f84a41b4ad783ebe00"
DEADLINE = dt.datetime(2026, 9, 26, 20, 59, tzinfo=dt.timezone(dt.timedelta(hours=9)))
SSH_OPTS = ["-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=no", "-o", "ConnectTimeout=6"]

RUNS: list[dict[str, Any]] = [
    {
        "job_id": "50668", "run_name": "v2_math500_llada", "model": "LLaDA-8B-Instruct",
        "task": "MATH-500", "server": "server1", "host": "10.0.12.120",
        "sha": "0dd161c8cf4bf3e7dbe4042234a0954950ce870e",
        "workdir": "/home/kimhj/repairable-state-discovery-v2-exec",
        "config": "repairable_diffusion/configs/v2/runs/full_math500_llada.yaml",
        "output": "/home/kimhj/repairable-state-discovery-v2-exec/repairable_diffusion/outputs/v2_measurement/v2_math500_llada",
        "items": 500, "temporal_items": 128, "mechanism_items": 128, "fresh_enabled": True,
    },
    {
        "job_id": "50669", "run_name": "v2_gsm8k_llada", "model": "LLaDA-8B-Instruct",
        "task": "GSM8K", "server": "server1", "host": "10.0.12.120",
        "sha": "0dd161c8cf4bf3e7dbe4042234a0954950ce870e",
        "workdir": "/home/kimhj/repairable-state-discovery-v2-exec",
        "config": "repairable_diffusion/configs/v2/runs/full_gsm8k_llada.yaml",
        "output": "/home/kimhj/repairable-state-discovery-v2-exec/repairable_diffusion/outputs/v2_measurement/v2_gsm8k_llada",
        "items": 1319, "temporal_items": 128, "mechanism_items": 128, "fresh_enabled": True,
    },
    {
        "job_id": "50738", "run_name": "v2_bbh_logical3_llada", "model": "LLaDA-8B-Instruct",
        "task": "BBH logical3", "server": "server1", "host": "10.0.12.120",
        "sha": "0dd161c8cf4bf3e7dbe4042234a0954950ce870e",
        "workdir": "/home/kimhj/repairable-state-discovery-v2-exec",
        "config": "repairable_diffusion/configs/v2/runs/full_bbh_logical3_llada.yaml",
        "output": "/home/kimhj/repairable-state-discovery-v2-exec/repairable_diffusion/outputs/v2_measurement/v2_bbh_logical3_llada",
        "items": 250, "temporal_items": 0, "mechanism_items": 0, "fresh_enabled": False,
    },
    {
        "job_id": "50752", "run_name": "v2_bbh_logical5_llada", "model": "LLaDA-8B-Instruct",
        "task": "BBH logical5", "server": "server2", "host": "10.0.12.121",
        "sha": "0dd161c8cf4bf3e7dbe4042234a0954950ce870e",
        "workdir": "/home/kimhj/repairable-state-discovery-v2-exec",
        "config": "repairable_diffusion/configs/v2/runs/full_bbh_logical5_llada.yaml",
        "output": "/home/kimhj/repairable-state-discovery-v2-exec/repairable_diffusion/outputs/v2_measurement/v2_bbh_logical5_llada",
        "items": 250, "temporal_items": 0, "mechanism_items": 0, "fresh_enabled": False,
    },
    {
        "job_id": "50753", "run_name": "v2_bbh_logical7_llada", "model": "LLaDA-8B-Instruct",
        "task": "BBH logical7", "server": "server2", "host": "10.0.12.121",
        "sha": "0dd161c8cf4bf3e7dbe4042234a0954950ce870e",
        "workdir": "/home/kimhj/repairable-state-discovery-v2-exec",
        "config": "repairable_diffusion/configs/v2/runs/full_bbh_logical7_llada.yaml",
        "output": "/home/kimhj/repairable-state-discovery-v2-exec/repairable_diffusion/outputs/v2_measurement/v2_bbh_logical7_llada",
        "items": 250, "temporal_items": 0, "mechanism_items": 0, "fresh_enabled": False,
    },
    {
        "job_id": "50754", "run_name": "v2_mbpp_llada", "model": "LLaDA-8B-Instruct",
        "task": "MBPP sanitized", "server": "server2", "host": "10.0.12.121",
        "sha": "0dd161c8cf4bf3e7dbe4042234a0954950ce870e",
        "workdir": "/home/kimhj/repairable-state-discovery-v2-exec",
        "config": "repairable_diffusion/configs/v2/runs/full_mbpp_llada.yaml",
        "output": "/home/kimhj/repairable-state-discovery-v2-exec/repairable_diffusion/outputs/v2_measurement/v2_mbpp_llada",
        "items": 257, "temporal_items": 0, "mechanism_items": 0, "fresh_enabled": False,
    },
    {
        "job_id": "50923", "run_name": "v2_math500_dream", "model": "Dream-v0-Instruct-7B",
        "task": "MATH-500", "server": "server4", "host": "10.0.12.163",
        "sha": "8b1361d3d8d60a58e28847ac35af8dfc2b023d2d",
        "workdir": "/data/kimhj/repairable-state-discovery-v2-dream-hotfix-8b1361d",
        "config": "repairable_diffusion/configs/v2/runs/full_math500_dream.yaml",
        "output": "/data/kimhj/repairable-state-discovery-v2-dream-hotfix-8b1361d/repairable_diffusion/outputs/v2_measurement/v2_math500_dream",
        "items": 500, "temporal_items": 0, "mechanism_items": 0, "fresh_enabled": False,
    },
    {
        "job_id": "50924", "run_name": "v2_gsm8k_dream", "model": "Dream-v0-Instruct-7B",
        "task": "GSM8K", "server": "server4", "host": "10.0.12.163",
        "sha": "8b1361d3d8d60a58e28847ac35af8dfc2b023d2d",
        "workdir": "/data/kimhj/repairable-state-discovery-v2-dream-hotfix-8b1361d",
        "config": "repairable_diffusion/configs/v2/runs/full_gsm8k_dream.yaml",
        "output": "/data/kimhj/repairable-state-discovery-v2-dream-hotfix-8b1361d/repairable_diffusion/outputs/v2_measurement/v2_gsm8k_dream",
        "items": 1319, "temporal_items": 0, "mechanism_items": 0, "fresh_enabled": False,
    },
]

REMOTE_CODE = r'''
import hashlib, json, os, subprocess, time
from collections import Counter, defaultdict
from pathlib import Path

specs = json.loads({spec_json!r})
def meta(path):
    p = Path(path)
    if not p.exists():
        return {"exists": False, "path": str(p)}
    st = p.stat()
    return {"exists": True, "path": str(p), "size_bytes": st.st_size,
            "mtime_epoch": st.st_mtime, "mtime_kst": time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(st.st_mtime))}
def line_count(path):
    try:
        with open(path, "rb") as fh:
            return sum(1 for line in fh if line.strip())
    except Exception:
        return None
def jsonl_summary(path):
    out = {"rows": 0, "stage": {}, "operator": {}, "stage_operator": {},
           "item_trajectory": 0, "items": 0, "steps": {}}
    seen = set(); items = set(); stages = Counter(); ops = Counter(); pairs = Counter(); steps = Counter()
    try:
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                if not line.strip(): continue
                r = json.loads(line); out["rows"] += 1
                stage = str(r.get("stage", "<none>")); op = str(r.get("operator_id", "<none>"))
                stages[stage] += 1; ops[op] += 1; pairs[f"{stage}/{op}"] += 1
                if "item_id" in r:
                    items.add(int(r["item_id"])); seen.add((int(r["item_id"]), int(r.get("trajectory_id", -1))))
                if "step_index" in r: steps[str(r["step_index"])] += 1
        out["stage"] = dict(stages); out["operator"] = dict(ops); out["stage_operator"] = dict(pairs)
        out["item_trajectory"] = len(seen); out["items"] = len(items); out["steps"] = dict(sorted(steps.items()))
    except Exception as exc:
        out["error"] = repr(exc)
    return out
def selector_expected(state_path):
    by = defaultdict(list)
    try:
        with open(state_path, encoding="utf-8") as fh:
            for line in fh:
                if line.strip():
                    r = json.loads(line); by[(int(r["item_id"]), int(r["trajectory_id"]))].append(r)
    except Exception:
        return {"records": None, "selector_rows": None, "unique_checkpoints": None, "confirmation_rows": None}
    def choices(rows):
        rows = sorted(rows, key=lambda r: int(r["step_index"]))
        digest = hashlib.sha256(f"selector|2027|{rows[0]['item_id']}|{rows[0]['trajectory_id']}".encode()).digest()
        idx = int.from_bytes(digest[:8], "big") % len(rows)
        near = lambda t: min(rows, key=lambda r: (abs(float(r["normalized_step"]) - t), int(r["step_index"])))
        chosen = [rows[idx], min(rows, key=lambda r: int(r["step_index"])), near(.25), near(.50), near(.75),
                  min(rows, key=lambda r: float(r.get("state_token_conf_mean", 0))),
                  max(rows, key=lambda r: float(r.get("masked_entropy_mean", 0))),
                  max(rows, key=lambda r: float(r.get("masked_ratio", 0))),
                  max(rows, key=lambda r: float(r.get("oof_value", float("-inf")))),
                  max(rows, key=lambda r: float(r.get("q_repair_loc", -1)))]
        return [int(x["step_index"]) for x in chosen]
    values = {k: choices(v) for k, v in by.items()}
    unique = sum(len(set(v)) for v in values.values())
    return {"records": len(values), "selector_rows": len(values) * 10,
            "unique_checkpoints": unique, "confirmation_rows": unique * 2 * 8}
def process_snapshot(run_name):
    rows = []
    try:
        ps = subprocess.run(["ps", "-eo", "pid=,etime=,pcpu=,pmem=,rss=,stat=,args="], text=True, capture_output=True, timeout=5).stdout
        for line in ps.splitlines():
            if "run_measurement" in line and run_name in line:
                rows.append(line.strip())
    except Exception: pass
    gpu = []
    try:
        text = subprocess.run(["nvidia-smi", "--query-compute-apps=pid,process_name,used_memory", "--format=csv,noheader"], text=True, capture_output=True, timeout=8).stdout
        gpu = [line.strip() for line in text.splitlines() if line.strip()]
    except Exception: pass
    return {"processes": rows, "gpu_compute_apps": gpu}

result = {"hostname": os.uname().nodename, "runs": {}, "liveness": process_snapshot(specs[0]["run_name"]) if specs else {}}
for s in specs:
    d = Path(s["output"])
    files = {}
    for name in ["run_manifest.json", "trajectories.pkl", "probe_complete.json", "probe_branches.jsonl", "state_values.jsonl", "selector_confirmation.csv", "fresh_sampling.jsonl", "existence.csv", "report.json", "scientific_provenance.json"]:
        files[name] = meta(d / name)
    branches = jsonl_summary(d / "probe_branches.jsonl") if files["probe_branches.jsonl"].get("exists") else {}
    state_rows = line_count(d / "state_values.jsonl") if files["state_values.jsonl"].get("exists") else None
    selector_rows = line_count(d / "selector_confirmation.csv")
    if selector_rows is not None and selector_rows > 0: selector_rows -= 1
    fresh_rows = line_count(d / "fresh_sampling.jsonl")
    existence_rows = line_count(d / "existence.csv")
    manifest = {}
    try: manifest = json.loads((d / "run_manifest.json").read_text())
    except Exception: pass
    prov = {}
    try: prov = json.loads((d / "scientific_provenance.json").read_text())
    except Exception: pass
    report = {}
    try: report = json.loads((d / "report.json").read_text())
    except Exception: pass
    expected = selector_expected(d / "state_values.jsonl") if state_rows else {}
    result["runs"][s["job_id"]] = {
        "files": files, "branches": branches, "state_rows": state_rows,
        "selector_rows": selector_rows, "fresh_rows": fresh_rows, "existence_rows": existence_rows,
        "manifest": manifest, "provenance": prov, "selector_expected": expected,
        "report": report,
        "liveness": process_snapshot(s["run_name"]),
    }
print(json.dumps(result, separators=(",", ":")))
'''


def now() -> dt.datetime:
    return dt.datetime.now(dt.timezone(dt.timedelta(hours=9)))


def iso(value: dt.datetime | None = None) -> str:
    return (value or now()).isoformat(timespec="seconds")


def run_cmd(args: list[str], *, timeout: int = 30, input_text: str | None = None) -> dict[str, Any]:
    try:
        proc = subprocess.run(args, input=input_text, text=True, capture_output=True, timeout=timeout)
        return {"ok": proc.returncode == 0, "returncode": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr}
    except Exception as exc:
        return {"ok": False, "returncode": None, "stdout": "", "stderr": repr(exc)}


def ssh(host: str, command: list[str], *, input_text: str | None = None, timeout: int = 30) -> dict[str, Any]:
    return run_cmd(["ssh", *SSH_OPTS, host, *command], timeout=timeout, input_text=input_text)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=False) + "\n", encoding="utf-8")


def read_json(path: Path, default: Any = None) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def parse_scontrol(text: str) -> dict[str, str]:
    pairs = re.findall(r"(\w+)=([^\s]+)", text)
    return dict(pairs)


def slurm_snapshot(job_id: str) -> dict[str, Any]:
    q = run_cmd(["squeue", "-h", "-j", job_id, "-o", "%i|%j|%T|%M|%l|%S|%R"], timeout=15)
    row: dict[str, Any] = {"job_id": job_id, "squeue": q["stdout"].strip(), "squeue_error": q["stderr"].strip()}
    if q["stdout"].strip():
        parts = q["stdout"].strip().split("|", 6)
        for key, value in zip(["job_id", "job_name", "state", "elapsed", "time_limit", "start_time", "reason"], parts):
            row[key] = value
    c = run_cmd(["scontrol", "show", "job", "-o", job_id], timeout=15)
    if c["ok"]:
        data = parse_scontrol(c["stdout"])
        for key in ["JobState", "RunTime", "TimeLimit", "StartTime", "EndTime", "ExitCode", "NodeList", "WorkDir", "StdOut", "StdErr", "Reason", "BatchHost"]:
            if key in data:
                row[key] = data[key]
    a = run_cmd(["sacct", "-X", "-n", "-P", "-j", job_id, "--format=JobIDRaw,State,Elapsed,ExitCode,NodeList"], timeout=15)
    row["sacct"] = a["stdout"].strip().splitlines()[:5]
    if row["sacct"]:
        parts = row["sacct"][0].split("|")
        if len(parts) >= 5:
            row.setdefault("job_id", parts[0])
            row["state"] = parts[1]
            row["elapsed"] = parts[2]
            row["exit_code"] = parts[3]
            row["node_list"] = parts[4]
    return row


def sstat_snapshot(job_id: str) -> dict[str, Any]:
    r = run_cmd(["sstat", "-j", f"{job_id}.batch", "--format=JobID,AveCPU,MaxRSS,MaxDiskWrite,MaxDiskRead", "-P"], timeout=15)
    return {"ok": r["ok"], "output": r["stdout"].strip(), "error": r["stderr"].strip()}


def remote_collect(host: str, specs: list[dict[str, Any]]) -> dict[str, Any]:
    spec_json = repr(json.dumps([{k: s[k] for k in ["job_id", "run_name", "output"]} for s in specs]))
    code = REMOTE_CODE.replace("{spec_json!r}", spec_json)
    result = ssh(host, ["python3", "-"], input_text=code, timeout=120)
    if not result["ok"]:
        return {"available": False, "host": host, "error": result["stderr"].strip() or result["stdout"].strip()}
    try:
        payload = json.loads(result["stdout"])
        payload["available"] = True
        return payload
    except Exception as exc:
        return {"available": False, "host": host, "error": f"invalid remote collector output: {exc}", "raw_tail": result["stdout"][-1000:]}


def collect_remote_by_host() -> dict[str, Any]:
    output: dict[str, Any] = {}
    for host, specs in _group_by(RUNS, "host").items():
        output[host] = remote_collect(host, specs)
    return output


def _group_by(values: list[dict[str, Any]], key: str) -> dict[str, list[dict[str, Any]]]:
    result: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for value in values:
        result[str(value[key])].append(value)
    return dict(result)


def local_git_state(repo: Path) -> dict[str, Any]:
    if not repo.exists():
        return {"path": str(repo), "available": False}
    head = run_cmd(["git", "-C", str(repo), "rev-parse", "HEAD"])
    branch = run_cmd(["git", "-C", str(repo), "branch", "--show-current"])
    status = run_cmd(["git", "-C", str(repo), "status", "--short"])
    remote = run_cmd(["git", "-C", str(repo), "rev-parse", "--verify", "origin/main"])
    tracked_dirty = [line for line in status["stdout"].splitlines() if line and not re.search(r"\?\? (results|outputs|logs|build)/", line)]
    return {"path": str(repo), "available": True, "head": head["stdout"].strip(), "branch": branch["stdout"].strip(),
            "origin_main": remote["stdout"].strip(), "status_lines": status["stdout"].splitlines(),
            "tracked_dirty": tracked_dirty}


def paper_observation() -> dict[str, Any]:
    state = local_git_state(PAPER_REPO)
    if not state.get("available"):
        return state
    files = {}
    for name in ["main.tex", "CLAIM_LEDGER.md", "PAPER_STATE.md", "RESULT_INTEGRATION.md", "Makefile", "main.pdf"]:
        p = PAPER_REPO / ("paper/" + name if name in {"main.tex", "main.pdf"} else name)
        files[name] = {"exists": p.exists(), "path": str(p), "size_bytes": p.stat().st_size if p.exists() else None}
    todo = run_cmd(["rg", "-n", "RESULT TODO|TODO|FIXME", str(PAPER_REPO / "paper"), "-g", "!build/**"], timeout=15)
    state["files"] = files
    state["todo_count"] = len(todo["stdout"].splitlines()) if todo["ok"] else 0 if todo["returncode"] == 1 else None
    state["claim_dependencies"] = {name: files[name]["exists"] for name in ["CLAIM_LEDGER.md", "PAPER_STATE.md", "RESULT_INTEGRATION.md"]}
    return state


def paper_build_observation(previous: dict[str, Any], *, force: bool = False) -> dict[str, Any]:
    previous_build = read_json(LIVE / "paper_build_status.json", {}) or {}
    head = previous.get("head")
    last = previous_build.get("checked_at_kst")
    due = force or not last
    if last:
        try:
            due = due or (now() - dt.datetime.fromisoformat(last)).total_seconds() >= 6 * 3600
        except ValueError:
            due = True
    result = {"checked_at_kst": iso(), "paper_head": head, "performed": False, "build_pass": previous_build.get("build_pass"), "submission_audit_pass": previous_build.get("submission_audit_pass"), "errors": []}
    if not due or not previous.get("available"):
        result["reason"] = "not_due" if previous.get("available") else "paper_repo_unavailable"
        return result
    result["performed"] = True
    tmp = Path(tempfile.mkdtemp(prefix="rsd-paper-build-", dir="/tmp"))
    try:
        archive = tmp / "paper.tar"
        ar = run_cmd(["git", "-C", str(PAPER_REPO), "archive", "--format=tar", "HEAD", "-o", str(archive)], timeout=60)
        if not ar["ok"]:
            result["errors"].append(f"git archive failed: {ar['stderr'][-1000:]}")
            return result
        ex = run_cmd(["tar", "xf", str(archive), "-C", str(tmp)], timeout=60)
        if not ex["ok"]:
            result["errors"].append(f"tar extraction failed: {ex['stderr'][-1000:]}")
            return result
        makefile = tmp / "Makefile"
        if not makefile.exists():
            result["errors"].append("Makefile not present in paper HEAD")
            return result
        # Execute the build only inside the temporary archive checkout.
        build_proc = subprocess.run(["make"], cwd=tmp, text=True, capture_output=True, timeout=900)
        result["build_pass"] = build_proc.returncode == 0
        result["build_returncode"] = build_proc.returncode
        result["build_stdout_tail"] = build_proc.stdout[-3000:]
        result["build_stderr_tail"] = build_proc.stderr[-3000:]
        pdfs = list(tmp.rglob("*.pdf"))
        result["pdfs"] = [{"path": str(p.relative_to(tmp)), "size_bytes": p.stat().st_size} for p in pdfs]
        audit_target = run_cmd(["make", "-n", "submission-audit"], timeout=60)
        if audit_target["ok"]:
            audit = subprocess.run(["make", "submission-audit"], cwd=tmp, text=True, capture_output=True, timeout=900)
            result["submission_audit_pass"] = audit.returncode == 0
            result["audit_returncode"] = audit.returncode
            result["audit_stdout_tail"] = audit.stdout[-3000:]
            result["audit_stderr_tail"] = audit.stderr[-3000:]
        else:
            result["submission_audit_pass"] = None
            result["audit_reason"] = "submission-audit target unavailable"
    except Exception as exc:
        result["errors"].append(repr(exc))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return result


def storage_observation() -> dict[str, Any]:
    out: dict[str, Any] = {"local": run_cmd(["df", "-P", "/", "/data"], timeout=15)["stdout"].splitlines()}
    for host in ["10.0.12.120", "10.0.12.121", "10.0.12.163"]:
        result = ssh(host, ["df", "-P", "/", "/data"], timeout=15)
        out[host] = result["stdout"].splitlines() if result["ok"] else {"available": False, "error": result["stderr"].strip()}
    return out


def collect_compact_artifacts(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Copy only terminal, sealed, allowlisted artifacts into the monitor branch."""
    events = []
    allowlist = ["report.json", "scientific_provenance.json", "run_manifest.json", "probe_complete.json", "existence.csv", "selector_confirmation.csv", "state_values.jsonl", "fresh_sampling.jsonl", "probe_branches.jsonl"]
    for row in rows:
        if row["status"] != "SEALED" or not row["source_available"] or row.get("integrity_alerts"):
            continue
        dest = ROOT / "results" / "v2_artifacts" / f"{row['run_name']}_{row['job_id']}"
        if (dest / "artifact_manifest.json").exists() or (dest / "report.json").exists():
            continue
        spec = next((r for r in RUNS if r["job_id"] == row["job_id"]), None)
        if not spec:
            continue
        dest.mkdir(parents=True, exist_ok=True)
        copied = []
        for name in allowlist:
            info = row["files"].get(name, {})
            if not info.get("exists") or int(info.get("size_bytes", 0)) > 80_000_000:
                continue
            remote_path = f"{spec['host']}:{spec['output']}/{name}"
            cp = run_cmd(["scp", *SSH_OPTS, remote_path, str(dest / name)], timeout=180)
            if cp["ok"]:
                copied.append(name)
        config_name = Path(spec["config"]).name
        remote_config = f"{spec['host']}:{spec['workdir']}/{spec['config']}"
        config_dest = dest / config_name
        config_cp = run_cmd(["scp", *SSH_OPTS, remote_config, str(config_dest)], timeout=60)
        if config_cp["ok"]:
            copied.append(config_name)
        if not copied:
            shutil.rmtree(dest, ignore_errors=True)
            continue
        checksums = []
        for p in sorted(dest.iterdir()):
            if p.is_file() and p.name not in {"SHA256SUMS", "artifact_manifest.json"}:
                digest = hashlib.sha256(p.read_bytes()).hexdigest()
                checksums.append(f"{digest}  {p.name}")
        (dest / "SHA256SUMS").write_text("\n".join(checksums) + "\n", encoding="utf-8")
        write_json(dest / "artifact_manifest.json", {"schema": "v2_compact_artifact_v1", "collected_at_kst": iso(), "job_id": row["job_id"], "run_name": row["run_name"], "source_server": spec["server"], "source_host": spec["host"], "source_output": spec["output"], "execution_sha": row["execution_sha"], "copied_files": copied, "excluded_files": ["trajectories.pkl", "model weights", "active logs"], "collection_rule": "terminal SEALED only; no recomputation"})
        events.append({"timestamp_kst": iso(), "type": "COMPACT_ARTIFACT_COLLECTED", "job_id": row["job_id"], "run_name": row["run_name"], "files": copied})
    return events


def expected_totals(run: dict[str, Any], observed: dict[str, Any]) -> dict[str, Any]:
    base = int(run["items"]) * 8
    b = observed.get("branches", {})
    files = observed.get("files", {})
    probe_complete = bool(files.get("probe_complete.json", {}).get("exists"))
    stage = b.get("stage", {}) if isinstance(b, dict) else {}
    fidelity = int(stage.get("fidelity", 0))
    localization = int(stage.get("localization", 0))
    state_rows = observed.get("state_rows")
    selected_records = observed.get("selector_expected", {}).get("records")
    selectors = observed.get("selector_expected", {}).get("selector_rows")
    confirmation_expected = observed.get("selector_expected", {}).get("confirmation_rows")
    return {
        "items": {"completed": run["items"] if files.get("trajectories.pkl", {}).get("exists") and observed.get("manifest", {}).get("status") == "trajectory_bank_ready" else None, "expected": run["items"]},
        "trajectories": {"completed": base if files.get("trajectories.pkl", {}).get("exists") and observed.get("manifest", {}).get("status") == "trajectory_bank_ready" else None, "expected": base},
        "localization": {"completed": localization, "expected": localization if probe_complete else "UNKNOWN_EXPECTED_TOTAL"},
        "state_value": {"completed": state_rows, "expected": fidelity if probe_complete and fidelity else "UNKNOWN_EXPECTED_TOTAL"},
        "confirmation": {"completed": int(stage.get("confirmation", 0)), "expected": confirmation_expected if confirmation_expected is not None else "UNKNOWN_EXPECTED_TOTAL"},
        "selector": {"completed": observed.get("selector_rows"), "expected": selectors if selectors is not None else "UNKNOWN_EXPECTED_TOTAL"},
        "mechanism_control": {"completed": 0, "expected": 0 if not run["mechanism_items"] else "UNKNOWN_EXPECTED_TOTAL"},
        "temporal": {"completed": None, "expected": run["temporal_items"] if run["temporal_items"] else 0},
        "fresh_sampling": {"completed": observed.get("fresh_rows"), "expected": "UNKNOWN_EXPECTED_TOTAL" if run["fresh_enabled"] else 0},
    }


def classify(run: dict[str, Any], slurm: dict[str, Any], observed: dict[str, Any]) -> str:
    if not observed.get("available", True):
        return "UNOBSERVABLE"
    state = str(slurm.get("state") or slurm.get("JobState") or "UNKNOWN")
    live = observed.get("liveness", {})
    process = bool(live.get("processes"))
    gpu = bool(live.get("gpu_compute_apps"))
    files = observed.get("files", {})
    recent = False
    current = dt.datetime.now().timestamp()
    for name in ["probe_branches.jsonl", "state_values.jsonl", "selector_confirmation.csv", "report.json"]:
        m = files.get(name, {}).get("mtime_epoch")
        if m and current - float(m) < 1800:
            recent = True
    if state == "RUNNING" and (process or gpu) and not recent:
        return "ACTIVE_COMPUTE_BUFFERED_OUTPUT"
    if state == "RUNNING" and recent:
        return "PROGRESSING_ARTIFACTS"
    if state == "RUNNING":
        return "UNOBSERVABLE"
    return state


def matrix_row(run: dict[str, Any], slurm: dict[str, Any], remote: dict[str, Any], baseline: dict[str, Any]) -> dict[str, Any]:
    observed = remote.get("runs", {}).get(run["job_id"], {}) if remote.get("available") else {"available": False}
    observed["available"] = bool(remote.get("available"))
    totals = expected_totals(run, observed) if remote.get("available") else {
        key: {"completed": "UNOBSERVABLE", "expected": (run["items"] if key == "items" else run["items"] * 8) if key in {"items", "trajectories"} else "UNKNOWN_EXPECTED_TOTAL"}
        for key in ["items", "trajectories", "localization", "state_value", "confirmation", "selector", "mechanism_control", "temporal", "fresh_sampling"]
    }
    files = observed.get("files", {})
    report = bool(files.get("report.json", {}).get("exists"))
    prov = bool(files.get("scientific_provenance.json", {}).get("exists"))
    prov_payload = observed.get("provenance", {})
    report_payload = observed.get("report", {})
    integrity_alerts = []
    for label, payload in [("run_manifest", observed.get("manifest", {})), ("report", report_payload), ("provenance", prov_payload)]:
        recorded_sha = payload.get("git_sha") if isinstance(payload, dict) else None
        if recorded_sha and recorded_sha != run["sha"]:
            integrity_alerts.append({"type": "EXECUTION_PROVENANCE_MISMATCH", "source": label, "expected": run["sha"], "observed": recorded_sha})
    if isinstance(observed.get("manifest"), dict) and isinstance(report_payload, dict):
        mcfg = observed["manifest"].get("config_sha256")
        rcfg = report_payload.get("config_sha256")
        if mcfg and rcfg and mcfg != rcfg:
            integrity_alerts.append({"type": "CONFIG_FINGERPRINT_MISMATCH", "expected": mcfg, "observed": rcfg})
    sealed = prov and str(prov_payload.get("status", "")).upper() == "SEALED"
    state = str(slurm.get("state") or slurm.get("JobState") or "UNKNOWN")
    if sealed and state == "COMPLETED": status = "SEALED"
    elif state == "COMPLETED" and not remote.get("available"): status = "UNOBSERVED"
    elif state == "RUNNING": status = "RUNNING"
    elif state in {"FAILED", "TIMEOUT", "CANCELLED", "OUT_OF_MEMORY"}: status = "FAILED_EXCLUDED"
    elif report: status = "COMPLETED_UNSEALED"
    else: status = "UNOBSERVED"
    return {"job_id": run["job_id"], "run_name": run["run_name"], "model": run["model"], "task": run["task"],
            "server": run["server"], "execution_sha": run["sha"], "config": run["config"], "slurm": slurm,
            "status": status, "classification": classify(run, slurm, observed), "totals": totals,
            "files": files, "manifest": observed.get("manifest", {}), "report": report_payload, "provenance": prov_payload,
            "integrity_alerts": integrity_alerts,
            "liveness": observed.get("liveness", {}), "sstat": sstat_snapshot(run["job_id"]),
            "source_available": remote.get("available", False), "source_error": remote.get("error"),
            "baseline": baseline}


def load_previous() -> dict[str, Any]:
    return read_json(LIVE / "current_status.json", {}) or {}


def count_delta(current: Any, previous: Any) -> Any:
    if not isinstance(current, int) or not isinstance(previous, int):
        return "UNOBSERVABLE"
    return current - previous


def progress_history(rows: list[dict[str, Any]], previous: dict[str, Any]) -> list[dict[str, Any]]:
    old = {str(row.get("job_id")): row for row in previous.get("jobs", []) if isinstance(row, dict)}
    result = []
    for row in rows:
        old_row = old.get(row["job_id"], {})
        totals = row["totals"]
        result.append({"timestamp_kst": iso(), "job_id": row["job_id"], "state": row["slurm"].get("state", row["slurm"].get("JobState")),
                       "stage": row["classification"], "persisted_completed": totals.get("confirmation", {}).get("completed"),
                       "expected": totals.get("confirmation", {}).get("expected"),
                       "confirmation_delta": count_delta(totals.get("confirmation", {}).get("completed"), old_row.get("totals", {}).get("confirmation", {}).get("completed")),
                       "localization_delta": count_delta(totals.get("localization", {}).get("completed"), old_row.get("totals", {}).get("localization", {}).get("completed")),
                       "state_value_delta": count_delta(totals.get("state_value", {}).get("completed"), old_row.get("totals", {}).get("state_value", {}).get("completed")),
                       "classification": row["classification"], "source_available": row["source_available"]})
    return result


def velocity_for(rows: list[dict[str, Any]]) -> None:
    history_path = LIVE / "progress_history.jsonl"
    if not history_path.exists():
        for row in rows: row["velocity"] = {"30m": "UNOBSERVABLE", "1h": "UNOBSERVABLE", "6h": "UNOBSERVABLE"}
        return
    entries = []
    for line in history_path.read_text(encoding="utf-8").splitlines():
        try: entries.append(json.loads(line))
        except Exception: pass
    current_time = now()
    for row in rows:
        current_value = row["totals"]["confirmation"].get("completed")
        values = {}
        for label, minutes in [("30m", 30), ("1h", 60), ("6h", 360)]:
            candidates = []
            for entry in entries:
                if str(entry.get("job_id")) != str(row["job_id"]): continue
                try: age = (current_time - dt.datetime.fromisoformat(entry["timestamp_kst"])).total_seconds() / 60
                except Exception: continue
                if 0 <= age <= minutes + 5 and isinstance(entry.get("persisted_completed"), int): candidates.append(entry)
            if not isinstance(current_value, int) or not candidates:
                values[label] = "UNOBSERVABLE"
            else:
                values[label] = current_value - min(candidates, key=lambda x: x["timestamp_kst"])["persisted_completed"]
        row["velocity"] = values


def event_list(rows: list[dict[str, Any]], previous: dict[str, Any]) -> list[dict[str, Any]]:
    old = {str(row.get("job_id")): row for row in previous.get("jobs", []) if isinstance(row, dict)}
    events = []
    for row in rows:
        before = old.get(row["job_id"], {})
        if before and before.get("status") != row.get("status"):
            events.append({"timestamp_kst": iso(), "type": "JOB_STATE_CHANGED", "job_id": row["job_id"], "from": before.get("status"), "to": row.get("status")})
        if row.get("status") == "SEALED" and before.get("status") != "SEALED":
            events.append({"timestamp_kst": iso(), "type": "PROVENANCE_SEALED", "job_id": row["job_id"], "run_name": row["run_name"]})
        if row.get("status") == "FAILED_EXCLUDED" and before.get("status") != "FAILED_EXCLUDED":
            events.append({"timestamp_kst": iso(), "type": "JOB_FAILED", "job_id": row["job_id"], "run_name": row["run_name"]})
        if row.get("integrity_alerts") and not before.get("integrity_alerts"):
            events.append({"timestamp_kst": iso(), "type": "EXECUTION_PROVENANCE_MISMATCH", "job_id": row["job_id"], "run_name": row["run_name"], "details": row["integrity_alerts"]})
        if row.get("source_available") is False and before.get("source_available") is True:
            events.append({"timestamp_kst": iso(), "type": "SERVER_ARTIFACT_ACCESS_LOST", "job_id": row["job_id"], "server": row["server"]})
        if row.get("source_available") is True and before.get("source_available") is False:
            events.append({"timestamp_kst": iso(), "type": "SERVER_ARTIFACT_ACCESS_RESTORED", "job_id": row["job_id"], "server": row["server"]})
    return events


def write_matrix(rows: list[dict[str, Any]]) -> None:
    path = LIVE / "v2_experiment_matrix.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["job_id", "run_name", "model", "task", "server", "execution_sha", "status", "classification", "slurm_state", "elapsed", "time_limit", "source_available", "trajectory_completed", "trajectory_expected", "localization_completed", "localization_expected", "state_value_completed", "state_value_expected", "confirmation_completed", "confirmation_expected", "selector_completed", "selector_expected", "report", "provenance", "sealed"]
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields); writer.writeheader()
        for row in rows:
            t = row["totals"]
            writer.writerow({"job_id": row["job_id"], "run_name": row["run_name"], "model": row["model"], "task": row["task"], "server": row["server"], "execution_sha": row["execution_sha"], "status": row["status"], "classification": row["classification"], "slurm_state": row["slurm"].get("state", row["slurm"].get("JobState", "")), "elapsed": row["slurm"].get("elapsed", row["slurm"].get("RunTime", "")), "time_limit": row["slurm"].get("time_limit", row["slurm"].get("TimeLimit", "")), "source_available": row["source_available"], "trajectory_completed": t["trajectories"]["completed"], "trajectory_expected": t["trajectories"]["expected"], "localization_completed": t["localization"]["completed"], "localization_expected": t["localization"]["expected"], "state_value_completed": t["state_value"]["completed"], "state_value_expected": t["state_value"]["expected"], "confirmation_completed": t["confirmation"]["completed"], "confirmation_expected": t["confirmation"]["expected"], "selector_completed": t["selector"]["completed"], "selector_expected": t["selector"]["expected"], "report": row["files"].get("report.json", {}).get("exists"), "provenance": row["files"].get("scientific_provenance.json", {}).get("exists"), "sealed": str(row["provenance"].get("status", "")).upper() == "SEALED"})


def write_attention(rows: list[dict[str, Any]], events: list[dict[str, Any]], readiness: dict[str, Any]) -> None:
    lines = [f"# Attention required\n\n{iso()}\n", "## NEW EVENTS"]
    lines += [f"- {e['type']}: job {e.get('job_id', '')}" for e in events] or ["- No new scientific or operational event since previous cycle."]
    lines += ["\n## P0"]
    lines += [f"- {x}" for x in readiness["blockers"]["p0"]] or ["- None observed"]
    lines += ["\n## P1"]
    lines += [f"- {x}" for x in readiness["blockers"]["p1"]] or ["- None observed"]
    lines += ["\n## ACTIVE JOBS"] + [f"- {r['job_id']} {r['run_name']}: {r['status']} / {r['classification']}" for r in rows if r["status"] == "RUNNING"]
    lines += ["\n## NEW SEALED RESULTS"] + [f"- {e.get('run_name', e.get('job_id'))}" for e in events if e["type"] == "PROVENANCE_SEALED"] or ["- None"]
    lines += ["\n## WHAT CHATGPT SHOULD READ NOW", "1. `status/live/current_status.json`", "2. `status/live/v2_experiment_matrix.csv`", "3. `status/live/analysis_handoff.json`"]
    (LIVE / "attention_required.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_readiness(rows: list[dict[str, Any]], paper: dict[str, Any], events: list[dict[str, Any]]) -> dict[str, Any]:
    sealed = [r for r in rows if r["status"] == "SEALED"]
    running = [r for r in rows if r["status"] == "RUNNING"]
    failed = [r for r in rows if r["status"] == "FAILED_EXCLUDED"]
    hours = (DEADLINE - now()).total_seconds() / 3600
    p0 = []
    p1 = []
    if not paper.get("available"):
        p0.append("paper repository unavailable")
    if any(r["status"] == "RUNNING" and r["task"] in {"MATH-500", "GSM8K"} and r["server"] == "server1" and not r["source_available"] for r in rows):
        p1.append("server1 artifact access unavailable for Tier-A observation")
    if any(r["job_id"] == "50752" and r["status"] == "FAILED_EXCLUDED" for r in rows):
        p1.append("BBH5 50752 failed and forensic root cause remains unresolved")
    for row in rows:
        if row.get("integrity_alerts"):
            p0.append(f"{row['job_id']} execution provenance mismatch; manual review before seal")
    if running:
        p1.append("active V2 jobs remain; final aggregate is intentionally not run")
    return {"generated_at_kst": iso(), "deadline_kst": DEADLINE.isoformat(), "hours_remaining": round(hours, 2),
            "experiment": {"sealed_rows": len(sealed), "running_rows": len(running), "failed_rows": len(failed), "aggregate_ready": len(sealed) == 8 and not running and not failed, "tier_a_status": [r["status"] for r in rows if r["task"] in {"MATH-500", "GSM8K"}], "backbone_status": {"LLaDA": sum(r["status"] == "SEALED" for r in rows if r["model"].startswith("LLaDA")), "Dream": sum(r["status"] == "SEALED" for r in rows if r["model"].startswith("Dream"))}},
            "paper": {"build_pass": paper.get("build", {}).get("build_pass"), "submission_audit_pass": paper.get("build", {}).get("submission_audit_pass"), "result_todos_remaining": paper.get("todo_count"), "generated_tables_ready": None, "generated_figures_ready": None, "anonymous_package_ready": False},
            "blockers": {"p0": p0, "p1": p1, "p2": []}, "latest_new_evidence": [e for e in events if e["type"] in {"PROVENANCE_SEALED", "REPORT_CREATED"}], "latest_event": events[-1] if events else None}


def append_jsonl(path: Path, values: list[dict[str, Any]]) -> None:
    if not values: return
    with path.open("a", encoding="utf-8") as fh:
        for value in values: fh.write(json.dumps(value, ensure_ascii=False, sort_keys=True) + "\n")


def git_commit_push(events: list[dict[str, Any]]) -> dict[str, Any]:
    add = run_cmd(["git", "-C", str(ROOT), "add", "-f", "status/live", "results/v2_artifacts"], timeout=30)
    if not add["ok"]: return {"commit": False, "push": False, "error": add["stderr"]}
    check = run_cmd(["git", "-C", str(ROOT), "status", "--short"], timeout=15)
    if not check["stdout"].strip(): return {"commit": False, "push": False, "message": "no changes"}
    message = f"monitor: {now().strftime('%Y-%m-%d %H:%M KST')}"
    if events: message = f"monitor: {events[0].get('type', 'event')}"
    commit = run_cmd(["git", "-C", str(ROOT), "commit", "-m", message], timeout=60)
    if not commit["ok"]: return {"commit": False, "push": False, "error": commit["stderr"]}
    push = run_cmd(["git", "-C", str(ROOT), "push", "origin", "HEAD:codex/iclr2027-live-monitor-20260923"], timeout=120)
    return {"commit": True, "push": push["ok"], "commit_output": commit["stdout"], "push_error": push["stderr"] if not push["ok"] else None}


def cycle() -> dict[str, Any]:
    started = now()
    previous = load_previous()
    remote_by_host = collect_remote_by_host()
    rows = []
    for run in RUNS:
        slurm = slurm_snapshot(run["job_id"])
        remote = remote_by_host.get(run["host"], {"available": False, "error": "host not collected"})
        row_remote = remote.get("runs", {}).get(run["job_id"], {})
        row_remote["available"] = bool(remote.get("available"))
        rows.append(matrix_row(run, slurm, remote, {"last_snapshot": previous.get("generated_at_kst")}))
    paper = paper_observation()
    storage = storage_observation()
    events = event_list(rows, previous)
    compact_events = collect_compact_artifacts(rows)
    events.extend(compact_events)
    velocity_for(rows)
    paper_build = paper_build_observation(paper, force=any(e["type"] == "PROVENANCE_SEALED" for e in events) or previous.get("paper", {}).get("head") != paper.get("head"))
    paper["build"] = paper_build
    history = progress_history(rows, previous)
    readiness = build_readiness(rows, paper, events)
    current = {"schema": "iclr2027_live_status_v1", "generated_at_kst": iso(), "collector_hostname": socket.gethostname(), "monitor_branch": "codex/iclr2027-live-monitor-20260923", "monitor_commit": run_cmd(["git", "-C", str(ROOT), "rev-parse", "HEAD"], timeout=15)["stdout"].strip(), "baseline_analysis_bundle_commit": BASELINE_COMMIT, "observation_sources": ["squeue", "sacct", "scontrol", "server1-4 read-only SSH where available", "execution artifact metadata"], "execution_generations": {"llada": "0dd161c8cf4bf3e7dbe4042234a0954950ce870e", "dream": "8b1361d3d8d60a58e28847ac35af8dfc2b023d2d"}, "jobs": rows, "paper": paper, "storage": storage, "readiness": readiness, "constraints": {"scientific_code_modified": False, "scientific_config_modified": False, "active_jobs_modified": False, "aggregate_created": False, "paper_sources_modified": False}}
    LIVE.mkdir(parents=True, exist_ok=True)
    write_json(LIVE / "current_status.json", current)
    write_json(LIVE / "aggregate_readiness.json", {"generated_at_kst": current["generated_at_kst"], "final_aggregate_ready": readiness["experiment"]["aggregate_ready"], "sealed_rows": readiness["experiment"]["sealed_rows"], "expected_rows": 8, "missing_rows": [r["job_id"] for r in rows if r["status"] != "SEALED"], "failed_excluded": [r["job_id"] for r in rows if r["status"] == "FAILED_EXCLUDED"], "blockers": readiness["blockers"]["p0"] + readiness["blockers"]["p1"]})
    write_json(LIVE / "submission_readiness.json", readiness)
    write_json(LIVE / "paper_status.json", paper)
    write_json(LIVE / "paper_build_status.json", paper_build)
    write_json(LIVE / "server_health.json", storage)
    write_json(LIVE / "claim_dependency_status.json", {"observation_only": True, "dependencies": paper.get("claim_dependencies", {}), "note": "Claim content is not modified by this monitor."})
    write_json(LIVE / "rq_evidence_readiness.json", {"observation_only": True, "rows": [{"job_id": r["job_id"], "status": r["status"], "report": r["files"].get("report.json", {}).get("exists"), "provenance": r["files"].get("scientific_provenance.json", {}).get("exists"), "sealed": r["status"] == "SEALED"} for r in rows]})
    write_json(LIVE / "analysis_handoff.json", {"generated_at_kst": current["generated_at_kst"], "runs": [{"job_id": r["job_id"], "run_name": r["run_name"], "status": r["status"], "execution_sha": r["execution_sha"], "server": r["server"], "artifact_path": next((x["output"] for x in RUNS if x["job_id"] == r["job_id"]), None), "remote_status": r["source_available"], "report_available": r["files"].get("report.json", {}).get("exists"), "provenance_available": r["files"].get("scientific_provenance.json", {}).get("exists")} for r in rows]})
    write_matrix(rows)
    append_jsonl(LIVE / "progress_history.jsonl", history)
    append_jsonl(LIVE / "event_history.jsonl", events)
    write_attention(rows, events, readiness)
    health = read_json(LIVE / "monitor_health.json", {}) or {}
    health.update({"monitor_start_time": health.get("monitor_start_time", iso()), "monitor_pid": os.getpid(), "last_cycle_start": iso(started), "last_successful_cycle": iso(), "next_expected_cycle": iso(now() + dt.timedelta(minutes=30)), "consecutive_cycle_failures": 0, "last_cycle_events": len(events), "last_cycle_source_failures": sum(not r["source_available"] for r in rows)})
    write_json(LIVE / "monitor_health.json", health)
    git = git_commit_push(events)
    health["last_successful_push"] = iso() if git.get("push") else health.get("last_successful_push")
    health["last_git_result"] = git
    write_json(LIVE / "monitor_health.json", health)
    run_cmd(["git", "-C", str(ROOT), "add", "-f", "status/live/monitor_health.json"], timeout=30)
    run_cmd(["git", "-C", str(ROOT), "commit", "-m", f"monitor: health {now().strftime('%Y-%m-%d %H:%M KST')}"], timeout=60)
    run_cmd(["git", "-C", str(ROOT), "push", "origin", "HEAD:codex/iclr2027-live-monitor-20260923"], timeout=120)
    return {"generated_at_kst": current["generated_at_kst"], "events": events, "readiness": readiness, "git": git, "rows": rows}


def main() -> int:
    RUNTIME.mkdir(parents=True, exist_ok=True)
    LIVE.mkdir(parents=True, exist_ok=True)
    with LOCK_PATH.open("w") as lock:
        try:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("monitor lock held; exiting")
            return 0
        try:
            result = cycle()
            print(json.dumps({"timestamp": result["generated_at_kst"], "events": result["events"], "sealed_rows": result["readiness"]["experiment"]["sealed_rows"], "push": result["git"].get("push")}, ensure_ascii=False))
            return 0
        except Exception as exc:
            health = read_json(LIVE / "monitor_health.json", {}) or {}
            health["consecutive_cycle_failures"] = int(health.get("consecutive_cycle_failures", 0)) + 1
            health["last_error"] = {"timestamp_kst": iso(), "error": repr(exc)}
            write_json(LIVE / "monitor_health.json", health)
            print(f"monitor cycle failed: {exc}", file=sys.stderr)
            return 1


if __name__ == "__main__":
    raise SystemExit(main())
