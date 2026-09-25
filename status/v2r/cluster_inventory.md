# V2R cluster inventory

2026-09-25T23:51:36.506965+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318670999552 available bytes; 82.22% used; 112476299 free inodes.

server1 `/home`: 318670999552 available bytes; 82.22% used; 112476299 free inodes.

server1 `/tmp`: 318670999552 available bytes; 82.22% used; 112476299 free inodes.

server1 `/var/tmp`: 318670999552 available bytes; 82.22% used; 112476299 free inodes.

server1 `/mnt/raid5`: 360067362816 available bytes; 98.35% used; 337538556 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22946238464 available bytes; 98.72% used; 110406236 free inodes.

server2 `/home`: 22946238464 available bytes; 98.72% used; 110406236 free inodes.

server2 `/tmp`: 22946238464 available bytes; 98.72% used; 110406236 free inodes.

server2 `/var/tmp`: 22946238464 available bytes; 98.72% used; 110406236 free inodes.

server2 `/mnt/raid5`: 296399908864 available bytes; 97.95% used; 445050343 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84349124608 available bytes; 95.29% used; 114152432 free inodes.

server3 `/home`: 84349124608 available bytes; 95.29% used; 114152432 free inodes.

server3 `/data`: 124807544832 available bytes; 98.28% used; 225811098 free inodes.

server3 `/tmp`: 84349124608 available bytes; 95.29% used; 114152432 free inodes.

server3 `/var/tmp`: 84349124608 available bytes; 95.29% used; 114152432 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105082470400 available bytes; 94.14% used; 114346616 free inodes.

server4 `/home`: 105082470400 available bytes; 94.14% used; 114346616 free inodes.

server4 `/data`: 178221637632 available bytes; 97.54% used; 224917593 free inodes.

server4 `/tmp`: 105082470400 available bytes; 94.14% used; 114346616 free inodes.

server4 `/var/tmp`: 105082470400 available bytes; 94.14% used; 114346616 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
