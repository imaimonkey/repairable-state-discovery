# V2R cluster inventory

2026-09-27T05:05:47.807073+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314797187072 available bytes; 82.44% used; 112442997 free inodes.

server1 `/home`: 314797187072 available bytes; 82.44% used; 112442997 free inodes.

server1 `/tmp`: 314797187072 available bytes; 82.44% used; 112442997 free inodes.

server1 `/var/tmp`: 314797187072 available bytes; 82.44% used; 112442997 free inodes.

server1 `/mnt/raid5`: 634732720128 available bytes; 97.09% used; 337400254 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17623650304 available bytes; 99.02% used; 110364998 free inodes.

server2 `/home`: 17623650304 available bytes; 99.02% used; 110364998 free inodes.

server2 `/tmp`: 17623650304 available bytes; 99.02% used; 110364998 free inodes.

server2 `/var/tmp`: 17623650304 available bytes; 99.02% used; 110364998 free inodes.

server2 `/mnt/raid5`: 575265099776 available bytes; 96.03% used; 444878511 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78611095552 available bytes; 95.61% used; 114062912 free inodes.

server3 `/home`: 78611095552 available bytes; 95.61% used; 114062912 free inodes.

server3 `/data`: 1333588828160 available bytes; 81.57% used; 225758283 free inodes.

server3 `/tmp`: 78611095552 available bytes; 95.61% used; 114062912 free inodes.

server3 `/var/tmp`: 78611095552 available bytes; 95.61% used; 114062912 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111000387584 available bytes; 93.81% used; 114372920 free inodes.

server4 `/home`: 111000387584 available bytes; 93.81% used; 114372920 free inodes.

server4 `/data`: 382071025664 available bytes; 94.72% used; 224778205 free inodes.

server4 `/tmp`: 111000387584 available bytes; 93.81% used; 114372920 free inodes.

server4 `/var/tmp`: 111000387584 available bytes; 93.81% used; 114372920 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
