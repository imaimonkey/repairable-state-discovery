# Canonical Repository State

Status: Phase 2A source build. No new GPU job or raw trajectory execution is authorized by this branch.

## Source identity

| Role | SHA / reference |
|---|---|
| Preferred canonical scientific source | `78fe5d7c1829b67d1bb1416b7205edfa647bb2fa` |
| Historical clean ancestor | `0dd161c8cf4bf3e7dbe4042234a0954950ce870e` |
| Phase 1 reconciliation input | `d8b07b09850ba208920a299193886bf9001cf093` |
| Phase 2A branch | `codex/repairable-state-canonical-reset` |
| Phase 2A runtime commit | `227cbcc99c7edfac83de7f34c452db7defd5bdcb` |

The preferred source is the frozen execution SHA bound to sealed reference evidence. The historical ancestor is retained for comparison; its descendants are not re-cherry-picked onto the preferred base.

## Scientific core retained

The canonical runtime retains the V2R schema, seed registry/collision checks, source-pinned reference sources, native sampler, reference gates, scientific execution semantics, deterministic planning, atomic/single-writer artifacts, strict merge, and sealing code under `repairable_diffusion/src/v2r/`.

The frozen V2 contract remains authoritative. No dataset, operator, branch count, selector, evaluator, or scientific claim boundary was changed in Phase 2A.

## Historical state separation

The following remain recoverable in Git history and the Phase 1 reconciliation branch but are not consumed by the canonical runtime:

- deadline/paper/submission readiness state;
- historical cancellation and reset records;
- dynamic monitor snapshots and old queue/status files;
- generated analysis bundles and legacy V1/V2 outputs.

No sealed scientific artifact was deleted. Runtime status is written under `status/reset/`; historical `status/v2r/` files are evidence, not authoritative state.

## Runtime authority

- `scripts/v2r_unified_monitor.py`: read-only observation and drift reporting.
- `scripts/v2r_orchestrator.py`: sole execution authority; requires explicit task and queue authorization.
- `scripts/v2r_watchdog.py`: service liveness only.
- `scripts/v2r_submit.py`: explicit authorization, storage, SHA, seed, GPU, and neutral-name gates.
- `scripts/v2r_inventory.py`: scheduler/GPU/filesystem/artifact inventory; Slurm remains authoritative.

Neutral service names are `rsd-monitor`, `rsd-orchestrator`, and `rsd-watchdog`. New scheduler metadata uses `rsd-*` names and `rsd-%j.out`/`rsd-%j.err` logs.

## Phase boundary

Source build, neutralization, CPU tests, and manifest generation are allowed in Phase 2A. New full MATH/GSM8K banks, counterfactual shards, or any other raw GPU execution require the separate storage and deployment gates in [STORAGE_EXECUTION_PLAN.md](STORAGE_EXECUTION_PLAN.md).
