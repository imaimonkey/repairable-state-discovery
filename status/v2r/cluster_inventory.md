# V2R cluster inventory

2026-09-25T01:45:45.525706+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319075184640 available bytes; 82.20% used; 112480772 free inodes.

server1 `/home`: 319075184640 available bytes; 82.20% used; 112480772 free inodes.

server1 `/tmp`: 319075184640 available bytes; 82.20% used; 112480772 free inodes.

server1 `/var/tmp`: 319075184640 available bytes; 82.20% used; 112480772 free inodes.

server1 `/mnt/raid5`: 416453922816 available bytes; 98.09% used; 337611125 free inodes.
| server2 | True | ['2', '3', '6'] | [] |

server2 `/`: 23040712704 available bytes; 98.71% used; 110410776 free inodes.

server2 `/home`: 23040712704 available bytes; 98.71% used; 110410776 free inodes.

server2 `/tmp`: 23040712704 available bytes; 98.71% used; 110410776 free inodes.

server2 `/var/tmp`: 23040712704 available bytes; 98.71% used; 110410776 free inodes.

server2 `/mnt/raid5`: 490611945472 available bytes; 96.61% used; 445160882 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84353941504 available bytes; 95.29% used; 114156080 free inodes.

server3 `/home`: 84353941504 available bytes; 95.29% used; 114156080 free inodes.

server3 `/data`: 146428661760 available bytes; 97.98% used; 225812027 free inodes.

server3 `/tmp`: 84353941504 available bytes; 95.29% used; 114156080 free inodes.

server3 `/var/tmp`: 84353941504 available bytes; 95.29% used; 114156080 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105761652736 available bytes; 94.10% used; 114348277 free inodes.

server4 `/home`: 105761652736 available bytes; 94.10% used; 114348277 free inodes.

server4 `/data`: 53313921024 available bytes; 99.26% used; 225030580 free inodes.

server4 `/tmp`: 105761652736 available bytes; 94.10% used; 114348277 free inodes.

server4 `/var/tmp`: 105761652736 available bytes; 94.10% used; 114348277 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
