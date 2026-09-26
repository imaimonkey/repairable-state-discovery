"""Shared runtime-state and approved-output path resolution for Generation 3.

The scientific design is tracked in the repository, while mutable readiness and
storage reservation state live outside the checkout.  Every runtime artifact is
addressed by a frozen logical namespace and resolved below the approved physical
storage root before it is created or read.
"""
from __future__ import annotations

import os
import subprocess
from pathlib import Path
from typing import Any, Mapping

from repairable_diffusion.src.v2r.schema import ContractError


DEFAULT_RUNTIME_STATE_ROOT = Path("/var/tmp/kimhj-rsd-ref-v3/runtime")
_LOGICAL_NAMESPACES = {
    "outputs/rsd_ref_v3": "outputs",
    "results/rsd_ref_v3": "results",
}


def runtime_state_root() -> Path:
    """Return the mutable runtime-state root, resolving the environment now."""
    raw = os.environ.get("RSD_RUNTIME_STATE_ROOT")
    return Path(raw).expanduser() if raw else DEFAULT_RUNTIME_STATE_ROOT


def storage_plan_path() -> Path:
    return runtime_state_root() / "storage_plan.json"


def readiness_path() -> Path:
    return runtime_state_root() / "execution_readiness.json"


def logical_run_root(config: Mapping[str, Any]) -> str:
    configured = config.get("paths", {}).get("run_root")
    if configured is None:
        configured = f"outputs/rsd_ref_v3/{config['run_name']}"
    return Path(str(configured)).as_posix()


def _approved_root(value: str | Path | Mapping[str, Any]) -> Path:
    if isinstance(value, Mapping):
        value = value.get("approved_output_root")
    if not isinstance(value, (str, Path)) or not str(value):
        raise ContractError("APPROVED_OUTPUT_ROOT_MISSING")
    root = Path(value).expanduser()
    if not root.is_absolute():
        raise ContractError("APPROVED_OUTPUT_ROOT_MUST_BE_ABSOLUTE")
    return root.resolve(strict=False)


def _is_relative_to(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def resolve_logical_artifact(logical_path: str | Path, approved_root: str | Path | Mapping[str, Any]) -> Path:
    """Resolve a Gen3 logical output/result path below the approved root.

    The namespace is checked lexically before filesystem resolution, then the
    resolved physical path is checked again.  This rejects ``..`` traversal and
    symlink escapes without relying on a symlinked repo output directory.
    """
    logical = Path(logical_path)
    if logical.is_absolute() or any(part in {"", ".", ".."} for part in logical.parts):
        raise ContractError(f"INVALID_LOGICAL_ARTIFACT_PATH: {logical_path}")
    parts = logical.parts
    namespace = "/".join(parts[:2]) if len(parts) >= 2 else ""
    if namespace not in _LOGICAL_NAMESPACES or len(parts) < 3:
        raise ContractError(f"UNSUPPORTED_LOGICAL_ARTIFACT_NAMESPACE: {logical_path}")
    root = _approved_root(approved_root)
    physical = (root.joinpath(*parts[2:])).resolve(strict=False)
    if not _is_relative_to(physical, root):
        raise ContractError(f"PHYSICAL_PATH_ESCAPES_APPROVED_ROOT: {logical_path}")
    return physical


def _existing_parent(path: Path) -> Path:
    candidate = path
    while not candidate.exists() and candidate != candidate.parent:
        candidate = candidate.parent
    return candidate


def filesystem_identity(path: str | Path) -> dict[str, Any]:
    """Return the device and mount carrying ``path`` without creating it."""
    resolved = Path(path).resolve(strict=False)
    existing = _existing_parent(resolved)
    stat = os.stat(existing)
    mount = f"device:{stat.st_dev}"
    try:
        result = subprocess.run(
            ["df", "-P", str(existing)],
            text=True,
            capture_output=True,
            check=False,
        )
        lines = [line for line in result.stdout.splitlines() if line.strip()]
        if len(lines) >= 2:
            fields = lines[-1].split()
            if fields:
                mount = fields[-1]
    except OSError:
        pass
    return {"filesystem_device": int(stat.st_dev), "filesystem_mount": mount}


def runtime_location(logical_path: str | Path, storage: Mapping[str, Any] | str | Path) -> dict[str, Any]:
    """Return auditable logical/physical location and filesystem provenance."""
    root = _approved_root(storage)
    physical = resolve_logical_artifact(logical_path, root)
    identity = filesystem_identity(physical)
    return {
        "logical_path": Path(logical_path).as_posix(),
        "physical_path": str(physical),
        "approved_output_root": str(root),
        **identity,
        "filesystem_device_or_mount": f"{identity['filesystem_device']}:{identity['filesystem_mount']}",
    }


def approved_root_is_valid(value: str | Path | Mapping[str, Any]) -> bool:
    try:
        root = _approved_root(value)
    except ContractError:
        return False
    return "rsd_ref_v3" in root.parts
