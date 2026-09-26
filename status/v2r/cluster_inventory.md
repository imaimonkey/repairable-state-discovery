# V2R cluster inventory

2026-09-26T01:13:02.242020+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318658019328 available bytes; 82.22% used; 112476294 free inodes.

server1 `/home`: 318658019328 available bytes; 82.22% used; 112476294 free inodes.

server1 `/tmp`: 318658019328 available bytes; 82.22% used; 112476294 free inodes.

server1 `/var/tmp`: 318658019328 available bytes; 82.22% used; 112476294 free inodes.

server1 `/mnt/raid5`: 345535959040 available bytes; 98.41% used; 337546632 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22938947584 available bytes; 98.72% used; 110406202 free inodes.

server2 `/home`: 22938947584 available bytes; 98.72% used; 110406202 free inodes.

server2 `/tmp`: 22938947584 available bytes; 98.72% used; 110406202 free inodes.

server2 `/var/tmp`: 22938947584 available bytes; 98.72% used; 110406202 free inodes.

server2 `/mnt/raid5`: 290683871232 available bytes; 97.99% used; 445056373 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340019200 available bytes; 95.29% used; 114152428 free inodes.

server3 `/home`: 84340019200 available bytes; 95.29% used; 114152428 free inodes.

server3 `/data`: 124936478720 available bytes; 98.27% used; 225818321 free inodes.

server3 `/tmp`: 84340019200 available bytes; 95.29% used; 114152428 free inodes.

server3 `/var/tmp`: 84340019200 available bytes; 95.29% used; 114152428 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105281400832 available bytes; 94.12% used; 114347079 free inodes.

server4 `/home`: 105281400832 available bytes; 94.12% used; 114347079 free inodes.

server4 `/data`: 141692018688 available bytes; 98.04% used; 224917308 free inodes.

server4 `/tmp`: 105281400832 available bytes; 94.12% used; 114347079 free inodes.

server4 `/var/tmp`: 105281400832 available bytes; 94.12% used; 114347079 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
