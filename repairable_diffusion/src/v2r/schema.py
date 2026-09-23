"""Small, dependency-free contracts for fail-closed V2R execution."""
from __future__ import annotations

import hashlib
import json
import math
import re
from pathlib import Path
from typing import Any, Mapping

NAMESPACE = "v2r_reference"
SCHEMA_VERSION = "v2r.1"
FORBIDDEN_METRICS = frozenset({"base_pass_at_k", "failed_items_probed"})
STAGES = frozenset({"r0_smoke", "r0_full", "r1_bridge", "r2_equivalence", "base", "r3_core", "mechanism", "temporal", "localization", "fresh_control"})
SCIENTIFIC_STAGES = frozenset({"base", "r3_core", "mechanism", "temporal", "localization", "fresh_control"})
DEEP_STAGES = SCIENTIFIC_STAGES - {"base"}
CHECKPOINT_GRID = [0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875]


class ContractError(ValueError):
    """Scientific, provenance, or filesystem contract is not satisfied."""


def canonical_bytes(value: Any) -> bytes:
    try:
        return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise ContractError(f"Not canonical JSON: {exc}") from exc


def canonical_hash(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def file_hash(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_metric_names(value: Any) -> None:
    if isinstance(value, Mapping):
        for key, child in value.items():
            if key in FORBIDDEN_METRICS:
                raise ContractError(f"Ambiguous V2 metric is forbidden in V2R: {key}")
            validate_metric_names(child)
    elif isinstance(value, (list, tuple)):
        for child in value:
            validate_metric_names(child)
    canonical_bytes(value)


def require_hash(value: Any, name: str, length: int = 64) -> None:
    if not isinstance(value, str) or not re.fullmatch(rf"[0-9a-f]{{{length}}}", value):
        raise ContractError(f"{name} must be an exact {length}-digit lowercase hexadecimal hash")


def manifest_binding(manifest: Mapping[str, Any]) -> dict[str, Any]:
    return {key: manifest[key] for key in (
        "run_fingerprint", "execution_git_sha", "config_sha256", "model_sha256",
        "dataset_sha256", "recipe_sha256", "design_sha256", "seed_registry_sha256",
    )}


def fingerprint_payload(manifest: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in manifest.items() if key not in {
        "run_fingerprint", "seed_registry", "seed_registry_sha256", "assignment_sha256", "shards",
    }}


def validate_manifest(manifest: Mapping[str, Any]) -> None:
    validate_metric_names(manifest)
    if manifest.get("schema_version") != SCHEMA_VERSION or manifest.get("namespace") != NAMESPACE:
        raise ContractError("This is not a V2R manifest")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", str(manifest.get("run_id", ""))):
        raise ContractError("Unsafe run_id")
    if manifest.get("stage") not in STAGES:
        raise ContractError("Unknown execution stage")
    require_hash(manifest.get("execution_git_sha"), "execution_git_sha", 40)
    require_hash(manifest.get("design_sha256"), "design_sha256")
    for name in ("config", "model", "dataset", "recipe"):
        if not isinstance(manifest.get(name), dict) or not manifest[name]:
            raise ContractError(f"Missing frozen {name}")
        if canonical_hash(manifest[name]) != manifest.get(f"{name}_sha256"):
            raise ContractError(f"{name} hash mismatch")
    for name in ("model", "dataset"):
        for field in ("id", "revision"):
            if not isinstance(manifest[name].get(field), str) or not manifest[name][field]:
                raise ContractError(f"Missing {name}.{field}")
        if manifest[name]["revision"] in {"main", "master", "latest", "HEAD"}:
            raise ContractError(f"Unpinned {name} revision")
    if not manifest["dataset"].get("split"):
        raise ContractError("Missing dataset split")
    if not re.fullmatch(r"[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*:[A-Za-z_]\w*", str(manifest.get("executor", ""))):
        raise ContractError("executor must be a pinned module:function")
    items = manifest.get("item_ids")
    if not isinstance(items, list) or not items or any(not isinstance(item, str) or not item for item in items):
        raise ContractError("item_ids must be a nonempty list of stable string IDs")
    if len(set(items)) != len(items) or sorted(items) != items:
        raise ContractError("item_ids must be sorted and unique")
    if canonical_hash(fingerprint_payload(manifest)) != manifest.get("run_fingerprint"):
        raise ContractError("Run fingerprint mismatch")
    if canonical_hash(manifest.get("shards")) != manifest.get("assignment_sha256"):
        raise ContractError("Shard assignment hash mismatch")
    assigned = [item for shard in manifest["shards"] for item in shard["item_ids"]]
    if len(assigned) != len(set(assigned)) or sorted(assigned) != items:
        raise ContractError("Duplicate or missing shard assignment")
    if [shard.get("shard_id") for shard in manifest["shards"]] != list(range(len(manifest["shards"]))):
        raise ContractError("Noncanonical shard IDs")
    from .seeds import validate_seed_registry
    validate_seed_registry(manifest["seed_registry"])
    if canonical_hash(manifest["seed_registry"]) != manifest.get("seed_registry_sha256"):
        raise ContractError("Seed registry hash mismatch")
    contexts = manifest["seed_registry"]["records"]
    if {row["context"]["item_id"] for row in contexts} != set(items):
        raise ContractError("Seed registry item coverage mismatch")
    if any(row["context"]["stage"] != manifest["stage"] for row in contexts):
        raise ContractError("Seed registry contains the wrong execution stage")
    if manifest["stage"] in DEEP_STAGES:
        subset = manifest.get("failed_pool_freeze")
        if not isinstance(subset, dict) or subset.get("status") != "FROZEN":
            raise ContractError("Scientific probing requires a frozen trajectory-bank subset")
        require_hash(subset.get("bank_sha256"), "bank_sha256")
        if subset.get("item_ids") != items:
            raise ContractError("Subset differs from the frozen failed pool")
        if manifest["config"].get("checkpoint_grid") != CHECKPOINT_GRID:
            raise ContractError("Reference probing requires the frozen normalized checkpoint grid")
        if manifest["config"].get("B_loc") != 4 or manifest["config"].get("B_eval") != 8:
            raise ContractError("Branch counts must be frozen at B_loc=4 and B_eval=8")
        if manifest["config"].get("tau_confirm") != 0.25:
            raise ContractError("Confirmation threshold must be 0.25")


def probability(value: Any, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or not 0 <= value <= 1:
        raise ContractError(f"Invalid probability: {name}")
    return float(value)
