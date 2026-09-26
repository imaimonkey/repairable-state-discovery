# V2R cluster inventory

2026-09-26T17:39:44.030518+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315588452352 available bytes; 82.39% used; 112445801 free inodes.

server1 `/home`: 315588452352 available bytes; 82.39% used; 112445801 free inodes.

server1 `/tmp`: 315588452352 available bytes; 82.39% used; 112445801 free inodes.

server1 `/var/tmp`: 315588452352 available bytes; 82.39% used; 112445801 free inodes.

server1 `/mnt/raid5`: 645852696576 available bytes; 97.04% used; 337467122 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18030911488 available bytes; 98.99% used; 110367630 free inodes.

server2 `/home`: 18030911488 available bytes; 98.99% used; 110367630 free inodes.

server2 `/tmp`: 18030911488 available bytes; 98.99% used; 110367630 free inodes.

server2 `/var/tmp`: 18030911488 available bytes; 98.99% used; 110367630 free inodes.

server2 `/mnt/raid5`: 605519007744 available bytes; 95.82% used; 444969212 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81275854848 available bytes; 95.46% used; 114065380 free inodes.

server3 `/home`: 81275854848 available bytes; 95.46% used; 114065380 free inodes.

server3 `/data`: 1349448404992 available bytes; 81.35% used; 225835775 free inodes.

server3 `/tmp`: 81275854848 available bytes; 95.46% used; 114065380 free inodes.

server3 `/var/tmp`: 81275854848 available bytes; 95.46% used; 114065380 free inodes.
| server4 | True | ['2', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105939976192 available bytes; 94.09% used; 114347854 free inodes.

server4 `/home`: 105939976192 available bytes; 94.09% used; 114347854 free inodes.

server4 `/data`: 410448809984 available bytes; 94.33% used; 224824355 free inodes.

server4 `/tmp`: 105939976192 available bytes; 94.09% used; 114347854 free inodes.

server4 `/var/tmp`: 105939976192 available bytes; 94.09% used; 114347854 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
