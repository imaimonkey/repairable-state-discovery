# Legacy job final disposition

The pre-cancellation forensic snapshot is `status/rsd/job_inventory.json`. It contains the requested job id, name, state, node/GPU, workdir, command/config, legacy SHA, output, purpose, last progress, artifact status, and disposition.

- **Safe to cancel after snapshot:** 53067, 53069, 53070, 53071, 53072, 53073, 53074. All were never started and were held/requeued server1 temporal jobs.
- **Safe to cancel after snapshot:** 53267, 53268, 53275. All were pending legacy MBPP/Dream/MATH jobs with no artifact or elapsed runtime.
- **Finish legacy:** 53262. It was actively using GPU 100% and had a recoverable GSM8K trajectory bank, but no final report. It was excluded from cancellation.
- **Already terminated before the Phase 2B cancellation step:** 53266, cancelled at 2026-09-26T21:24:59+09:00 by the job owner as recorded by sacct. Its partial BBH logical7 trajectory and manifest were preserved; no artifact was deleted.

Only the exact pending/held ids listed above are eligible for cancellation. No other user's job, source, model cache, manifest, sealed artifact, or unknown path is in scope.

The exact cancellation was executed at 2026-09-26T21:34:28+09:00. `sacct` confirmed all ten authorized ids terminal as `CANCELLED by 1021`; `squeue -u kimhj` then showed only 53262 remaining. Artifact deletion count was zero.
