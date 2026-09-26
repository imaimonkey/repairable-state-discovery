# V2R cluster inventory

2026-09-26T02:56:59.738795+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318418472960 available bytes; 82.24% used; 112476265 free inodes.

server1 `/home`: 318418472960 available bytes; 82.24% used; 112476265 free inodes.

server1 `/tmp`: 318418472960 available bytes; 82.24% used; 112476265 free inodes.

server1 `/var/tmp`: 318418472960 available bytes; 82.24% used; 112476265 free inodes.

server1 `/mnt/raid5`: 331091795968 available bytes; 98.48% used; 337545979 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22934982656 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22934982656 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22934982656 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22934982656 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 288207224832 available bytes; 98.01% used; 445053583 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84309872640 available bytes; 95.30% used; 114152366 free inodes.

server3 `/home`: 84309872640 available bytes; 95.30% used; 114152366 free inodes.

server3 `/data`: 125444726784 available bytes; 98.27% used; 225831256 free inodes.

server3 `/tmp`: 84309872640 available bytes; 95.30% used; 114152366 free inodes.

server3 `/var/tmp`: 84309872640 available bytes; 95.30% used; 114152366 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105918943232 available bytes; 94.09% used; 114347153 free inodes.

server4 `/home`: 105918943232 available bytes; 94.09% used; 114347153 free inodes.

server4 `/data`: 109761191936 available bytes; 98.48% used; 224915380 free inodes.

server4 `/tmp`: 105918943232 available bytes; 94.09% used; 114347153 free inodes.

server4 `/var/tmp`: 105918943232 available bytes; 94.09% used; 114347153 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
