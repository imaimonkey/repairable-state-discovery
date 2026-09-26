# V2R cluster inventory

2026-09-26T00:14:59.762448+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318669246464 available bytes; 82.22% used; 112476300 free inodes.

server1 `/home`: 318669246464 available bytes; 82.22% used; 112476300 free inodes.

server1 `/tmp`: 318669246464 available bytes; 82.22% used; 112476300 free inodes.

server1 `/var/tmp`: 318669246464 available bytes; 82.22% used; 112476300 free inodes.

server1 `/mnt/raid5`: 359563710464 available bytes; 98.35% used; 337547050 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22948061184 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22948061184 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22948061184 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22948061184 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 275408269312 available bytes; 98.10% used; 445058522 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84341583872 available bytes; 95.29% used; 114152433 free inodes.

server3 `/home`: 84341583872 available bytes; 95.29% used; 114152433 free inodes.

server3 `/data`: 124946567168 available bytes; 98.27% used; 225819312 free inodes.

server3 `/tmp`: 84341583872 available bytes; 95.29% used; 114152433 free inodes.

server3 `/var/tmp`: 84341583872 available bytes; 95.29% used; 114152433 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105453715456 available bytes; 94.12% used; 114348398 free inodes.

server4 `/home`: 105453715456 available bytes; 94.12% used; 114348398 free inodes.

server4 `/data`: 178047590400 available bytes; 97.54% used; 224917551 free inodes.

server4 `/tmp`: 105453715456 available bytes; 94.12% used; 114348398 free inodes.

server4 `/var/tmp`: 105453715456 available bytes; 94.12% used; 114348398 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
