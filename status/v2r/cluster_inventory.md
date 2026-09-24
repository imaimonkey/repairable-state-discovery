# V2R cluster inventory

2026-09-24T20:31:05.259351+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323982868480 available bytes; 81.93% used; 112481438 free inodes.

server1 `/home`: 323982868480 available bytes; 81.93% used; 112481438 free inodes.

server1 `/tmp`: 323982868480 available bytes; 81.93% used; 112481438 free inodes.

server1 `/var/tmp`: 323982868480 available bytes; 81.93% used; 112481438 free inodes.

server1 `/mnt/raid5`: 415622000640 available bytes; 98.09% used; 337634327 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30159192064 available bytes; 98.32% used; 110411378 free inodes.

server2 `/home`: 30159192064 available bytes; 98.32% used; 110411378 free inodes.

server2 `/tmp`: 30159192064 available bytes; 98.32% used; 110411378 free inodes.

server2 `/var/tmp`: 30159192064 available bytes; 98.32% used; 110411378 free inodes.

server2 `/mnt/raid5`: 492239769600 available bytes; 96.60% used; 445157164 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84397694976 available bytes; 95.29% used; 114156102 free inodes.

server3 `/home`: 84397694976 available bytes; 95.29% used; 114156102 free inodes.

server3 `/data`: 151453773824 available bytes; 97.91% used; 225804369 free inodes.

server3 `/tmp`: 84397694976 available bytes; 95.29% used; 114156102 free inodes.

server3 `/var/tmp`: 84397694976 available bytes; 95.29% used; 114156102 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105640374272 available bytes; 94.10% used; 114348390 free inodes.

server4 `/home`: 105640374272 available bytes; 94.10% used; 114348390 free inodes.

server4 `/data`: 85468823552 available bytes; 98.82% used; 225257764 free inodes.

server4 `/tmp`: 105640374272 available bytes; 94.10% used; 114348390 free inodes.

server4 `/var/tmp`: 105640374272 available bytes; 94.10% used; 114348390 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
