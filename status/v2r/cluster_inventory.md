# V2R cluster inventory

2026-09-23T15:25:33.015315+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['7'] | [] |

server2 `/`: 41432154112 available bytes; 97.69% used; 110435179 free inodes.

server2 `/home`: 41432154112 available bytes; 97.69% used; 110435179 free inodes.

server2 `/tmp`: 41432154112 available bytes; 97.69% used; 110435179 free inodes.

server2 `/var/tmp`: 41432154112 available bytes; 97.69% used; 110435179 free inodes.

server2 `/mnt/raid5`: 550394953728 available bytes; 96.20% used; 445224147 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] |

server3 `/`: 377638846464 available bytes; 78.93% used; 114304757 free inodes.

server3 `/home`: 377638846464 available bytes; 78.93% used; 114304757 free inodes.

server3 `/data`: 124965548032 available bytes; 98.27% used; 225840900 free inodes.

server3 `/tmp`: 377638846464 available bytes; 78.93% used; 114304757 free inodes.

server3 `/var/tmp`: 377638846464 available bytes; 78.93% used; 114304757 free inodes.
| server4 | True | ['1', '2', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111672672256 available bytes; 93.77% used; 114378455 free inodes.

server4 `/home`: 111672672256 available bytes; 93.77% used; 114378455 free inodes.

server4 `/data`: 38907064320 available bytes; 99.46% used; 225495120 free inodes.

server4 `/tmp`: 111672672256 available bytes; 93.77% used; 114378455 free inodes.

server4 `/var/tmp`: 111672672256 available bytes; 93.77% used; 114378455 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
