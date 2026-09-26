# V2R cluster inventory

2026-09-26T02:27:54.679599+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318418993152 available bytes; 82.24% used; 112476277 free inodes.

server1 `/home`: 318418993152 available bytes; 82.24% used; 112476277 free inodes.

server1 `/tmp`: 318418993152 available bytes; 82.24% used; 112476277 free inodes.

server1 `/var/tmp`: 318418993152 available bytes; 82.24% used; 112476277 free inodes.

server1 `/mnt/raid5`: 344973045760 available bytes; 98.42% used; 337546161 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22942969856 available bytes; 98.72% used; 110406218 free inodes.

server2 `/home`: 22942969856 available bytes; 98.72% used; 110406218 free inodes.

server2 `/tmp`: 22942969856 available bytes; 98.72% used; 110406218 free inodes.

server2 `/var/tmp`: 22942969856 available bytes; 98.72% used; 110406218 free inodes.

server2 `/mnt/raid5`: 289050783744 available bytes; 98.00% used; 445054531 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84317839360 available bytes; 95.29% used; 114152372 free inodes.

server3 `/home`: 84317839360 available bytes; 95.29% used; 114152372 free inodes.

server3 `/data`: 124785758208 available bytes; 98.28% used; 225817045 free inodes.

server3 `/tmp`: 84317839360 available bytes; 95.29% used; 114152372 free inodes.

server3 `/var/tmp`: 84317839360 available bytes; 95.29% used; 114152372 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106126737408 available bytes; 94.08% used; 114349422 free inodes.

server4 `/home`: 106126737408 available bytes; 94.08% used; 114349422 free inodes.

server4 `/data`: 130847305728 available bytes; 98.19% used; 224915706 free inodes.

server4 `/tmp`: 106126737408 available bytes; 94.08% used; 114349422 free inodes.

server4 `/var/tmp`: 106126737408 available bytes; 94.08% used; 114349422 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
