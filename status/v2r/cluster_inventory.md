# V2R cluster inventory

2026-09-24T07:35:23.693606+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324448575488 available bytes; 81.90% used; 112491089 free inodes.

server1 `/home`: 324448575488 available bytes; 81.90% used; 112491089 free inodes.

server1 `/tmp`: 324448575488 available bytes; 81.90% used; 112491089 free inodes.

server1 `/var/tmp`: 324448575488 available bytes; 81.90% used; 112491089 free inodes.

server1 `/mnt/raid5`: 517410369536 available bytes; 97.63% used; 337722779 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57842077696 available bytes; 96.77% used; 110431152 free inodes.

server2 `/home`: 57842077696 available bytes; 96.77% used; 110431152 free inodes.

server2 `/tmp`: 57842077696 available bytes; 96.77% used; 110431152 free inodes.

server2 `/var/tmp`: 57842077696 available bytes; 96.77% used; 110431152 free inodes.

server2 `/mnt/raid5`: 518104801280 available bytes; 96.42% used; 445180642 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 126782095360 available bytes; 92.93% used; 114174982 free inodes.

server3 `/home`: 126782095360 available bytes; 92.93% used; 114174982 free inodes.

server3 `/data`: 138747789312 available bytes; 98.08% used; 225833667 free inodes.

server3 `/tmp`: 126782095360 available bytes; 92.93% used; 114174982 free inodes.

server3 `/var/tmp`: 126782095360 available bytes; 92.93% used; 114174982 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105780527104 available bytes; 94.10% used; 114349185 free inodes.

server4 `/home`: 105780527104 available bytes; 94.10% used; 114349185 free inodes.

server4 `/data`: 285806338048 available bytes; 96.05% used; 225366876 free inodes.

server4 `/tmp`: 105780527104 available bytes; 94.10% used; 114349185 free inodes.

server4 `/var/tmp`: 105780527104 available bytes; 94.10% used; 114349185 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
