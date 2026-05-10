from __future__ import annotations

from typing import Any

from repairable_diffusion.src.backends.dream import DreamBackend
from repairable_diffusion.src.backends.rfba_llada import RFBALLADABackend
from repairable_diffusion.src.backends.transformers_causal import TransformersCausalBackend


def create_backend(backend_cfg: dict[str, Any]):
    backend_type = backend_cfg["type"]
    if backend_type == "rfba_llada":
        return RFBALLADABackend(backend_cfg)
    if backend_type == "dream":
        return DreamBackend(backend_cfg)
    if backend_type == "transformers_causal":
        return TransformersCausalBackend(backend_cfg)
    raise ValueError(f"Unsupported backend.type: {backend_type}")
