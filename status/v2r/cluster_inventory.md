# V2R cluster inventory

2026-09-25T23:41:23.131083+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318672723968 available bytes; 82.22% used; 112476310 free inodes.

server1 `/home`: 318672723968 available bytes; 82.22% used; 112476310 free inodes.

server1 `/tmp`: 318672723968 available bytes; 82.22% used; 112476310 free inodes.

server1 `/var/tmp`: 318672723968 available bytes; 82.22% used; 112476310 free inodes.

server1 `/mnt/raid5`: 360091193344 available bytes; 98.35% used; 337538601 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22950789120 available bytes; 98.72% used; 110406238 free inodes.

server2 `/home`: 22950789120 available bytes; 98.72% used; 110406238 free inodes.

server2 `/tmp`: 22950789120 available bytes; 98.72% used; 110406238 free inodes.

server2 `/var/tmp`: 22950789120 available bytes; 98.72% used; 110406238 free inodes.

server2 `/mnt/raid5`: 296697004032 available bytes; 97.95% used; 445050912 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84351922176 available bytes; 95.29% used; 114152440 free inodes.

server3 `/home`: 84351922176 available bytes; 95.29% used; 114152440 free inodes.

server3 `/data`: 124806045696 available bytes; 98.28% used; 225811305 free inodes.

server3 `/tmp`: 84351922176 available bytes; 95.29% used; 114152440 free inodes.

server3 `/var/tmp`: 84351922176 available bytes; 95.29% used; 114152440 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105082777600 available bytes; 94.14% used; 114346616 free inodes.

server4 `/home`: 105082777600 available bytes; 94.14% used; 114346616 free inodes.

server4 `/data`: 178220654592 available bytes; 97.54% used; 224917594 free inodes.

server4 `/tmp`: 105082777600 available bytes; 94.14% used; 114346616 free inodes.

server4 `/var/tmp`: 105082777600 available bytes; 94.14% used; 114346616 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
