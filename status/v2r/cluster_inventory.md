# V2R cluster inventory

2026-09-26T05:03:46.766896+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318397923328 available bytes; 82.24% used; 112476272 free inodes.

server1 `/home`: 318397923328 available bytes; 82.24% used; 112476272 free inodes.

server1 `/tmp`: 318397923328 available bytes; 82.24% used; 112476272 free inodes.

server1 `/var/tmp`: 318397923328 available bytes; 82.24% used; 112476272 free inodes.

server1 `/mnt/raid5`: 329913266176 available bytes; 98.49% used; 337544696 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22929158144 available bytes; 98.72% used; 110406196 free inodes.

server2 `/home`: 22929158144 available bytes; 98.72% used; 110406196 free inodes.

server2 `/tmp`: 22929158144 available bytes; 98.72% used; 110406196 free inodes.

server2 `/var/tmp`: 22929158144 available bytes; 98.72% used; 110406196 free inodes.

server2 `/mnt/raid5`: 284502736896 available bytes; 98.03% used; 445049666 free inodes.
| server3 | True | [] | [] |

server3 `/`: 83811704832 available bytes; 95.32% used; 114139133 free inodes.

server3 `/home`: 83811704832 available bytes; 95.32% used; 114139133 free inodes.

server3 `/data`: 124615581696 available bytes; 98.28% used; 225825531 free inodes.

server3 `/tmp`: 83811704832 available bytes; 95.32% used; 114139133 free inodes.

server3 `/var/tmp`: 83811704832 available bytes; 95.32% used; 114139133 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105993060352 available bytes; 94.09% used; 114348206 free inodes.

server4 `/home`: 105993060352 available bytes; 94.09% used; 114348206 free inodes.

server4 `/data`: 107001065472 available bytes; 98.52% used; 224929215 free inodes.

server4 `/tmp`: 105993060352 available bytes; 94.09% used; 114348206 free inodes.

server4 `/var/tmp`: 105993060352 available bytes; 94.09% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
