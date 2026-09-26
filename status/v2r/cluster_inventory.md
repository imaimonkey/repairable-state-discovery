# V2R cluster inventory

2026-09-25T23:59:43.042207+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318672031744 available bytes; 82.22% used; 112476306 free inodes.

server1 `/home`: 318672031744 available bytes; 82.22% used; 112476306 free inodes.

server1 `/tmp`: 318672031744 available bytes; 82.22% used; 112476306 free inodes.

server1 `/var/tmp`: 318672031744 available bytes; 82.22% used; 112476306 free inodes.

server1 `/mnt/raid5`: 360011829248 available bytes; 98.35% used; 337538505 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22943854592 available bytes; 98.72% used; 110406236 free inodes.

server2 `/home`: 22943854592 available bytes; 98.72% used; 110406236 free inodes.

server2 `/tmp`: 22943854592 available bytes; 98.72% used; 110406236 free inodes.

server2 `/var/tmp`: 22943854592 available bytes; 98.72% used; 110406236 free inodes.

server2 `/mnt/raid5`: 296164671488 available bytes; 97.95% used; 445050099 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84347981824 available bytes; 95.29% used; 114152432 free inodes.

server3 `/home`: 84347981824 available bytes; 95.29% used; 114152432 free inodes.

server3 `/data`: 124801392640 available bytes; 98.28% used; 225810934 free inodes.

server3 `/tmp`: 84347981824 available bytes; 95.29% used; 114152432 free inodes.

server3 `/var/tmp`: 84347981824 available bytes; 95.29% used; 114152432 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105082220544 available bytes; 94.14% used; 114346614 free inodes.

server4 `/home`: 105082220544 available bytes; 94.14% used; 114346614 free inodes.

server4 `/data`: 178136223744 available bytes; 97.54% used; 224917574 free inodes.

server4 `/tmp`: 105082220544 available bytes; 94.14% used; 114346614 free inodes.

server4 `/var/tmp`: 105082220544 available bytes; 94.14% used; 114346614 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
