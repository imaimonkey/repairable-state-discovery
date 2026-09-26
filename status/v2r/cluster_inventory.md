# V2R cluster inventory

2026-09-26T04:54:37.015803+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318400430080 available bytes; 82.24% used; 112476282 free inodes.

server1 `/home`: 318400430080 available bytes; 82.24% used; 112476282 free inodes.

server1 `/tmp`: 318400430080 available bytes; 82.24% used; 112476282 free inodes.

server1 `/var/tmp`: 318400430080 available bytes; 82.24% used; 112476282 free inodes.

server1 `/mnt/raid5`: 330462355456 available bytes; 98.48% used; 337545334 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22937792512 available bytes; 98.72% used; 110406196 free inodes.

server2 `/home`: 22937792512 available bytes; 98.72% used; 110406196 free inodes.

server2 `/tmp`: 22937792512 available bytes; 98.72% used; 110406196 free inodes.

server2 `/var/tmp`: 22937792512 available bytes; 98.72% used; 110406196 free inodes.

server2 `/mnt/raid5`: 284260720640 available bytes; 98.04% used; 445049867 free inodes.
| server3 | True | [] | [] |

server3 `/`: 83811696640 available bytes; 95.32% used; 114139100 free inodes.

server3 `/home`: 83811696640 available bytes; 95.32% used; 114139100 free inodes.

server3 `/data`: 124381065216 available bytes; 98.28% used; 225816505 free inodes.

server3 `/tmp`: 83811696640 available bytes; 95.32% used; 114139100 free inodes.

server3 `/var/tmp`: 83811696640 available bytes; 95.32% used; 114139100 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106001711104 available bytes; 94.08% used; 114348206 free inodes.

server4 `/home`: 106001711104 available bytes; 94.08% used; 114348206 free inodes.

server4 `/data`: 107025731584 available bytes; 98.52% used; 224929298 free inodes.

server4 `/tmp`: 106001711104 available bytes; 94.08% used; 114348206 free inodes.

server4 `/var/tmp`: 106001711104 available bytes; 94.08% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
