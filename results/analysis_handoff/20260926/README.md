# Repairable State Discovery — Analysis Handoff (2026-09-26)

This directory is a compact, GitHub-friendly handoff for Codex Desktop or another
reviewer to analyze the experiment state without access to the cluster filesystems.
It contains small, provenance-bearing summaries rather than raw trajectory banks.

## What is included

### `current/`

- Legacy V2 measurement aggregate, Tables 1–3, job/final manifests, execution
  collection manifest, and readiness stamps.
- V2R reference-primary status, gate, provenance, paper-readiness, dispatch, and
  shard snapshots.

The legacy V2 matrix is intentionally preserved as partial: the 2026-09-26
aggregate has only `v2_bbh_logical3_llada` completed, seven runs missing, and
`tier_a_complete: false`. Do not interpret it as a complete full-suite result.

The V2R reference-primary status is a separate scientific generation. Its sealed
reference runs and validated Dream auxiliary lanes must not be numerically pooled
with the legacy V2 measurement rows.

### `analyses/`

- Server 3 exact-reference analysis.
- Server 2/4 independent-lane analysis.
- Historical V1/old-environment MATH-500 and GSM8K reports.
- Historical V2 pilot, breadth, Dream, and seed-collision reports.

## Evidence boundary

The strongest current scientific evidence is the V2R reference-primary material:

- Server 3: LLaDA MATH-500/GSM8K reference baselines plus MATH core/temporal
  sealed bundles; all declared R0/R1/R2 gates pass.
- Server 2/4: independent supporting lanes with `MERGED_VALID` artifacts and
  declared gates passing; these are not full rerun reproducibility evidence and
  must not be silently pooled with Server 3 exact-reference evidence.
- Server 1: no authoritative consolidated aggregate is included here; the latest
  dispatch snapshot marks it reference-incompatible due to exact-native-replay
  failure. Do not use it as primary evidence.

The historical V1 reports are development/history artifacts. They used a limited
200-item slice, eight trajectories per item, and the old RFBA/LLaDA pipeline. The
old V2 pilot reports use the older `0dd161c` implementation and are retained to
document the baseline/reproducibility problem, not as final-paper evidence.

## Raw artifact policy

Raw `trajectories.pkl`, branch `jsonl`, model caches, and cluster-local logs remain
on the original execution filesystems and are not copied into this Git handoff.
They are large (the relevant checkouts are approximately 1–1.7 GB) and are already
excluded by the repository ignore rules. The included manifests and reports retain
the execution SHA, configuration hashes, job IDs, artifact hashes where available,
and source paths needed to locate or audit the raw artifacts.

## Source checkouts

- Active V2 checkout: `/home/kimhj/repairable-state-discovery-v2-exec`
- Latest legacy V2 execution checkout: `/data/kimhj/repairable-state-discovery-v2-exec-20260925`
- V2R reference-primary checkout: `/data/kimhj/repairable-state-discovery-reference-20260923`
- Historical forensic checkout: `/data/kimhj/repairable-state-discovery-seed-forensic-20260923`

This handoff is an analysis snapshot, not a claim that all queued Slurm jobs are
complete. Read `current/v2r_current_status.json`,
`current/v2r_paper_readiness.json`, and
`current/v2_measurement_final_execution_manifest.json` first.
