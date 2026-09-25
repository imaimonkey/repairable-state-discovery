# V2R cluster inventory

2026-09-25T23:18:01.673905+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318683025408 available bytes; 82.22% used; 112476296 free inodes.

server1 `/home`: 318683025408 available bytes; 82.22% used; 112476296 free inodes.

server1 `/tmp`: 318683025408 available bytes; 82.22% used; 112476296 free inodes.

server1 `/var/tmp`: 318683025408 available bytes; 82.22% used; 112476296 free inodes.

server1 `/mnt/raid5`: 360138240000 available bytes; 98.35% used; 337538713 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22946385920 available bytes; 98.72% used; 110406232 free inodes.

server2 `/home`: 22946385920 available bytes; 98.72% used; 110406232 free inodes.

server2 `/tmp`: 22946385920 available bytes; 98.72% used; 110406232 free inodes.

server2 `/var/tmp`: 22946385920 available bytes; 98.72% used; 110406232 free inodes.

server2 `/mnt/raid5`: 297663090688 available bytes; 97.94% used; 445051522 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84348567552 available bytes; 95.29% used; 114152434 free inodes.

server3 `/home`: 84348567552 available bytes; 95.29% used; 114152434 free inodes.

server3 `/data`: 124752605184 available bytes; 98.28% used; 225805137 free inodes.

server3 `/tmp`: 84348567552 available bytes; 95.29% used; 114152434 free inodes.

server3 `/var/tmp`: 84348567552 available bytes; 95.29% used; 114152434 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105159057408 available bytes; 94.13% used; 114346790 free inodes.

server4 `/home`: 105159057408 available bytes; 94.13% used; 114346790 free inodes.

server4 `/data`: 185129746432 available bytes; 97.44% used; 224917632 free inodes.

server4 `/tmp`: 105159057408 available bytes; 94.13% used; 114346790 free inodes.

server4 `/var/tmp`: 105159057408 available bytes; 94.13% used; 114346790 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
