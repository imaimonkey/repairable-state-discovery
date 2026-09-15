# Dream memory fix complete — 2026-09-15

The Dream-v0-Instruct-7B follow-up failed in trajectory collection job `47521` with CUDA OOM. Existing LLaDA/MATH-500 claim-bearing results remain unchanged.

The Dream backend was changed without reducing the scientific protocol: generation/repair loops now run under `torch.inference_mode()`, diagnostic current-token probabilities are computed only at required non-prompt positions, and diagnostic probability/entropy reductions use chunked float32 vocabulary reductions instead of materializing full-vocabulary FP32 softmax tensors.

Implementation commit: `4241ec37371dcc6cecf122a7da49eb0461e7c75f`.

A dedicated `dream-memory-ci` regression compares the chunked probability and entropy calculations against dense softmax on CPU tensors, including bfloat16 inputs. That CI passed on branch head `6fa95b24725b24cce90a8ef26eecc59c534ef93e`; the existing unbiased-evaluation CI also remains green.

The corrected full Dream experiment must use the same benchmark/protocol settings as the failed run and a fresh output directory. The previous partial run remains failure provenance and must not be aggregated as a scientific result.
