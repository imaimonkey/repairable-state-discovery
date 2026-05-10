from __future__ import annotations

import unittest
from types import SimpleNamespace

from repairable_diffusion.src.backends.dream import DreamBackend


def _backend(
    *,
    model_mask_token_id=None,
    model_pad_token_id=None,
    tokenizer_mask_token_id=None,
    tokenizer_pad_token_id=None,
    tokenizer_eos_token_id=None,
) -> DreamBackend:
    backend = object.__new__(DreamBackend)
    backend.model = SimpleNamespace(
        generation_config=SimpleNamespace(
            mask_token_id=model_mask_token_id,
            pad_token_id=model_pad_token_id,
        )
    )
    backend.tokenizer = SimpleNamespace(
        mask_token_id=tokenizer_mask_token_id,
        pad_token_id=tokenizer_pad_token_id,
        eos_token_id=tokenizer_eos_token_id,
    )
    return backend


class DreamBackendTokenTests(unittest.TestCase):
    def test_mask_token_falls_back_to_generation_config(self) -> None:
        backend = _backend(model_mask_token_id=None, tokenizer_mask_token_id=None)

        self.assertEqual(backend._mask_token_id({"mask_id": 126336}), 126336)

    def test_mask_token_prefers_model_generation_config(self) -> None:
        backend = _backend(model_mask_token_id=7, tokenizer_mask_token_id=9)

        self.assertEqual(backend._mask_token_id({"mask_id": 126336}), 7)

    def test_mask_token_uses_tokenizer_after_config(self) -> None:
        backend = _backend(model_mask_token_id=None, tokenizer_mask_token_id=42)

        self.assertEqual(backend._mask_token_id({}), 42)

    def test_missing_mask_token_has_actionable_error(self) -> None:
        backend = _backend()

        with self.assertRaisesRegex(ValueError, "generation.mask_id"):
            backend._mask_token_id({})

    def test_pad_token_falls_back_to_tokenizer_eos(self) -> None:
        backend = _backend(model_pad_token_id=None, tokenizer_pad_token_id=None, tokenizer_eos_token_id=2)

        self.assertEqual(backend._pad_token_id(), 2)


if __name__ == "__main__":
    unittest.main()
