# V2R cluster inventory

2026-09-26T23:25:49.074383+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315458048000 available bytes; 82.40% used; 112445693 free inodes.

server1 `/home`: 315458048000 available bytes; 82.40% used; 112445693 free inodes.

server1 `/tmp`: 315458048000 available bytes; 82.40% used; 112445693 free inodes.

server1 `/var/tmp`: 315458048000 available bytes; 82.40% used; 112445693 free inodes.

server1 `/mnt/raid5`: 645842145280 available bytes; 97.04% used; 337467050 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17946271744 available bytes; 99.00% used; 110367450 free inodes.

server2 `/home`: 17946271744 available bytes; 99.00% used; 110367450 free inodes.

server2 `/tmp`: 17946271744 available bytes; 99.00% used; 110367450 free inodes.

server2 `/var/tmp`: 17946271744 available bytes; 99.00% used; 110367450 free inodes.

server2 `/mnt/raid5`: 595213000704 available bytes; 95.89% used; 444959704 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 81080549376 available bytes; 95.48% used; 114069877 free inodes.

server3 `/home`: 81080549376 available bytes; 95.48% used; 114069877 free inodes.

server3 `/data`: 1349231304704 available bytes; 81.35% used; 225826445 free inodes.

server3 `/tmp`: 81080549376 available bytes; 95.48% used; 114069877 free inodes.

server3 `/var/tmp`: 81080549376 available bytes; 95.48% used; 114069877 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105889415168 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105889415168 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409599561728 available bytes; 94.34% used; 224823790 free inodes.

server4 `/tmp`: 105889415168 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105889415168 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
