# Protected execution and evidence map

This document implements the final master request. No protected worktree is a V2R write target.

| Server | Existing execution path | Protected jobs/evidence | V2R treatment |
|---|---|---|---|
| server1 / devbox | `/home/kimhj/repairable-state-discovery-v2-exec` | 50668, 50669 running; 50738 completed unobserved | Never mutate/cancel. SSH unavailable; Slurm-only observation. |
| server2 | `/home/kimhj/repairable-state-discovery-v2-exec` | 50752 FAILED_EXCLUDED; 50753,50754 SEALED | Read-only. No new raw work on critical root/RAID filesystems. |
| server4 | `/data/kimhj/repairable-state-discovery-v2-dream-hotfix-8b1361d` | 50923 SEALED; 50924 COMPLETED_UNSEALED | Read-only. 50924 forensic remains separate; never relax validator. |
| server3 / ubuntu | existing `repairable-state-discovery-*` worktrees | all historical and active scientific artifacts | No raw writes on critical `/data`; new reference execution worktree required. |

Protected process: tmux `iclr2027-live-monitor`, branch `codex/iclr2027-live-monitor-20260923`. Do not replace its 30-minute loop. New controller uses tmux `iclr2027-reference-orchestrator` and branch `codex/iclr2027-reference-live-20260923`.

Other users' allocations and GPU processes, and our unrelated job 49256, are not preemption targets. No multi-process GPU packing. A GPU candidate only becomes usable after Slurm grants its exclusive GRES allocation and process/storage checks pass inside the job.

Inventory captured in `status/v2r/cluster_inventory.json` with exact byte and inode counts. Critical usage threshold is 95% of user-available filesystem capacity; reserve 50 GiB plus twice projected shard output. server3 `/var/tmp` is on separate root NVMe, observed below threshold; `/data` is rejected. Candidate paths are rechecked immediately before launch.

Preemption recommendation requires measured reference throughput/cutoff infeasibility and necessary occupied GPU identification, including existing progress/ETA/loss. Missing server1 progress is UNKNOWN, never guessed. A recommendation never cancels a job.

All new scientific execution starts at an immutable detached commit, records that start SHA, and leaves finalization SHA separate. Status/paper commits happen only in their separate worktrees. No pull, checkout, merge, reset, commit, or artifact commit in a live scientific worktree.
