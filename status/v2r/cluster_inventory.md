# V2R cluster inventory

2026-09-24T21:37:42.378724+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323955294208 available bytes; 81.93% used; 112481418 free inodes.

server1 `/home`: 323955294208 available bytes; 81.93% used; 112481418 free inodes.

server1 `/tmp`: 323955294208 available bytes; 81.93% used; 112481418 free inodes.

server1 `/var/tmp`: 323955294208 available bytes; 81.93% used; 112481418 free inodes.

server1 `/mnt/raid5`: 415485546496 available bytes; 98.09% used; 337626573 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30137958400 available bytes; 98.32% used; 110411334 free inodes.

server2 `/home`: 30137958400 available bytes; 98.32% used; 110411334 free inodes.

server2 `/tmp`: 30137958400 available bytes; 98.32% used; 110411334 free inodes.

server2 `/var/tmp`: 30137958400 available bytes; 98.32% used; 110411334 free inodes.

server2 `/mnt/raid5`: 489641885696 available bytes; 96.62% used; 445155003 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84385751040 available bytes; 95.29% used; 114156093 free inodes.

server3 `/home`: 84385751040 available bytes; 95.29% used; 114156093 free inodes.

server3 `/data`: 150182096896 available bytes; 97.92% used; 225803052 free inodes.

server3 `/tmp`: 84385751040 available bytes; 95.29% used; 114156093 free inodes.

server3 `/var/tmp`: 84385751040 available bytes; 95.29% used; 114156093 free inodes.
| server4 | True | ['1', '4', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105629913088 available bytes; 94.11% used; 114348348 free inodes.

server4 `/home`: 105629913088 available bytes; 94.11% used; 114348348 free inodes.

server4 `/data`: 82784677888 available bytes; 98.86% used; 225252463 free inodes.

server4 `/tmp`: 105629913088 available bytes; 94.11% used; 114348348 free inodes.

server4 `/var/tmp`: 105629913088 available bytes; 94.11% used; 114348348 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
