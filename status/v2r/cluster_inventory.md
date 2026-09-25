# V2R cluster inventory

2026-09-25T22:21:54.289957+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318696747008 available bytes; 82.22% used; 112476299 free inodes.

server1 `/home`: 318696747008 available bytes; 82.22% used; 112476299 free inodes.

server1 `/tmp`: 318696747008 available bytes; 82.22% used; 112476299 free inodes.

server1 `/var/tmp`: 318696747008 available bytes; 82.22% used; 112476299 free inodes.

server1 `/mnt/raid5`: 360261373952 available bytes; 98.35% used; 337538984 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22946897920 available bytes; 98.72% used; 110406236 free inodes.

server2 `/home`: 22946897920 available bytes; 98.72% used; 110406236 free inodes.

server2 `/tmp`: 22946897920 available bytes; 98.72% used; 110406236 free inodes.

server2 `/var/tmp`: 22946897920 available bytes; 98.72% used; 110406236 free inodes.

server2 `/mnt/raid5`: 299228598272 available bytes; 97.93% used; 445053428 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84354105344 available bytes; 95.29% used; 114152498 free inodes.

server3 `/home`: 84354105344 available bytes; 95.29% used; 114152498 free inodes.

server3 `/data`: 124829728768 available bytes; 98.27% used; 225806107 free inodes.

server3 `/tmp`: 84354105344 available bytes; 95.29% used; 114152498 free inodes.

server3 `/var/tmp`: 84354105344 available bytes; 95.29% used; 114152498 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105311846400 available bytes; 94.12% used; 114347134 free inodes.

server4 `/home`: 105311846400 available bytes; 94.12% used; 114347134 free inodes.

server4 `/data`: 200405557248 available bytes; 97.23% used; 224917838 free inodes.

server4 `/tmp`: 105311846400 available bytes; 94.12% used; 114347134 free inodes.

server4 `/var/tmp`: 105311846400 available bytes; 94.12% used; 114347134 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
