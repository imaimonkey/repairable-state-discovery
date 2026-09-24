# V2R cluster inventory

2026-09-24T04:19:25.398378+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324708270080 available bytes; 81.89% used; 112493336 free inodes.

server1 `/home`: 324708270080 available bytes; 81.89% used; 112493336 free inodes.

server1 `/tmp`: 324708270080 available bytes; 81.89% used; 112493336 free inodes.

server1 `/var/tmp`: 324708270080 available bytes; 81.89% used; 112493336 free inodes.

server1 `/mnt/raid5`: 435985752064 available bytes; 98.00% used; 337724734 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40794943488 available bytes; 97.72% used; 110430728 free inodes.

server2 `/home`: 40794943488 available bytes; 97.72% used; 110430728 free inodes.

server2 `/tmp`: 40794943488 available bytes; 97.72% used; 110430728 free inodes.

server2 `/var/tmp`: 40794943488 available bytes; 97.72% used; 110430728 free inodes.

server2 `/mnt/raid5`: 525689376768 available bytes; 96.37% used; 445196136 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292068515840 available bytes; 83.70% used; 114185055 free inodes.

server3 `/home`: 292068515840 available bytes; 83.70% used; 114185055 free inodes.

server3 `/data`: 31695532032 available bytes; 99.56% used; 225841648 free inodes.

server3 `/tmp`: 292068515840 available bytes; 83.70% used; 114185055 free inodes.

server3 `/var/tmp`: 292068515840 available bytes; 83.70% used; 114185055 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105851953152 available bytes; 94.09% used; 114349453 free inodes.

server4 `/home`: 105851953152 available bytes; 94.09% used; 114349453 free inodes.

server4 `/data`: 256705945600 available bytes; 96.45% used; 225381788 free inodes.

server4 `/tmp`: 105851953152 available bytes; 94.09% used; 114349453 free inodes.

server4 `/var/tmp`: 105851953152 available bytes; 94.09% used; 114349453 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
