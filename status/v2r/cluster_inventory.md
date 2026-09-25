# V2R cluster inventory

2026-09-25T00:42:36.090250+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319086940160 available bytes; 82.20% used; 112480770 free inodes.

server1 `/home`: 319086940160 available bytes; 82.20% used; 112480770 free inodes.

server1 `/tmp`: 319086940160 available bytes; 82.20% used; 112480770 free inodes.

server1 `/var/tmp`: 319086940160 available bytes; 82.20% used; 112480770 free inodes.

server1 `/mnt/raid5`: 416827953152 available bytes; 98.09% used; 337618412 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23077691392 available bytes; 98.71% used; 110410771 free inodes.

server2 `/home`: 23077691392 available bytes; 98.71% used; 110410771 free inodes.

server2 `/tmp`: 23077691392 available bytes; 98.71% used; 110410771 free inodes.

server2 `/var/tmp`: 23077691392 available bytes; 98.71% used; 110410771 free inodes.

server2 `/mnt/raid5`: 501423362048 available bytes; 96.54% used; 445162313 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84352913408 available bytes; 95.29% used; 114156088 free inodes.

server3 `/home`: 84352913408 available bytes; 95.29% used; 114156088 free inodes.

server3 `/data`: 148673064960 available bytes; 97.95% used; 225813207 free inodes.

server3 `/tmp`: 84352913408 available bytes; 95.29% used; 114156088 free inodes.

server3 `/var/tmp`: 84352913408 available bytes; 95.29% used; 114156088 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105788600320 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105788600320 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 56468557824 available bytes; 99.22% used; 225041067 free inodes.

server4 `/tmp`: 105788600320 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105788600320 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
