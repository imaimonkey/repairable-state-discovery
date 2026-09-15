import torch

from repairable_diffusion.src.backends.dream import (
    _chunked_entropy_from_logits,
    _chunked_token_probabilities,
)


def test_chunked_token_probabilities_match_dense_softmax():
    torch.manual_seed(7)
    logits = torch.randn(5, 23, dtype=torch.float32)
    token_ids = torch.tensor([0, 3, 7, 12, 22], dtype=torch.long)

    expected = torch.softmax(logits, dim=-1).gather(-1, token_ids.unsqueeze(-1)).squeeze(-1)
    actual = _chunked_token_probabilities(logits, token_ids, chunk_size=5)

    torch.testing.assert_close(actual, expected, rtol=1e-5, atol=1e-6)


def test_chunked_entropy_matches_dense_softmax():
    torch.manual_seed(11)
    logits = torch.randn(4, 29, dtype=torch.float32)

    probs = torch.softmax(logits, dim=-1)
    expected = -(probs * torch.log(probs.clamp_min(1e-12))).sum(dim=-1)
    actual = _chunked_entropy_from_logits(logits, chunk_size=7)

    torch.testing.assert_close(actual, expected, rtol=1e-5, atol=1e-6)


def test_chunked_helpers_accept_bfloat16_without_full_precision_output():
    torch.manual_seed(19)
    logits = torch.randn(3, 17, dtype=torch.float32).to(torch.bfloat16)
    token_ids = torch.tensor([1, 5, 16], dtype=torch.long)

    probs = _chunked_token_probabilities(logits, token_ids, chunk_size=4)
    entropy = _chunked_entropy_from_logits(logits, chunk_size=4)

    assert probs.dtype == torch.float32
    assert entropy.dtype == torch.float32
    assert torch.isfinite(probs).all()
    assert torch.isfinite(entropy).all()
