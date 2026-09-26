#!/usr/bin/env python3
"""Prepare or submit a neutral Slurm command for a gated Gen3 shard."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from repairable_diffusion.src.rsd_ref_v3.runner import (  # noqa: E402
    design_freeze_sha,
    load_run_config,
    require_runtime_readiness,
)


FORBIDDEN = ("iclr", "naacl", "acl", "emnlp", "conference", "submission")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=("reference", "core", "temporal", "mechanism", "successful-harm"), required=True)
    parser.add_argument("--task", choices=("llada_math", "llada_gsm8k"), required=True)
    parser.add_argument("--shard", type=int, required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    config_path, config = load_run_config(args.task, args.stage)
    freeze_sha = design_freeze_sha()
    if args.dry_run:
        readiness = {"status": "NOT_CHECKED_IN_DRY_RUN"}
    else:
        readiness = require_runtime_readiness()
    job_name = f"rsd-{args.task}-{args.stage.replace('_', '-')}-s{args.shard:03d}".lower()
    command = [sys.executable, str(ROOT / "scripts/run_rsd_ref_v3.py"), "--stage", args.stage,
               "--task", args.task, "--shard", str(args.shard), "--gates", "GATES.json"]
    sbatch = ["sbatch", "--parsable", "--job-name", job_name, "--output", "rsd-%j.out", "--error", "rsd-%j.err"] + command
    if any(token in value.lower() for value in sbatch for token in FORBIDDEN):
        raise RuntimeError("NON_NEUTRAL_SLURM_METADATA")
    payload = {"status": "DRY_RUN_ONLY" if args.dry_run else "SUBMITTED", "job_name": job_name,
               "task": args.task, "stage": args.stage, "shard": args.shard,
               "config": str(config_path.relative_to(ROOT)), "config_sha256": __import__("hashlib").sha256(config_path.read_bytes()).hexdigest(),
               "design_freeze_sha256": freeze_sha, "slurm_command": sbatch, "readiness": readiness}
    if args.dry_run:
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0
    result = subprocess.run(sbatch, cwd=ROOT, text=True, capture_output=True, check=False)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    payload["job_id"] = result.stdout.strip().split(";")[0]
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
