"""Generation 3 execution bridge over the verified V2R runtime.

This module owns the Generation 3 boundary: it resolves only frozen
``rsd_ref_v3`` configs, requires a valid design freeze and runtime readiness,
and then delegates sampling, seed planning, atomic shards, merge, and sealing
to the already-audited V2R implementation.  It is intentionally safe to
import; no model is loaded and no output is written until ``run_stage`` is
called without ``dry_run`` and every gate passes.
"""
from __future__ import annotations

import copy
import hashlib
import json
import os
import random
import socket
import subprocess
from pathlib import Path
from typing import Any, Mapping

from repairable_diffusion.src.utils.io import load_yaml
from repairable_diffusion.src.v2r.artifacts import (
    COMPACT_FILES,
    atomic_json,
    merge_run,
    read_json,
    run_worker,
    seal_run,
)
from repairable_diffusion.src.v2r.planning import make_plan
from repairable_diffusion.src.v2r.schema import ContractError, canonical_hash, file_hash
from repairable_diffusion.src.v2r.science import execute_base, execute_probe, runtime
from repairable_diffusion.src.rsd_ref_v3.runtime import (
    logical_run_root,
    readiness_path,
    resolve_logical_artifact,
    runtime_location,
    storage_plan_path,
)


ROOT = Path(__file__).resolve().parents[3]
CONFIG_ROOT = ROOT / "repairable_diffusion/configs/rsd_ref_v3/runs"
CONTRACT = ROOT / "repairable_diffusion/configs/rsd_ref_v3/measurement_contract.yaml"
DESIGN_FREEZE = ROOT / "status/rsd_ref_v3/design_freeze.json"
FORBIDDEN_IDENTIFIERS = ("iclr", "naacl", "acl", "emnlp", "conference", "submission")

STAGE_CONFIG_SUFFIX = {
    "reference": "reference",
    "core": "core",
    "temporal": "temporal",
    "mechanism": "mechanism",
    "successful-harm": "successful_harm",
}
INTERNAL_STAGE = {"reference": "base", "core": "r3_core", "temporal": "temporal",
                  "mechanism": "mechanism", "successful-harm": "successful_harm"}
DEEP_STAGES = frozenset({"core", "temporal", "mechanism", "successful-harm"})
Q_C = "native_continuation_qC"
Q_R = "low_confidence_remask_v2_qR"
RANDOM = "matched_count_random_position_remask"
FRESH = "fresh_sampling_compute_control"
CORE = "CoRe-snapshot"


def _json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ContractError(f"Expected JSON object: {path}")
    return value


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def current_git_sha() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def assert_clean_checkout() -> None:
    tracked = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=no"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if tracked.returncode or tracked.stdout.strip():
        raise ContractError("DIRTY_EXECUTION_TREE: tracked files differ from the committed SHA")


def config_path(task: str, stage: str) -> Path:
    if task not in {"llada_math", "llada_gsm8k"}:
        raise ContractError(f"Generation 3 primary runner does not accept task: {task}")
    suffix = STAGE_CONFIG_SUFFIX.get(stage)
    if suffix is None:
        raise ContractError(f"Unsupported Generation 3 stage: {stage}")
    path = CONFIG_ROOT / f"{task}_{suffix}.yaml"
    if not path.is_file():
        raise ContractError(f"Missing frozen run config: {path.relative_to(ROOT)}")
    return path


def load_run_config(task: str, stage: str) -> tuple[Path, dict[str, Any]]:
    path = config_path(task, stage)
    config = load_yaml(path)
    if config.get("generation_id") != "rsd_ref_v3":
        raise ContractError(f"Wrong generation in {path.name}")
    if not str(config.get("run_name", "")).startswith("rsd_ref_v3_"):
        raise ContractError(f"Non-neutral Generation 3 run name: {path.name}")
    declared_task = config.get("task") or config.get("dataset", {}).get("task")
    if declared_task != task:
        raise ContractError(f"Config task mismatch: {path.name}")
    if any(token in str(config).lower() for token in FORBIDDEN_IDENTIFIERS):
        raise ContractError(f"Forbidden conference identifier in config: {path.name}")
    return path, config


def design_freeze_sha() -> str:
    if not DESIGN_FREEZE.is_file():
        raise ContractError("Missing Generation 3 design freeze")
    freeze = _json(DESIGN_FREEZE)
    if freeze.get("generation_id") != "rsd_ref_v3" or freeze.get("status") != "FROZEN_BEFORE_CONFIRMATORY_OUTCOMES":
        raise ContractError("Invalid Generation 3 design freeze status")
    if freeze.get("confirmatory_results_observed") is not False or freeze.get("confirmatory_execution_started") is not False:
        raise ContractError("Design freeze contains confirmatory outcomes or execution")
    files = freeze.get("files")
    if not isinstance(files, dict) or not files:
        raise ContractError("Design freeze has no immutable scientific fingerprint")
    for relative, expected in files.items():
        path = ROOT / relative
        if not path.is_file() or _sha256(path) != expected:
            raise ContractError(f"DESIGN_FREEZE_HASH_MISMATCH: {relative}")
    return _sha256(DESIGN_FREEZE)


def _filesystem_gate(approved_root: Path, minimum_free: int, minimum_inode_fraction: float) -> dict[str, Any]:
    approved_root.mkdir(parents=True, exist_ok=True)
    stat = os.statvfs(approved_root)
    available = stat.f_bavail * stat.f_frsize
    total = stat.f_blocks * stat.f_frsize
    usage = 1.0 - (available / total if total else 0.0)
    inode_fraction = stat.f_favail / stat.f_files if stat.f_files else 0.0
    if usage >= 0.95:
        raise ContractError("STORAGE_GATE_FAILED: filesystem use is at or above 95 percent")
    if available < minimum_free:
        raise ContractError(f"STORAGE_GATE_FAILED: {available} free bytes < {minimum_free}")
    if inode_fraction < minimum_inode_fraction:
        raise ContractError("STORAGE_GATE_FAILED: free inode fraction below 10 percent")
    return {"available_bytes": available, "usage_fraction": usage, "free_inode_fraction": inode_fraction}


def require_runtime_readiness() -> dict[str, Any]:
    storage = _json(storage_plan_path())
    readiness = _json(readiness_path())
    expected_sha = readiness.get("expected_execution_git_sha")
    if not isinstance(expected_sha, str) or expected_sha != current_git_sha():
        raise ContractError("EXECUTION_GIT_SHA_MISMATCH")
    expected_freeze = readiness.get("design_freeze_sha256")
    actual_freeze = design_freeze_sha()
    if not isinstance(expected_freeze, str) or expected_freeze != actual_freeze:
        raise ContractError("DESIGN_FREEZE_SHA256_MISMATCH")
    if storage.get("status") != "STORAGE_READY" or storage.get("execution_allowed") is not True:
        raise ContractError("STORAGE_NOT_READY: storage reservation is not approved")
    gate = readiness.get("single_server_primary_gate", {})
    if gate.get("canonical_source_config_sha_match") is not True:
        raise ContractError("CANONICAL_SOURCE_CONFIG_SHA_MISMATCH")
    if readiness.get("server1", {}).get("scientific_execution_qualification") != "SCIENTIFIC_EXECUTION_QUALIFIED":
        raise ContractError("SERVER_QUALIFICATION_MISSING")
    if readiness.get("protocol", {}).get("design_freeze") != "FROZEN":
        raise ContractError("PROTOCOL_FREEZE_MISSING")
    if gate.get("execution_allowed") is not True or gate.get("storage_ready") is not True:
        raise ContractError("READINESS_GATE_CLOSED")
    approved_root = storage.get("approved_output_root")
    reservation_id = storage.get("reservation_id")
    reserved_bytes = storage.get("reserved_bytes")
    if not approved_root or not isinstance(reservation_id, str) or not reservation_id:
        raise ContractError("STORAGE_RESERVATION_METADATA_MISSING")
    if not isinstance(reserved_bytes, int) or reserved_bytes < 200 * 1024**3:
        raise ContractError("STORAGE_RESERVATION_TOO_SMALL")
    if not str(approved_root).startswith("/") or "rsd_ref_v3" not in Path(approved_root).resolve(strict=False).parts:
        raise ContractError("APPROVED_OUTPUT_ROOT_NAMESPACE_MISMATCH")
    live = _filesystem_gate(Path(approved_root).resolve(strict=False), int(storage.get("minimum_free_after_run_bytes", 200 * 1024**3)), 0.10)
    return {"storage": storage, "readiness": readiness, "live_filesystem": live}


def _recipe(task: str) -> tuple[dict[str, Any], str]:
    recipe_path = ROOT / "results/v2r_reference/reference_recipes/llada.json"
    recipe = _json(recipe_path)
    recipe_task = "math500" if task == "llada_math" else "gsm8k"
    return recipe, recipe_task


def _dataset_payload(task: str, config: Mapping[str, Any], rows: list[dict[str, Any]]) -> dict[str, Any]:
    dataset = config["dataset"]
    return {
        "id": dataset["population"],
        "revision": dataset["source_archive_sha256"],
        "split": dataset["split"],
        "task": "math500" if task == "llada_math" else "gsm8k",
        "source_mode": "native",
        "content_sha256": canonical_hash(rows),
        "archive_sha256": dataset["source_archive_sha256"],
    }


def resolve_run_root(config: Mapping[str, Any], storage: Mapping[str, Any]) -> dict[str, Any]:
    """Resolve a config's frozen logical run root below approved storage."""
    return runtime_location(logical_run_root(config), storage)


def _base_plan(task: str, config_path_value: Path, config: dict[str, Any], rows: list[dict[str, Any]],
               recipe: dict[str, Any], recipe_task: str, freeze_sha: str, timing: float,
               location: Mapping[str, Any], storage: Mapping[str, Any]) -> dict[str, Any]:
    model = {
        "id": config["backend"]["model_id"],
        "revision": config["backend"]["model_revision"],
        "backbone": "llada",
    }
    dataset = _dataset_payload(task, config, rows)
    spec = {
        "namespace": "rsd_ref_v3",
        "run_id": config["run_name"],
        "stage": "base",
        "execution_git_sha": current_git_sha(),
        "design_sha256": freeze_sha,
        "design_freeze_sha256": freeze_sha,
        "generation_id": "rsd_ref_v3",
        "artifact_namespace": "rsd_ref_v3",
        "storage_reservation_id": storage.get("reservation_id", "PENDING_STORAGE_RESERVATION"),
        "logical_run_root": location["logical_path"],
        "physical_run_root": location["physical_path"],
        "approved_output_root": location["approved_output_root"],
        "filesystem_device": location["filesystem_device"],
        "filesystem_mount": location["filesystem_mount"],
        "filesystem_device_or_mount": location["filesystem_device_or_mount"],
        "server_id": os.environ.get("RSD_SERVER_ID", socket.gethostname()),
        "model": model,
        "dataset": dataset,
        "recipe": recipe,
        "config": config,
        "runtime_paths": {
            "source_cache": os.environ.get("RSD_SOURCE_CACHE", "/var/tmp/repairable-state-discovery/upstream"),
            "model_cache": os.environ.get("RSD_MODEL_CACHE", "/var/tmp/repairable-state-discovery/model-cache"),
        },
        "executor": "repairable_diffusion.src.rsd_ref_v3.runner:execute_reference_item",
        "item_ids": [str(row["item_id"]) for row in rows],
        "seed_plan": [{
            "purpose": "base", "trajectory_ids": [0], "checkpoints": [0], "branches": 1,
            "operators": ["reference"], "rng_role": "future", "paired_rng_group": None,
        }],
        "timing": {"seconds_per_item": timing, "target_shard_hours": 4.0},
        "provenance_required": [
            "generation_id", "execution_git_sha", "config_sha256", "model_revision",
            "dataset_archive_sha256", "source_recipe_sha256", "design_freeze_sha256",
            "subset_manifest_sha256", "server_id", "storage_reservation_id",
        ],
    }
    return make_plan(spec)


def _materialized_subset(config: Mapping[str, Any], storage: Mapping[str, Any]) -> tuple[Path, dict[str, Any]]:
    frozen_path = ROOT / config["subset_manifest"]
    if not frozen_path.is_file():
        raise ContractError(f"Missing predeclared subset: {frozen_path}")
    frozen = _json(frozen_path)
    if isinstance(frozen.get("item_ids"), list):
        return frozen_path, frozen
    runtime_path = resolve_logical_artifact(f"results/rsd_ref_v3/subsets/{frozen_path.name}", storage)
    if not runtime_path.is_file():
        raise ContractError(f"Subset is not materialized after base-bank sealing: {runtime_path}")
    runtime = _json(runtime_path)
    if runtime.get("status") != "FROZEN" or not isinstance(runtime.get("item_ids"), list):
        raise ContractError(f"Invalid runtime subset manifest: {runtime_path}")
    return runtime_path, runtime


def _checkpoint_steps(config: Mapping[str, Any]) -> list[int]:
    generation = config.get("generation", {})
    steps = int(generation["steps"])
    gen_length = int(generation["gen_length"])
    block_length = int(generation["block_length"])
    steps_per_block = steps // (gen_length // block_length)
    valid = [step for step in range(1, steps) if step % steps_per_block]
    targets = [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]
    selected = [min(valid, key=lambda value: (abs(value / steps - target), value)) for target in targets]
    if len(set(selected)) != len(selected):
        raise ContractError("Frozen checkpoint grid does not map to distinct active states")
    return selected


def _trajectory_index(base_root: Path, item_ids: list[str]) -> dict[str, dict[str, str]]:
    index: dict[str, dict[str, str]] = {}
    for item_id in item_ids:
        path = base_root / "shards"
        matches = list(path.glob(f"shard-*/items/{canonical_hash(item_id)}/trajectory.json"))
        if len(matches) != 1:
            raise ContractError(f"Expected one sealed base trajectory for {item_id}, found {len(matches)}")
        index[item_id] = {"path": str(matches[0]), "sha256": file_hash(matches[0])}
    return index


def _deep_plan(task: str, stage: str, config_path_value: Path, config: dict[str, Any],
               rows: list[dict[str, Any]], recipe: dict[str, Any], freeze_sha: str,
               subset_path: Path, subset: dict[str, Any], base_root: Path, timing: float,
               location: Mapping[str, Any], storage: Mapping[str, Any]) -> dict[str, Any]:
    item_ids = sorted(str(value) for value in subset.get("item_ids", []))
    if not item_ids:
        raise ContractError("Materialized subset has no item IDs")
    internal = INTERNAL_STAGE[stage]
    checkpoints = _checkpoint_steps(config)
    if stage == "core":
        seed_plan = [
            {"purpose": "localization", "checkpoints": checkpoints, "branches": 4,
             "operators": [Q_C, Q_R], "rng_role": "future", "paired_rng_group": "qC-qR"},
            {"purpose": "confirmation", "checkpoints": checkpoints, "branches": 8,
             "operators": [Q_C, Q_R], "rng_role": "future", "paired_rng_group": "qC-qR"},
        ]
        executor = "repairable_diffusion.src.rsd_ref_v3.runner:execute_core_item"
    elif stage == "temporal":
        seed_plan = [{"purpose": "confirmation", "checkpoints": checkpoints, "branches": 8,
                      "operators": [Q_C, Q_R], "rng_role": "future", "paired_rng_group": "qC-qR"}]
        executor = "repairable_diffusion.src.rsd_ref_v3.runner:execute_temporal_item"
    elif stage == "mechanism":
        seed_plan = [{"purpose": "mechanism", "checkpoints": checkpoints, "branches": 8,
                      "operators": [Q_R, RANDOM, CORE, FRESH], "rng_role": "future", "paired_rng_group": None}]
        executor = "repairable_diffusion.src.rsd_ref_v3.runner:execute_mechanism_item"
    else:
        seed_plan = [{"purpose": "successful_harm", "checkpoints": checkpoints, "branches": 8,
                      "operators": [Q_R, RANDOM, FRESH], "rng_role": "future", "paired_rng_group": None}]
        executor = "repairable_diffusion.src.rsd_ref_v3.runner:execute_successful_harm_item"
    model = {"id": config.get("model_id", "GSAI-ML/LLaDA-8B-Instruct"),
             "revision": config.get("model_revision", "08b83a6feb34df1a6011b80c3c00c7563e963b07"),
             "backbone": "llada"}
    dataset = {"id": config.get("population"), "revision": config.get("source_archive_sha256"),
               "split": "test", "task": "math500" if task == "llada_math" else "gsm8k",
               "source_mode": "native", "archive_sha256": config.get("source_archive_sha256"),
               "content_sha256": canonical_hash(rows)}
    freeze_key = "successful_pool_freeze" if stage == "successful-harm" else "failed_pool_freeze"
    pool = {"status": "FROZEN", "bank_sha256": subset["bank_sha256"], "item_ids": item_ids,
            "selection_sha256": subset.get("selection_sha256", _sha256(subset_path))}
    manifest_config = copy.deepcopy(config)
    manifest_config["checkpoint_grid"] = [0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]
    manifest_config["tau_confirm"] = 0.25
    manifest_config["B_loc"] = int(config.get("B_loc", 4))
    manifest_config["B_eval"] = int(config.get("B_eval", 8))
    spec = {
        "namespace": "rsd_ref_v3", "run_id": config["run_name"], "stage": internal,
        "execution_git_sha": current_git_sha(), "design_sha256": freeze_sha,
        "design_freeze_sha256": freeze_sha, "generation_id": "rsd_ref_v3",
        "artifact_namespace": "rsd_ref_v3", "storage_reservation_id": storage.get("reservation_id", "PENDING_STORAGE_RESERVATION"),
        "logical_run_root": location["logical_path"],
        "physical_run_root": location["physical_path"],
        "approved_output_root": location["approved_output_root"],
        "filesystem_device": location["filesystem_device"],
        "filesystem_mount": location["filesystem_mount"],
        "filesystem_device_or_mount": location["filesystem_device_or_mount"],
        "server_id": os.environ.get("RSD_SERVER_ID", socket.gethostname()), "model": model,
        "dataset": dataset, "recipe": recipe, "config": manifest_config,
        "runtime_paths": {"source_cache": os.environ.get("RSD_SOURCE_CACHE", "/var/tmp/repairable-state-discovery/upstream"),
                          "model_cache": os.environ.get("RSD_MODEL_CACHE", "/var/tmp/repairable-state-discovery/model-cache")},
        "executor": executor, "operator_names": {"qC": Q_C, "qR": Q_R},
        freeze_key: pool, "trajectory_index": _trajectory_index(base_root, item_ids),
        "subset_manifest_sha256": _sha256(subset_path), "item_ids": item_ids,
        "seed_plan": seed_plan, "timing": {"seconds_per_item": timing, "target_shard_hours": 4.0},
    }
    return make_plan(spec)


def _rows_from_base(base_root: Path) -> list[dict[str, Any]]:
    aggregate = _json(base_root / "aggregate" / "aggregate.json")
    if aggregate.get("status") != "MERGED_VALID":
        raise ContractError("Base bank is not merged and valid")
    return list(aggregate.get("items", []))


def materialize_subsets(task: str, config: Mapping[str, Any], base_root: Path, output_root: Path) -> list[Path]:
    rows = _rows_from_base(base_root)
    if not rows:
        raise ContractError("Base bank has no rows")
    bank_sha = canonical_hash(rows)
    outputs: list[Path] = []
    output_root.mkdir(parents=True, exist_ok=True)
    for purpose in ("core", "temporal", "mechanism", "successful_harm"):
        path = ROOT / f"status/rsd_ref_v3/subsets/{task}_{purpose}.json"
        frozen = _json(path)
        candidates = [row for row in rows if bool(row["result"].get("correct")) is (purpose == "successful_harm")]
        target = int(frozen["target"])
        minimum = int(frozen["minimum"])
        ranked = sorted(candidates, key=lambda row: canonical_hash([314159265, "llada", task, purpose, row["item_id"], 0]))
        selected = ranked[:target]
        if len(selected) < minimum:
            raise ContractError(f"{purpose} subset shortage: {len(selected)} < {minimum}")
        payload = {
            "generation_id": "rsd_ref_v3", "status": "FROZEN", "task": task,
            "purpose": purpose, "population": frozen.get("population"), "target": target,
            "minimum": minimum, "bank_sha256": bank_sha,
            "selection_rule": "SHA256(generation|design_seed|backbone|task|purpose|item_id|trajectory_id)",
            "selection_sha256": canonical_hash([task, purpose, bank_sha, [r["item_id"] for r in selected]]),
            "item_ids": sorted(str(row["item_id"]) for row in selected),
            "failed_pool_count": sum(not bool(row["result"].get("correct")) for row in rows),
            "successful_pool_count": sum(bool(row["result"].get("correct")) for row in rows),
        }
        output = output_root / path.name
        atomic_json(output, payload)
        outputs.append(output)
    return outputs


def execute_reference_item(manifest: Mapping[str, Any], item_id: str, item_output_dir: Path,
                           seed_records: list[dict[str, Any]]) -> Mapping[str, Any]:
    return execute_base(manifest, item_id, item_output_dir, seed_records)


def execute_core_item(manifest: Mapping[str, Any], item_id: str, item_output_dir: Path,
                      seed_records: list[dict[str, Any]]) -> Mapping[str, Any]:
    return execute_probe(manifest, item_id, item_output_dir, seed_records)


def execute_temporal_item(manifest: Mapping[str, Any], item_id: str, item_output_dir: Path,
                          seed_records: list[dict[str, Any]]) -> Mapping[str, Any]:
    return execute_probe(manifest, item_id, item_output_dir, seed_records)


def _eligible_positions(snapshot: Mapping[str, Any]) -> list[int]:
    return [index for index, confidence in enumerate(snapshot["token_confidences"]) if confidence is not None]


def _random_positions(snapshot: Mapping[str, Any], target: list[int], seed: int) -> list[int]:
    eligible = _eligible_positions(snapshot)
    if not eligible or not target:
        return []
    return sorted(random.Random(seed).sample(eligible, min(len(target), len(eligible))))


def _core_snapshot_positions(sampler: Any, snapshot: Mapping[str, Any], target: list[int]) -> list[int]:
    """Apply the pinned V2 CoRe-snapshot position rule to a native snapshot."""
    import torch
    import torch.nn.functional as functional

    prompt_len = int(snapshot["prompt_len"])
    block_length = int(sampler.generation["block_length"])
    steps = int(sampler.generation["steps"])
    gen_length = int(sampler.generation["gen_length"])
    steps_per_block = steps // (gen_length // block_length)
    if int(snapshot["step_in_block"]) >= steps_per_block:
        return []
    start = prompt_len + int(snapshot["block_index"]) * block_length
    end = start + block_length
    mask_id = int(sampler.generation["mask_id"])
    device = next(sampler.model.parameters()).device
    tokens = torch.tensor(snapshot["full_token_ids"], dtype=torch.long, device=device).unsqueeze(0)
    with torch.no_grad():
        logits = sampler.model(tokens).logits
        probabilities = functional.softmax(logits.to(torch.float32), dim=-1)
    committed = [absolute for absolute in range(start, end) if int(tokens[0, absolute].item()) != mask_id]
    if not committed:
        return []
    top2, _ = probabilities[0, committed].topk(2, dim=-1)
    margins = top2[:, 0] - top2[:, 1]
    candidate_count = min(32, len(committed))
    _, candidate_indices = torch.topk(-margins, k=candidate_count)
    verify_absolute = [committed[int(index)] for index in candidate_indices.detach().cpu().tolist()]
    verified_tokens = tokens.clone()
    verified_tokens[0, verify_absolute] = mask_id
    with torch.no_grad():
        verified_logits = sampler.model(verified_tokens).logits
        verified_probabilities = functional.softmax(verified_logits.to(torch.float32), dim=-1)
    original_tokens = tokens[0, verify_absolute]
    original_probability = verified_probabilities[0, verify_absolute].gather(-1, original_tokens.unsqueeze(-1)).squeeze(-1)
    replacement = torch.argmax(verified_logits[0, verify_absolute], dim=-1)
    replacement_probability = verified_probabilities[0, verify_absolute].gather(-1, replacement.unsqueeze(-1)).squeeze(-1)
    valid = (replacement != original_tokens) & (replacement_probability >= 0.30)
    valid_indices = torch.where(valid)[0]
    if valid_indices.numel() == 0 or not target:
        return []
    log_probability = torch.log(original_probability + 1e-10)
    desired = min(len(target), int(valid_indices.numel()))
    _, selected = torch.topk(-log_probability[valid_indices], k=desired)
    selected_indices = valid_indices[selected]
    return sorted(verify_absolute[int(index)] - prompt_len for index in selected_indices.detach().cpu().tolist())


def _load_selected_trajectory(manifest: Mapping[str, Any], item_id: str) -> tuple[Any, dict[str, Any], dict[str, Any]]:
    sampler, items = runtime(manifest)
    source = manifest["trajectory_index"][item_id]
    if file_hash(source["path"]) != source["sha256"]:
        raise ContractError("Original bank snapshot hash mismatch")
    payload = read_json(source["path"])
    return sampler, items[item_id], payload["trajectory"]


def _control_result(sampler: Any, item: dict[str, Any], snapshot: dict[str, Any], operator: str,
                   record: Mapping[str, Any], target: list[int]) -> dict[str, Any]:
    if operator == Q_R:
        modified = target
        outcome = sampler.continue_llada(item, snapshot, seed=record["seed"], modified_positions=modified)
        return {"correct": outcome["correct"], "answer": outcome["answer"], "nfe": outcome["nfe"],
                "seconds": outcome["seconds"], "modified_positions": modified,
                "mask_count": outcome["mask_count"]}
    if operator == RANDOM:
        modified = _random_positions(snapshot, target, int(record["seed"]))
        outcome = sampler.continue_llada(item, snapshot, seed=record["seed"], modified_positions=modified)
        return {"correct": outcome["correct"], "answer": outcome["answer"], "nfe": outcome["nfe"],
                "seconds": outcome["seconds"], "modified_positions": modified,
                "mask_count": outcome["mask_count"]}
    if operator == FRESH:
        outcome = sampler.generate(item, int(record["seed"]), False)
        return {"correct": outcome["correct"], "answer": outcome["final_answer"], "nfe": outcome["nfe"],
                "seconds": outcome["seconds"], "modified_positions": [], "mask_count": outcome["mask_count"]}
    if operator == CORE:
        modified = _core_snapshot_positions(sampler, snapshot, target)
        outcome = sampler.continue_llada(item, snapshot, seed=record["seed"], modified_positions=modified)
        return {"correct": outcome["correct"], "answer": outcome["answer"], "nfe": outcome["nfe"],
                "seconds": outcome["seconds"], "modified_positions": modified,
                "mask_count": outcome["mask_count"], "core_source_repository": "UCF-CRCV/CoRe",
                "core_source_revision": "524e01e11a8751afb67b81a2c930f938faf9a70e", "label": "CoRe-snapshot"}
    raise ContractError(f"Unsupported Generation 3 mechanism operator: {operator}")


def _execute_controls(manifest: Mapping[str, Any], item_id: str, item_output_dir: Path,
                      seed_records: list[dict[str, Any]], expected: set[str], pool_key: str) -> Mapping[str, Any]:
    sampler, item, trajectory = _load_selected_trajectory(manifest, item_id)
    rows = []
    consumed = set()
    states = {int(key): value for key, value in trajectory["snapshots"].items() if int(key) < trajectory["total_steps"]}
    lookup = {(r["context"]["checkpoint"], r["context"]["branch"], r["context"]["operator"]): r for r in seed_records}
    for step in sorted(states):
        snapshot = states[step]
        target = []
        eligible = [(index, float(value)) for index, value in enumerate(snapshot["token_confidences"]) if value is not None]
        eligible.sort(key=lambda row: (row[1], row[0]))
        if eligible:
            count = min(len(eligible), max(4, int(__import__("math").ceil(len(eligible) * 0.25))))
            target = sorted(index for index, _ in eligible[:count])
        for branch in range(int(manifest["config"].get("B_eval", 8))):
            for operator in sorted({record["context"]["operator"] for record in seed_records}):
                record = lookup[(step, branch, operator)]
                result = _control_result(sampler, item, snapshot, operator, record, target)
                if result.get("mask_count"):
                    raise ContractError("Control continuation left masked tokens")
                consumed.add(record["context_id"])
                rows.append({"step": step, "normalized_progress": step / trajectory["total_steps"],
                             "branch": branch, "operator": operator, "seed_context_id": record["context_id"],
                             **result})
    if consumed != expected:
        raise ContractError("Mechanism/harm executor did not consume the complete seed registry")
    artifact_name = "successful_harm.json" if manifest["stage"] == "successful_harm" else "mechanism.json"
    atomic_json(item_output_dir / artifact_name, {"item_id": item_id, "trajectory_id": 0,
                 "bank_sha256": manifest[pool_key]["bank_sha256"], "controls": rows,
                 "deterministic_reference": True, "independent_bernoulli_replicates_claimed": False})
    return {"evidence_kind": "reference_scientific", "trajectory_id": 0,
            "bank_sha256": manifest[pool_key]["bank_sha256"], "seed_context_ids": sorted(consumed),
            "unused_seed_context_ids": [], "controls_file": artifact_name,
            "controls_sha256": file_hash(item_output_dir / artifact_name),
            "harm_rows": sum(1 for row in rows if row["operator"] in {Q_R, RANDOM, FRESH} and row["correct"] is False)}


def execute_mechanism_item(manifest: Mapping[str, Any], item_id: str, item_output_dir: Path,
                           seed_records: list[dict[str, Any]]) -> Mapping[str, Any]:
    expected = {row["context_id"] for row in seed_records}
    return _execute_controls(manifest, item_id, item_output_dir, seed_records, expected, "failed_pool_freeze")


def execute_successful_harm_item(manifest: Mapping[str, Any], item_id: str, item_output_dir: Path,
                                seed_records: list[dict[str, Any]]) -> Mapping[str, Any]:
    expected = {row["context_id"] for row in seed_records}
    return _execute_controls(manifest, item_id, item_output_dir, seed_records, expected, "successful_pool_freeze")


def dry_run_summary(task: str, stage: str, source_stage: str = "reference") -> dict[str, Any]:
    path, config = load_run_config(task, source_stage if stage in {"aggregate", "seal"} else stage)
    freeze_sha = design_freeze_sha()
    return {"status": "DRY_RUN_ONLY", "generation_id": "rsd_ref_v3", "task": task, "stage": stage,
            "config": str(path.relative_to(ROOT)), "config_sha256": _sha256(path),
            "design_freeze_sha256": freeze_sha, "execution_allowed": False,
            "required_stage_dependency": "sealed_base_bank" if stage in DEEP_STAGES else ("completed_shards" if stage == "aggregate" else "merged_aggregate" if stage == "seal" else "none"),
            "logical_run_root": logical_run_root(config), "physical_run_root": "PENDING_STORAGE_READY",
            "output_namespace": "outputs/rsd_ref_v3", "storage_gate": config.get("storage_gate", "not_applicable")}


def run_stage(task: str, stage: str, *, dry_run: bool = False, shard: int | None = None,
              gates_path: Path | None = None, seconds_per_item: float = 7200.0,
              source_stage: str = "reference", compact_dir: Path | None = None) -> dict[str, Any]:
    if dry_run:
        return dry_run_summary(task, stage, source_stage)
    assert_clean_checkout()
    freeze_sha = design_freeze_sha()
    readiness = require_runtime_readiness()
    if stage in {"aggregate", "seal"}:
        path, config = load_run_config(task, source_stage)
        location = resolve_run_root(config, readiness["storage"])
        run_root = Path(location["physical_path"])
        manifest = _json(run_root / "run_manifest.json")
        if gates_path is None or not gates_path.is_file():
            raise ContractError("A frozen R0/R1/R2 gate report bundle is required")
        gates = _json(gates_path)
        if stage == "aggregate":
            aggregate = merge_run(manifest, run_root, gates=gates)
            return {"status": aggregate["status"], "run": str(run_root), "item_count": aggregate["item_count"],
                    "design_freeze_sha256": freeze_sha, "storage_reservation_id": readiness["storage"].get("reservation_id")}
        if compact_dir is None:
            raise ContractError("seal stage requires --compact-dir with precomputed scientific summaries")
        compact = {name: compact_dir / name for name in (COMPACT_FILES - {"reference_recipe.json", "run_manifest.json", "scientific_provenance.json"})}
        sealed = seal_run(manifest, run_root, run_root / "sealed", gates=gates, compact_artifacts=compact)
        return {"status": sealed["status"], "bundle": str(run_root / "sealed"),
                "design_freeze_sha256": freeze_sha, "storage_reservation_id": readiness["storage"].get("reservation_id")}
    path, config = load_run_config(task, stage)
    if gates_path is None or not gates_path.is_file():
        raise ContractError("A frozen R0/R1/R2 gate report bundle is required")
    gates = _json(gates_path)
    source_cache = Path(os.environ.get("RSD_SOURCE_CACHE", "/var/tmp/repairable-state-discovery/upstream"))
    from repairable_diffusion.src.rsd_ref_v3.task_adapters import load_source_task
    recipe, sources, rows = load_source_task(task, source_cache)
    location = resolve_run_root(config, readiness["storage"])
    if stage == "reference":
        manifest = _base_plan(task, path, config, rows, recipe, "math500" if task == "llada_math" else "gsm8k", freeze_sha, seconds_per_item,
                              location, readiness["storage"])
        executor = execute_reference_item
    else:
        subset_path, subset = _materialized_subset(config, readiness["storage"])
        base_config_path, base_config = load_run_config(task, "reference")
        base_location = resolve_run_root(base_config, readiness["storage"])
        base_root = Path(base_location["physical_path"])
        manifest = _deep_plan(task, stage, path, {**config, "generation": base_config["generation"],
                            "model_id": base_config["backend"]["model_id"],
                            "model_revision": base_config["backend"]["model_revision"],
                            "population": base_config["dataset"]["population"],
                            "source_archive_sha256": base_config["dataset"]["source_archive_sha256"]},
                            rows, recipe, freeze_sha, subset_path, subset, base_root, seconds_per_item,
                            location, readiness["storage"])
        executor = {"core": execute_core_item, "temporal": execute_temporal_item,
                    "mechanism": execute_mechanism_item, "successful-harm": execute_successful_harm_item}[stage]
    run_root = Path(location["physical_path"])
    run_root.mkdir(parents=True, exist_ok=True)
    atomic_json(run_root / "run_manifest.json", manifest)
    selected_shards = [shard] if shard is not None else list(range(len(manifest["shards"])))
    for shard_id in selected_shards:
        run_worker(manifest, shard_id, run_root, executor, gates=gates)
    if shard is None:
        aggregate = merge_run(manifest, run_root, gates=gates)
        return {"status": "MERGED_VALID", "run": str(run_root), "item_count": aggregate["item_count"],
                "design_freeze_sha256": freeze_sha, "storage_reservation_id": readiness["storage"].get("reservation_id")}
    return {"status": "SHARD_DONE", "run": str(run_root), "shard": shard, "shards": len(manifest["shards"])}


def materialize_task_subsets(task: str, *, dry_run: bool = False) -> dict[str, Any]:
    _, config = load_run_config(task, "reference")
    if dry_run:
        return {"status": "DRY_RUN_ONLY", "task": task, "base_run": logical_run_root(config),
                "logical_output_root": "results/rsd_ref_v3/subsets", "physical_output_root": "PENDING_STORAGE_READY",
                "output_namespace": "results/rsd_ref_v3/subsets", "execution_allowed": False}
    assert_clean_checkout()
    readiness = require_runtime_readiness()
    base_location = resolve_run_root(config, readiness["storage"])
    output_location = runtime_location("results/rsd_ref_v3/subsets", readiness["storage"])
    outputs = materialize_subsets(task, config, Path(base_location["physical_path"]), Path(output_location["physical_path"]))
    return {"status": "SUBSETS_FROZEN", "task": task, "outputs": [str(p) for p in outputs],
            "logical_output_root": output_location["logical_path"],
            "physical_output_root": output_location["physical_path"],
            "approved_output_root": output_location["approved_output_root"],
            "filesystem_device": output_location["filesystem_device"],
            "filesystem_mount": output_location["filesystem_mount"]}
