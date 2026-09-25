# V2R cluster inventory

2026-09-25T01:59:35.730746+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319025000448 available bytes; 82.20% used; 112480597 free inodes.

server1 `/home`: 319025000448 available bytes; 82.20% used; 112480597 free inodes.

server1 `/tmp`: 319025000448 available bytes; 82.20% used; 112480597 free inodes.

server1 `/var/tmp`: 319025000448 available bytes; 82.20% used; 112480597 free inodes.

server1 `/mnt/raid5`: 416277540864 available bytes; 98.09% used; 337609492 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23025614848 available bytes; 98.72% used; 110410441 free inodes.

server2 `/home`: 23025614848 available bytes; 98.72% used; 110410441 free inodes.

server2 `/tmp`: 23025614848 available bytes; 98.72% used; 110410441 free inodes.

server2 `/var/tmp`: 23025614848 available bytes; 98.72% used; 110410441 free inodes.

server2 `/mnt/raid5`: 492164067328 available bytes; 96.60% used; 445157076 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84352507904 available bytes; 95.29% used; 114156074 free inodes.

server3 `/home`: 84352507904 available bytes; 95.29% used; 114156074 free inodes.

server3 `/data`: 146177925120 available bytes; 97.98% used; 225811726 free inodes.

server3 `/tmp`: 84352507904 available bytes; 95.29% used; 114156074 free inodes.

server3 `/var/tmp`: 84352507904 available bytes; 95.29% used; 114156074 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105761206272 available bytes; 94.10% used; 114348258 free inodes.

server4 `/home`: 105761206272 available bytes; 94.10% used; 114348258 free inodes.

server4 `/data`: 50100322304 available bytes; 99.31% used; 225030406 free inodes.

server4 `/tmp`: 105761206272 available bytes; 94.10% used; 114348258 free inodes.

server4 `/var/tmp`: 105761206272 available bytes; 94.10% used; 114348258 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
