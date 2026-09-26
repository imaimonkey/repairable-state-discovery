# Keep / Archive / Delete Plan

Phase 1 is non-destructive. No files, worktrees, branches, jobs, processes, or artifacts are deleted. “Delete later” below means only after independent approval, manifest verification, and a recoverable archive exists.

## KEEP

| Target | Why | Required condition |
|---|---|---|
| `78fe5d7c…` | frozen scientific execution SHA with sealed evidence continuity | preferred Phase 2 scientific base; separate generic runtime from state |
| `origin/main` at `0dd161c…` | clean historical V2 ancestor | immutable comparison anchor, not preferred scientific base |
| provenance/boundary commits through `435e24e…` | source provenance and tested Dream boundary behavior | cherry-pick/port with tests |
| source-pinned V2R gate/sampler/seed/artifact/shard logic | required for reference execution and scientific identity | neutralize names; preserve exact hashes |
| reference execution SHA `78fe5d7…` and all sealed gate evidence | current reference-primary evidence | retain immutable; do not rewrite |
| current 12 jobs until forensic disposition | seven held server1 lanes are forensic/cancel candidates; five are legacy measurement jobs | snapshot and re-query before any action |
| server2 fingerprint CSV and older source copy | closes non-Git ambiguity without changing server2 | retain as legacy provenance |
| all old V2/reference-primary/MATH-500/GSM8K/Dream/BBH/MBPP outputs | reproducibility and forensic value | classify individually |
| seed-collision audits, manifests, SHA lists, and provenance records | evidence of scientific integrity | preserve alongside source identity |

## ARCHIVE

| Target | Reason | Archive form |
|---|---|---|
| paper/deadline worktrees and docs | useful for paper production but not portable runtime | immutable Git refs plus metadata manifest |
| live monitor/status history | operational evidence and debugging context | retain snapshots; separate from canonical source |
| analysis bundles and handoff branches | derived evidence, not source | preserve checksums and source SHA |
| legacy/V1 worktrees | historical reproduction | keep read-only; label legacy and unknown where needed |
| completed audit probe records | infrastructure provenance | scheduler history and this inventory |

## CURRENT JOB DISPOSITION (NO ACTION TAKEN)

- `53067, 53069–53074`: `HOLD_FOR_FORENSIC`; server1 reports `reference_compatible=false` with `exact_native_replay_failed`, while primary MATH temporal is already sealed by job `53195`. They are `CANCEL_AFTER_SNAPSHOT` candidates, not reference-critical dependencies.
- `53262, 53266`: `LEGACY_RUNNING_FORENSIC`; inspect progress/final-report proximity. Finish only if near complete and useful as legacy evidence; otherwise snapshot then cancel after explicit approval.
- `53267, 53268, 53275`: `LEGACY_PENDING`; snapshot and cancel candidates because they are from the old `926495e…` measurement generation and are not primary evidence for the confirmatory plan.

No cancellation or other scheduler mutation is performed in this correction pass.

## DELETE LATER (not performed)

No immediate deletion candidate is approved. After the scientific work is closed and an independent archive is verified, possible candidates are limited to:

- duplicate generated logs or caches proven byte-identical and not referenced by a manifest;
- abandoned temporary worktrees whose Git commits and artifact manifests are archived;
- stale monitor PID/status files proven unrelated to any live process;
- failed/incomplete outputs only when their failure record is preserved and no replay/forensic need remains.

Raw scientific outputs, sealed artifacts, source checkouts, job manifests, seed registries, and unclassified server2 data are explicitly not deletion candidates.

## Decision gates before any cleanup

1. Re-run inventory on all four servers and confirm no live process references the target.
2. Resolve the artifact’s source SHA/config/dataset/seed lineage.
3. Create and verify a recoverable archive plus checksum manifest.
4. Confirm the target is not needed for a reference replay, paper claim, or audit.
5. Obtain explicit approval for the exact paths; never use broad recursive cleanup.

## PHASE 2 PRECONDITIONS

Do not begin a canonical execution or build raw trajectory banks until the selected primary pool has an approved filesystem, at least `max(200 GiB, 3 × projected maximum single-shard raw output)` free, at least 10% free inodes, and an explicit retention/archive plan.
