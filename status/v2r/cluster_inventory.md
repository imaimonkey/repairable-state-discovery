# V2R cluster inventory

2026-09-25T23:54:39.570214+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318671663104 available bytes; 82.22% used; 112476304 free inodes.

server1 `/home`: 318671663104 available bytes; 82.22% used; 112476304 free inodes.

server1 `/tmp`: 318671663104 available bytes; 82.22% used; 112476304 free inodes.

server1 `/var/tmp`: 318671663104 available bytes; 82.22% used; 112476304 free inodes.

server1 `/mnt/raid5`: 360057978880 available bytes; 98.35% used; 337538531 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22944055296 available bytes; 98.72% used; 110406236 free inodes.

server2 `/home`: 22944055296 available bytes; 98.72% used; 110406236 free inodes.

server2 `/tmp`: 22944055296 available bytes; 98.72% used; 110406236 free inodes.

server2 `/var/tmp`: 22944055296 available bytes; 98.72% used; 110406236 free inodes.

server2 `/mnt/raid5`: 296306135040 available bytes; 97.95% used; 445050135 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84346834944 available bytes; 95.29% used; 114152432 free inodes.

server3 `/home`: 84346834944 available bytes; 95.29% used; 114152432 free inodes.

server3 `/data`: 124802985984 available bytes; 98.28% used; 225811027 free inodes.

server3 `/tmp`: 84346834944 available bytes; 95.29% used; 114152432 free inodes.

server3 `/var/tmp`: 84346834944 available bytes; 95.29% used; 114152432 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105082384384 available bytes; 94.14% used; 114346616 free inodes.

server4 `/home`: 105082384384 available bytes; 94.14% used; 114346616 free inodes.

server4 `/data`: 178213490688 available bytes; 97.54% used; 224917581 free inodes.

server4 `/tmp`: 105082384384 available bytes; 94.14% used; 114346616 free inodes.

server4 `/var/tmp`: 105082384384 available bytes; 94.14% used; 114346616 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
