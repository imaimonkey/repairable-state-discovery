# V2R cluster inventory

2026-09-25T00:33:20.562088+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319086907392 available bytes; 82.20% used; 112480773 free inodes.

server1 `/home`: 319086907392 available bytes; 82.20% used; 112480773 free inodes.

server1 `/tmp`: 319086907392 available bytes; 82.20% used; 112480773 free inodes.

server1 `/var/tmp`: 319086907392 available bytes; 82.20% used; 112480773 free inodes.

server1 `/mnt/raid5`: 416848035840 available bytes; 98.09% used; 337619499 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23074443264 available bytes; 98.71% used; 110410765 free inodes.

server2 `/home`: 23074443264 available bytes; 98.71% used; 110410765 free inodes.

server2 `/tmp`: 23074443264 available bytes; 98.71% used; 110410765 free inodes.

server2 `/var/tmp`: 23074443264 available bytes; 98.71% used; 110410765 free inodes.

server2 `/mnt/raid5`: 501721104384 available bytes; 96.53% used; 445162852 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84349812736 available bytes; 95.29% used; 114156084 free inodes.

server3 `/home`: 84349812736 available bytes; 95.29% used; 114156084 free inodes.

server3 `/data`: 148835598336 available bytes; 97.94% used; 225813388 free inodes.

server3 `/tmp`: 84349812736 available bytes; 95.29% used; 114156084 free inodes.

server3 `/var/tmp`: 84349812736 available bytes; 95.29% used; 114156084 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105788862464 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105788862464 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 56612851712 available bytes; 99.22% used; 225054248 free inodes.

server4 `/tmp`: 105788862464 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105788862464 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
