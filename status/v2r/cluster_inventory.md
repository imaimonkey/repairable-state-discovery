# V2R cluster inventory

2026-09-27T01:27:46.893704+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315147010048 available bytes; 82.42% used; 112443442 free inodes.

server1 `/home`: 315147010048 available bytes; 82.42% used; 112443442 free inodes.

server1 `/tmp`: 315147010048 available bytes; 82.42% used; 112443442 free inodes.

server1 `/var/tmp`: 315147010048 available bytes; 82.42% used; 112443442 free inodes.

server1 `/mnt/raid5`: 637520896000 available bytes; 97.08% used; 337405521 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17629716480 available bytes; 99.02% used; 110364996 free inodes.

server2 `/home`: 17629716480 available bytes; 99.02% used; 110364996 free inodes.

server2 `/tmp`: 17629716480 available bytes; 99.02% used; 110364996 free inodes.

server2 `/var/tmp`: 17629716480 available bytes; 99.02% used; 110364996 free inodes.

server2 `/mnt/raid5`: 582211989504 available bytes; 95.98% used; 444886431 free inodes.
| server3 | True | ['0', '3'] | [] |

server3 `/`: 79499059200 available bytes; 95.56% used; 114068700 free inodes.

server3 `/home`: 79499059200 available bytes; 95.56% used; 114068700 free inodes.

server3 `/data`: 1342410534912 available bytes; 81.45% used; 225763598 free inodes.

server3 `/tmp`: 79499059200 available bytes; 95.56% used; 114068700 free inodes.

server3 `/var/tmp`: 79499059200 available bytes; 95.56% used; 114068700 free inodes.
| server4 | True | ['0', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105869508608 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105869508608 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 406540898304 available bytes; 94.38% used; 224782880 free inodes.

server4 `/tmp`: 105869508608 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105869508608 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
