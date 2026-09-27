# V2R cluster inventory

2026-09-27T01:29:18.313404+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315145027584 available bytes; 82.42% used; 112443373 free inodes.

server1 `/home`: 315145027584 available bytes; 82.42% used; 112443373 free inodes.

server1 `/tmp`: 315145027584 available bytes; 82.42% used; 112443373 free inodes.

server1 `/var/tmp`: 315145027584 available bytes; 82.42% used; 112443373 free inodes.

server1 `/mnt/raid5`: 637519642624 available bytes; 97.08% used; 337405521 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17628848128 available bytes; 99.02% used; 110364996 free inodes.

server2 `/home`: 17628848128 available bytes; 99.02% used; 110364996 free inodes.

server2 `/tmp`: 17628848128 available bytes; 99.02% used; 110364996 free inodes.

server2 `/var/tmp`: 17628848128 available bytes; 99.02% used; 110364996 free inodes.

server2 `/mnt/raid5`: 582708912128 available bytes; 95.97% used; 444886395 free inodes.
| server3 | True | ['0', '3'] | [] |

server3 `/`: 79498416128 available bytes; 95.56% used; 114068700 free inodes.

server3 `/home`: 79498416128 available bytes; 95.56% used; 114068700 free inodes.

server3 `/data`: 1342409052160 available bytes; 81.45% used; 225763554 free inodes.

server3 `/tmp`: 79498416128 available bytes; 95.56% used; 114068700 free inodes.

server3 `/var/tmp`: 79498416128 available bytes; 95.56% used; 114068700 free inodes.
| server4 | True | ['0', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105869471744 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105869471744 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 406539223040 available bytes; 94.38% used; 224782882 free inodes.

server4 `/tmp`: 105869471744 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105869471744 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
