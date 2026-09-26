# Canonical Build Plan

This is a planning document. No live worktree is merged, reset, overwritten, or redirected by this file.

## Canonical base SHA

**Base:** `0dd161c8cf4bf3e7dbe4042234a0954950ce870e` (`origin/main`).

Reason: it is the clean remote-tracking V2 baseline observed in the shared clone and is the common base for the clean V2 execution checkouts. It is a source anchor, not a claim that every historical artifact was produced from it.

## Changes to keep or port

Port in isolated commits, with tests and manifest fixtures after each step:

1. V2 provenance freeze and boundary fixes from `435e24ea1` and its tested predecessors `14c5a4a28`, `baefbe775`, and `8b1361d3d`.
2. V2R schema, canonical seed registry/collision audit, source-pinned reference sources, native sampler, exact snapshot/replay semantics, and reference gates from the `45c295f…` family.
3. Immutable shard planning, item-level completion, single-writer/atomic writes, strict merge, stage-aware reduction, and compact sealing from the V2R artifact/planning families.
4. Model code hashes/cache isolation and execution-manifest binding.
5. Only the generic parts of scheduler observation, dispatch, worker, and watchdog behavior. Every submission must carry source SHA, config/recipe hash, dataset/source hash, seed registry version, output namespace, and writer identity.

## Changes to reimplement, not blindly cherry-pick

- `v2r_unified_monitor.py`: retain Slurm/GPU/filesystem/job-manifest observation, but remove named-deadline branches, paper state, legacy job assumptions, and hardcoded historical worktree names.
- `v2r_watchdog.py`: retain liveness checks, but use a neutral service identity and explicit ownership; do not auto-start the old named tmux session.
- `v2r_orchestrator.py`/dispatch: retain gate-aware dependency handling and single-writer rules, but make job families/configs declarative and source-pinned.
- Legacy-job recovery/cancellation logic: convert to a read-only historical report first; no implicit cancellation.
- `v2r_status.py` and submission wrappers: split scientific status from paper/deadline status and prohibit conference/deadline identifiers in new Slurm job names or stdout/stderr names.

## Changes to archive from canonical source

- paper branches, PDF audit, submission bundles, author-review status, named-deadline docs, and deadline priority files;
- historical `iclr2027-*` monitor/watchdog names and status loops;
- analysis/handoff branches and generated result bundles;
- legacy V1 worktrees and old pilot scripts, while preserving them as read-only reproduction inputs.

Archive does not mean delete. Preserve Git refs, checksums, manifests, and source lineage.

## Changes to discard from the canonical source

The following are not carried into a clean canonical runtime unless a later audit proves they are generic and required:

- untracked generated configs/results with no manifest lineage;
- duplicate status writes and monitor loops that disagree with Slurm;
- automatic cancellation/reallocation policy inherited from a historical deadline;
- conference/deadline-specific job names, stdout/stderr names, and paper state transitions;
- source changes that cannot be tied to a commit, test, manifest, or artifact lineage.

This is a source-disposition decision only; no such files are deleted in Phase 1.

## Unresolved conflicts and blockers

1. Baseline and unified/provenance variants differ in `v2/backends.py` and `validate_v2_backends.py`; the provenance branch also differs in `run_measurement.py`. Behavioral tests and artifact lineage must decide the canonical implementation.
2. The live V2R reference worktree is dynamically changing; its exact development HEAD is not a stable source anchor. Use the recorded execution SHA `78fe5d7…` for evidence and capture a fresh clean export before porting.
3. server2’s main directory is not a Git repository, so its exact source identity is unresolved.
4. Current V2 measurement jobs 53262, 53266, 53267, 53268, and 53275 have incomplete or queued evidence; no result should be promoted until final reports and manifests agree.
5. Nearly full filesystems constrain copying and may affect future runs; storage reservation is a prerequisite for any new execution.
6. Existing monitors report drift relative to Slurm; scheduler state remains authoritative until a neutral monitor is verified.

## Exact canonical source state at Phase 1 exit

The exact reproducible starting state is:

```text
repository: repairable-state-discovery
base:       origin/main
commit:     0dd161c8cf4bf3e7dbe4042234a0954950ce870e
tree:       clean at the new reconciliation worktree
execution:  no jobs launched or modified by reconciliation
artifacts:  existing artifacts retained in place; not copied or rewritten
```

The next implementation phase must create a second clean worktree from this SHA, apply the kept commits in an auditable order, run unit/CPU/reference-gate tests, and only then compare against sealed artifacts. It must not modify the live execution or reference worktrees.
