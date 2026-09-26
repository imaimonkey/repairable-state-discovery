"""Atomic shard-local execution, strict single-writer merge, and compact sealing.

Executor API: ``execute_item(manifest, item_id, item_output_dir, seed_records)``.
The executor writes raw files below the supplied temporary item directory and
returns a JSON object containing ``seed_context_ids`` for every consumed context.
The infrastructure publishes an item only after result and payload hashing. It
never computes aggregate reports in a worker and never treats CPU fixtures as
scientific gate evidence.
"""
from __future__ import annotations

import contextlib
import csv
import fcntl
import importlib
import inspect
import io
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Callable, Iterator, Mapping

from .schema import (ContractError, DEEP_STAGES, SCIENTIFIC_STAGES, canonical_bytes,
                     canonical_hash, file_hash, manifest_binding, validate_manifest,
                     validate_metric_names)


def read_json(path: str | Path) -> Any:
    with Path(path).open(encoding="utf-8") as handle:
        return json.load(handle)


def atomic_json(path: str | Path, value: Any) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = canonical_bytes(value) + b"\n"
    fd, temp = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp, path)
        _fsync_dir(path.parent)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


def _fsync_dir(path: Path) -> None:
    fd = os.open(path, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


@contextlib.contextmanager
def writer_lock(path: Path) -> Iterator[None]:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as handle:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise ContractError(f"Another writer owns {path}") from exc
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def assert_namespace(path: str | Path, namespace: str = "v2r_reference") -> Path:
    path = Path(path).resolve()
    if namespace == "v2r_reference":
        valid = "v2r_reference" in path.parts and "v2_measurement" not in path.parts
    elif namespace == "rsd_ref_v3":
        valid = "rsd_ref_v3" in path.parts and "v2_measurement" not in path.parts and "v2r_reference" not in path.parts
    else:
        valid = False
    if not valid:
        raise ContractError(f"Outputs must be isolated inside the {namespace} namespace")
    return path


def verify_execution_checkout(repo: str | Path, manifest: Mapping[str, Any]) -> None:
    repo = Path(repo).resolve()
    actual = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
    if actual != manifest["execution_git_sha"]:
        raise ContractError("Execution checkout differs from the frozen start-time SHA")
    for command in (["git", "diff", "--quiet"], ["git", "diff", "--cached", "--quiet"]):
        if subprocess.run(command, cwd=repo, check=False).returncode != 0:
            raise ContractError("Execution checkout has tracked changes")
    module, _ = manifest["executor"].split(":")
    origin = inspect.getsourcefile(importlib.import_module(module))
    if origin is None:
        raise ContractError("Executor source cannot be located")
    try:
        relative = Path(origin).resolve().relative_to(repo)
    except ValueError as exc:
        raise ContractError("Executor is outside the frozen execution checkout") from exc
    tracked = subprocess.run(["git", "ls-files", "--error-unmatch", str(relative)], cwd=repo,
                             capture_output=True, text=True, check=False)
    if tracked.returncode:
        raise ContractError("Executor must be tracked in the exact frozen commit")


def validate_gate_chain(manifest: Mapping[str, Any], gates: Mapping[str, Mapping[str, Any]]) -> None:
    dependencies = {"r0_smoke": (), "r0_full": ("R0",), "r1_bridge": ("R0",),
                    "r2_equivalence": ("R0", "R1")}
    required = dependencies.get(manifest["stage"], ("R0", "R1", "R2"))
    if not required:
        return
    from .reference_gates import validate_gate_report
    for name in required:
        report = gates.get(name)
        if not isinstance(report, Mapping) or report.get("gate") != name or report.get("status") != "PASS":
            raise ContractError(f"Missing proven {name} PASS; scientific execution is blocked")
        errors = validate_gate_report(report)
        if errors:
            raise ContractError(f"Invalid {name} evidence: {'; '.join(errors)}")
        expected = {"execution_git_sha": manifest["execution_git_sha"],
                    "config_sha256": manifest["config_sha256"], "recipe_sha256": manifest["recipe_sha256"],
                    "model_revision": manifest["model"]["revision"],
                    "dataset_revision": manifest["dataset"]["revision"]}
        for key, value in expected.items():
            if report.get(key) != value:
                raise ContractError(f"{name} {key} differs from this execution contract")
        if report.get("backbone") != manifest["model"].get("backbone") or report.get("task") != manifest["dataset"].get("task"):
            raise ContractError(f"{name} backbone/task differs from this run")


def _inventory(root: Path, *, exclude: set[str] | None = None) -> dict[str, str]:
    result = {}
    exclude = exclude or set()
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ContractError(f"Symlink is forbidden inside an artifact: {path}")
        if path.is_file():
            relative = path.relative_to(root).as_posix()
            if relative not in exclude:
                result[relative] = file_hash(path)
    return result


def _verify_inventory(root: Path, expected: Mapping[str, str], *, exclude: set[str] | None = None) -> None:
    if _inventory(root, exclude=exclude) != dict(expected):
        raise ContractError(f"Artifact hashes or file inventory differ: {root}")


def _item_directory(shard: Path, item_id: str) -> Path:
    return shard / "items" / canonical_hash(item_id)


def _item_seed_records(manifest: Mapping[str, Any], item_id: str) -> list[dict[str, Any]]:
    return [row for row in manifest["seed_registry"]["records"] if row["context"]["item_id"] == item_id]


def _validate_result(manifest: Mapping[str, Any], item_id: str, result: Mapping[str, Any]) -> None:
    validate_metric_names(result)
    expected = sorted(row["context_id"] for row in _item_seed_records(manifest, item_id))
    consumed = result.get("seed_context_ids")
    unused = result.get("unused_seed_context_ids", [])
    if (not isinstance(consumed, list) or not isinstance(unused, list)
            or len(set(consumed + unused)) != len(consumed + unused)
            or sorted(consumed + unused) != expected):
        raise ContractError("Executor did not partition the complete predeclared seed registry")
    if unused:
        if manifest["stage"] != "r3_core" or result.get("unused_seed_context_reason") != "not_selected_checkpoint":
            raise ContractError("Unconsumed RNG contexts need a frozen selection reason")
        selected = result.get("selected_checkpoint")
        for record in _item_seed_records(manifest, item_id):
            c = record["context"]
            should_skip = c["purpose"] == "confirmation" and c["checkpoint"] != selected
            if (record["context_id"] in unused) != should_skip:
                raise ContractError("Unused RNG context is not an unselected confirmation checkpoint")
    if manifest["stage"] in {"base", "r0_full", "r0_smoke"}:
        if type(result.get("correct")) is not bool:
            raise ContractError("A base trajectory requires an explicit boolean correctness result")
    if manifest["stage"] in SCIENTIFIC_STAGES and result.get("evidence_kind") != "reference_scientific":
        raise ContractError("Scientific outputs require reference_scientific evidence")
    if manifest["stage"] in DEEP_STAGES:
        subset_key = "successful_pool_freeze" if manifest["stage"] == "successful_harm" else "failed_pool_freeze"
        if result.get("bank_sha256") != manifest[subset_key]["bank_sha256"]:
            raise ContractError("Repairability result does not refer to the frozen reference trajectory bank")


def validate_completed_item(path: Path, manifest: Mapping[str, Any], item_id: str) -> dict[str, Any]:
    if not path.is_dir() or path.is_symlink():
        raise ContractError(f"Missing atomic completed item: {item_id}")
    completion = read_json(path / "COMPLETE.json")
    if completion.get("binding") != manifest_binding(manifest) or completion.get("item_id") != item_id:
        raise ContractError("Stale item provenance: refusing cache reuse")
    _verify_inventory(path, completion["artifact_hashes"], exclude={"COMPLETE.json"})
    result = read_json(path / "result.json")
    _validate_result(manifest, item_id, result)
    return result


def run_worker(manifest: Mapping[str, Any], shard_id: int, run_dir: str | Path,
               executor: Callable[..., Mapping[str, Any]], *, gates: Mapping[str, Mapping[str, Any]]) -> dict[str, Any]:
    validate_manifest(manifest)
    validate_gate_chain(manifest, gates)
    run_dir = assert_namespace(run_dir, manifest["namespace"])
    if isinstance(shard_id, bool) or not isinstance(shard_id, int) or not 0 <= shard_id < len(manifest["shards"]):
        raise ContractError("Unknown shard")
    spec = manifest["shards"][shard_id]
    shard = run_dir / "shards" / f"shard-{shard_id:03d}"
    shard.mkdir(parents=True, exist_ok=True)
    expected_manifest = {"binding": manifest_binding(manifest), "assignment_sha256": manifest["assignment_sha256"],
                         "shard": spec, "gate_reports_sha256": canonical_hash(gates)}
    with writer_lock(shard / ".writer.lock"):
        local_manifest = shard / "shard_manifest.json"
        if local_manifest.exists() and read_json(local_manifest) != expected_manifest:
            raise ContractError("Shard manifest mismatch: stale output cannot be resumed")
        if not local_manifest.exists():
            atomic_json(local_manifest, expected_manifest)
        if (shard / "DONE.json").exists():
            validate_shard(shard, manifest, shard_id, gates=gates)
            return read_json(shard / "DONE.json")
        (shard / "items").mkdir(exist_ok=True)
        completed: list[str] = []
        for item in spec["item_ids"]:
            destination = _item_directory(shard, item)
            if destination.exists():
                validate_completed_item(destination, manifest, item)
            else:
                temporary = Path(tempfile.mkdtemp(prefix=".partial-", dir=shard / "items"))
                try:
                    result = dict(executor(manifest, item, temporary, _item_seed_records(manifest, item)))
                    _validate_result(manifest, item, result)
                    for forbidden in ("result.json", "COMPLETE.json"):
                        if (temporary / forbidden).exists():
                            raise ContractError(f"Executor wrote reserved file {forbidden}")
                    atomic_json(temporary / "result.json", result)
                    hashes = _inventory(temporary)
                    atomic_json(temporary / "COMPLETE.json", {"binding": manifest_binding(manifest),
                                "item_id": item, "artifact_hashes": hashes})
                    os.rename(temporary, destination)
                    _fsync_dir(destination.parent)
                except BaseException:
                    # Preserve partial evidence for diagnosis; never reuse it as completed.
                    raise
            completed.append(item)
            atomic_json(shard / "progress.json", {"binding": manifest_binding(manifest),
                        "shard_id": shard_id, "completed_item_ids": completed,
                        "completed_count": len(completed), "expected_count": len(spec["item_ids"])})
        done = {"status": "DONE", "binding": manifest_binding(manifest), "shard_id": shard_id,
                "item_count": len(completed), "item_ids": completed,
                "shard_manifest_sha256": file_hash(local_manifest),
                "item_completion_hashes": {item: file_hash(_item_directory(shard, item) / "COMPLETE.json") for item in completed}}
        atomic_json(shard / "DONE.json", done)
        validate_shard(shard, manifest, shard_id, gates=gates)
        return done


def validate_shard(shard: Path, manifest: Mapping[str, Any], shard_id: int,
                   *, gates: Mapping[str, Mapping[str, Any]]) -> list[dict[str, Any]]:
    spec = manifest["shards"][shard_id]
    if shard.is_symlink():
        raise ContractError("Shard directory cannot be a symlink")
    done = read_json(shard / "DONE.json")
    expected_local = {"binding": manifest_binding(manifest), "assignment_sha256": manifest["assignment_sha256"],
                      "shard": spec, "gate_reports_sha256": canonical_hash(gates)}
    if read_json(shard / "shard_manifest.json") != expected_local:
        raise ContractError("Shard binding, gate reports, or assignment mismatch")
    if done.get("status") != "DONE" or done.get("binding") != manifest_binding(manifest) or done.get("shard_id") != shard_id:
        raise ContractError("Invalid DONE provenance")
    if done.get("item_ids") != spec["item_ids"] or done.get("item_count") != len(spec["item_ids"]):
        raise ContractError("DONE has missing or duplicate items")
    if done.get("shard_manifest_sha256") != file_hash(shard / "shard_manifest.json"):
        raise ContractError("Shard manifest hash mismatch")
    actual_dirs = {path.name for path in (shard / "items").iterdir() if not path.name.startswith(".partial-")}
    if actual_dirs != {canonical_hash(item) for item in spec["item_ids"]}:
        raise ContractError("Unexpected or missing completed item directories")
    rows = []
    expected_hashes = {}
    for item in spec["item_ids"]:
        directory = _item_directory(shard, item)
        result = validate_completed_item(directory, manifest, item)
        expected_hashes[item] = file_hash(directory / "COMPLETE.json")
        rows.append({"item_id": item, "trajectory_id": 0, "result": result,
                     "completion_sha256": expected_hashes[item]})
    if done.get("item_completion_hashes") != expected_hashes:
        raise ContractError("DONE item completion hash inventory mismatch")
    return rows


def merge_run(manifest: Mapping[str, Any], run_dir: str | Path, *, gates: Mapping[str, Mapping[str, Any]],
              shard_locations: Mapping[int, str | Path] | None = None) -> dict[str, Any]:
    """Validate every expected DONE, then publish one atomic aggregate directory.

    Optional explicit locations permit read-only aggregation across mounted or
    transferred shards without assuming shared storage. Raw snapshots stay put.
    """
    validate_manifest(manifest)
    validate_gate_chain(manifest, gates)
    run_dir = assert_namespace(run_dir, manifest["namespace"])
    expected_ids = set(range(len(manifest["shards"])))
    if shard_locations is None:
        roots = {index: run_dir / "shards" / f"shard-{index:03d}" for index in expected_ids}
        existing = {p.name for p in (run_dir / "shards").glob("shard-*")}
        if existing != {f"shard-{index:03d}" for index in expected_ids}:
            raise ContractError("Missing or unexpected shard directories")
    else:
        if set(shard_locations) != expected_ids:
            raise ContractError("Remote shard mapping has missing or unexpected shards")
        roots = {index: Path(path) for index, path in shard_locations.items()}
        if len({path.resolve() for path in roots.values()}) != len(roots):
            raise ContractError("Remote shard mapping contains duplicate locations")
    with writer_lock(run_dir / ".merge.lock"):
        rows, done_hashes = [], {}
        for index in sorted(expected_ids):
            rows.extend(validate_shard(roots[index], manifest, index, gates=gates))
            done_hashes[str(index)] = file_hash(roots[index] / "DONE.json")
        rows.sort(key=lambda row: row["item_id"])
        if [row["item_id"] for row in rows] != manifest["item_ids"]:
            raise ContractError("Merged result contains duplicate or missing items")
        aggregate = {"status": "MERGED_VALID", "binding": manifest_binding(manifest),
                     "stage": manifest["stage"], "item_count": len(rows), "items": rows,
                     "shard_done_hashes": done_hashes, "gate_reports_sha256": canonical_hash(gates)}
        if manifest["stage"] in {"base", "r0_full", "r0_smoke"}:
            failed = sum(not row["result"]["correct"] for row in rows)
            aggregate["base_report"] = {"sampled_trajectory_count": len(rows),
                "sampled_failed_trajectory_count": failed,
                "items_with_at_least_one_failed_trajectory": failed,
                "reference_trajectory_accuracy": (len(rows) - failed) / len(rows)}
        destination = run_dir / "aggregate"
        if destination.exists():
            _verify_inventory(destination, read_json(destination / "MERGED.json")["artifact_hashes"], exclude={"MERGED.json"})
            if read_json(destination / "aggregate.json") != aggregate:
                raise ContractError("Existing aggregate differs; refusing overwrite")
            return aggregate
        temporary = Path(tempfile.mkdtemp(prefix=".merge-", dir=run_dir))
        atomic_json(temporary / "aggregate.json", aggregate)
        atomic_json(temporary / "run_manifest.json", manifest)
        atomic_json(temporary / "gate_reports.json", gates)
        atomic_json(temporary / "MERGED.json", {"status": "MERGED_VALID", "binding": manifest_binding(manifest),
                    "artifact_hashes": _inventory(temporary)})
        os.rename(temporary, destination)
        _fsync_dir(run_dir)
        return aggregate


COMPACT_FILES = frozenset({"reference_recipe.json", "run_manifest.json", "scientific_provenance.json",
    "base_report.json", "existence.csv", "temporal_summary.csv", "mechanism_summary.csv",
    "selector_summary.csv", "decoder_regime_summary.json"})


def seal_run(manifest: Mapping[str, Any], run_dir: str | Path, bundle_dir: str | Path,
             *, gates: Mapping[str, Mapping[str, Any]], compact_artifacts: Mapping[str, str | Path],
             max_compact_bytes: int = 32 * 1024 * 1024) -> dict[str, Any]:
    """Publish compact evidence only; missing scientific summaries block sealing.

    Stage-specific scientific reducers supply the compact CSV/JSON files. This
    layer verifies provenance and hashes and deliberately does not invent rows,
    effect estimates, successful tests, or unavailable baseline observations.
    """
    validate_manifest(manifest)
    if manifest["stage"] not in SCIENTIFIC_STAGES:
        raise ContractError("Gate/smoke runs cannot be sealed as primary scientific evidence")
    validate_gate_chain(manifest, gates)
    run_dir = assert_namespace(run_dir, manifest["namespace"])
    bundle_dir = assert_namespace(bundle_dir, manifest["namespace"])
    merged = run_dir / "aggregate"
    marker = read_json(merged / "MERGED.json")
    if marker.get("binding") != manifest_binding(manifest) or marker.get("status") != "MERGED_VALID":
        raise ContractError("No valid merge for this execution fingerprint")
    _verify_inventory(merged, marker["artifact_hashes"], exclude={"MERGED.json"})
    aggregate = read_json(merged / "aggregate.json")
    if aggregate.get("binding") != manifest_binding(manifest) or aggregate.get("gate_reports_sha256") != canonical_hash(gates):
        raise ContractError("Aggregate provenance or gate report changed")
    if read_json(merged / "run_manifest.json") != manifest:
        raise ContractError("Sealing manifest is not the merged execution manifest")
    supplied = set(compact_artifacts)
    generated = {"reference_recipe.json", "run_manifest.json", "scientific_provenance.json"}
    if supplied != COMPACT_FILES - generated:
        raise ContractError(f"A complete compact bundle is required; expected {sorted(COMPACT_FILES - generated)}")
    total = 0
    for name, source in compact_artifacts.items():
        path = Path(source)
        if path.is_symlink() or not path.is_file():
            raise ContractError(f"Invalid compact artifact {name}")
        total += path.stat().st_size
        if name.endswith(".json"):
            value = read_json(path)
            validate_metric_names(value)
            if value.get("binding") != manifest_binding(manifest):
                raise ContractError(f"Compact {name} is not bound to this execution")
        else:
            with path.open(newline="", encoding="utf-8") as handle:
                reader = csv.DictReader(handle)
                if not reader.fieldnames or "run_fingerprint" not in reader.fieldnames:
                    raise ContractError(f"Compact {name} lacks provenance columns")
                validate_metric_names({field: None for field in reader.fieldnames})
                rows = list(reader)
                if not rows:
                    raise ContractError(f"Empty scientific summary cannot be sealed: {name}")
                if any(row.get("run_fingerprint") != manifest["run_fingerprint"] for row in rows):
                    raise ContractError(f"Compact {name} contains a different run")
                if any(row.get("status") in {"PENDING", "BLOCKED", "UNAVAILABLE", "PLACEHOLDER"} for row in rows):
                    raise ContractError(f"Unfinished evidence in {name}")
    if total > max_compact_bytes:
        raise ContractError("Compact artifact budget exceeded; raw trajectories do not belong in the sealed bundle")
    with writer_lock(bundle_dir.parent / f".{bundle_dir.name}.seal.lock"):
        if bundle_dir.exists():
            seal = read_json(bundle_dir / "SEALED.json")
            if seal.get("binding") != manifest_binding(manifest):
                raise ContractError("Existing seal has a different execution fingerprint")
            _verify_inventory(bundle_dir, seal["artifact_hashes"], exclude={"SEALED.json"})
            return seal
        temporary = Path(tempfile.mkdtemp(prefix=".seal-", dir=bundle_dir.parent))
        for name, source in compact_artifacts.items():
            shutil.copyfile(source, temporary / name)
        atomic_json(temporary / "reference_recipe.json", manifest["recipe"])
        atomic_json(temporary / "run_manifest.json", manifest)
        atomic_json(temporary / "scientific_provenance.json", {"binding": manifest_binding(manifest),
            "execution_git_sha": manifest["execution_git_sha"], "gate_reports": gates,
            "merged_sha256": file_hash(merged / "aggregate.json"),
            "scientific_claims_require_author_review": True})
        hashes = _inventory(temporary)
        (temporary / "SHA256SUMS").write_text("".join(f"{digest}  {name}\n" for name, digest in sorted(hashes.items())), encoding="utf-8")
        seal = {"status": "SEALED", "binding": manifest_binding(manifest),
                "artifact_hashes": _inventory(temporary), "raw_artifacts_included": False}
        atomic_json(temporary / "SEALED.json", seal)
        os.rename(temporary, bundle_dir)
        _fsync_dir(bundle_dir.parent)
        return seal
