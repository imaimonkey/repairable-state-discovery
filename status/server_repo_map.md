# Server / Git topology observation

Snapshot time: `2026-09-23T13:53:16+09:00 KST`  
Collector source commit: `0dd161c8cf4bf3e7dbe4042234a0954950ce870e`

This is an observation map. SHA differences are preserved; no checkout, pull,
reset, or synchronization was performed.

| server | role / node | repo or worktree | branch | HEAD | origin/main | dirty state | purpose | active-job dependency |
|---|---|---|---|---|---|---|---|---|
| server1 | `devbox` | `/home/kimhj/repairable-state-discovery-v2-exec` | detached (from Slurm metadata) | `0dd161c8` | `0dd161c8` | not observable: SSH denied | active LLaDA execution | 50668, 50669 active; 50738 completed |
| server1 | `devbox` | `/home/kimhj/repairable-state-discovery-v2-unified-8b1361d` | detached | `8b1361d3` | `0dd161c8` | historical manifest says clean; not rechecked | future execution checkout | none directly |
| server2 | `server2` | `/home/kimhj/repairable-state-discovery-v2-exec` | detached | `0dd161c8` | `0dd161c8` | `?? results/v2_measurement/` | active/completed LLaDA execution artifacts | 50752 failed; 50753/50754 completed |
| server2 | `server2` | `/home/kimhj/repairable-state-discovery-v2-unified-8b1361d` | detached | `8b1361d3` | `0dd161c8` | clean | future execution checkout | none directly |
| server3 | `ubuntu` | `/data/kimhj/repairable-state-discovery-v2-exec` | `codex/current-job-status-20260921` | `b5f8e52b` | `0dd161c8` | clean | local Slurm controller/collector worktree; historical status branch | no target job execution dependency |
| server3 | `ubuntu` | `/data/kimhj/repairable-state-discovery-v2-unified-8b1361d` | detached | `8b1361d3` | `0dd161c8` | clean | local unified checkout | no target job execution dependency |
| server4 | `server4` | `/data/kimhj/repairable-state-discovery-v2-exec` | detached | `0dd161c8` | `0dd161c8` | `?? results/v2_measurement/` | base-SHA Dream/legacy artifact checkout | excluded historical artifacts |
| server4 | `server4` | `/data/kimhj/repairable-state-discovery-v2-unified-8b1361d` | detached | `8b1361d3` | `0dd161c8` | clean | unified checkout | none directly |
| server4 | `server4` | `/data/kimhj/repairable-state-discovery-v2-dream-hotfix-8b1361d` | `codex/dream-math500-compact-artifacts-20260922` | `15f40e05` | `0dd161c8` | `?? results/v2_measurement/` | Dream hotfix execution + per-run analysis artifacts | 50923 completed; 50924 active |
| local status | `ubuntu/server3` | `/data/kimhj/repairable-state-discovery-status-20260923` | `codex/iclr2027-status-20260923` | created from `0dd161c8` | `0dd161c8` | clean before snapshot generation | clean status worktree only | no active job dependency |

## Access notes

- `server2` was read through `10.0.12.121`; `server4` through `10.0.12.163`.
- `devbox`/server1 (`10.0.12.120`) resolved but rejected the available SSH
  credentials. Its Slurm metadata is reliable; its artifact-derived fields are
  deliberately left unobserved in the JSON/CSV snapshot.
- The server2/server4 working trees contain untracked result artifacts created
  by the experiments. They were not cleaned or modified.
- The status worktree is separate from the active execution worktrees and is
  the only worktree changed by this task.

