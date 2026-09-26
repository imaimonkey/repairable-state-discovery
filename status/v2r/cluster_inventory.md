# V2R cluster inventory

2026-09-26T17:22:57.871632+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315620114432 available bytes; 82.39% used; 112445845 free inodes.

server1 `/home`: 315620114432 available bytes; 82.39% used; 112445845 free inodes.

server1 `/tmp`: 315620114432 available bytes; 82.39% used; 112445845 free inodes.

server1 `/var/tmp`: 315620114432 available bytes; 82.39% used; 112445845 free inodes.

server1 `/mnt/raid5`: 645846867968 available bytes; 97.04% used; 337467116 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18024050688 available bytes; 98.99% used; 110367561 free inodes.

server2 `/home`: 18024050688 available bytes; 98.99% used; 110367561 free inodes.

server2 `/tmp`: 18024050688 available bytes; 98.99% used; 110367561 free inodes.

server2 `/var/tmp`: 18024050688 available bytes; 98.99% used; 110367561 free inodes.

server2 `/mnt/raid5`: 606289338368 available bytes; 95.81% used; 444969828 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81274400768 available bytes; 95.46% used; 114065342 free inodes.

server3 `/home`: 81274400768 available bytes; 95.46% used; 114065342 free inodes.

server3 `/data`: 1349216608256 available bytes; 81.35% used; 225836294 free inodes.

server3 `/tmp`: 81274400768 available bytes; 95.46% used; 114065342 free inodes.

server3 `/var/tmp`: 81274400768 available bytes; 95.46% used; 114065342 free inodes.
| server4 | True | ['0', '2', '3', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105952296960 available bytes; 94.09% used; 114347873 free inodes.

server4 `/home`: 105952296960 available bytes; 94.09% used; 114347873 free inodes.

server4 `/data`: 410519191552 available bytes; 94.33% used; 224824485 free inodes.

server4 `/tmp`: 105952296960 available bytes; 94.09% used; 114347873 free inodes.

server4 `/var/tmp`: 105952296960 available bytes; 94.09% used; 114347873 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
