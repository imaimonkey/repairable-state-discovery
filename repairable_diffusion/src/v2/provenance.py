from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping


def canonical_json(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: str | Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        while True:
            chunk = fh.read(1024 * 1024)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def config_sha256(cfg: Mapping[str, Any]) -> str:
    return sha256_text(canonical_json(dict(cfg)))


def scientific_fingerprint(payload: Mapping[str, Any]) -> str:
    """Hash only explicitly declared scientific provenance fields.

    Callers should construct `payload` from the required fields in the V2
    measurement contract. Runtime/logging paths must not be included.
    """

    return sha256_text(canonical_json(dict(payload)))


def assert_fingerprint_match(expected: str, observed: str, *, artifact: str) -> None:
    if expected != observed:
        raise RuntimeError(
            f"stale or incompatible V2 artifact: {artifact}; "
            f"expected fingerprint={expected}, observed={observed}"
        )
