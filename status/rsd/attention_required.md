# Phase 2B attention required

- **Storage gate is FAIL on all four servers.** The measured mounts are at 95–99% use and no explicit reservation exists. The projection is based on observed pilot/full artifact bytes rather than an assumed 200 GiB, but model/cache and the unmeasured MBPP/Dream portions remain outside the estimate.
- **Scientific qualification and equivalence are separate.** server1 passed the real-model local GPU R2 gate and is `SCIENTIFIC_EXECUTION_QUALIFIED`, but its equivalence group is only `SINGLE_SERVER_ONLY`; server2/3 have not had GPU qualification and server4 is `UNKNOWN` because it is Blackwell/SM120 with no research Python stack.
- **No server is `PRIMARY_POOLABLE_*`.** Cross-server GPU equivalence has not been measured, and full-run storage remains `STORAGE_NOT_RESERVED` on every server.
- **Legacy server1 temporal replay failed to become a usable replay.** Jobs 53067, 53069–53074 were never started and are retained only for forensic evidence until the pre-cancel snapshot is closed.
- **53262 is intentionally preserved as `FINISH_LEGACY`.** It is using the old SHA 926495e and actively consumes a GPU; it has a recoverable trajectory bank but no final report yet.
- **53266 terminated before this Phase 2B cancellation step.** Its partial trajectory and manifest remain preserved; no deletion is authorized.
- **Phase 3/full scientific matrix must not start.** The remaining blockers are the full-run storage reservation and cross-server equivalence if pooled execution is required; server1's local scientific qualification does not waive either gate.
