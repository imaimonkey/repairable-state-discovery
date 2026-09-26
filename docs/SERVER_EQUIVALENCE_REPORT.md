# Phase 2B server equivalence report

The local deterministic gate ran against the new canonical detached worktree and selected research venv on server1, server2, and server3: 7/7 tests passed on each. The checks cover token IDs, deterministic text/evaluator contract, NFE/schedule mapping, snapshot restore state identity, seed pairing, and native-versus-instrumented replay on a CPU fixture. In addition, server1 completed a real-model MATH-500 R2 GPU calibration: 32 fixed items × two seed scenarios, with native/instrumented replay and snapshot continuation checks.

The server1 R2 gate passed exact final tokens, final text, answer, correctness, schedule, NFE, RNG, and snapshot-grid checks. Therefore server1 is `SCIENTIFIC_EXECUTION_QUALIFIED` for local execution and its equivalence axis is `SINGLE_SERVER_ONLY`. This is not a cross-server equivalence result: server2 could not allocate a GPU (`Requested nodes are busy`), server3 GPUs were occupied by legacy jobs, and server4 lacks the research stack/Blackwell compatibility proof. No server is `PRIMARY_POOLABLE_EXACT` or `PRIMARY_POOLABLE_VALIDATED`; server1 remains auxiliary-only for pooled execution.

The calibration is intentionally not a full benchmark and does not authorize raw/confirmatory runs. Full-run storage remains a separate `STORAGE_NOT_RESERVED` gate.

The old server1 temporal jobs are forensic-only. The server2 legacy source was not used; its canonical detached worktree was used for the CPU gate.
