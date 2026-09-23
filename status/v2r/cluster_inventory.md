# V2R cluster inventory

2026-09-23T21:48:59.002733+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325714436096 available bytes; 81.83% used; 112501406 free inodes.

server1 `/home`: 325714436096 available bytes; 81.83% used; 112501406 free inodes.

server1 `/tmp`: 325714436096 available bytes; 81.83% used; 112501406 free inodes.

server1 `/var/tmp`: 325714436096 available bytes; 81.83% used; 112501406 free inodes.

server1 `/mnt/raid5`: 1388124708864 available bytes; 93.63% used; 337739916 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41107001344 available bytes; 97.71% used; 110432650 free inodes.

server2 `/home`: 41107001344 available bytes; 97.71% used; 110432650 free inodes.

server2 `/tmp`: 41107001344 available bytes; 97.71% used; 110432650 free inodes.

server2 `/var/tmp`: 41107001344 available bytes; 97.71% used; 110432650 free inodes.

server2 `/mnt/raid5`: 537937846272 available bytes; 96.28% used; 445207944 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292433424384 available bytes; 83.68% used; 114181455 free inodes.

server3 `/home`: 292433424384 available bytes; 83.68% used; 114181455 free inodes.

server3 `/data`: 82471235584 available bytes; 98.86% used; 225848080 free inodes.

server3 `/tmp`: 292433424384 available bytes; 83.68% used; 114181455 free inodes.

server3 `/var/tmp`: 292433424384 available bytes; 83.68% used; 114181455 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106465746944 available bytes; 94.06% used; 114355852 free inodes.

server4 `/home`: 106465746944 available bytes; 94.06% used; 114355852 free inodes.

server4 `/data`: 300237934592 available bytes; 95.85% used; 225447215 free inodes.

server4 `/tmp`: 106465746944 available bytes; 94.06% used; 114355852 free inodes.

server4 `/var/tmp`: 106465746944 available bytes; 94.06% used; 114355852 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
