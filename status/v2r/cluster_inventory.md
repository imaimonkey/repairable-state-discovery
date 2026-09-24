# V2R cluster inventory

2026-09-24T05:02:13.840220+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324613234688 available bytes; 81.89% used; 112492680 free inodes.

server1 `/home`: 324613234688 available bytes; 81.89% used; 112492680 free inodes.

server1 `/tmp`: 324613234688 available bytes; 81.89% used; 112492680 free inodes.

server1 `/var/tmp`: 324613234688 available bytes; 81.89% used; 112492680 free inodes.

server1 `/mnt/raid5`: 469509689344 available bytes; 97.85% used; 337724570 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40758521856 available bytes; 97.73% used; 110430404 free inodes.

server2 `/home`: 40758521856 available bytes; 97.73% used; 110430404 free inodes.

server2 `/tmp`: 40758521856 available bytes; 97.73% used; 110430404 free inodes.

server2 `/var/tmp`: 40758521856 available bytes; 97.73% used; 110430404 free inodes.

server2 `/mnt/raid5`: 523530534912 available bytes; 96.38% used; 445194911 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 291673358336 available bytes; 83.72% used; 114162087 free inodes.

server3 `/home`: 291673358336 available bytes; 83.72% used; 114162087 free inodes.

server3 `/data`: 23295401984 available bytes; 99.68% used; 225840395 free inodes.

server3 `/tmp`: 291673358336 available bytes; 83.72% used; 114162087 free inodes.

server3 `/var/tmp`: 291673358336 available bytes; 83.72% used; 114162087 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105826869248 available bytes; 94.09% used; 114349383 free inodes.

server4 `/home`: 105826869248 available bytes; 94.09% used; 114349383 free inodes.

server4 `/data`: 252701626368 available bytes; 96.51% used; 225366802 free inodes.

server4 `/tmp`: 105826869248 available bytes; 94.09% used; 114349383 free inodes.

server4 `/var/tmp`: 105826869248 available bytes; 94.09% used; 114349383 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
