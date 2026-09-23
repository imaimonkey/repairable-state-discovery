"""Outcome-independent resource budgets, failed-pool freezes, and shard plans."""
from __future__ import annotations

import math
from datetime import datetime
from typing import Any, Iterable, Mapping

from .schema import ContractError, NAMESPACE, SCHEMA_VERSION, canonical_hash, fingerprint_payload, validate_manifest
from .seeds import build_seed_registry, enumerate_contexts


def select_budget(*, backbone: str, purpose: str, seconds_per_item: float,
                  bytes_per_item: int, available_gpu_hours: float, deadline_hours: float,
                  gpu_count: int, free_bytes: int, safety_margin_bytes: int,
                  filesystem_used_fraction: float, pilot_item_count: int,
                  failed_pool_size: int, reserve_hours: float = 0.0) -> dict[str, Any]:
    """Choose N using resource observations only; never accepts effect estimates."""
    if backbone not in {"llada", "dream"} or purpose not in {"core", "mechanism", "temporal"}:
        raise ContractError("Unknown predeclared budget family")
    if purpose != "core" and backbone != "llada":
        raise ContractError("Deep mechanism/temporal budgets are predeclared for LLaDA only")
    numeric = (seconds_per_item, available_gpu_hours, deadline_hours, reserve_hours, filesystem_used_fraction)
    if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or v < 0 for v in numeric):
        raise ContractError("Resource estimates must be finite and nonnegative")
    for value in (bytes_per_item, gpu_count, free_bytes, safety_margin_bytes, pilot_item_count, failed_pool_size):
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ContractError("Resource counts must be nonnegative integers")
    if seconds_per_item <= 0 or bytes_per_item <= 0 or gpu_count <= 0 or not 8 <= pilot_item_count <= 16:
        raise ContractError("An 8–16 item measured timing/storage pilot and positive resources are required")
    target, minimum = (64, 32) if backbone == "llada" and purpose == "core" else (32, 32)
    usable_hours = min(available_gpu_hours, gpu_count * max(0, deadline_hours - reserve_hours))
    time_capacity = math.floor(usable_hours * 3600 / (1.25 * seconds_per_item))
    storage_capacity = max(0, (free_bytes - safety_margin_bytes) // (2 * bytes_per_item))
    feasible = min(target, failed_pool_size, time_capacity, storage_capacity)
    reasons = []
    if filesystem_used_fraction >= 0.95:
        reasons.append("FILESYSTEM_CRITICAL")
    if feasible < minimum:
        reasons.append("BELOW_PREDECLARED_MINIMUM")
    return {"status": "BLOCKED" if reasons else "FROZEN", "reasons": reasons,
            "backbone": backbone, "purpose": purpose, "target": target, "minimum": minimum,
            "selected_n": None if reasons else feasible, "feasible_n": feasible,
            "rule": "min(target, failed_pool, measured_time_capacity, doubled_storage_capacity)",
            "inputs": {"seconds_per_item": seconds_per_item, "bytes_per_item": bytes_per_item,
                "available_gpu_hours": available_gpu_hours, "deadline_hours": deadline_hours,
                "gpu_count": gpu_count, "reserve_hours": reserve_hours, "free_bytes": free_bytes,
                "safety_margin_bytes": safety_margin_bytes, "filesystem_used_fraction": filesystem_used_fraction,
                "pilot_item_count": pilot_item_count, "failed_pool_size": failed_pool_size},
            "time_capacity": time_capacity, "storage_capacity": storage_capacity}


def validate_budget(budget: Mapping[str, Any]) -> None:
    expected = select_budget(backbone=budget["backbone"], purpose=budget["purpose"], **budget["inputs"])
    if dict(budget) != expected or budget["status"] != "FROZEN":
        raise ContractError("Budget is blocked or was changed after resource-only selection")


def freeze_failed_subset(bank: Iterable[Mapping[str, Any]], *, bank_sha256: str,
                         budget: Mapping[str, Any], design_seed: int,
                         backbone: str, task: str, purpose: str = "core") -> dict[str, Any]:
    validate_budget(budget)
    rows = list(bank)
    if canonical_hash(rows) != bank_sha256:
        raise ContractError("Trajectory bank hash does not match freeze input")
    seen = set()
    for row in rows:
        key = (row["item_id"], row["trajectory_id"])
        if key in seen or row["trajectory_id"] != 0 or type(row.get("correct")) is not bool:
            raise ContractError("Bank must contain exactly one uniquely identified trajectory per item")
        seen.add(key)
    failed = [row for row in rows if row["correct"] is False]
    if len(failed) != budget["inputs"]["failed_pool_size"] or budget["backbone"] != backbone or budget["purpose"] != purpose:
        raise ContractError("Budget does not describe this failed pool")
    ranked = sorted(failed, key=lambda row: canonical_hash([
        design_seed, backbone, task, *([] if purpose == "core" else [purpose]), row["item_id"], row["trajectory_id"]]))
    selected = ranked[:budget["selected_n"]]
    result = {"status": "FROZEN", "bank_sha256": bank_sha256, "design_seed": design_seed,
        "backbone": backbone, "task": task, "purpose": purpose, "budget": dict(budget),
        "selection_rule": "sha256(design_seed,backbone,task,purpose,item_id,trajectory_id)",
        "item_ids": sorted(row["item_id"] for row in selected),
        "selected_trajectories": [{"item_id": row["item_id"], "trajectory_id": row["trajectory_id"]} for row in selected],
        "failed_pool_count": len(failed), "sampled_trajectory_count": len(rows)}
    result["selection_sha256"] = canonical_hash(result)
    return result


def map_checkpoints(total_steps: int, valid_active_steps: Iterable[int], grid: Iterable[float]) -> list[dict[str, Any]]:
    """Map schedule-only active states; ties resolve to the earlier state."""
    valid = sorted(set(valid_active_steps))
    if total_steps <= 0 or not valid or any(type(step) is not int or not 0 < step < total_steps for step in valid):
        raise ContractError("Invalid active-phase schedule states")
    mapped = []
    for target in grid:
        if not 0 < target < 1:
            raise ContractError("Checkpoint targets must be strictly internal")
        step = min(valid, key=lambda value: (abs(value / total_steps - target), value))
        mapped.append({"target_progress": target, "step": step, "actual_progress": step / total_steps})
    if len({row["step"] for row in mapped}) != len(mapped):
        raise ContractError("Decoder has insufficient distinct valid states for the frozen grid")
    return mapped


def plan_shards(item_ids: Iterable[str], *, run_fingerprint: str, seconds_per_item: float,
                target_hours: float = 4.0, max_hours: float = 6.0) -> list[dict[str, Any]]:
    if not math.isfinite(seconds_per_item) or seconds_per_item <= 0 or not 2 <= target_hours <= 4 or not target_hours <= max_hours <= 6:
        raise ContractError("Shard timing must target 2–4 hours with a 6-hour upper bound")
    if seconds_per_item > max_hours * 3600:
        raise ContractError("An item exceeds the maximum shard walltime; do not submit")
    items = list(item_ids)
    if not items or len(set(items)) != len(items):
        raise ContractError("Cannot shard an empty or duplicate item set")
    size = max(1, math.floor(target_hours * 3600 / seconds_per_item))
    ranked = sorted(items, key=lambda item: (canonical_hash([run_fingerprint, item]), item))
    return [{"shard_id": index // size, "item_ids": ranked[index:index + size],
             "projected_seconds": len(ranked[index:index + size]) * seconds_per_item}
            for index in range(0, len(ranked), size)]


def make_plan(spec: Mapping[str, Any]) -> dict[str, Any]:
    """Materialize the complete seed registry and deterministic assignment."""
    manifest = dict(spec)
    for reserved in ("run_fingerprint", "seed_registry", "seed_registry_sha256", "shards", "assignment_sha256"):
        if reserved in spec:
            raise ContractError(f"Derived plan field supplied by caller: {reserved}")
    manifest.update(schema_version=SCHEMA_VERSION, namespace=NAMESPACE)
    manifest["item_ids"] = sorted(spec["item_ids"])
    for name in ("model", "dataset", "recipe", "config"):
        manifest[f"{name}_sha256"] = canonical_hash(spec[name])
    manifest["run_fingerprint"] = canonical_hash(fingerprint_payload(manifest))
    manifest["seed_registry"] = build_seed_registry(
        enumerate_contexts(manifest["item_ids"], manifest["stage"], manifest["seed_plan"]),
        design_seed=manifest["design_seed"], scope=manifest["run_fingerprint"])
    manifest["seed_registry_sha256"] = canonical_hash(manifest["seed_registry"])
    manifest["shards"] = plan_shards(manifest["item_ids"], run_fingerprint=manifest["run_fingerprint"],
        seconds_per_item=manifest["timing"]["seconds_per_item"],
        target_hours=manifest["timing"].get("target_shard_hours", 4.0))
    manifest["assignment_sha256"] = canonical_hash(manifest["shards"])
    validate_manifest(manifest)
    return manifest
