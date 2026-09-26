# V2R cluster inventory

2026-09-26T04:59:11.841448+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318399152128 available bytes; 82.24% used; 112476288 free inodes.

server1 `/home`: 318399152128 available bytes; 82.24% used; 112476288 free inodes.

server1 `/tmp`: 318399152128 available bytes; 82.24% used; 112476288 free inodes.

server1 `/var/tmp`: 318399152128 available bytes; 82.24% used; 112476288 free inodes.

server1 `/mnt/raid5`: 329930350592 available bytes; 98.49% used; 337544752 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22931488768 available bytes; 98.72% used; 110406204 free inodes.

server2 `/home`: 22931488768 available bytes; 98.72% used; 110406204 free inodes.

server2 `/tmp`: 22931488768 available bytes; 98.72% used; 110406204 free inodes.

server2 `/var/tmp`: 22931488768 available bytes; 98.72% used; 110406204 free inodes.

server2 `/mnt/raid5`: 284123181056 available bytes; 98.04% used; 445049558 free inodes.
| server3 | True | [] | [] |

server3 `/`: 83811135488 available bytes; 95.32% used; 114139101 free inodes.

server3 `/home`: 83811135488 available bytes; 95.32% used; 114139101 free inodes.

server3 `/data`: 124624793600 available bytes; 98.28% used; 225825682 free inodes.

server3 `/tmp`: 83811135488 available bytes; 95.32% used; 114139101 free inodes.

server3 `/var/tmp`: 83811135488 available bytes; 95.32% used; 114139101 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105993207808 available bytes; 94.09% used; 114348206 free inodes.

server4 `/home`: 105993207808 available bytes; 94.09% used; 114348206 free inodes.

server4 `/data`: 106996191232 available bytes; 98.52% used; 224929230 free inodes.

server4 `/tmp`: 105993207808 available bytes; 94.09% used; 114348206 free inodes.

server4 `/var/tmp`: 105993207808 available bytes; 94.09% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
