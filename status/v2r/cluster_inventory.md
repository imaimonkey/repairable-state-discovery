# V2R cluster inventory

2026-09-24T02:14:56.213778+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325433671680 available bytes; 81.85% used; 112499161 free inodes.

server1 `/home`: 325433671680 available bytes; 81.85% used; 112499161 free inodes.

server1 `/tmp`: 325433671680 available bytes; 81.85% used; 112499161 free inodes.

server1 `/var/tmp`: 325433671680 available bytes; 81.85% used; 112499161 free inodes.

server1 `/mnt/raid5`: 711646011392 available bytes; 96.74% used; 337733475 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40905981952 available bytes; 97.72% used; 110431646 free inodes.

server2 `/home`: 40905981952 available bytes; 97.72% used; 110431646 free inodes.

server2 `/tmp`: 40905981952 available bytes; 97.72% used; 110431646 free inodes.

server2 `/var/tmp`: 40905981952 available bytes; 97.72% used; 110431646 free inodes.

server2 `/mnt/raid5`: 528945348608 available bytes; 96.35% used; 445199981 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292667555840 available bytes; 83.67% used; 114210517 free inodes.

server3 `/home`: 292667555840 available bytes; 83.67% used; 114210517 free inodes.

server3 `/data`: 18078056448 available bytes; 99.75% used; 225841248 free inodes.

server3 `/tmp`: 292667555840 available bytes; 83.67% used; 114210517 free inodes.

server3 `/var/tmp`: 292667555840 available bytes; 83.67% used; 114210517 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105932292096 available bytes; 94.09% used; 114348264 free inodes.

server4 `/home`: 105932292096 available bytes; 94.09% used; 114348264 free inodes.

server4 `/data`: 289757868032 available bytes; 96.00% used; 225388445 free inodes.

server4 `/tmp`: 105932292096 available bytes; 94.09% used; 114348264 free inodes.

server4 `/var/tmp`: 105932292096 available bytes; 94.09% used; 114348264 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
