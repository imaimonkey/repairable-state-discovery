# Phase 2B environment fingerprint report

The per-server machine-readable fingerprints are in `status/rsd/environment/server{1..4}.json`; the cross-server comparison matrix is `status/rsd/environment_matrix.json`. The raw selected-environment package captures are `status/rsd/environment/server{1..3}_pip_freeze.txt`.

server1, server2, and server3 expose the same core package tuple but not the same full environment. Valid raw `uv pip freeze --python` hashes are server1 `b9702acf…`, server2 `0c1b5715…`, and server3 `7f56c41d…`; the prior empty SHA was invalid and has been removed from the evidence. Their GPUs differ materially (A6000/A6000/H200), so this is not a scientific equivalence proof.

The model revision is resolved to `08b83a6feb34df1a6011b80c3c00c7563e963b07`; config and tokenizer file hashes are identical on server1–3. MATH-500 is pinned to `6e4ed1a2a79af7d8630a6b768ec859cb5af4d3be`, GSM8K to `740312add88f781978c0658806c59bc2815b9866`, with fixed calibration content hashes recorded in each JSON fingerprint.

flash-attn is not installed and is explicitly `NOT_USED`; PyTorch SDPA flags and TF32/matmul/determinism settings are recorded. server4 is an RTX PRO 6000 Blackwell Server Edition with an otherwise bare system Python: torch, transformers, accelerate, numpy, and tokenizers were unavailable. Its SM120/backend compatibility is therefore `UNKNOWN`, not assumed compatible.

server1 then passed the real-model local GPU qualification: MATH-500 R2 over 32 fixed items and two seed scenarios produced exact final tokens, final text, answers, correctness, schedule, NFE, RNG, and snapshot-grid checks. This establishes `SCIENTIFIC_EXECUTION_QUALIFIED` for server1 only; it does not establish cross-server equivalence or storage readiness. The R2 evidence is summarized in `status/rsd/gpu_calibration_manifest.json`.
