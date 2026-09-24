# V2R cluster inventory

2026-09-24T05:58:53.447393+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324532989952 available bytes; 81.90% used; 112491970 free inodes.

server1 `/home`: 324532989952 available bytes; 81.90% used; 112491970 free inodes.

server1 `/tmp`: 324532989952 available bytes; 81.90% used; 112491970 free inodes.

server1 `/var/tmp`: 324532989952 available bytes; 81.90% used; 112491970 free inodes.

server1 `/mnt/raid5`: 517603684352 available bytes; 97.63% used; 337723843 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57904570368 available bytes; 96.77% used; 110431300 free inodes.

server2 `/home`: 57904570368 available bytes; 96.77% used; 110431300 free inodes.

server2 `/tmp`: 57904570368 available bytes; 96.77% used; 110431300 free inodes.

server2 `/var/tmp`: 57904570368 available bytes; 96.77% used; 110431300 free inodes.

server2 `/mnt/raid5`: 521225523200 available bytes; 96.40% used; 445193009 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 127179223040 available bytes; 92.90% used; 114199812 free inodes.

server3 `/home`: 127179223040 available bytes; 92.90% used; 114199812 free inodes.

server3 `/data`: 185851904000 available bytes; 97.43% used; 225838507 free inodes.

server3 `/tmp`: 127179223040 available bytes; 92.90% used; 114199812 free inodes.

server3 `/var/tmp`: 127179223040 available bytes; 92.90% used; 114199812 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105815433216 available bytes; 94.10% used; 114349323 free inodes.

server4 `/home`: 105815433216 available bytes; 94.10% used; 114349323 free inodes.

server4 `/data`: 339827462144 available bytes; 95.30% used; 225374713 free inodes.

server4 `/tmp`: 105815433216 available bytes; 94.10% used; 114349323 free inodes.

server4 `/var/tmp`: 105815433216 available bytes; 94.10% used; 114349323 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
