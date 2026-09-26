# Phase 2B server deployment report

Deployment completed without resetting or overwriting an existing worktree. A new detached execution worktree was created on each server at exact canonical scientific source SHA `227cbcc99c7edfac83de7f34c452db7defd5bdcb`.

| Server | Detached path | Head | Clean | Result |
|---|---|---|---|---|
| server1/devbox | `/home/kimhj/repairable-state-discovery-rsd-exec` | `227cbcc99c7edfac83de7f34c452db7defd5bdcb` | yes | deployed by direct-URL fetch because old repo had no remote |
| server2 | `/home/kimhj/repairable-state-discovery-rsd-exec` | `227cbcc99c7edfac83de7f34c452db7defd5bdcb` | yes | deployed from origin branch |
| server3/ubuntu | `/data/kimhj/repairable-state-discovery-rsd-exec` | `227cbcc99c7edfac83de7f34c452db7defd5bdcb` | yes | deployed from origin branch |
| server4 | `/data/kimhj/repairable-state-discovery-rsd-exec` | `227cbcc99c7edfac83de7f34c452db7defd5bdcb` | yes | deployed from origin branch |

No Phase 2B scientific job was submitted. All new audit/calibration job names used the neutral `rsd-*` namespace. Existing legacy V2 jobs retain their historical names and SHA `926495e`; they are not evidence of canonical deployment.
