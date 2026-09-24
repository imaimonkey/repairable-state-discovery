# V2R cluster inventory

2026-09-24T01:46:47.313298+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325456400384 available bytes; 81.84% used; 112499459 free inodes.

server1 `/home`: 325456400384 available bytes; 81.84% used; 112499459 free inodes.

server1 `/tmp`: 325456400384 available bytes; 81.84% used; 112499459 free inodes.

server1 `/var/tmp`: 325456400384 available bytes; 81.84% used; 112499459 free inodes.

server1 `/mnt/raid5`: 828037103616 available bytes; 96.20% used; 337733798 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40929439744 available bytes; 97.72% used; 110431867 free inodes.

server2 `/home`: 40929439744 available bytes; 97.72% used; 110431867 free inodes.

server2 `/tmp`: 40929439744 available bytes; 97.72% used; 110431867 free inodes.

server2 `/var/tmp`: 40929439744 available bytes; 97.72% used; 110431867 free inodes.

server2 `/mnt/raid5`: 530281541632 available bytes; 96.34% used; 445200832 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292718395392 available bytes; 83.67% used; 114211058 free inodes.

server3 `/home`: 292718395392 available bytes; 83.67% used; 114211058 free inodes.

server3 `/data`: 71393742848 available bytes; 99.01% used; 225841948 free inodes.

server3 `/tmp`: 292718395392 available bytes; 83.67% used; 114211058 free inodes.

server3 `/var/tmp`: 292718395392 available bytes; 83.67% used; 114211058 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105951911936 available bytes; 94.09% used; 114348584 free inodes.

server4 `/home`: 105951911936 available bytes; 94.09% used; 114348584 free inodes.

server4 `/data`: 289763069952 available bytes; 96.00% used; 225388487 free inodes.

server4 `/tmp`: 105951911936 available bytes; 94.09% used; 114348584 free inodes.

server4 `/var/tmp`: 105951911936 available bytes; 94.09% used; 114348584 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
