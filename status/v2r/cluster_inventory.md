# V2R cluster inventory

2026-09-26T02:41:42.802601+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318419460096 available bytes; 82.24% used; 112476262 free inodes.

server1 `/home`: 318419460096 available bytes; 82.24% used; 112476262 free inodes.

server1 `/tmp`: 318419460096 available bytes; 82.24% used; 112476262 free inodes.

server1 `/var/tmp`: 318419460096 available bytes; 82.24% used; 112476262 free inodes.

server1 `/mnt/raid5`: 331129876480 available bytes; 98.48% used; 337546059 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22941016064 available bytes; 98.72% used; 110406218 free inodes.

server2 `/home`: 22941016064 available bytes; 98.72% used; 110406218 free inodes.

server2 `/tmp`: 22941016064 available bytes; 98.72% used; 110406218 free inodes.

server2 `/var/tmp`: 22941016064 available bytes; 98.72% used; 110406218 free inodes.

server2 `/mnt/raid5`: 288108580864 available bytes; 98.01% used; 445054121 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84321320960 available bytes; 95.29% used; 114152370 free inodes.

server3 `/home`: 84321320960 available bytes; 95.29% used; 114152370 free inodes.

server3 `/data`: 124784844800 available bytes; 98.28% used; 225816789 free inodes.

server3 `/tmp`: 84321320960 available bytes; 95.29% used; 114152370 free inodes.

server3 `/var/tmp`: 84321320960 available bytes; 95.29% used; 114152370 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105921441792 available bytes; 94.09% used; 114347162 free inodes.

server4 `/home`: 105921441792 available bytes; 94.09% used; 114347162 free inodes.

server4 `/data`: 109768843264 available bytes; 98.48% used; 224915413 free inodes.

server4 `/tmp`: 105921441792 available bytes; 94.09% used; 114347162 free inodes.

server4 `/var/tmp`: 105921441792 available bytes; 94.09% used; 114347162 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
