# V2R cluster inventory

2026-09-24T20:18:44.801710+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323988205568 available bytes; 81.93% used; 112481427 free inodes.

server1 `/home`: 323988205568 available bytes; 81.93% used; 112481427 free inodes.

server1 `/tmp`: 323988205568 available bytes; 81.93% used; 112481427 free inodes.

server1 `/var/tmp`: 323988205568 available bytes; 81.93% used; 112481427 free inodes.

server1 `/mnt/raid5`: 415664447488 available bytes; 98.09% used; 337635765 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30170832896 available bytes; 98.32% used; 110411378 free inodes.

server2 `/home`: 30170832896 available bytes; 98.32% used; 110411378 free inodes.

server2 `/tmp`: 30170832896 available bytes; 98.32% used; 110411378 free inodes.

server2 `/var/tmp`: 30170832896 available bytes; 98.32% used; 110411378 free inodes.

server2 `/mnt/raid5`: 492897259520 available bytes; 96.59% used; 445157049 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84399570944 available bytes; 95.29% used; 114156111 free inodes.

server3 `/home`: 84399570944 available bytes; 95.29% used; 114156111 free inodes.

server3 `/data`: 151664250880 available bytes; 97.90% used; 225804686 free inodes.

server3 `/tmp`: 84399570944 available bytes; 95.29% used; 114156111 free inodes.

server3 `/var/tmp`: 84399570944 available bytes; 95.29% used; 114156111 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105640910848 available bytes; 94.10% used; 114348396 free inodes.

server4 `/home`: 105640910848 available bytes; 94.10% used; 114348396 free inodes.

server4 `/data`: 87322435584 available bytes; 98.79% used; 225258669 free inodes.

server4 `/tmp`: 105640910848 available bytes; 94.10% used; 114348396 free inodes.

server4 `/var/tmp`: 105640910848 available bytes; 94.10% used; 114348396 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
