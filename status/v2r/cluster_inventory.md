# V2R cluster inventory

2026-09-25T04:24:25.449774+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318929862656 available bytes; 82.21% used; 112480374 free inodes.

server1 `/home`: 318929862656 available bytes; 82.21% used; 112480374 free inodes.

server1 `/tmp`: 318929862656 available bytes; 82.21% used; 112480374 free inodes.

server1 `/var/tmp`: 318929862656 available bytes; 82.21% used; 112480374 free inodes.

server1 `/mnt/raid5`: 408752431104 available bytes; 98.12% used; 337592379 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22956101632 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22956101632 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22956101632 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22956101632 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 442566406144 available bytes; 96.94% used; 445109992 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340428800 available bytes; 95.29% used; 114156072 free inodes.

server3 `/home`: 84340428800 available bytes; 95.29% used; 114156072 free inodes.

server3 `/data`: 143682785280 available bytes; 98.01% used; 225816249 free inodes.

server3 `/tmp`: 84340428800 available bytes; 95.29% used; 114156072 free inodes.

server3 `/var/tmp`: 84340428800 available bytes; 95.29% used; 114156072 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105673789440 available bytes; 94.10% used; 114350881 free inodes.

server4 `/home`: 105673789440 available bytes; 94.10% used; 114350881 free inodes.

server4 `/data`: 32814129152 available bytes; 99.55% used; 224963203 free inodes.

server4 `/tmp`: 105673789440 available bytes; 94.10% used; 114350881 free inodes.

server4 `/var/tmp`: 105673789440 available bytes; 94.10% used; 114350881 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
