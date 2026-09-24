# V2R cluster inventory

2026-09-24T04:00:22.018137+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324723642368 available bytes; 81.88% used; 112493541 free inodes.

server1 `/home`: 324723642368 available bytes; 81.88% used; 112493541 free inodes.

server1 `/tmp`: 324723642368 available bytes; 81.88% used; 112493541 free inodes.

server1 `/var/tmp`: 324723642368 available bytes; 81.88% used; 112493541 free inodes.

server1 `/mnt/raid5`: 416633556992 available bytes; 98.09% used; 337724773 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40812077056 available bytes; 97.72% used; 110430876 free inodes.

server2 `/home`: 40812077056 available bytes; 97.72% used; 110430876 free inodes.

server2 `/tmp`: 40812077056 available bytes; 97.72% used; 110430876 free inodes.

server2 `/var/tmp`: 40812077056 available bytes; 97.72% used; 110430876 free inodes.

server2 `/mnt/raid5`: 526286573568 available bytes; 96.36% used; 445196914 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292043816960 available bytes; 83.70% used; 114186535 free inodes.

server3 `/home`: 292043816960 available bytes; 83.70% used; 114186535 free inodes.

server3 `/data`: 33868881920 available bytes; 99.53% used; 225842403 free inodes.

server3 `/tmp`: 292043816960 available bytes; 83.70% used; 114186535 free inodes.

server3 `/var/tmp`: 292043816960 available bytes; 83.70% used; 114186535 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105791385600 available bytes; 94.10% used; 114349505 free inodes.

server4 `/home`: 105791385600 available bytes; 94.10% used; 114349505 free inodes.

server4 `/data`: 258347909120 available bytes; 96.43% used; 225382405 free inodes.

server4 `/tmp`: 105791385600 available bytes; 94.10% used; 114349505 free inodes.

server4 `/var/tmp`: 105791385600 available bytes; 94.10% used; 114349505 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
