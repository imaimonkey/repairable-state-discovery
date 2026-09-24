# V2R cluster inventory

2026-09-24T20:14:07.306113+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323988770816 available bytes; 81.93% used; 112481427 free inodes.

server1 `/home`: 323988770816 available bytes; 81.93% used; 112481427 free inodes.

server1 `/tmp`: 323988770816 available bytes; 81.93% used; 112481427 free inodes.

server1 `/var/tmp`: 323988770816 available bytes; 81.93% used; 112481427 free inodes.

server1 `/mnt/raid5`: 415524290560 available bytes; 98.09% used; 337627224 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30177591296 available bytes; 98.32% used; 110411378 free inodes.

server2 `/home`: 30177591296 available bytes; 98.32% used; 110411378 free inodes.

server2 `/tmp`: 30177591296 available bytes; 98.32% used; 110411378 free inodes.

server2 `/var/tmp`: 30177591296 available bytes; 98.32% used; 110411378 free inodes.

server2 `/mnt/raid5`: 493373546496 available bytes; 96.59% used; 445157325 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84399140864 available bytes; 95.29% used; 114156117 free inodes.

server3 `/home`: 84399140864 available bytes; 95.29% used; 114156117 free inodes.

server3 `/data`: 151689854976 available bytes; 97.90% used; 225798676 free inodes.

server3 `/tmp`: 84399140864 available bytes; 95.29% used; 114156117 free inodes.

server3 `/var/tmp`: 84399140864 available bytes; 95.29% used; 114156117 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105641156608 available bytes; 94.10% used; 114348411 free inodes.

server4 `/home`: 105641156608 available bytes; 94.10% used; 114348411 free inodes.

server4 `/data`: 89782464512 available bytes; 98.76% used; 225266046 free inodes.

server4 `/tmp`: 105641156608 available bytes; 94.10% used; 114348411 free inodes.

server4 `/var/tmp`: 105641156608 available bytes; 94.10% used; 114348411 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
