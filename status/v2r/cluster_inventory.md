# V2R cluster inventory

2026-09-26T17:03:08.571412+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315636469760 available bytes; 82.39% used; 112445969 free inodes.

server1 `/home`: 315636469760 available bytes; 82.39% used; 112445969 free inodes.

server1 `/tmp`: 315636469760 available bytes; 82.39% used; 112445969 free inodes.

server1 `/var/tmp`: 315636469760 available bytes; 82.39% used; 112445969 free inodes.

server1 `/mnt/raid5`: 645891739648 available bytes; 97.04% used; 337469591 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18029641728 available bytes; 98.99% used; 110367561 free inodes.

server2 `/home`: 18029641728 available bytes; 98.99% used; 110367561 free inodes.

server2 `/tmp`: 18029641728 available bytes; 98.99% used; 110367561 free inodes.

server2 `/var/tmp`: 18029641728 available bytes; 98.99% used; 110367561 free inodes.

server2 `/mnt/raid5`: 606832435200 available bytes; 95.81% used; 444970220 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 81274978304 available bytes; 95.46% used; 114065341 free inodes.

server3 `/home`: 81274978304 available bytes; 95.46% used; 114065341 free inodes.

server3 `/data`: 1349323726848 available bytes; 81.35% used; 225836843 free inodes.

server3 `/tmp`: 81274978304 available bytes; 95.46% used; 114065341 free inodes.

server3 `/var/tmp`: 81274978304 available bytes; 95.46% used; 114065341 free inodes.
| server4 | True | ['0', '2', '3', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105952780288 available bytes; 94.09% used; 114347873 free inodes.

server4 `/home`: 105952780288 available bytes; 94.09% used; 114347873 free inodes.

server4 `/data`: 410523906048 available bytes; 94.33% used; 224824518 free inodes.

server4 `/tmp`: 105952780288 available bytes; 94.09% used; 114347873 free inodes.

server4 `/var/tmp`: 105952780288 available bytes; 94.09% used; 114347873 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
