# V2R cluster inventory

2026-09-25T02:01:08.565876+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319024787456 available bytes; 82.20% used; 112480589 free inodes.

server1 `/home`: 319024787456 available bytes; 82.20% used; 112480589 free inodes.

server1 `/tmp`: 319024787456 available bytes; 82.20% used; 112480589 free inodes.

server1 `/var/tmp`: 319024787456 available bytes; 82.20% used; 112480589 free inodes.

server1 `/mnt/raid5`: 395626291200 available bytes; 98.19% used; 337609311 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23026262016 available bytes; 98.72% used; 110410444 free inodes.

server2 `/home`: 23026262016 available bytes; 98.72% used; 110410444 free inodes.

server2 `/tmp`: 23026262016 available bytes; 98.72% used; 110410444 free inodes.

server2 `/var/tmp`: 23026262016 available bytes; 98.72% used; 110410444 free inodes.

server2 `/mnt/raid5`: 489543352320 available bytes; 96.62% used; 445150130 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84352933888 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84352933888 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 146155139072 available bytes; 97.98% used; 225811686 free inodes.

server3 `/tmp`: 84352933888 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84352933888 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105761140736 available bytes; 94.10% used; 114348257 free inodes.

server4 `/home`: 105761140736 available bytes; 94.10% used; 114348257 free inodes.

server4 `/data`: 50098507776 available bytes; 99.31% used; 225030354 free inodes.

server4 `/tmp`: 105761140736 available bytes; 94.10% used; 114348257 free inodes.

server4 `/var/tmp`: 105761140736 available bytes; 94.10% used; 114348257 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
