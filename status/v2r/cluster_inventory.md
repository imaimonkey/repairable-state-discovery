# V2R cluster inventory

2026-09-25T00:13:23.337525+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319088799744 available bytes; 82.20% used; 112480795 free inodes.

server1 `/home`: 319088799744 available bytes; 82.20% used; 112480795 free inodes.

server1 `/tmp`: 319088799744 available bytes; 82.20% used; 112480795 free inodes.

server1 `/var/tmp`: 319088799744 available bytes; 82.20% used; 112480795 free inodes.

server1 `/mnt/raid5`: 416891858944 available bytes; 98.09% used; 337621819 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23092469760 available bytes; 98.71% used; 110410783 free inodes.

server2 `/home`: 23092469760 available bytes; 98.71% used; 110410783 free inodes.

server2 `/tmp`: 23092469760 available bytes; 98.71% used; 110410783 free inodes.

server2 `/var/tmp`: 23092469760 available bytes; 98.71% used; 110410783 free inodes.

server2 `/mnt/raid5`: 487122853888 available bytes; 96.63% used; 445163753 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84352536576 available bytes; 95.29% used; 114156084 free inodes.

server3 `/home`: 84352536576 available bytes; 95.29% used; 114156084 free inodes.

server3 `/data`: 149182873600 available bytes; 97.94% used; 225813751 free inodes.

server3 `/tmp`: 84352536576 available bytes; 95.29% used; 114156084 free inodes.

server3 `/var/tmp`: 84352536576 available bytes; 95.29% used; 114156084 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105797775360 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105797775360 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 56917929984 available bytes; 99.21% used; 225081959 free inodes.

server4 `/tmp`: 105797775360 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105797775360 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
