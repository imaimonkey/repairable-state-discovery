# V2R cluster inventory

2026-09-24T20:06:24.045771+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323990310912 available bytes; 81.93% used; 112481421 free inodes.

server1 `/home`: 323990310912 available bytes; 81.93% used; 112481421 free inodes.

server1 `/tmp`: 323990310912 available bytes; 81.93% used; 112481421 free inodes.

server1 `/var/tmp`: 323990310912 available bytes; 81.93% used; 112481421 free inodes.

server1 `/mnt/raid5`: 415538745344 available bytes; 98.09% used; 337628136 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30174793728 available bytes; 98.32% used; 110411378 free inodes.

server2 `/home`: 30174793728 available bytes; 98.32% used; 110411378 free inodes.

server2 `/tmp`: 30174793728 available bytes; 98.32% used; 110411378 free inodes.

server2 `/var/tmp`: 30174793728 available bytes; 98.32% used; 110411378 free inodes.

server2 `/mnt/raid5`: 493616021504 available bytes; 96.59% used; 445157568 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84400582656 available bytes; 95.29% used; 114156128 free inodes.

server3 `/home`: 84400582656 available bytes; 95.29% used; 114156128 free inodes.

server3 `/data`: 151821094912 available bytes; 97.90% used; 225798818 free inodes.

server3 `/tmp`: 84400582656 available bytes; 95.29% used; 114156128 free inodes.

server3 `/var/tmp`: 84400582656 available bytes; 95.29% used; 114156128 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105641381888 available bytes; 94.10% used; 114348411 free inodes.

server4 `/home`: 105641381888 available bytes; 94.10% used; 114348411 free inodes.

server4 `/data`: 89805733888 available bytes; 98.76% used; 225266243 free inodes.

server4 `/tmp`: 105641381888 available bytes; 94.10% used; 114348411 free inodes.

server4 `/var/tmp`: 105641381888 available bytes; 94.10% used; 114348411 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
