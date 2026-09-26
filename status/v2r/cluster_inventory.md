# V2R cluster inventory

2026-09-26T03:36:43.042642+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318416052224 available bytes; 82.24% used; 112476265 free inodes.

server1 `/home`: 318416052224 available bytes; 82.24% used; 112476265 free inodes.

server1 `/tmp`: 318416052224 available bytes; 82.24% used; 112476265 free inodes.

server1 `/var/tmp`: 318416052224 available bytes; 82.24% used; 112476265 free inodes.

server1 `/mnt/raid5`: 331005272064 available bytes; 98.48% used; 337545781 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22938951680 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22938951680 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22938951680 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22938951680 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 287040782336 available bytes; 98.02% used; 445052244 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84310421504 available bytes; 95.30% used; 114152360 free inodes.

server3 `/home`: 84310421504 available bytes; 95.30% used; 114152360 free inodes.

server3 `/data`: 125364944896 available bytes; 98.27% used; 225830487 free inodes.

server3 `/tmp`: 84310421504 available bytes; 95.30% used; 114152360 free inodes.

server3 `/var/tmp`: 84310421504 available bytes; 95.30% used; 114152360 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105766477824 available bytes; 94.10% used; 114346784 free inodes.

server4 `/home`: 105766477824 available bytes; 94.10% used; 114346784 free inodes.

server4 `/data`: 108897341440 available bytes; 98.49% used; 224914731 free inodes.

server4 `/tmp`: 105766477824 available bytes; 94.10% used; 114346784 free inodes.

server4 `/var/tmp`: 105766477824 available bytes; 94.10% used; 114346784 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
