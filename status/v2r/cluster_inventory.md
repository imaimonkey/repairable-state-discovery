# V2R cluster inventory

2026-09-24T04:38:33.446257+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324627410944 available bytes; 81.89% used; 112492918 free inodes.

server1 `/home`: 324627410944 available bytes; 81.89% used; 112492918 free inodes.

server1 `/tmp`: 324627406848 available bytes; 81.89% used; 112492918 free inodes.

server1 `/var/tmp`: 324627406848 available bytes; 81.89% used; 112492918 free inodes.

server1 `/mnt/raid5`: 455306510336 available bytes; 97.91% used; 337724644 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40773955584 available bytes; 97.73% used; 110430500 free inodes.

server2 `/home`: 40773955584 available bytes; 97.73% used; 110430500 free inodes.

server2 `/tmp`: 40773955584 available bytes; 97.73% used; 110430500 free inodes.

server2 `/var/tmp`: 40773955584 available bytes; 97.73% used; 110430500 free inodes.

server2 `/mnt/raid5`: 524814270464 available bytes; 96.37% used; 445195682 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292405067776 available bytes; 83.68% used; 114200261 free inodes.

server3 `/home`: 292405075968 available bytes; 83.68% used; 114200261 free inodes.

server3 `/data`: 24373493760 available bytes; 99.66% used; 225840769 free inodes.

server3 `/tmp`: 292405112832 available bytes; 83.68% used; 114200261 free inodes.

server3 `/var/tmp`: 292405121024 available bytes; 83.68% used; 114200261 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105836691456 available bytes; 94.09% used; 114349415 free inodes.

server4 `/home`: 105836691456 available bytes; 94.09% used; 114349415 free inodes.

server4 `/data`: 253397073920 available bytes; 96.50% used; 225366867 free inodes.

server4 `/tmp`: 105836691456 available bytes; 94.09% used; 114349415 free inodes.

server4 `/var/tmp`: 105836691456 available bytes; 94.09% used; 114349415 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
