# Canonical Build Plan

This is a planning document. No live worktree is merged, reset, overwritten, redirected, or used to launch a new scientific job by this correction.

## Two distinct bases

### Historical clean ancestor

`0dd161c8cf4bf3e7dbe4042234a0954950ce870e` (`origin/main`) is the clean V2 ancestor and remains the comparison anchor. It is useful for auditing provenance and for understanding the pre-reference state, but it is not the preferred scientific reconstruction point.

### Preferred canonical scientific source base

`78fe5d7c1829b67d1bb1416b7205edfa647bb2fa` is exactly 18 commits ahead of `0dd161c8…` and is the frozen execution SHA bound to the sealed reference evidence. Its scientific portion contains source-pinned recipes, R0/R1/R2 gates, V2R schema/science/seeds, reference sampling and snapshot/replay semantics, shard planning/worker/merge, artifact handling, and the associated CPU/contract/pipeline tests.

**Decision: use `78fe5d7c…` as the preferred canonical scientific source base for Phase 2.** This correction does not yet create the Phase 2 canonical branch.

## Base-choice comparison

| Choice | Evidence continuity | Dependency risk | Decision |
|---|---|---|---|
| A: rebuild selected scientific commits from `0dd161c…` | lower; sealed evidence was produced by a later combined tree | high; a missing gate, seed, sampler, schema, shard, or sealing dependency could invalidate replay | historical/porting reference only |
| B: start from `78fe5d7…`, then remove/archive deadline/status state and neutralize runtime | high; sealed MATH/GSM reference evidence is tied to this execution SHA | lower for scientific dependencies; still requires deliberate runtime refactor and tests | **preferred** |

The `0dd→78fe` diff is 62 files and 7,896 added lines. The scientific subset is valuable; the same diff also contains paper/deadline documents, status snapshots, historical cancellation records, and named monitor/orchestrator state. Therefore the plan is “B plus separation,” not a blind merge of the whole tree.

## Changes to keep from `78fe5d7…`

Port or retain in an isolated clean Phase 2 worktree:

1. `repairable_diffusion/src/v2r/{schema,seeds,reference_sources,reference_sampler,reference_gates,science,planning,artifacts}.py`.
2. `tests/test_v2r_pipeline.py`, `tests/test_v2r_reference_cpu.py`, and the V2 contract tests, after adapting fixture paths.
3. Source-pinned reference recipe and model-code-hash records required to reproduce the sealed execution.
4. V2 provenance freeze, Dream terminal boundary behavior, and the associated tests already in the `78fe` ancestry.
5. Atomic writes, writer locks, immutable shard planning, exact replay/continue state, strict merge, compact sealing, and manifest-to-execution-SHA binding.

Do not re-cherry-pick `14c5a4a28`, `baefbe775`, `8b1361d3d`, or `435e24ea1` on top of `78fe`; they are already ancestors of the preferred base.

## Changes to reimplement or neutralize

- `v2r_unified_monitor.py`: keep Slurm/GPU/filesystem/job-manifest observation, but remove named-deadline branches, paper state, legacy job assumptions, and hardcoded historical worktree names.
- `v2r_watchdog.py`: keep liveness checks, but use a neutral service identity and explicit ownership; do not auto-start the old named tmux session.
- `v2r_orchestrator.py`, `v2r_submit.py`, and dispatch: retain gate-aware dependencies and single-writer rules, but make job families/configs declarative and source-pinned.
- `v2r_status.py`: split scientific status from paper/deadline status and make scheduler state authoritative when monitor state drifts.
- Historical cancellation/reallocation logic: retain as read-only evidence only; never replay it automatically.
- New Slurm submission names and stdout/stderr names must remain neutral and contain no conference/deadline identifiers.

## Changes to archive from canonical source

- `docs/V2R_FINAL_MASTER_REQUEST_20260923.md`, full-reset/deadline documents, paper branches, PDF audits, submission bundles, author-review state, and deadline priority files;
- `status/v2r/*` snapshots, legacy reset/cancellation records, monitor histories, and dynamic operational state;
- `iclr2027-*` monitor/watchdog names and status loops;
- analysis/handoff branches and generated result bundles;
- V1/server2 legacy worktrees and old pilot scripts, while preserving them as read-only reproduction inputs.

Archive does not mean delete. Preserve Git refs, checksums, manifests, and source lineage.

## Changes to discard from the canonical source

The following are not carried into a clean canonical runtime unless a later audit proves they are generic and required:

- untracked generated configs/results with no manifest lineage;
- duplicate status writes and monitor loops that disagree with Slurm;
- automatic cancellation/reallocation policy inherited from a historical deadline;
- conference/deadline-specific job names, stdout/stderr names, and paper state transitions;
- source changes that cannot be tied to a commit, test, manifest, or artifact lineage.

This is a source-disposition decision only. No such files are deleted in this correction.

## Phase 2 entry gates

Do not create the canonical execution worktree or launch new primary raw trajectory jobs until all of the following are true:

- the `78fe5d7…` scientific base is checked out in a clean, separately named worktree;
- the server2 fingerprint is archived and confirms no server2-only scientific fix is being lost;
- held server1 jobs are snapshot-classified rather than treated as scientific dependencies;
- old V2 jobs have explicit legacy dispositions;
- scientific, operational/status, paper/artifact, and uncommitted overlays are separated;
- each selected primary pool has an explicitly approved output filesystem with at least `max(200 GiB, 3 × projected maximum single-shard raw output)` free, at least 10% free inodes, and a retention/archive plan;
- source-pinned unit/CPU/reference-gate tests pass before any new GPU execution.

Current storage state fails the output reservation gate: observed free space is approximately 204G on server1 `/mnt/raid5`, 19G on server2 `/`, 116G on server3 `/data`, and 83G on server4 `/data`, with 95–99% utilization. No raw output should be submitted to these paths until an approved reservation exists.

## Unresolved risks

1. The frozen `78fe` scientific source is the preferred base, but its deadline/status files must be separated without changing the source identity attached to sealed evidence.
2. Backend/validator differences between the older `0dd` baseline and later unified/provenance variants still require behavioral tests; the `78fe` versions are the evidence-continuous candidates.
3. Current legacy jobs may finish or advance while this document is static; scheduler state must be re-queried before any approval for cancellation.
4. Nearly full filesystems can invalidate a long run independently of source correctness.

## Exact Phase 1 exit state

```text
reconciliation branch: codex/repairable-state-reconciliation-20260926
historical ancestor:   0dd161c8cf4bf3e7dbe4042234a0954950ce870e
preferred science:     78fe5d7c1829b67d1bb1416b7205edfa647bb2fa
phase:                  Phase 1 correction complete; Phase 2 not started
execution:              no scientific jobs launched or modified by reconciliation
artifacts:              existing artifacts retained in place; no raw copy or rewrite
```

The next phase may create a separate clean worktree from `78fe5d7…`, archive/remove only derived deadline/status state in that new worktree, implement a neutral runtime, and run source-pinned tests. It must not modify the live execution/reference worktrees.
