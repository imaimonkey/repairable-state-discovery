# V2R cluster inventory

2026-09-24T21:42:19.134326+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323954511872 available bytes; 81.93% used; 112481419 free inodes.

server1 `/home`: 323954511872 available bytes; 81.93% used; 112481419 free inodes.

server1 `/tmp`: 323954511872 available bytes; 81.93% used; 112481419 free inodes.

server1 `/var/tmp`: 323954511872 available bytes; 81.93% used; 112481419 free inodes.

server1 `/mnt/raid5`: 415475601408 available bytes; 98.09% used; 337626037 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30132006912 available bytes; 98.32% used; 110411316 free inodes.

server2 `/home`: 30132006912 available bytes; 98.32% used; 110411316 free inodes.

server2 `/tmp`: 30132006912 available bytes; 98.32% used; 110411316 free inodes.

server2 `/var/tmp`: 30132006912 available bytes; 98.32% used; 110411316 free inodes.

server2 `/mnt/raid5`: 490032742400 available bytes; 96.61% used; 445154758 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84384317440 available bytes; 95.29% used; 114156093 free inodes.

server3 `/home`: 84384317440 available bytes; 95.29% used; 114156093 free inodes.

server3 `/data`: 150106562560 available bytes; 97.93% used; 225802970 free inodes.

server3 `/tmp`: 84384317440 available bytes; 95.29% used; 114156093 free inodes.

server3 `/var/tmp`: 84384317440 available bytes; 95.29% used; 114156093 free inodes.
| server4 | True | ['1', '4', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105629761536 available bytes; 94.11% used; 114348346 free inodes.

server4 `/home`: 105629761536 available bytes; 94.11% used; 114348346 free inodes.

server4 `/data`: 81551110144 available bytes; 98.87% used; 225252396 free inodes.

server4 `/tmp`: 105629761536 available bytes; 94.11% used; 114348346 free inodes.

server4 `/var/tmp`: 105629761536 available bytes; 94.11% used; 114348346 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
