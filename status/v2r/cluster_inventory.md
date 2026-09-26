# V2R cluster inventory

2026-09-26T17:35:09.676405+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315599974400 available bytes; 82.39% used; 112445882 free inodes.

server1 `/home`: 315599974400 available bytes; 82.39% used; 112445882 free inodes.

server1 `/tmp`: 315599974400 available bytes; 82.39% used; 112445882 free inodes.

server1 `/var/tmp`: 315599974400 available bytes; 82.39% used; 112445882 free inodes.

server1 `/mnt/raid5`: 645851705344 available bytes; 97.04% used; 337467120 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18029019136 available bytes; 98.99% used; 110367628 free inodes.

server2 `/home`: 18029019136 available bytes; 98.99% used; 110367628 free inodes.

server2 `/tmp`: 18029019136 available bytes; 98.99% used; 110367628 free inodes.

server2 `/var/tmp`: 18029019136 available bytes; 98.99% used; 110367628 free inodes.

server2 `/mnt/raid5`: 605649813504 available bytes; 95.82% used; 444969473 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81274621952 available bytes; 95.46% used; 114065373 free inodes.

server3 `/home`: 81274621952 available bytes; 95.46% used; 114065373 free inodes.

server3 `/data`: 1349210054656 available bytes; 81.35% used; 225836051 free inodes.

server3 `/tmp`: 81274621952 available bytes; 95.46% used; 114065373 free inodes.

server3 `/var/tmp`: 81274621952 available bytes; 95.46% used; 114065373 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105940140032 available bytes; 94.09% used; 114347878 free inodes.

server4 `/home`: 105940140032 available bytes; 94.09% used; 114347878 free inodes.

server4 `/data`: 410445291520 available bytes; 94.33% used; 224824484 free inodes.

server4 `/tmp`: 105940140032 available bytes; 94.09% used; 114347878 free inodes.

server4 `/var/tmp`: 105940140032 available bytes; 94.09% used; 114347878 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
