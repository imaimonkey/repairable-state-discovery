from __future__ import annotations

import argparse
import json
import os
import shlex
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from repairable_diffusion.src.utils.io import load_yaml


ROOT = Path(__file__).resolve().parents[1]
RESULT_ROOT = ROOT / "results/v2_measurement"
JOB_MANIFEST = RESULT_ROOT / "job_manifest.json"
LOG_ROOT = ROOT / "logs/v2_measurement"

FULL_CONFIGS = [
    "repairable_diffusion/configs/v2/runs/full_math500_llada.yaml",
    "repairable_diffusion/configs/v2/runs/full_gsm8k_llada.yaml",
    "repairable_diffusion/configs/v2/runs/full_math500_dream.yaml",
    "repairable_diffusion/configs/v2/runs/full_gsm8k_dream.yaml",
    "repairable_diffusion/configs/v2/runs/full_bbh_logical3_llada.yaml",
    "repairable_diffusion/configs/v2/runs/full_bbh_logical5_llada.yaml",
    "repairable_diffusion/configs/v2/runs/full_bbh_logical7_llada.yaml",
    "repairable_diffusion/configs/v2/runs/full_mbpp_llada.yaml",
]
PILOT_CONFIGS = [
    "repairable_diffusion/configs/v2/runs/pilot_math500_llada.yaml",
    "repairable_diffusion/configs/v2/runs/pilot_gsm8k_llada.yaml",
]


def _git_sha() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def _load_manifest() -> dict[str, Any]:
    if not JOB_MANIFEST.exists():
        return {"jobs": [], "git_sha": _git_sha()}
    return json.loads(JOB_MANIFEST.read_text(encoding="utf-8"))


def _save_manifest(payload: dict[str, Any]) -> None:
    JOB_MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    payload["updated_at_utc"] = datetime.now(timezone.utc).isoformat()
    JOB_MANIFEST.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def _run_name(config_rel: str) -> str:
    return str(load_yaml(ROOT / config_rel)["run_name"])


def _report_exists(config_rel: str) -> bool:
    return (ROOT / "repairable_diffusion/outputs/v2_measurement" / _run_name(config_rel) / "report.json").is_file()


def _active_job_ids(manifest: dict[str, Any]) -> set[str]:
    ids = [str(row["job_id"]) for row in manifest.get("jobs", []) if row.get("job_id")]
    if not ids or not shutil_which("squeue"):
        return set()
    proc = subprocess.run(
        ["squeue", "-h", "-j", ",".join(ids), "-o", "%i"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        return set()
    return {line.strip() for line in proc.stdout.splitlines() if line.strip()}


def shutil_which(name: str) -> str | None:
    import shutil
    return shutil.which(name)


def _sbatch_command(config_rel: str) -> list[str]:
    run_name = _run_name(config_rel)
    LOG_ROOT.mkdir(parents=True, exist_ok=True)
    partition = os.environ.get("V2_SLURM_PARTITION")
    time_limit = os.environ.get("V2_SLURM_TIME", "24:00:00")
    mem = os.environ.get("V2_SLURM_MEM", "64G")
    cpus = os.environ.get("V2_SLURM_CPUS", "8")
    gpus = os.environ.get("V2_SLURM_GPUS", "1")
    python_bin = os.environ.get("PYTHON_BIN", "python")
    activate = os.environ.get("V2_ENV_ACTIVATE", ":")
    command = (
        f"set -euo pipefail; cd {shlex.quote(str(ROOT))}; {activate}; "
        f"{shlex.quote(python_bin)} -m repairable_diffusion.src.v2.run_measurement "
        f"--config {shlex.quote(config_rel)}"
    )
    args = [
        "sbatch",
        "--parsable",
        "--job-name", f"v2-{run_name[:40]}",
        "--time", time_limit,
        "--mem", mem,
        "--cpus-per-task", cpus,
        "--gres", f"gpu:{gpus}",
        "--output", str(LOG_ROOT / f"{run_name}-%j.out"),
        "--error", str(LOG_ROOT / f"{run_name}-%j.err"),
    ]
    if partition:
        args += ["--partition", partition]
    extra = os.environ.get("V2_SLURM_EXTRA", "").strip()
    if extra:
        args += shlex.split(extra)
    args += ["--wrap", command]
    return args


def _preflight_for_full() -> None:
    subprocess.run(
        [os.environ.get("PYTHON_BIN", "python"), "scripts/audit_v2_design.py", "--mode", "full"],
        cwd=ROOT,
        check=True,
    )


def submit(configs: list[str], *, dry_run: bool, resume: bool) -> None:
    if not shutil_which("sbatch") and not dry_run:
        raise SystemExit("sbatch is unavailable; use --dry-run or scripts/run_v2_suite.sh full-local")
    manifest = _load_manifest()
    current_sha = _git_sha()
    if manifest.get("git_sha") not in (None, current_sha) and manifest.get("jobs"):
        raise SystemExit("existing V2 job manifest belongs to another git SHA; do not mix execution generations")
    manifest["git_sha"] = current_sha
    active = _active_job_ids(manifest)
    active_by_config = {
        row["config"] for row in manifest.get("jobs", []) if str(row.get("job_id")) in active
    }
    for config_rel in configs:
        if _report_exists(config_rel):
            print(f"[skip complete] {config_rel}")
            continue
        if resume and config_rel in active_by_config:
            print(f"[skip active] {config_rel}")
            continue
        cmd = _sbatch_command(config_rel)
        print(" ".join(shlex.quote(x) for x in cmd))
        if dry_run:
            continue
        proc = subprocess.run(cmd, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        if proc.returncode != 0:
            raise RuntimeError(f"sbatch failed for {config_rel}: {proc.stderr.strip()}")
        job_id = proc.stdout.strip().split(";")[0]
        manifest.setdefault("jobs", []).append(
            {
                "config": config_rel,
                "run_name": _run_name(config_rel),
                "job_id": job_id,
                "submitted_at_utc": datetime.now(timezone.utc).isoformat(),
                "git_sha": current_sha,
            }
        )
        _save_manifest(manifest)
        print(f"submitted {config_rel} -> {job_id}")
    _save_manifest(manifest)


def status() -> None:
    manifest = _load_manifest()
    jobs = manifest.get("jobs", [])
    if not jobs:
        print("no recorded V2 jobs")
        return
    ids = [str(row["job_id"]) for row in jobs if row.get("job_id")]
    live: dict[str, str] = {}
    if ids and shutil_which("squeue"):
        proc = subprocess.run(
            ["squeue", "-h", "-j", ",".join(ids), "-o", "%i|%T|%M|%R"],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if proc.returncode == 0:
            for line in proc.stdout.splitlines():
                parts = line.split("|", 1)
                if len(parts) == 2:
                    live[parts[0].strip()] = parts[1].strip()
    for row in jobs:
        config_rel = row["config"]
        jid = str(row.get("job_id", ""))
        if _report_exists(config_rel):
            state = "COMPLETE(report)"
        elif jid in live:
            state = live[jid]
        else:
            state = "NOT_IN_QUEUE/INCOMPLETE"
        print(f"{jid:>10}  {state:<32}  {config_rel}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tier", choices=["pilot", "full"], default="full")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()
    if args.status:
        status()
        return
    if args.tier == "full":
        _preflight_for_full()
        configs = FULL_CONFIGS
    else:
        configs = PILOT_CONFIGS
    submit(configs, dry_run=args.dry_run, resume=args.resume)


if __name__ == "__main__":
    main()
