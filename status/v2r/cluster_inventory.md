# V2R cluster inventory

2026-09-25T23:18:28.198081+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318682726400 available bytes; 82.22% used; 112476296 free inodes.

server1 `/home`: 318682726400 available bytes; 82.22% used; 112476296 free inodes.

server1 `/tmp`: 318682726400 available bytes; 82.22% used; 112476296 free inodes.

server1 `/var/tmp`: 318682726400 available bytes; 82.22% used; 112476296 free inodes.

server1 `/mnt/raid5`: 360137695232 available bytes; 98.35% used; 337538713 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22945976320 available bytes; 98.72% used; 110406230 free inodes.

server2 `/home`: 22945976320 available bytes; 98.72% used; 110406230 free inodes.

server2 `/tmp`: 22945976320 available bytes; 98.72% used; 110406230 free inodes.

server2 `/var/tmp`: 22945976320 available bytes; 98.72% used; 110406230 free inodes.

server2 `/mnt/raid5`: 297640771584 available bytes; 97.94% used; 445051485 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84348256256 available bytes; 95.29% used; 114152434 free inodes.

server3 `/home`: 84348256256 available bytes; 95.29% used; 114152434 free inodes.

server3 `/data`: 124752080896 available bytes; 98.28% used; 225805119 free inodes.

server3 `/tmp`: 84348256256 available bytes; 95.29% used; 114152434 free inodes.

server3 `/var/tmp`: 84348256256 available bytes; 95.29% used; 114152434 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105159041024 available bytes; 94.13% used; 114346790 free inodes.

server4 `/home`: 105159041024 available bytes; 94.13% used; 114346790 free inodes.

server4 `/data`: 185129734144 available bytes; 97.44% used; 224917632 free inodes.

server4 `/tmp`: 105159041024 available bytes; 94.13% used; 114346790 free inodes.

server4 `/var/tmp`: 105159041024 available bytes; 94.13% used; 114346790 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
