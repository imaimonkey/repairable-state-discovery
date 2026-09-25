# V2R cluster inventory

2026-09-25T00:48:45.095547+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319087292416 available bytes; 82.20% used; 112480768 free inodes.

server1 `/home`: 319087292416 available bytes; 82.20% used; 112480768 free inodes.

server1 `/tmp`: 319087292416 available bytes; 82.20% used; 112480768 free inodes.

server1 `/var/tmp`: 319087292416 available bytes; 82.20% used; 112480768 free inodes.

server1 `/mnt/raid5`: 416825139200 available bytes; 98.09% used; 337617785 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23076024320 available bytes; 98.71% used; 110410767 free inodes.

server2 `/home`: 23076024320 available bytes; 98.71% used; 110410767 free inodes.

server2 `/tmp`: 23076024320 available bytes; 98.71% used; 110410767 free inodes.

server2 `/var/tmp`: 23076024320 available bytes; 98.71% used; 110410767 free inodes.

server2 `/mnt/raid5`: 501259456512 available bytes; 96.54% used; 445162928 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84357324800 available bytes; 95.29% used; 114156094 free inodes.

server3 `/home`: 84357324800 available bytes; 95.29% used; 114156094 free inodes.

server3 `/data`: 148585418752 available bytes; 97.95% used; 225813085 free inodes.

server3 `/tmp`: 84357324800 available bytes; 95.29% used; 114156094 free inodes.

server3 `/var/tmp`: 84357324800 available bytes; 95.29% used; 114156094 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105788456960 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105788456960 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 56368726016 available bytes; 99.22% used; 225032459 free inodes.

server4 `/tmp`: 105788456960 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105788456960 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
