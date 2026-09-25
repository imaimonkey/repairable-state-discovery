# V2R cluster inventory

2026-09-25T23:36:48.201953+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318673850368 available bytes; 82.22% used; 112476314 free inodes.

server1 `/home`: 318673850368 available bytes; 82.22% used; 112476314 free inodes.

server1 `/tmp`: 318673850368 available bytes; 82.22% used; 112476314 free inodes.

server1 `/var/tmp`: 318673850368 available bytes; 82.22% used; 112476314 free inodes.

server1 `/mnt/raid5`: 360099143680 available bytes; 98.35% used; 337538610 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22952583168 available bytes; 98.72% used; 110406236 free inodes.

server2 `/home`: 22952583168 available bytes; 98.72% used; 110406236 free inodes.

server2 `/tmp`: 22952583168 available bytes; 98.72% used; 110406236 free inodes.

server2 `/var/tmp`: 22952583168 available bytes; 98.72% used; 110406236 free inodes.

server2 `/mnt/raid5`: 296810893312 available bytes; 97.95% used; 445050688 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84352630784 available bytes; 95.29% used; 114152440 free inodes.

server3 `/home`: 84352630784 available bytes; 95.29% used; 114152440 free inodes.

server3 `/data`: 124804259840 available bytes; 98.28% used; 225811397 free inodes.

server3 `/tmp`: 84352630784 available bytes; 95.29% used; 114152440 free inodes.

server3 `/var/tmp`: 84352630784 available bytes; 95.29% used; 114152440 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105082925056 available bytes; 94.14% used; 114346616 free inodes.

server4 `/home`: 105082925056 available bytes; 94.14% used; 114346616 free inodes.

server4 `/data`: 178221846528 available bytes; 97.54% used; 224917598 free inodes.

server4 `/tmp`: 105082925056 available bytes; 94.14% used; 114346616 free inodes.

server4 `/var/tmp`: 105082925056 available bytes; 94.14% used; 114346616 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
