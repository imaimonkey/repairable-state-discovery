# V2R cluster inventory

2026-09-23T11:52:58.019613+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['6'] | [] |

server2 `/`: 41821442048 available bytes; 97.67% used; 110436697 free inodes.

server2 `/home`: 41821442048 available bytes; 97.67% used; 110436697 free inodes.

server2 `/tmp`: 41821442048 available bytes; 97.67% used; 110436697 free inodes.

server2 `/var/tmp`: 41821442048 available bytes; 97.67% used; 110436697 free inodes.

server2 `/mnt/raid5`: 558415966208 available bytes; 96.14% used; 445231530 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 380102926336 available bytes; 78.79% used; 114347661 free inodes.

server3 `/home`: 380102926336 available bytes; 78.79% used; 114347661 free inodes.

server3 `/data`: 137460695040 available bytes; 98.10% used; 225864991 free inodes.

server3 `/tmp`: 380102926336 available bytes; 78.79% used; 114347661 free inodes.

server3 `/var/tmp`: 380102926336 available bytes; 78.79% used; 114347661 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111605284864 available bytes; 93.77% used; 114379004 free inodes.

server4 `/home`: 111605284864 available bytes; 93.77% used; 114379004 free inodes.

server4 `/data`: 67429126144 available bytes; 99.07% used; 225411861 free inodes.

server4 `/tmp`: 111605284864 available bytes; 93.77% used; 114379004 free inodes.

server4 `/var/tmp`: 111605284864 available bytes; 93.77% used; 114379004 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
