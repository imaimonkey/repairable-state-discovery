# V2R cluster inventory

2026-09-24T23:56:22.978112+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318998974464 available bytes; 82.20% used; 112480780 free inodes.

server1 `/home`: 318998974464 available bytes; 82.20% used; 112480780 free inodes.

server1 `/tmp`: 318998974464 available bytes; 82.20% used; 112480780 free inodes.

server1 `/var/tmp`: 318998974464 available bytes; 82.20% used; 112480780 free inodes.

server1 `/mnt/raid5`: 416921890816 available bytes; 98.09% used; 337623811 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23099564032 available bytes; 98.71% used; 110410779 free inodes.

server2 `/home`: 23099564032 available bytes; 98.71% used; 110410779 free inodes.

server2 `/tmp`: 23099564032 available bytes; 98.71% used; 110410779 free inodes.

server2 `/var/tmp`: 23099564032 available bytes; 98.71% used; 110410779 free inodes.

server2 `/mnt/raid5`: 487479353344 available bytes; 96.63% used; 445164000 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84354420736 available bytes; 95.29% used; 114156078 free inodes.

server3 `/home`: 84354420736 available bytes; 95.29% used; 114156078 free inodes.

server3 `/data`: 149517996032 available bytes; 97.93% used; 225814065 free inodes.

server3 `/tmp`: 84354420736 available bytes; 95.29% used; 114156078 free inodes.

server3 `/var/tmp`: 84354420736 available bytes; 95.29% used; 114156078 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105798844416 available bytes; 94.10% used; 114348295 free inodes.

server4 `/home`: 105798844416 available bytes; 94.10% used; 114348295 free inodes.

server4 `/data`: 60811431936 available bytes; 99.16% used; 225108309 free inodes.

server4 `/tmp`: 105798844416 available bytes; 94.10% used; 114348295 free inodes.

server4 `/var/tmp`: 105798844416 available bytes; 94.10% used; 114348295 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
