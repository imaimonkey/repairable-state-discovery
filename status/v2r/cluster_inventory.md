# V2R cluster inventory

2026-09-25T00:17:59.625616+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319089364992 available bytes; 82.20% used; 112480795 free inodes.

server1 `/home`: 319089364992 available bytes; 82.20% used; 112480795 free inodes.

server1 `/tmp`: 319089364992 available bytes; 82.20% used; 112480795 free inodes.

server1 `/var/tmp`: 319089364992 available bytes; 82.20% used; 112480795 free inodes.

server1 `/mnt/raid5`: 416881213440 available bytes; 98.09% used; 337621288 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23084363776 available bytes; 98.71% used; 110410783 free inodes.

server2 `/home`: 23084363776 available bytes; 98.71% used; 110410783 free inodes.

server2 `/tmp`: 23084363776 available bytes; 98.71% used; 110410783 free inodes.

server2 `/var/tmp`: 23084363776 available bytes; 98.71% used; 110410783 free inodes.

server2 `/mnt/raid5`: 502208352256 available bytes; 96.53% used; 445163469 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84356005888 available bytes; 95.29% used; 114156084 free inodes.

server3 `/home`: 84356005888 available bytes; 95.29% used; 114156084 free inodes.

server3 `/data`: 149096718336 available bytes; 97.94% used; 225813659 free inodes.

server3 `/tmp`: 84356005888 available bytes; 95.29% used; 114156084 free inodes.

server3 `/var/tmp`: 84356005888 available bytes; 95.29% used; 114156084 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105797672960 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105797672960 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 56834686976 available bytes; 99.21% used; 225075254 free inodes.

server4 `/tmp`: 105797672960 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105797672960 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
