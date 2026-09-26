# Cleanup Manifest

Status: preparation only. No cleanup action has been executed by Phase 2A.

## Scheduler candidates

| Target | Snapshot requirement | Proposed disposition | Action in this branch |
|---|---|---|---|
| 53067, 53069–53074 | `scontrol show job`, `sacct`, command/SHA/config/output evidence, dispatcher incompatibility record | `SAFE_TO_CANCEL_AFTER_SNAPSHOT` | none |
| 53267, 53268, 53275 | scheduler record, old-generation SHA/config, pending reason, output manifest | `SAFE_TO_CANCEL_AFTER_SNAPSHOT` | none |
| 53262, 53266 | latest progress, artifact mtime, report presence, estimated remaining work | `FINISH_LEGACY` or `SAFE_TO_CANCEL_AFTER_SNAPSHOT` | none |

The seven server1 jobs are not scientific dependencies because exact native replay failed and primary MATH temporal evidence is already sealed by job 53195. The five V2 jobs are from the old measurement generation. This conclusion does not authorize cancellation.

## Filesystem candidates

No raw scientific output, sealed artifact, source checkout, seed registry, manifest, or unclassified server2 file is a cleanup target.

Future candidates may include only byte-identical caches/logs with no manifest references, abandoned temporary worktrees after Git/archive verification, or stale service files proven unrelated to live processes.

## Required approval sequence

1. Capture a final scheduler and artifact snapshot.
2. Verify no live process references the target.
3. Store a recoverable archive and checksum manifest.
4. Record the exact path/job ID and reason in a cleanup event.
5. Obtain explicit approval for each target.
6. Execute only the exact approved target and re-run inventory.

Broad recursive deletion, branch resets, blind synchronization, and raw-result removal are prohibited.
