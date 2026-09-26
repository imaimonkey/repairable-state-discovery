# Execution Worktree Policy

## Worktree roles

1. **Canonical source worktree**: derived from `78fe5d7…`; clean, tested, and immutable after source freeze.
2. **Execution worktree**: a separate checkout at the frozen canonical SHA; no uncommitted source changes; only approved V2 output namespaces.
3. **Reference/evidence worktrees**: historical or sealed evidence; read-only from this branch.
4. **Operational state**: `status/reset/`, scheduler records, and service health; never treated as scientific source.

The live reference and existing measurement worktrees must not be reset, overwritten, rebased, or synchronized from this branch.

## Submission invariants

Every authorized task must record source SHA, normalized config hash, recipe/model/source hashes, dataset identity, seed registry, output namespace, and writer identity. A dirty tree or SHA mismatch fails closed.

New scheduler jobs must use neutral `rsd-*` names and `rsd-%j.out`/`rsd-%j.err` paths. No historical project, venue, paper, or deadline identifier is allowed in new scheduler metadata.

## Authority boundaries

- Monitor: read-only observation, drift detection, and status writes.
- Orchestrator: only component allowed to transition an explicitly authorized task toward execution.
- Watchdog: service liveness and restart; it does not decide scientific work and does not cancel jobs.
- Slurm: authoritative job state. Cached monitor state is advisory and conflicts become `MONITOR_DRIFT`.

## Phase gates

Phase 2A may compile and test the source without GPU execution. Phase 2B requires an approved output filesystem, reserved free space, inode margin, environment fingerprint, clean deployment of the exact SHA on all selected servers, and cross-server equivalence checks.
