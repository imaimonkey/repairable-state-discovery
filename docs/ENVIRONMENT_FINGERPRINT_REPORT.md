# Phase 2B environment fingerprint report

The per-server machine-readable fingerprints are in `status/rsd/environment/server{1..4}.json`; the cross-server comparison matrix is `status/rsd/environment_matrix.json`.

server1, server2, and server3 expose the same selected research venv package tuple and pip-freeze hash: Python 3.11, torch 2.1.2+cu121, transformers 4.49.0, accelerate 0.34.2, numpy 1.26.4, tokenizers 0.21.1, hash `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. Their GPUs differ materially (A6000/A6000/H200), so this is not a scientific equivalence proof.

server4 is an RTX PRO 6000 Blackwell Server Edition with an otherwise bare system Python: torch, transformers, accelerate, numpy, and tokenizers were unavailable. Its SM120/backend compatibility is therefore `UNKNOWN`, not assumed compatible.

The model identity observed in existing manifests is `GSAI-ML/LLaDA-8B-Instruct`, revision `default`. Dataset cache identity and flash-attention package identity were not safely comparable in this pass and remain explicitly unknown.
