# V2R cluster inventory

2026-09-26T05:06:50.090772+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318399012864 available bytes; 82.24% used; 112476272 free inodes.

server1 `/home`: 318399012864 available bytes; 82.24% used; 112476272 free inodes.

server1 `/tmp`: 318399012864 available bytes; 82.24% used; 112476272 free inodes.

server1 `/var/tmp`: 318399012864 available bytes; 82.24% used; 112476272 free inodes.

server1 `/mnt/raid5`: 326819028992 available bytes; 98.50% used; 337544523 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22928592896 available bytes; 98.72% used; 110406196 free inodes.

server2 `/home`: 22928592896 available bytes; 98.72% used; 110406196 free inodes.

server2 `/tmp`: 22928592896 available bytes; 98.72% used; 110406196 free inodes.

server2 `/var/tmp`: 22928592896 available bytes; 98.72% used; 110406196 free inodes.

server2 `/mnt/raid5`: 284413812736 available bytes; 98.03% used; 445049470 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84081901568 available bytes; 95.31% used; 114165828 free inodes.

server3 `/home`: 84081901568 available bytes; 95.31% used; 114165828 free inodes.

server3 `/data`: 124608794624 available bytes; 98.28% used; 225825352 free inodes.

server3 `/tmp`: 84081901568 available bytes; 95.31% used; 114165828 free inodes.

server3 `/var/tmp`: 84081901568 available bytes; 95.31% used; 114165828 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105992962048 available bytes; 94.09% used; 114348206 free inodes.

server4 `/home`: 105992962048 available bytes; 94.09% used; 114348206 free inodes.

server4 `/data`: 106999971840 available bytes; 98.52% used; 224929220 free inodes.

server4 `/tmp`: 105992962048 available bytes; 94.09% used; 114348206 free inodes.

server4 `/var/tmp`: 105992962048 available bytes; 94.09% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
