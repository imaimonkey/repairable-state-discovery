# V2R cluster inventory

2026-09-26T17:36:41.172294+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315597934592 available bytes; 82.39% used; 112445863 free inodes.

server1 `/home`: 315597934592 available bytes; 82.39% used; 112445863 free inodes.

server1 `/tmp`: 315597934592 available bytes; 82.39% used; 112445863 free inodes.

server1 `/var/tmp`: 315597934592 available bytes; 82.39% used; 112445863 free inodes.

server1 `/mnt/raid5`: 645853650944 available bytes; 97.04% used; 337467122 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18030067712 available bytes; 98.99% used; 110367630 free inodes.

server2 `/home`: 18030067712 available bytes; 98.99% used; 110367630 free inodes.

server2 `/tmp`: 18030067712 available bytes; 98.99% used; 110367630 free inodes.

server2 `/var/tmp`: 18030067712 available bytes; 98.99% used; 110367630 free inodes.

server2 `/mnt/raid5`: 605601861632 available bytes; 95.82% used; 444969334 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81274421248 available bytes; 95.46% used; 114065394 free inodes.

server3 `/home`: 81274421248 available bytes; 95.46% used; 114065394 free inodes.

server3 `/data`: 1349458391040 available bytes; 81.35% used; 225835954 free inodes.

server3 `/tmp`: 81274421248 available bytes; 95.46% used; 114065394 free inodes.

server3 `/var/tmp`: 81274421248 available bytes; 95.46% used; 114065394 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105940111360 available bytes; 94.09% used; 114347878 free inodes.

server4 `/home`: 105940111360 available bytes; 94.09% used; 114347878 free inodes.

server4 `/data`: 410443649024 available bytes; 94.33% used; 224824424 free inodes.

server4 `/tmp`: 105940111360 available bytes; 94.09% used; 114347878 free inodes.

server4 `/var/tmp`: 105940111360 available bytes; 94.09% used; 114347878 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
