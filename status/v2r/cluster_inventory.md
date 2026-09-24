# V2R cluster inventory

2026-09-24T21:48:27.826177+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323948597248 available bytes; 81.93% used; 112481413 free inodes.

server1 `/home`: 323948597248 available bytes; 81.93% used; 112481413 free inodes.

server1 `/tmp`: 323948597248 available bytes; 81.93% used; 112481413 free inodes.

server1 `/var/tmp`: 323948597248 available bytes; 81.93% used; 112481413 free inodes.

server1 `/mnt/raid5`: 415461470208 available bytes; 98.09% used; 337625313 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30131392512 available bytes; 98.32% used; 110411306 free inodes.

server2 `/home`: 30131392512 available bytes; 98.32% used; 110411306 free inodes.

server2 `/tmp`: 30131392512 available bytes; 98.32% used; 110411306 free inodes.

server2 `/var/tmp`: 30131392512 available bytes; 98.32% used; 110411306 free inodes.

server2 `/mnt/raid5`: 489842647040 available bytes; 96.62% used; 445154373 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84380860416 available bytes; 95.29% used; 114156081 free inodes.

server3 `/home`: 84380860416 available bytes; 95.29% used; 114156081 free inodes.

server3 `/data`: 149992534016 available bytes; 97.93% used; 225802837 free inodes.

server3 `/tmp`: 84380860416 available bytes; 95.29% used; 114156081 free inodes.

server3 `/var/tmp`: 84380860416 available bytes; 95.29% used; 114156081 free inodes.
| server4 | True | ['1', '4', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105819910144 available bytes; 94.09% used; 114348341 free inodes.

server4 `/home`: 105819910144 available bytes; 94.09% used; 114348341 free inodes.

server4 `/data`: 80468619264 available bytes; 98.89% used; 225243660 free inodes.

server4 `/tmp`: 105819910144 available bytes; 94.09% used; 114348341 free inodes.

server4 `/var/tmp`: 105819910144 available bytes; 94.09% used; 114348341 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
