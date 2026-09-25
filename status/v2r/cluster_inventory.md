# V2R cluster inventory

2026-09-25T22:46:20.982840+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318692110336 available bytes; 82.22% used; 112476293 free inodes.

server1 `/home`: 318692110336 available bytes; 82.22% used; 112476293 free inodes.

server1 `/tmp`: 318692110336 available bytes; 82.22% used; 112476293 free inodes.

server1 `/var/tmp`: 318692110336 available bytes; 82.22% used; 112476293 free inodes.

server1 `/mnt/raid5`: 360210669568 available bytes; 98.35% used; 337538871 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22946070528 available bytes; 98.72% used; 110406228 free inodes.

server2 `/home`: 22946070528 available bytes; 98.72% used; 110406228 free inodes.

server2 `/tmp`: 22946070528 available bytes; 98.72% used; 110406228 free inodes.

server2 `/var/tmp`: 22946070528 available bytes; 98.72% used; 110406228 free inodes.

server2 `/mnt/raid5`: 298501283840 available bytes; 97.94% used; 445052442 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84350808064 available bytes; 95.29% used; 114152432 free inodes.

server3 `/home`: 84350808064 available bytes; 95.29% used; 114152432 free inodes.

server3 `/data`: 124821696512 available bytes; 98.27% used; 225805663 free inodes.

server3 `/tmp`: 84350808064 available bytes; 95.29% used; 114152432 free inodes.

server3 `/var/tmp`: 84350808064 available bytes; 95.29% used; 114152432 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105235550208 available bytes; 94.13% used; 114346964 free inodes.

server4 `/home`: 105235550208 available bytes; 94.13% used; 114346964 free inodes.

server4 `/data`: 192135069696 available bytes; 97.34% used; 224917676 free inodes.

server4 `/tmp`: 105235550208 available bytes; 94.13% used; 114346964 free inodes.

server4 `/var/tmp`: 105235550208 available bytes; 94.13% used; 114346964 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
