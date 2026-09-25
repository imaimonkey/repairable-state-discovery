# V2R cluster inventory

2026-09-25T07:07:40.257736+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318872657920 available bytes; 82.21% used; 112480379 free inodes.

server1 `/home`: 318872657920 available bytes; 82.21% used; 112480379 free inodes.

server1 `/tmp`: 318872657920 available bytes; 82.21% used; 112480379 free inodes.

server1 `/var/tmp`: 318872657920 available bytes; 82.21% used; 112480379 free inodes.

server1 `/mnt/raid5`: 401119363072 available bytes; 98.16% used; 337560429 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22870867968 available bytes; 98.72% used; 110410520 free inodes.

server2 `/home`: 22870867968 available bytes; 98.72% used; 110410520 free inodes.

server2 `/tmp`: 22870867968 available bytes; 98.72% used; 110410520 free inodes.

server2 `/var/tmp`: 22870867968 available bytes; 98.72% used; 110410520 free inodes.

server2 `/mnt/raid5`: 330341666816 available bytes; 97.72% used; 445097762 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84447354880 available bytes; 95.29% used; 114156033 free inodes.

server3 `/home`: 84447354880 available bytes; 95.29% used; 114156033 free inodes.

server3 `/data`: 142453637120 available bytes; 98.03% used; 225813095 free inodes.

server3 `/tmp`: 84447354880 available bytes; 95.29% used; 114156033 free inodes.

server3 `/var/tmp`: 84447354880 available bytes; 95.29% used; 114156033 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105638559744 available bytes; 94.10% used; 114350361 free inodes.

server4 `/home`: 105638559744 available bytes; 94.10% used; 114350361 free inodes.

server4 `/data`: 249485799424 available bytes; 96.55% used; 225016697 free inodes.

server4 `/tmp`: 105638559744 available bytes; 94.10% used; 114350361 free inodes.

server4 `/var/tmp`: 105638559744 available bytes; 94.10% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
