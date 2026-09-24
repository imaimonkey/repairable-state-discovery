# V2R cluster inventory

2026-09-24T01:48:20.777606+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325455314944 available bytes; 81.84% used; 112499443 free inodes.

server1 `/home`: 325455314944 available bytes; 81.84% used; 112499443 free inodes.

server1 `/tmp`: 325455314944 available bytes; 81.84% used; 112499443 free inodes.

server1 `/var/tmp`: 325455314944 available bytes; 81.84% used; 112499443 free inodes.

server1 `/mnt/raid5`: 804844818432 available bytes; 96.31% used; 337733763 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40926154752 available bytes; 97.72% used; 110431851 free inodes.

server2 `/home`: 40926154752 available bytes; 97.72% used; 110431851 free inodes.

server2 `/tmp`: 40926154752 available bytes; 97.72% used; 110431851 free inodes.

server2 `/var/tmp`: 40926154752 available bytes; 97.72% used; 110431851 free inodes.

server2 `/mnt/raid5`: 530234269696 available bytes; 96.34% used; 445200742 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292717215744 available bytes; 83.67% used; 114210740 free inodes.

server3 `/home`: 292717215744 available bytes; 83.67% used; 114210740 free inodes.

server3 `/data`: 71100395520 available bytes; 99.02% used; 225841930 free inodes.

server3 `/tmp`: 292717215744 available bytes; 83.67% used; 114210740 free inodes.

server3 `/var/tmp`: 292717215744 available bytes; 83.67% used; 114210740 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105951100928 available bytes; 94.09% used; 114348572 free inodes.

server4 `/home`: 105951100928 available bytes; 94.09% used; 114348572 free inodes.

server4 `/data`: 289761697792 available bytes; 96.00% used; 225388485 free inodes.

server4 `/tmp`: 105951100928 available bytes; 94.09% used; 114348572 free inodes.

server4 `/var/tmp`: 105951100928 available bytes; 94.09% used; 114348572 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
