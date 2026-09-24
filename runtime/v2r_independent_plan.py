#!/usr/bin/env python3
"""Materialize paper-separated plans for a server-local V2R variant.

This helper is orchestration metadata only.  Scientific execution still runs
from the immutable execution checkout named in each manifest and must pass the
server-local R0/R1/R2 reports.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from repairable_diffusion.src.v2r.artifacts import atomic_json, merge_run, read_json  # noqa: E402
from repairable_diffusion.src.v2r.planning import freeze_failed_subset, make_plan, select_budget  # noqa: E402
from repairable_diffusion.src.v2r.reference_sources import load_records  # noqa: E402
from repairable_diffusion.src.v2r.schema import canonical_hash, file_hash  # noqa: E402

EXECUTION_SHA = "78fe5d7c1829b67d1bb1416b7205edfa647bb2fa"


def config(recipe: dict, task: str) -> dict:
    return {
        "design_generation": 2,
        "task": task,
        "generation": recipe["tasks"][task]["generation"],
        "checkpoint_grid": [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875],
        "B_loc": 4,
        "B_eval": 8,
        "tau_confirm": 0.25,
        "design_seed": 20260923,
    }


def make_base(args: argparse.Namespace) -> None:
    recipe = read_json(ROOT / "results/v2r_reference/reference_recipes/llada.json")
    task = getattr(args, "task", "math500")
    source_cache = Path(args.source_cache)
    rows = load_records(recipe, task, "bridge", source_cache)
    model = {
        "backbone": "llada",
        "id": recipe["model_id"],
        "revision": recipe["model_revision"],
        "tokenizer_revision": recipe["tokenizer_revision"],
    }
    dataset = {
        "id": recipe["tasks"][task]["bridge_dataset"]["path"],
        "revision": recipe["tasks"][task]["bridge_dataset"]["revision"],
        "split": recipe["tasks"][task]["bridge_dataset"]["split"],
        "task": task,
        "content_sha256": canonical_hash(rows),
    }
    spec = {
        "run_id": f"llada_{task}_base_independent_{args.server}_v1",
        "stage": "base",
        "design_seed": 20260923,
        "design_sha256": canonical_hash(read_json(ROOT / "status/v2r/design_freeze.json")),
        "execution_git_sha": EXECUTION_SHA,
        "model": model,
        "dataset": dataset,
        "recipe": recipe,
        "config": config(recipe, task),
        "item_ids": [str(row["item_id"]) for row in rows],
        "executor": "repairable_diffusion.src.v2r.science:execute_base",
        "runtime_paths": {
            "source_cache": args.source_cache,
            "model_cache": args.model_cache,
        },
        "execution_worktree": args.execution_root,
        "timing": {
            "seconds_per_item": float(args.seconds_per_item),
            "target_shard_hours": float(args.target_shard_hours),
        },
        "seed_plan": [{
            "purpose": "base",
            "checkpoints": [0],
            "branches": 1,
            "operators": ["reference"],
            "rng_role": "future",
        }],
    }
    atomic_json(args.manifest_out, make_plan(spec))


def make_bank(manifest: dict, run_dir: Path) -> tuple[list[dict], str, dict[str, dict]]:
    aggregate = read_json(run_dir / "aggregate/aggregate.json")
    shard_for = {
        item: shard["shard_id"]
        for shard in manifest["shards"]
        for item in shard["item_ids"]
    }
    bank, index = [], {}
    for row in aggregate["items"]:
        item = str(row["item_id"])
        path = run_dir / "shards" / f"shard-{shard_for[item]:03d}" / "items" / canonical_hash(item) / "trajectory.json"
        entry = {
            "item_id": item,
            "trajectory_id": 0,
            "correct": bool(row["result"]["correct"]),
            "path": str(path),
            "sha256": file_hash(path),
        }
        bank.append(entry)
        index[item] = {"path": str(path), "sha256": entry["sha256"]}
    bank.sort(key=lambda row: row["item_id"])
    bank_sha = canonical_hash(bank)
    atomic_json(run_dir / "bank.json", {
        "status": "FROZEN_INPUT",
        "bank_sha256": bank_sha,
        "items": bank,
        "source_manifest_sha256": canonical_hash(manifest),
    })
    return bank, bank_sha, index


def make_deep(args: argparse.Namespace) -> None:
    execution_root = Path(args.execution_root)
    sys.path.insert(0, str(execution_root))
    manifest = read_json(args.base_manifest)
    gates = read_json(args.gates)
    base_run = Path(args.base_run_dir)
    merge_run(manifest, base_run, gates=gates)
    bank, bank_sha, index = make_bank(manifest, base_run)
    recipe = manifest["recipe"]
    task = manifest["dataset"]["task"]
    failed = sum(not row["correct"] for row in bank)
    base_seconds = float(manifest["timing"]["seconds_per_item"])
    report = {
        "status": "READY",
        "variant": args.server,
        "base_run_dir": str(base_run),
        "bank_sha256": bank_sha,
        "sampled_count": len(bank),
        "failed_pool_count": failed,
        "plans": {},
    }
    deep_parent = Path(args.deep_parent)
    for purpose, multiplier in (("core", 79.0), ("temporal", 112.0)):
        value = os.statvfs(deep_parent)
        free = value.f_bavail * value.f_frsize
        used = (value.f_blocks - value.f_bfree) * value.f_frsize
        budget = select_budget(
            backbone="llada",
            purpose=purpose,
            seconds_per_item=max(1.0, base_seconds * multiplier),
            bytes_per_item=16 * 1024 * 1024,
            available_gpu_hours=float(args.available_gpu_hours),
            deadline_hours=float(args.deadline_hours),
            gpu_count=4,
            free_bytes=free,
            safety_margin_bytes=50 * 1024**3,
            filesystem_used_fraction=used / (used + free),
            pilot_item_count=8,
            failed_pool_size=failed,
            reserve_hours=6.0,
        )
        row = {"budget": budget}
        if budget["status"] == "FROZEN":
            frozen = freeze_failed_subset(
                bank,
                bank_sha256=bank_sha,
                budget=budget,
                design_seed=20260923,
                backbone="llada",
                task=task,
                purpose=purpose,
            )
            selected = frozen["item_ids"]
            sample = read_json(index[selected[0]]["path"])["trajectory"]
            checkpoints = [row["step"] for row in sample["checkpoint_mapping"]]
            stage = "r3_core" if purpose == "core" else "temporal"
            plan = ([
                {"purpose": "localization", "checkpoints": checkpoints, "branches": 4,
                 "operators": ["matched_continuation", "canonical_repair"],
                 "rng_role": "future", "paired_rng_group": "matched-future"},
                {"purpose": "confirmation", "checkpoints": checkpoints, "branches": 8,
                 "operators": ["matched_continuation", "canonical_repair"],
                 "rng_role": "future", "paired_rng_group": "matched-future"},
            ] if purpose == "core" else [{
                "purpose": "confirmation", "checkpoints": checkpoints, "branches": 8,
                "operators": ["matched_continuation", "canonical_repair"],
                "rng_role": "future", "paired_rng_group": "matched-future",
            }])
            deep_manifest = make_plan({
                "run_id": f"llada_{task}_{purpose}_independent_{args.server}_v1",
                "stage": stage,
                "design_seed": 20260923,
                "design_sha256": manifest["design_sha256"],
                "execution_git_sha": manifest["execution_git_sha"],
                "model": manifest["model"],
                "dataset": manifest["dataset"],
                "recipe": recipe,
                "config": manifest["config"],
                "item_ids": selected,
                "executor": "repairable_diffusion.src.v2r.science:execute_probe",
                "runtime_paths": manifest["runtime_paths"],
                "execution_worktree": manifest["execution_worktree"],
                "trajectory_index": {item: index[item] for item in selected},
                "failed_pool_freeze": frozen,
                "budget": budget,
                "timing": {"seconds_per_item": budget["inputs"]["seconds_per_item"], "target_shard_hours": 4.0},
                "seed_plan": plan,
            })
            manifest_path = deep_parent / f"{purpose}_manifest.json"
            gates_path = deep_parent / f"{purpose}_gates.json"
            atomic_json(manifest_path, deep_manifest)
            atomic_json(gates_path, gates)
            row.update({"status": "READY", "manifest": str(manifest_path), "gates": str(gates_path),
                        "run_dir": str(deep_parent / deep_manifest["run_id"]),
                        "selected_n": len(selected), "shard_count": len(deep_manifest["shards"])})
        else:
            row["status"] = "BLOCKED"
        report["plans"][purpose] = row
    atomic_json(Path(args.report_out), report)


def replan_temporal(args: argparse.Namespace) -> None:
    """Materialize a temporal-only plan from the same frozen base bank.

    This is used when the first resource projection is conservative but a
    larger, explicitly recorded GPU-hour envelope is still schedulable before
    the deadline.  It never changes the base manifest, failed-item pool,
    model/gate binding, execution SHA, or scientific executor.
    """
    execution_root = Path(args.execution_root)
    sys.path.insert(0, str(execution_root))
    manifest = read_json(args.base_manifest)
    gates = read_json(args.gates)
    base_run = Path(args.base_run_dir)
    merge_run(manifest, base_run, gates=gates)
    bank, bank_sha, index = make_bank(manifest, base_run)
    recipe = manifest["recipe"]
    task = manifest["dataset"]["task"]
    failed = sum(not row["correct"] for row in bank)
    base_seconds = float(manifest["timing"]["seconds_per_item"])
    value = os.statvfs(args.deep_parent)
    free = value.f_bavail * value.f_frsize
    used = value.f_blocks - value.f_bfree
    budget = select_budget(
        backbone="llada", purpose="temporal",
        seconds_per_item=max(1.0, base_seconds * 112.0),
        bytes_per_item=16 * 1024 * 1024,
        available_gpu_hours=float(args.available_gpu_hours),
        deadline_hours=float(args.deadline_hours), gpu_count=4,
        free_bytes=free * value.f_frsize,
        safety_margin_bytes=50 * 1024**3,
        filesystem_used_fraction=used / value.f_blocks,
        pilot_item_count=8, failed_pool_size=failed, reserve_hours=6.0,
    )
    report = {"status": budget["status"], "purpose": "temporal",
              "budget": budget, "base_run_dir": str(base_run),
              "bank_sha256": bank_sha, "execution_git_sha": manifest["execution_git_sha"]}
    if budget["status"] != "FROZEN":
        atomic_json(Path(args.report_out), report)
        return
    frozen = freeze_failed_subset(
        bank, bank_sha256=bank_sha, budget=budget, design_seed=20260923,
        backbone="llada", task=task, purpose="temporal")
    selected = frozen["item_ids"]
    sample = read_json(index[selected[0]]["path"])["trajectory"]
    checkpoints = [row["step"] for row in sample["checkpoint_mapping"]]
    deep_manifest = make_plan({
        "run_id": args.run_id or f"llada_{task}_temporal_independent_{args.server}_v2",
        "stage": "temporal", "design_seed": 20260923,
        "design_sha256": manifest["design_sha256"],
        "execution_git_sha": manifest["execution_git_sha"],
        "model": manifest["model"], "dataset": manifest["dataset"],
        "recipe": recipe, "config": manifest["config"],
        "item_ids": selected, "executor": "repairable_diffusion.src.v2r.science:execute_probe",
        "runtime_paths": manifest["runtime_paths"],
        "execution_worktree": manifest["execution_worktree"],
        "trajectory_index": {item: index[item] for item in selected},
        "failed_pool_freeze": frozen,
        "budget": budget,
        "timing": {"seconds_per_item": budget["inputs"]["seconds_per_item"], "target_shard_hours": 4.0},
        "seed_plan": [{
            "purpose": "confirmation", "checkpoints": checkpoints, "branches": 8,
            "operators": ["matched_continuation", "canonical_repair"],
            "rng_role": "future", "paired_rng_group": "matched-future",
        }],
    })
    deep_parent = Path(args.deep_parent)
    manifest_path = deep_parent / "temporal_v2_manifest.json"
    gates_path = deep_parent / "temporal_v2_gates.json"
    atomic_json(manifest_path, deep_manifest)
    atomic_json(gates_path, gates)
    report.update({"status": "READY", "manifest": str(manifest_path),
                   "gates": str(gates_path), "run_dir": str(deep_parent / deep_manifest["run_id"]),
                   "selected_n": len(selected), "shard_count": len(deep_manifest["shards"])})
    atomic_json(Path(args.report_out), report)


def merge_stage(args: argparse.Namespace) -> None:
    manifest = read_json(args.manifest)
    gates = read_json(args.gates)
    aggregate = merge_run(manifest, Path(args.run_dir), gates=gates)
    atomic_json(args.report_out, {
        "status": aggregate["status"],
        "stage": manifest["stage"],
        "run_id": manifest["run_id"],
        "manifest_sha256": canonical_hash(manifest),
        "aggregate_sha256": file_hash(Path(args.run_dir) / "aggregate/aggregate.json"),
        "item_count": aggregate["item_count"],
    })


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    base = sub.add_parser("base")
    base.add_argument("--server", required=True)
    base.add_argument("--task", choices=["math500", "gsm8k"], default="math500")
    base.add_argument("--execution-root", required=True)
    base.add_argument("--source-cache", required=True)
    base.add_argument("--model-cache", required=True)
    base.add_argument("--seconds-per-item", required=True, type=float)
    base.add_argument("--target-shard-hours", default=4.0, type=float)
    base.add_argument("--manifest-out", required=True)
    final = sub.add_parser("finalize")
    final.add_argument("--server", required=True)
    final.add_argument("--execution-root", required=True)
    final.add_argument("--base-manifest", required=True)
    final.add_argument("--gates", required=True)
    final.add_argument("--base-run-dir", required=True)
    final.add_argument("--deep-parent", required=True)
    final.add_argument("--available-gpu-hours", default=60.0, type=float)
    final.add_argument("--deadline-hours", default=60.0, type=float)
    final.add_argument("--report-out", required=True)
    replan = sub.add_parser("replan-temporal")
    replan.add_argument("--server", required=True)
    replan.add_argument("--execution-root", required=True)
    replan.add_argument("--base-manifest", required=True)
    replan.add_argument("--gates", required=True)
    replan.add_argument("--base-run-dir", required=True)
    replan.add_argument("--deep-parent", required=True)
    replan.add_argument("--report-out", required=True)
    replan.add_argument("--run-id", default=None)
    replan.add_argument("--available-gpu-hours", default=80.0, type=float)
    replan.add_argument("--deadline-hours", default=60.0, type=float)
    merged = sub.add_parser("merge")
    merged.add_argument("--manifest", required=True)
    merged.add_argument("--gates", required=True)
    merged.add_argument("--run-dir", required=True)
    merged.add_argument("--report-out", required=True)
    args = parser.parse_args()
    if args.command == "base":
        make_base(args)
    elif args.command == "finalize":
        make_deep(args)
    elif args.command == "replan-temporal":
        replan_temporal(args)
    else:
        merge_stage(args)


if __name__ == "__main__":
    main()
