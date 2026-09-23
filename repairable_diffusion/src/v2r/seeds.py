"""Explicit paired RNG equivalence classes, with a pre-submission collision audit.

Seeds are stable 63-bit hashes, not assumed to be collision-free. The complete
expected registry must be enumerated and checked before any job is submitted.
No process-local hash(), truncation to 31 bits, or silent collision repair occurs.
"""
from __future__ import annotations

import hashlib
from typing import Any, Iterable, Mapping

from .schema import ContractError, canonical_bytes, canonical_hash

PURPOSES = frozenset({"base", "equivalence", "localization", "confirmation", "fresh_sampling", "independent_control"})
CONTEXT_KEYS = frozenset({"stage", "purpose", "item_id", "trajectory_id", "checkpoint", "branch", "operator", "rng_role", "paired_rng_group"})


def rng_group(context: Mapping[str, Any]) -> dict[str, Any]:
    if set(context) != CONTEXT_KEYS:
        raise ContractError(f"RNG context keys must be exactly {sorted(CONTEXT_KEYS)}")
    if context["purpose"] not in PURPOSES:
        raise ContractError("Unknown RNG purpose")
    for key in ("stage", "item_id", "operator", "rng_role"):
        if not isinstance(context[key], str) or not context[key]:
            raise ContractError(f"Invalid RNG context {key}")
    for key in ("trajectory_id", "checkpoint", "branch"):
        if isinstance(context[key], bool) or not isinstance(context[key], int) or context[key] < 0:
            raise ContractError(f"Invalid nonnegative RNG index {key}")
    paired = context["paired_rng_group"]
    if paired is not None and (not isinstance(paired, str) or not paired):
        raise ContractError("paired_rng_group must be null or an explicit nonempty name")
    if paired and context["rng_role"] != "future":
        raise ContractError("Only future continuation noise may be intentionally paired")
    group = dict(context)
    if paired:
        group.pop("operator")
    return group


def seed_for_group(design_seed: int, scope: str, group: Mapping[str, Any]) -> int:
    digest = hashlib.sha256(canonical_bytes([design_seed, scope, group])).digest()
    return int.from_bytes(digest[:8], "big") & ((1 << 63) - 1)


def build_seed_registry(contexts: Iterable[Mapping[str, Any]], *, design_seed: int, scope: str) -> dict[str, Any]:
    if isinstance(design_seed, bool) or not isinstance(design_seed, int) or design_seed < 0 or not scope:
        raise ContractError("A nonnegative design seed and frozen scope are required")
    records = []
    seen_contexts: set[str] = set()
    owners: dict[int, str] = {}
    for context in contexts:
        context = dict(context)
        group = rng_group(context)
        context_id, group_id = canonical_hash(context), canonical_hash(group)
        if context_id in seen_contexts:
            raise ContractError("Duplicate seed context in expected registry")
        seen_contexts.add(context_id)
        seed = seed_for_group(design_seed, scope, group)
        if seed in owners and owners[seed] != group_id:
            raise ContractError(f"Unintended seed collision detected before submission: {seed}")
        owners[seed] = group_id
        records.append({"context_id": context_id, "group_id": group_id, "seed": seed, "context": context})
    if not records:
        raise ContractError("The full expected seed registry cannot be empty")
    records.sort(key=lambda row: row["context_id"])
    return {"scheme": "sha256_63bit_preaudited_v1", "design_seed": design_seed, "scope": scope,
            "context_count": len(records), "unique_seed_count": len(owners), "records": records}


def validate_seed_registry(registry: Mapping[str, Any]) -> None:
    if registry.get("scheme") != "sha256_63bit_preaudited_v1":
        raise ContractError("Unsupported seed registry scheme")
    expected = build_seed_registry((row["context"] for row in registry["records"]),
                                   design_seed=registry["design_seed"], scope=registry["scope"])
    if expected != registry:
        raise ContractError("Seed registry was modified or is incomplete")


def enumerate_contexts(item_ids: Iterable[str], stage: str, seed_plan: Iterable[Mapping[str, Any]]) -> list[dict[str, Any]]:
    """Expand the predeclared stage plan; operators may share an explicit group.

    A row has purpose, checkpoints, branches, operators, rng_role, and optional
    paired_rng_group / trajectory_ids. Each operator is a distinct context.
    """
    contexts = []
    for plan in seed_plan:
        for item in sorted(item_ids):
            for trajectory in plan.get("trajectory_ids", [0]):
                for checkpoint in plan["checkpoints"]:
                    for branch in range(plan["branches"]):
                        for operator in plan["operators"]:
                            contexts.append({"stage": stage, "purpose": plan["purpose"], "item_id": item,
                                "trajectory_id": trajectory, "checkpoint": checkpoint, "branch": branch,
                                "operator": operator, "rng_role": plan.get("rng_role", "future"),
                                "paired_rng_group": plan.get("paired_rng_group")})
    return contexts
