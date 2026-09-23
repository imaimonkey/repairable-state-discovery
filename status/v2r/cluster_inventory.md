# V2R cluster inventory

2026-09-23T15:21:39.231584+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['7'] | [] |

server2 `/`: 41432862720 available bytes; 97.69% used; 110435179 free inodes.

server2 `/home`: 41432862720 available bytes; 97.69% used; 110435179 free inodes.

server2 `/tmp`: 41432862720 available bytes; 97.69% used; 110435179 free inodes.

server2 `/var/tmp`: 41432862720 available bytes; 97.69% used; 110435179 free inodes.

server2 `/mnt/raid5`: 551030358016 available bytes; 96.19% used; 445224130 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 377643319296 available bytes; 78.93% used; 114305095 free inodes.

server3 `/home`: 377643319296 available bytes; 78.93% used; 114305095 free inodes.

server3 `/data`: 124966375424 available bytes; 98.27% used; 225840975 free inodes.

server3 `/tmp`: 377643319296 available bytes; 78.93% used; 114305095 free inodes.

server3 `/var/tmp`: 377643319296 available bytes; 78.93% used; 114305095 free inodes.
| server4 | True | ['1', '2'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111672774656 available bytes; 93.77% used; 114378449 free inodes.

server4 `/home`: 111672774656 available bytes; 93.77% used; 114378449 free inodes.

server4 `/data`: 38946639872 available bytes; 99.46% used; 225495142 free inodes.

server4 `/tmp`: 111672774656 available bytes; 93.77% used; 114378449 free inodes.

server4 `/var/tmp`: 111672774656 available bytes; 93.77% used; 114378449 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
