# V2R cluster inventory

2026-09-25T00:37:57.170501+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319086034944 available bytes; 82.20% used; 112480771 free inodes.

server1 `/home`: 319086034944 available bytes; 82.20% used; 112480771 free inodes.

server1 `/tmp`: 319086034944 available bytes; 82.20% used; 112480771 free inodes.

server1 `/var/tmp`: 319086034944 available bytes; 82.20% used; 112480771 free inodes.

server1 `/mnt/raid5`: 416839360512 available bytes; 98.09% used; 337618956 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23076204544 available bytes; 98.71% used; 110410767 free inodes.

server2 `/home`: 23076204544 available bytes; 98.71% used; 110410767 free inodes.

server2 `/tmp`: 23076204544 available bytes; 98.71% used; 110410767 free inodes.

server2 `/var/tmp`: 23076204544 available bytes; 98.71% used; 110410767 free inodes.

server2 `/mnt/raid5`: 501581869056 available bytes; 96.53% used; 445162706 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84349341696 available bytes; 95.29% used; 114156086 free inodes.

server3 `/home`: 84349341696 available bytes; 95.29% used; 114156086 free inodes.

server3 `/data`: 148760772608 available bytes; 97.94% used; 225813305 free inodes.

server3 `/tmp`: 84349341696 available bytes; 95.29% used; 114156086 free inodes.

server3 `/var/tmp`: 84349341696 available bytes; 95.29% used; 114156086 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105788743680 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105788743680 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 56537759744 available bytes; 99.22% used; 225047587 free inodes.

server4 `/tmp`: 105788743680 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105788743680 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
