# V2R cluster inventory

2026-09-24T05:08:34.237946+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324597084160 available bytes; 81.89% used; 112492592 free inodes.

server1 `/home`: 324597084160 available bytes; 81.89% used; 112492592 free inodes.

server1 `/tmp`: 324597084160 available bytes; 81.89% used; 112492592 free inodes.

server1 `/var/tmp`: 324597084160 available bytes; 81.89% used; 112492592 free inodes.

server1 `/mnt/raid5`: 489209298944 available bytes; 97.76% used; 337724554 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40756731904 available bytes; 97.73% used; 110430378 free inodes.

server2 `/home`: 40756731904 available bytes; 97.73% used; 110430378 free inodes.

server2 `/tmp`: 40756731904 available bytes; 97.73% used; 110430378 free inodes.

server2 `/var/tmp`: 40756731904 available bytes; 97.73% used; 110430378 free inodes.

server2 `/mnt/raid5`: 523318853632 available bytes; 96.38% used; 445194486 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 291994755072 available bytes; 83.71% used; 114176121 free inodes.

server3 `/home`: 291994755072 available bytes; 83.71% used; 114176121 free inodes.

server3 `/data`: 23290089472 available bytes; 99.68% used; 225840272 free inodes.

server3 `/tmp`: 291994755072 available bytes; 83.71% used; 114176121 free inodes.

server3 `/var/tmp`: 291994755072 available bytes; 83.71% used; 114176121 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105826615296 available bytes; 94.09% used; 114349383 free inodes.

server4 `/home`: 105826615296 available bytes; 94.09% used; 114349383 free inodes.

server4 `/data`: 252613627904 available bytes; 96.51% used; 225366768 free inodes.

server4 `/tmp`: 105826615296 available bytes; 94.09% used; 114349383 free inodes.

server4 `/var/tmp`: 105826615296 available bytes; 94.09% used; 114349383 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
