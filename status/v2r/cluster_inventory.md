# V2R cluster inventory

2026-09-25T00:19:31.682509+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319089049600 available bytes; 82.20% used; 112480793 free inodes.

server1 `/home`: 319089049600 available bytes; 82.20% used; 112480793 free inodes.

server1 `/tmp`: 319089049600 available bytes; 82.20% used; 112480793 free inodes.

server1 `/var/tmp`: 319089049600 available bytes; 82.20% used; 112480793 free inodes.

server1 `/mnt/raid5`: 416877637632 available bytes; 98.09% used; 337621112 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23084150784 available bytes; 98.71% used; 110410783 free inodes.

server2 `/home`: 23084150784 available bytes; 98.71% used; 110410783 free inodes.

server2 `/tmp`: 23084150784 available bytes; 98.71% used; 110410783 free inodes.

server2 `/var/tmp`: 23084150784 available bytes; 98.71% used; 110410783 free inodes.

server2 `/mnt/raid5`: 502164639744 available bytes; 96.53% used; 445163299 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84355796992 available bytes; 95.29% used; 114156084 free inodes.

server3 `/home`: 84355796992 available bytes; 95.29% used; 114156084 free inodes.

server3 `/data`: 149070139392 available bytes; 97.94% used; 225813636 free inodes.

server3 `/tmp`: 84355796992 available bytes; 95.29% used; 114156084 free inodes.

server3 `/var/tmp`: 84355796992 available bytes; 95.29% used; 114156084 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105789255680 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105789255680 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 56811737088 available bytes; 99.21% used; 225072767 free inodes.

server4 `/tmp`: 105789255680 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105789255680 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
