# V2R cluster inventory

2026-09-24T21:40:46.914680+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323954712576 available bytes; 81.93% used; 112481419 free inodes.

server1 `/home`: 323954712576 available bytes; 81.93% used; 112481419 free inodes.

server1 `/tmp`: 323954712576 available bytes; 81.93% used; 112481419 free inodes.

server1 `/var/tmp`: 323954712576 available bytes; 81.93% used; 112481419 free inodes.

server1 `/mnt/raid5`: 415481225216 available bytes; 98.09% used; 337626220 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30138081280 available bytes; 98.32% used; 110411316 free inodes.

server2 `/home`: 30138081280 available bytes; 98.32% used; 110411316 free inodes.

server2 `/tmp`: 30138081280 available bytes; 98.32% used; 110411316 free inodes.

server2 `/var/tmp`: 30138081280 available bytes; 98.32% used; 110411316 free inodes.

server2 `/mnt/raid5`: 489537085440 available bytes; 96.62% used; 445154708 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84384919552 available bytes; 95.29% used; 114156093 free inodes.

server3 `/home`: 84384919552 available bytes; 95.29% used; 114156093 free inodes.

server3 `/data`: 150131548160 available bytes; 97.93% used; 225802988 free inodes.

server3 `/tmp`: 84384919552 available bytes; 95.29% used; 114156093 free inodes.

server3 `/var/tmp`: 84384919552 available bytes; 95.29% used; 114156093 free inodes.
| server4 | True | ['1', '4', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105629806592 available bytes; 94.11% used; 114348347 free inodes.

server4 `/home`: 105629806592 available bytes; 94.11% used; 114348347 free inodes.

server4 `/data`: 81656610816 available bytes; 98.87% used; 225252423 free inodes.

server4 `/tmp`: 105629806592 available bytes; 94.11% used; 114348347 free inodes.

server4 `/var/tmp`: 105629806592 available bytes; 94.11% used; 114348347 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
