#!/usr/bin/env python3
"""Run one explicit RSD Generation 3 stage, or emit a side-effect-free plan."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from repairable_diffusion.src.rsd_ref_v3.runner import (  # noqa: E402
    materialize_task_subsets,
    run_stage,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=("reference", "materialize-subsets", "core", "temporal", "mechanism", "successful-harm", "aggregate", "seal"), required=True)
    parser.add_argument("--task", choices=("llada_math", "llada_gsm8k"))
    parser.add_argument("--source-stage", choices=("reference", "core", "temporal", "mechanism", "successful-harm"), default="reference")
    parser.add_argument("--shard", type=int)
    parser.add_argument("--gates", type=Path)
    parser.add_argument("--compact-dir", type=Path)
    parser.add_argument("--seconds-per-item", type=float, default=7200.0)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.stage == "materialize-subsets":
        tasks = [args.task] if args.task else ["llada_math", "llada_gsm8k"]
        payload = {"status": "DRY_RUN_ONLY" if args.dry_run else "SUBSETS_FROZEN",
                   "tasks": [materialize_task_subsets(task, dry_run=args.dry_run) for task in tasks]}
    else:
        if not args.task:
            parser.error(f"--task is required for --stage {args.stage}")
        payload = run_stage(args.task, args.stage, dry_run=args.dry_run, shard=args.shard,
                            gates_path=args.gates, seconds_per_item=args.seconds_per_item,
                            source_stage=args.source_stage, compact_dir=args.compact_dir)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
