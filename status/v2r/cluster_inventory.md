# V2R cluster inventory

2026-09-24T21:51:32.254381+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323948097536 available bytes; 81.93% used; 112481413 free inodes.

server1 `/home`: 323948097536 available bytes; 81.93% used; 112481413 free inodes.

server1 `/tmp`: 323948097536 available bytes; 81.93% used; 112481413 free inodes.

server1 `/var/tmp`: 323948097536 available bytes; 81.93% used; 112481413 free inodes.

server1 `/mnt/raid5`: 415454150656 available bytes; 98.09% used; 337624953 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30130536448 available bytes; 98.32% used; 110411302 free inodes.

server2 `/home`: 30130536448 available bytes; 98.32% used; 110411302 free inodes.

server2 `/tmp`: 30130536448 available bytes; 98.32% used; 110411302 free inodes.

server2 `/var/tmp`: 30130536448 available bytes; 98.32% used; 110411302 free inodes.

server2 `/mnt/raid5`: 489752809472 available bytes; 96.62% used; 445154458 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84380540928 available bytes; 95.29% used; 114156081 free inodes.

server3 `/home`: 84380540928 available bytes; 95.29% used; 114156081 free inodes.

server3 `/data`: 149935439872 available bytes; 97.93% used; 225802781 free inodes.

server3 `/tmp`: 84380540928 available bytes; 95.29% used; 114156081 free inodes.

server3 `/var/tmp`: 84380540928 available bytes; 95.29% used; 114156081 free inodes.
| server4 | True | ['1', '4', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105819795456 available bytes; 94.09% used; 114348340 free inodes.

server4 `/home`: 105819795456 available bytes; 94.09% used; 114348340 free inodes.

server4 `/data`: 80466001920 available bytes; 98.89% used; 225243599 free inodes.

server4 `/tmp`: 105819795456 available bytes; 94.09% used; 114348340 free inodes.

server4 `/var/tmp`: 105819795456 available bytes; 94.09% used; 114348340 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
