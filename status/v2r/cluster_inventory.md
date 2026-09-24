# V2R cluster inventory

2026-09-24T01:26:41.034120+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325464510464 available bytes; 81.84% used; 112499705 free inodes.

server1 `/home`: 325464510464 available bytes; 81.84% used; 112499705 free inodes.

server1 `/tmp`: 325464510464 available bytes; 81.84% used; 112499705 free inodes.

server1 `/var/tmp`: 325464510464 available bytes; 81.84% used; 112499705 free inodes.

server1 `/mnt/raid5`: 912267587584 available bytes; 95.82% used; 337734032 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40950853632 available bytes; 97.72% used; 110432019 free inodes.

server2 `/home`: 40950853632 available bytes; 97.72% used; 110432019 free inodes.

server2 `/tmp`: 40950853632 available bytes; 97.72% used; 110432019 free inodes.

server2 `/var/tmp`: 40950853632 available bytes; 97.72% used; 110432019 free inodes.

server2 `/mnt/raid5`: 531067179008 available bytes; 96.33% used; 445201732 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292345929728 available bytes; 83.69% used; 114187452 free inodes.

server3 `/home`: 292345929728 available bytes; 83.69% used; 114187452 free inodes.

server3 `/data`: 82044018688 available bytes; 98.87% used; 225842328 free inodes.

server3 `/tmp`: 292345929728 available bytes; 83.69% used; 114187452 free inodes.

server3 `/var/tmp`: 292345929728 available bytes; 83.69% used; 114187452 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105970982912 available bytes; 94.09% used; 114348888 free inodes.

server4 `/home`: 105970982912 available bytes; 94.09% used; 114348888 free inodes.

server4 `/data`: 290824032256 available bytes; 95.98% used; 225396989 free inodes.

server4 `/tmp`: 105970982912 available bytes; 94.09% used; 114348888 free inodes.

server4 `/var/tmp`: 105970982912 available bytes; 94.09% used; 114348888 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
