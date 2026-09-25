# V2R cluster inventory

2026-09-25T01:56:31.506856+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319025688576 available bytes; 82.20% used; 112480597 free inodes.

server1 `/home`: 319025688576 available bytes; 82.20% used; 112480597 free inodes.

server1 `/tmp`: 319025688576 available bytes; 82.20% used; 112480597 free inodes.

server1 `/var/tmp`: 319025688576 available bytes; 82.20% used; 112480597 free inodes.

server1 `/mnt/raid5`: 416430047232 available bytes; 98.09% used; 337609859 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23032029184 available bytes; 98.72% used; 110410441 free inodes.

server2 `/home`: 23032029184 available bytes; 98.72% used; 110410441 free inodes.

server2 `/tmp`: 23032029184 available bytes; 98.72% used; 110410441 free inodes.

server2 `/var/tmp`: 23032029184 available bytes; 98.72% used; 110410441 free inodes.

server2 `/mnt/raid5`: 493773959168 available bytes; 96.59% used; 445160632 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84353273856 available bytes; 95.29% used; 114156073 free inodes.

server3 `/home`: 84353273856 available bytes; 95.29% used; 114156073 free inodes.

server3 `/data`: 146235150336 available bytes; 97.98% used; 225811794 free inodes.

server3 `/tmp`: 84353273856 available bytes; 95.29% used; 114156073 free inodes.

server3 `/var/tmp`: 84353273856 available bytes; 95.29% used; 114156073 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105761284096 available bytes; 94.10% used; 114348260 free inodes.

server4 `/home`: 105761284096 available bytes; 94.10% used; 114348260 free inodes.

server4 `/data`: 51706310656 available bytes; 99.29% used; 225030466 free inodes.

server4 `/tmp`: 105761284096 available bytes; 94.10% used; 114348260 free inodes.

server4 `/var/tmp`: 105761284096 available bytes; 94.10% used; 114348260 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
