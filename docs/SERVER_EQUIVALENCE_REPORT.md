# Phase 2B server equivalence report

The local deterministic gate ran against the new canonical detached worktree and selected research venv on server1, server2, and server3: 7/7 tests passed on each. The checks cover token IDs, deterministic text/evaluator contract, NFE/schedule mapping, snapshot restore state identity, seed pairing, and native-versus-instrumented replay on a CPU fixture.

This is intentionally a small contract gate, not a full benchmark. GPU exact replay and cross-server calibration were not run: server2 could not allocate a GPU (`Requested nodes are busy`), server3 GPUs were occupied by legacy jobs, server4 lacks the research stack, and the storage gate failed. Accordingly, server1/2/3 are `AUXILIARY_ONLY`, server4 is `UNKNOWN`, and no server is `PRIMARY_POOLABLE_EXACT` or `PRIMARY_POOLABLE_VALIDATED`.

The old server1 temporal jobs are forensic-only. The server2 legacy source was not used; its canonical detached worktree was used for the CPU gate.
