# V2R cluster inventory

2026-09-23T15:20:24.088662+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['7'] | [] |

server2 `/`: 41433341952 available bytes; 97.69% used; 110435179 free inodes.

server2 `/home`: 41433341952 available bytes; 97.69% used; 110435179 free inodes.

server2 `/tmp`: 41433341952 available bytes; 97.69% used; 110435179 free inodes.

server2 `/var/tmp`: 41433341952 available bytes; 97.69% used; 110435179 free inodes.

server2 `/mnt/raid5`: 551069302784 available bytes; 96.19% used; 445224084 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 377643433984 available bytes; 78.93% used; 114305137 free inodes.

server3 `/home`: 377643433984 available bytes; 78.93% used; 114305137 free inodes.

server3 `/data`: 124967477248 available bytes; 98.27% used; 225840993 free inodes.

server3 `/tmp`: 377643433984 available bytes; 78.93% used; 114305137 free inodes.

server3 `/var/tmp`: 377643433984 available bytes; 78.93% used; 114305137 free inodes.
| server4 | True | ['1', '2'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111672819712 available bytes; 93.77% used; 114378455 free inodes.

server4 `/home`: 111672819712 available bytes; 93.77% used; 114378455 free inodes.

server4 `/data`: 38956331008 available bytes; 99.46% used; 225495194 free inodes.

server4 `/tmp`: 111672819712 available bytes; 93.77% used; 114378455 free inodes.

server4 `/var/tmp`: 111672819712 available bytes; 93.77% used; 114378455 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
