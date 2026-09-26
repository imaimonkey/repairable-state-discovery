# Legacy and Historical Index

This index prevents historical state from being mistaken for canonical scientific source. Entries are preserved unless a later approved cleanup explicitly says otherwise.

| Entry | Classification | Canonical treatment | Recovery |
|---|---|---|---|
| V1 `f45569d…` worktrees and server2 non-Git copy | `LEGACY_EXPERIMENT_ONLY` | archive-only; never V2 evidence | original worktree/path and Phase 1 fingerprint |
| `0dd161c…` | historical clean V2 ancestor | comparison anchor; not preferred Phase 2 base | Git object and reconciliation matrix |
| `78fe5d7…` sealed reference execution | `SEALED_REFERENCE_PILOT` / preferred scientific base | preserve source core; separate derived state | Git object, recipes, manifests, sealed outputs |
| `status/v2r/` | operational/status evidence | not authoritative for canonical runtime | original Git tree and Phase 1 inventory |
| paper/readiness/PDF state | paper artifact lineage | archive-only | original Git paths and commits |
| live monitor/reference worktrees | operational overlays | never edit from this branch | original worktrees and branch refs |
| `926495e…` V2 measurement generation | `LEGACY_MEASUREMENT` plus operational overlay | no primary confirmatory claims | active manifests and job records |
| jobs 53067, 53069–53074 | `HOLD_FOR_FORENSIC` | snapshot, then explicit cancel decision | Slurm `scontrol`, `sacct`, output paths |
| jobs 53262 and 53266 | `LEGACY_RUNNING_FORENSIC` | finish only if near complete; otherwise snapshot/cancel | current logs/manifests and scheduler records |
| jobs 53267, 53268, 53275 | `LEGACY_PENDING` | snapshot and cancel candidate | scheduler and submission manifests |

The current canonical branch does not cancel jobs, alter live worktrees, or remove raw artifacts. The index is a disposition guide, not an execution command.
