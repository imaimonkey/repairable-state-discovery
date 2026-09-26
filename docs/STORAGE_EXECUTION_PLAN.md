# Storage Execution Plan

Raw scientific execution is disabled in Phase 2A.

## Required reservation

For every selected primary execution filesystem:

```text
free_bytes >= max(200 GiB, 3 × projected maximum single-shard raw output)
free_inode_fraction >= 10%
approved retention/archive policy = true
```

The projected maximum must include raw trajectory bank, counterfactual branches, logs, temporary high-water mark, and sealing/merge workspace. It must be measured from existing pilot artifacts rather than guessed from source size.

## Observed baseline

| Server/filesystem | Approx. free | Phase 2B status |
|---|---:|---|
| server1 `/mnt/raid5` | 204G | no approved reservation; unsafe at 99% usage |
| server2 `/` | 19G | fails minimum |
| server3 `/data` | 116G | fails minimum |
| server4 `/data` | 83G | fails minimum |

These values are forensic snapshots and must be re-measured before deployment. No raw output should be routed automatically to a nearly full filesystem.

## Capacity calculation procedure

1. Measure the largest existing valid pilot trajectory bank and counterfactual shard.
2. Measure log and temporary merge/seal overhead.
3. Multiply the maximum single-shard raw size by three for reservation safety.
4. Compare against 200 GiB minimum and select only a filesystem that passes both.
5. Record the approved path, owner, free bytes, inode margin, projected high-water mark, retention window, and archive destination in the execution manifest.

Storage approval is independent of source correctness. Passing this plan does not authorize a scientific run until the exact canonical SHA, environment, gates, and deployment equivalence are also verified.
