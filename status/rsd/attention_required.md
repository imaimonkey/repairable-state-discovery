# Phase 2B attention required

- **Storage gate is FAIL on all four servers.** The measured mounts are at 95–99% use and no explicit reservation exists. The projection is based on observed pilot/full artifact bytes rather than an assumed 200 GiB, but model/cache and the unmeasured MBPP/Dream portions remain outside the estimate.
- **No server is `PRIMARY_POOLABLE_*`.** server1/2/3 pass the small CPU exact replay/instrumentation fixture (7/7) but have no GPU exact/cross-server proof. server4 is `UNKNOWN` because it is Blackwell/SM120 with no research Python stack.
- **Legacy server1 temporal replay failed to become a usable replay.** Jobs 53067, 53069–53074 were never started and are retained only for forensic evidence until the pre-cancel snapshot is closed.
- **53262 is intentionally preserved as `FINISH_LEGACY`.** It is using the old SHA 926495e and actively consumes a GPU; it has a recoverable trajectory bank but no final report yet.
- **53266 terminated before this Phase 2B cancellation step.** Its partial trajectory and manifest remain preserved; no deletion is authorized.
- **Phase 3 must not start.** The blocking condition is the conjunction of `STORAGE_FAIL` and `NONE_QUALIFIED` poolability.
