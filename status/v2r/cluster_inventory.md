# V2R cluster inventory

2026-09-26T08:31:45.518858+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318747099136 available bytes; 82.22% used; 112475801 free inodes.

server1 `/home`: 318747099136 available bytes; 82.22% used; 112475801 free inodes.

server1 `/tmp`: 318747099136 available bytes; 82.22% used; 112475801 free inodes.

server1 `/var/tmp`: 318747099136 available bytes; 82.22% used; 112475801 free inodes.

server1 `/mnt/raid5`: 219100614656 available bytes; 98.99% used; 337538932 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22318342144 available bytes; 98.75% used; 110403906 free inodes.

server2 `/home`: 22318342144 available bytes; 98.75% used; 110403906 free inodes.

server2 `/tmp`: 22318342144 available bytes; 98.75% used; 110403906 free inodes.

server2 `/var/tmp`: 22318342144 available bytes; 98.75% used; 110403906 free inodes.

server2 `/mnt/raid5`: 255660691456 available bytes; 98.23% used; 445024775 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82678550528 available bytes; 95.39% used; 114110809 free inodes.

server3 `/home`: 82678550528 available bytes; 95.39% used; 114110809 free inodes.

server3 `/data`: 123913150464 available bytes; 98.29% used; 225828859 free inodes.

server3 `/tmp`: 82678550528 available bytes; 95.39% used; 114110809 free inodes.

server3 `/var/tmp`: 82678550528 available bytes; 95.39% used; 114110809 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106064097280 available bytes; 94.08% used; 114348133 free inodes.

server4 `/home`: 106064097280 available bytes; 94.08% used; 114348133 free inodes.

server4 `/data`: 89369112576 available bytes; 98.76% used; 224883397 free inodes.

server4 `/tmp`: 106064097280 available bytes; 94.08% used; 114348133 free inodes.

server4 `/var/tmp`: 106064097280 available bytes; 94.08% used; 114348133 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
