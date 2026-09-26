# V2R cluster inventory

2026-09-26T04:56:08.557809+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318399942656 available bytes; 82.24% used; 112476282 free inodes.

server1 `/home`: 318399942656 available bytes; 82.24% used; 112476282 free inodes.

server1 `/tmp`: 318399942656 available bytes; 82.24% used; 112476282 free inodes.

server1 `/var/tmp`: 318399942656 available bytes; 82.24% used; 112476282 free inodes.

server1 `/mnt/raid5`: 309811269632 available bytes; 98.58% used; 337545322 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22937927680 available bytes; 98.72% used; 110406198 free inodes.

server2 `/home`: 22937927680 available bytes; 98.72% used; 110406198 free inodes.

server2 `/tmp`: 22937927680 available bytes; 98.72% used; 110406198 free inodes.

server2 `/var/tmp`: 22937927680 available bytes; 98.72% used; 110406198 free inodes.

server2 `/mnt/raid5`: 284745052160 available bytes; 98.03% used; 445049704 free inodes.
| server3 | True | [] | [] |

server3 `/`: 83811405824 available bytes; 95.32% used; 114139095 free inodes.

server3 `/home`: 83811405824 available bytes; 95.32% used; 114139095 free inodes.

server3 `/data`: 124619440128 available bytes; 98.28% used; 225825731 free inodes.

server3 `/tmp`: 83811405824 available bytes; 95.32% used; 114139095 free inodes.

server3 `/var/tmp`: 83811405824 available bytes; 95.32% used; 114139095 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105993277440 available bytes; 94.09% used; 114348206 free inodes.

server4 `/home`: 105993277440 available bytes; 94.09% used; 114348206 free inodes.

server4 `/data`: 106998206464 available bytes; 98.52% used; 224929242 free inodes.

server4 `/tmp`: 105993277440 available bytes; 94.09% used; 114348206 free inodes.

server4 `/var/tmp`: 105993277440 available bytes; 94.09% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
