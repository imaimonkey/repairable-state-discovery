# V2R cluster inventory

2026-09-27T00:17:39.001393+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315169169408 available bytes; 82.42% used; 112443632 free inodes.

server1 `/home`: 315169169408 available bytes; 82.42% used; 112443632 free inodes.

server1 `/tmp`: 315169169408 available bytes; 82.42% used; 112443632 free inodes.

server1 `/var/tmp`: 315169169408 available bytes; 82.42% used; 112443632 free inodes.

server1 `/mnt/raid5`: 637717389312 available bytes; 97.07% used; 337408004 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 17932529664 available bytes; 99.00% used; 110367281 free inodes.

server2 `/home`: 17932529664 available bytes; 99.00% used; 110367281 free inodes.

server2 `/tmp`: 17932529664 available bytes; 99.00% used; 110367281 free inodes.

server2 `/var/tmp`: 17932529664 available bytes; 99.00% used; 110367281 free inodes.

server2 `/mnt/raid5`: 593038360576 available bytes; 95.90% used; 444957700 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 79509774336 available bytes; 95.56% used; 114068840 free inodes.

server3 `/home`: 79509774336 available bytes; 95.56% used; 114068840 free inodes.

server3 `/data`: 1349111955456 available bytes; 81.35% used; 225825768 free inodes.

server3 `/tmp`: 79509774336 available bytes; 95.56% used; 114068840 free inodes.

server3 `/var/tmp`: 79509774336 available bytes; 95.56% used; 114068840 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105879678976 available bytes; 94.09% used; 114347842 free inodes.

server4 `/home`: 105879678976 available bytes; 94.09% used; 114347842 free inodes.

server4 `/data`: 409566298112 available bytes; 94.34% used; 224823636 free inodes.

server4 `/tmp`: 105879678976 available bytes; 94.09% used; 114347842 free inodes.

server4 `/var/tmp`: 105879678976 available bytes; 94.09% used; 114347842 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
