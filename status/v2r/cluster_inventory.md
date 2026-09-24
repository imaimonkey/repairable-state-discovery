# V2R cluster inventory

2026-09-24T22:48:26.845047+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323933306880 available bytes; 81.93% used; 112481415 free inodes.

server1 `/home`: 323933306880 available bytes; 81.93% used; 112481415 free inodes.

server1 `/tmp`: 323933306880 available bytes; 81.93% used; 112481415 free inodes.

server1 `/var/tmp`: 323933306880 available bytes; 81.93% used; 112481415 free inodes.

server1 `/mnt/raid5`: 415333281792 available bytes; 98.09% used; 337618154 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23159947264 available bytes; 98.71% used; 110410910 free inodes.

server2 `/home`: 23159947264 available bytes; 98.71% used; 110410910 free inodes.

server2 `/tmp`: 23159947264 available bytes; 98.71% used; 110410910 free inodes.

server2 `/var/tmp`: 23159947264 available bytes; 98.71% used; 110410910 free inodes.

server2 `/mnt/raid5`: 487441436672 available bytes; 96.63% used; 445152621 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84372307968 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84372307968 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 148973727744 available bytes; 97.94% used; 225801711 free inodes.

server3 `/tmp`: 84372307968 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84372307968 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['0', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105801158656 available bytes; 94.10% used; 114348320 free inodes.

server4 `/home`: 105801158656 available bytes; 94.10% used; 114348320 free inodes.

server4 `/data`: 62769889280 available bytes; 99.13% used; 225206563 free inodes.

server4 `/tmp`: 105801158656 available bytes; 94.10% used; 114348320 free inodes.

server4 `/var/tmp`: 105801158656 available bytes; 94.10% used; 114348320 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
