# V2R cluster inventory

2026-09-25T22:55:30.997998+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318695387136 available bytes; 82.22% used; 112476299 free inodes.

server1 `/home`: 318695387136 available bytes; 82.22% used; 112476299 free inodes.

server1 `/tmp`: 318695387136 available bytes; 82.22% used; 112476299 free inodes.

server1 `/var/tmp`: 318695387136 available bytes; 82.22% used; 112476299 free inodes.

server1 `/mnt/raid5`: 360187170816 available bytes; 98.35% used; 337538817 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22945697792 available bytes; 98.72% used; 110406228 free inodes.

server2 `/home`: 22945697792 available bytes; 98.72% used; 110406228 free inodes.

server2 `/tmp`: 22945697792 available bytes; 98.72% used; 110406228 free inodes.

server2 `/var/tmp`: 22945697792 available bytes; 98.72% used; 110406228 free inodes.

server2 `/mnt/raid5`: 298240454656 available bytes; 97.94% used; 445052153 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84351725568 available bytes; 95.29% used; 114152434 free inodes.

server3 `/home`: 84351725568 available bytes; 95.29% used; 114152434 free inodes.

server3 `/data`: 124823400448 available bytes; 98.27% used; 225805529 free inodes.

server3 `/tmp`: 84351725568 available bytes; 95.29% used; 114152434 free inodes.

server3 `/var/tmp`: 84351725568 available bytes; 95.29% used; 114152434 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105201721344 available bytes; 94.13% used; 114346877 free inodes.

server4 `/home`: 105201721344 available bytes; 94.13% used; 114346877 free inodes.

server4 `/data`: 188681101312 available bytes; 97.39% used; 224917669 free inodes.

server4 `/tmp`: 105201721344 available bytes; 94.13% used; 114346877 free inodes.

server4 `/var/tmp`: 105201721344 available bytes; 94.13% used; 114346877 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
