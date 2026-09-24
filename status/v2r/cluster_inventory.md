# V2R cluster inventory

2026-09-24T06:30:01.154594+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324508966912 available bytes; 81.90% used; 112491671 free inodes.

server1 `/home`: 324508966912 available bytes; 81.90% used; 112491671 free inodes.

server1 `/tmp`: 324508966912 available bytes; 81.90% used; 112491671 free inodes.

server1 `/var/tmp`: 324508966912 available bytes; 81.90% used; 112491671 free inodes.

server1 `/mnt/raid5`: 517573779456 available bytes; 97.63% used; 337723769 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57882677248 available bytes; 96.77% used; 110431209 free inodes.

server2 `/home`: 57882677248 available bytes; 96.77% used; 110431209 free inodes.

server2 `/tmp`: 57882677248 available bytes; 96.77% used; 110431209 free inodes.

server2 `/var/tmp`: 57882677248 available bytes; 96.77% used; 110431209 free inodes.

server2 `/mnt/raid5`: 519732686848 available bytes; 96.41% used; 445192039 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 127185096704 available bytes; 92.90% used; 114194571 free inodes.

server3 `/home`: 127185096704 available bytes; 92.90% used; 114194571 free inodes.

server3 `/data`: 140512186368 available bytes; 98.06% used; 225835763 free inodes.

server3 `/tmp`: 127185096704 available bytes; 92.90% used; 114194571 free inodes.

server3 `/var/tmp`: 127185096704 available bytes; 92.90% used; 114194571 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105805484032 available bytes; 94.10% used; 114349279 free inodes.

server4 `/home`: 105805484032 available bytes; 94.10% used; 114349279 free inodes.

server4 `/data`: 328485576704 available bytes; 95.46% used; 225373008 free inodes.

server4 `/tmp`: 105805484032 available bytes; 94.10% used; 114349279 free inodes.

server4 `/var/tmp`: 105805484032 available bytes; 94.10% used; 114349279 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
