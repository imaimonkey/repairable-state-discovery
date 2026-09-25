# V2R cluster inventory

2026-09-25T04:41:23.814967+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318915854336 available bytes; 82.21% used; 112480369 free inodes.

server1 `/home`: 318915854336 available bytes; 82.21% used; 112480369 free inodes.

server1 `/tmp`: 318915854336 available bytes; 82.21% used; 112480369 free inodes.

server1 `/var/tmp`: 318915854336 available bytes; 82.21% used; 112480369 free inodes.

server1 `/mnt/raid5`: 408698888192 available bytes; 98.13% used; 337590329 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22947385344 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22947385344 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22947385344 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22947385344 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 462689783808 available bytes; 96.80% used; 445109581 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340686848 available bytes; 95.29% used; 114156078 free inodes.

server3 `/home`: 84340686848 available bytes; 95.29% used; 114156078 free inodes.

server3 `/data`: 143331983360 available bytes; 98.02% used; 225815925 free inodes.

server3 `/tmp`: 84340686848 available bytes; 95.29% used; 114156078 free inodes.

server3 `/var/tmp`: 84340686848 available bytes; 95.29% used; 114156078 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105663995904 available bytes; 94.10% used; 114350595 free inodes.

server4 `/home`: 105663995904 available bytes; 94.10% used; 114350595 free inodes.

server4 `/data`: 31175118848 available bytes; 99.57% used; 224962352 free inodes.

server4 `/tmp`: 105663995904 available bytes; 94.10% used; 114350595 free inodes.

server4 `/var/tmp`: 105663995904 available bytes; 94.10% used; 114350595 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
