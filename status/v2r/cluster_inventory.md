# V2R cluster inventory

2026-09-23T15:17:55.967931+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['7'] | [] |

server2 `/`: 41434025984 available bytes; 97.69% used; 110435187 free inodes.

server2 `/home`: 41434025984 available bytes; 97.69% used; 110435187 free inodes.

server2 `/tmp`: 41434025984 available bytes; 97.69% used; 110435187 free inodes.

server2 `/var/tmp`: 41434025984 available bytes; 97.69% used; 110435187 free inodes.

server2 `/mnt/raid5`: 551148658688 available bytes; 96.19% used; 445224380 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 377644879872 available bytes; 78.93% used; 114304636 free inodes.

server3 `/home`: 377644879872 available bytes; 78.93% used; 114304636 free inodes.

server3 `/data`: 124970074112 available bytes; 98.27% used; 225841028 free inodes.

server3 `/tmp`: 377644879872 available bytes; 78.93% used; 114304636 free inodes.

server3 `/var/tmp`: 377644879872 available bytes; 78.93% used; 114304636 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111672897536 available bytes; 93.77% used; 114378451 free inodes.

server4 `/home`: 111672897536 available bytes; 93.77% used; 114378451 free inodes.

server4 `/data`: 39014608896 available bytes; 99.46% used; 225495307 free inodes.

server4 `/tmp`: 111672897536 available bytes; 93.77% used; 114378451 free inodes.

server4 `/var/tmp`: 111672897536 available bytes; 93.77% used; 114378451 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
