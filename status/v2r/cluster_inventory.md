# V2R cluster inventory

2026-09-26T03:42:49.423328+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318416539648 available bytes; 82.24% used; 112476271 free inodes.

server1 `/home`: 318416539648 available bytes; 82.24% used; 112476271 free inodes.

server1 `/tmp`: 318416539648 available bytes; 82.24% used; 112476271 free inodes.

server1 `/var/tmp`: 318416539648 available bytes; 82.24% used; 112476271 free inodes.

server1 `/mnt/raid5`: 330991136768 available bytes; 98.48% used; 337545744 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22939361280 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22939361280 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22939361280 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22939361280 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 286872489984 available bytes; 98.02% used; 445052167 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84312211456 available bytes; 95.30% used; 114152362 free inodes.

server3 `/home`: 84312211456 available bytes; 95.30% used; 114152362 free inodes.

server3 `/data`: 125359132672 available bytes; 98.27% used; 225830367 free inodes.

server3 `/tmp`: 84312211456 available bytes; 95.30% used; 114152362 free inodes.

server3 `/var/tmp`: 84312211456 available bytes; 95.30% used; 114152362 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105766301696 available bytes; 94.10% used; 114346784 free inodes.

server4 `/home`: 105766301696 available bytes; 94.10% used; 114346784 free inodes.

server4 `/data`: 108866588672 available bytes; 98.50% used; 224914716 free inodes.

server4 `/tmp`: 105766301696 available bytes; 94.10% used; 114346784 free inodes.

server4 `/var/tmp`: 105766301696 available bytes; 94.10% used; 114346784 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
