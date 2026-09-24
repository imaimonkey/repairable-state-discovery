# V2R cluster inventory

2026-09-24T21:15:50.390996+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323962740736 available bytes; 81.93% used; 112481418 free inodes.

server1 `/home`: 323962740736 available bytes; 81.93% used; 112481418 free inodes.

server1 `/tmp`: 323962740736 available bytes; 81.93% used; 112481418 free inodes.

server1 `/var/tmp`: 323962740736 available bytes; 81.93% used; 112481418 free inodes.

server1 `/mnt/raid5`: 415533129728 available bytes; 98.09% used; 337629125 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 30134738944 available bytes; 98.32% used; 110411373 free inodes.

server2 `/home`: 30134738944 available bytes; 98.32% used; 110411373 free inodes.

server2 `/tmp`: 30134738944 available bytes; 98.32% used; 110411373 free inodes.

server2 `/var/tmp`: 30134738944 available bytes; 98.32% used; 110411373 free inodes.

server2 `/mnt/raid5`: 490851532800 available bytes; 96.61% used; 445155426 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 84383838208 available bytes; 95.29% used; 114156111 free inodes.

server3 `/home`: 84383838208 available bytes; 95.29% used; 114156111 free inodes.

server3 `/data`: 150548070400 available bytes; 97.92% used; 225803470 free inodes.

server3 `/tmp`: 84383838208 available bytes; 95.29% used; 114156111 free inodes.

server3 `/var/tmp`: 84383838208 available bytes; 95.29% used; 114156111 free inodes.
| server4 | True | ['4', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105632608256 available bytes; 94.11% used; 114348354 free inodes.

server4 `/home`: 105632608256 available bytes; 94.11% used; 114348354 free inodes.

server4 `/data`: 71833878528 available bytes; 99.01% used; 225253594 free inodes.

server4 `/tmp`: 105632608256 available bytes; 94.11% used; 114348354 free inodes.

server4 `/var/tmp`: 105632608256 available bytes; 94.11% used; 114348354 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
