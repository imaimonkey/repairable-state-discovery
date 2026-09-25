# V2R cluster inventory

2026-09-25T22:31:04.103304+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318694641664 available bytes; 82.22% used; 112476313 free inodes.

server1 `/home`: 318694641664 available bytes; 82.22% used; 112476313 free inodes.

server1 `/tmp`: 318694641664 available bytes; 82.22% used; 112476313 free inodes.

server1 `/var/tmp`: 318694641664 available bytes; 82.22% used; 112476313 free inodes.

server1 `/mnt/raid5`: 360243990528 available bytes; 98.35% used; 337538938 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22953639936 available bytes; 98.72% used; 110406238 free inodes.

server2 `/home`: 22953639936 available bytes; 98.72% used; 110406238 free inodes.

server2 `/tmp`: 22953639936 available bytes; 98.72% used; 110406238 free inodes.

server2 `/var/tmp`: 22953639936 available bytes; 98.72% used; 110406238 free inodes.

server2 `/mnt/raid5`: 298395123712 available bytes; 97.94% used; 445052883 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84353531904 available bytes; 95.29% used; 114152428 free inodes.

server3 `/home`: 84353531904 available bytes; 95.29% used; 114152428 free inodes.

server3 `/data`: 124826492928 available bytes; 98.27% used; 225805928 free inodes.

server3 `/tmp`: 84353531904 available bytes; 95.29% used; 114152428 free inodes.

server3 `/var/tmp`: 84353531904 available bytes; 95.29% used; 114152428 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105244401664 available bytes; 94.13% used; 114346967 free inodes.

server4 `/home`: 105244401664 available bytes; 94.13% used; 114346967 free inodes.

server4 `/data`: 192242941952 available bytes; 97.34% used; 224917722 free inodes.

server4 `/tmp`: 105244401664 available bytes; 94.13% used; 114346967 free inodes.

server4 `/var/tmp`: 105244401664 available bytes; 94.13% used; 114346967 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
