# V2R cluster inventory

2026-09-24T05:25:52.127768+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324555218944 available bytes; 81.89% used; 112492420 free inodes.

server1 `/home`: 324555218944 available bytes; 81.89% used; 112492420 free inodes.

server1 `/tmp`: 324555218944 available bytes; 81.89% used; 112492420 free inodes.

server1 `/var/tmp`: 324555218944 available bytes; 81.89% used; 112492420 free inodes.

server1 `/mnt/raid5`: 512591749120 available bytes; 97.65% used; 337724317 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57169682432 available bytes; 96.81% used; 110431201 free inodes.

server2 `/home`: 57169682432 available bytes; 96.81% used; 110431201 free inodes.

server2 `/tmp`: 57169682432 available bytes; 96.81% used; 110431201 free inodes.

server2 `/var/tmp`: 57169682432 available bytes; 96.81% used; 110431201 free inodes.

server2 `/mnt/raid5`: 522528190464 available bytes; 96.39% used; 445194006 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 271728926720 available bytes; 84.84% used; 114199740 free inodes.

server3 `/home`: 271728926720 available bytes; 84.84% used; 114199740 free inodes.

server3 `/data`: 21146718208 available bytes; 99.71% used; 225839724 free inodes.

server3 `/tmp`: 271728926720 available bytes; 84.84% used; 114199740 free inodes.

server3 `/var/tmp`: 271728926720 available bytes; 84.84% used; 114199740 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105817276416 available bytes; 94.10% used; 114349367 free inodes.

server4 `/home`: 105817276416 available bytes; 94.10% used; 114349367 free inodes.

server4 `/data`: 252562575360 available bytes; 96.51% used; 225366549 free inodes.

server4 `/tmp`: 105817276416 available bytes; 94.10% used; 114349367 free inodes.

server4 `/var/tmp`: 105817276416 available bytes; 94.10% used; 114349367 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
