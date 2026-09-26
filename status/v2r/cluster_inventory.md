# V2R cluster inventory

2026-09-26T02:49:21.302790+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318418735104 available bytes; 82.24% used; 112476265 free inodes.

server1 `/home`: 318418735104 available bytes; 82.24% used; 112476265 free inodes.

server1 `/tmp`: 318418735104 available bytes; 82.24% used; 112476265 free inodes.

server1 `/var/tmp`: 318418735104 available bytes; 82.24% used; 112476265 free inodes.

server1 `/mnt/raid5`: 331108220928 available bytes; 98.48% used; 337546011 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22936576000 available bytes; 98.72% used; 110406218 free inodes.

server2 `/home`: 22936576000 available bytes; 98.72% used; 110406218 free inodes.

server2 `/tmp`: 22936576000 available bytes; 98.72% used; 110406218 free inodes.

server2 `/var/tmp`: 22936576000 available bytes; 98.72% used; 110406218 free inodes.

server2 `/mnt/raid5`: 287888388096 available bytes; 98.01% used; 445053767 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84319891456 available bytes; 95.29% used; 114152372 free inodes.

server3 `/home`: 84319891456 available bytes; 95.29% used; 114152372 free inodes.

server3 `/data`: 124782895104 available bytes; 98.28% used; 225816666 free inodes.

server3 `/tmp`: 84319891456 available bytes; 95.29% used; 114152372 free inodes.

server3 `/var/tmp`: 84319891456 available bytes; 95.29% used; 114152372 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105919209472 available bytes; 94.09% used; 114347153 free inodes.

server4 `/home`: 105919209472 available bytes; 94.09% used; 114347153 free inodes.

server4 `/data`: 109770055680 available bytes; 98.48% used; 224915403 free inodes.

server4 `/tmp`: 105919209472 available bytes; 94.09% used; 114347153 free inodes.

server4 `/var/tmp`: 105919209472 available bytes; 94.09% used; 114347153 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
