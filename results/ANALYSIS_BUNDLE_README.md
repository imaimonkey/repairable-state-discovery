# ICLR 2027 Repairable-State-Discovery analysis bundle

This branch is an operational observation and compact-artifact bundle for
independent analysis of the distributed V2 execution state as of
2026-09-23 KST.

## Included

- `status/`: read-only Slurm, repository, experiment-matrix, aggregate-readiness,
  and artifact-index snapshots.
- `results/v2_artifacts/v2_bbh_logical7_llada_50753/`: completed and sealed
  LLaDA BBH logical7 result artifacts.
- `results/v2_artifacts/v2_mbpp_llada_50754/`: completed and sealed LLaDA
  MBPP result artifacts.
- `results/v2_artifacts/v2_math500_dream_50923/`: completed and sealed Dream
  MATH-500 compact artifacts, including the existing per-run analysis.
- `results/v2_forensics/v2_bbh_logical5_50752/`: BBH logical5 forensic index,
  shard plan, and the completed shard-00 event/summary files.
- `results/analysis_bundle_manifest.json`: per-run inclusion and exclusion
  rules, provenance, and known limitations.

## Important interpretation rules

- This is **not** the final V2 aggregate. No aggregate was created here.
- `0dd161c8...` LLaDA runs and `8b1361d3...` Dream-hotfix runs are separate
  execution generations and must retain their per-run SHA provenance.
- `50752` is failed and remains excluded; the included forensic files do not
  establish a scientific result or root cause.
- Active jobs `50668`, `50669`, and `50924` were not copied or modified. Their
  server-side paths and status are recorded in `status/`.
- `trajectories.pkl`, logs, model weights, and other large/raw execution files
  are intentionally excluded. Their checksums were not recomputed here.
- Legacy jobs and historical V1/full-paper artifacts are indexed separately
  and must not be mixed into the frozen V2 matrix.

Use `SHA256SUMS` files inside each compact artifact directory to verify the
copied files. The status snapshots are observational metadata, not a claim
that all eight V2 rows are complete.
