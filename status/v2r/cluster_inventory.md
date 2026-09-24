# V2R cluster inventory

2026-09-24T21:46:55.690260+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323948748800 available bytes; 81.93% used; 112481413 free inodes.

server1 `/home`: 323948748800 available bytes; 81.93% used; 112481413 free inodes.

server1 `/tmp`: 323948748800 available bytes; 81.93% used; 112481413 free inodes.

server1 `/var/tmp`: 323948748800 available bytes; 81.93% used; 112481413 free inodes.

server1 `/mnt/raid5`: 415464226816 available bytes; 98.09% used; 337625491 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30130393088 available bytes; 98.32% used; 110411304 free inodes.

server2 `/home`: 30130393088 available bytes; 98.32% used; 110411304 free inodes.

server2 `/tmp`: 30130393088 available bytes; 98.32% used; 110411304 free inodes.

server2 `/var/tmp`: 30130393088 available bytes; 98.32% used; 110411304 free inodes.

server2 `/mnt/raid5`: 489357807616 available bytes; 96.62% used; 445154485 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84380336128 available bytes; 95.29% used; 114156081 free inodes.

server3 `/home`: 84380336128 available bytes; 95.29% used; 114156081 free inodes.

server3 `/data`: 150018392064 available bytes; 97.93% used; 225802867 free inodes.

server3 `/tmp`: 84380336128 available bytes; 95.29% used; 114156081 free inodes.

server3 `/var/tmp`: 84380336128 available bytes; 95.29% used; 114156081 free inodes.
| server4 | True | ['1', '4', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105365688320 available bytes; 94.12% used; 114318595 free inodes.

server4 `/home`: 105365688320 available bytes; 94.12% used; 114318597 free inodes.

server4 `/data`: 80470536192 available bytes; 98.89% used; 225243704 free inodes.

server4 `/tmp`: 105365688320 available bytes; 94.12% used; 114318599 free inodes.

server4 `/var/tmp`: 105365688320 available bytes; 94.12% used; 114318600 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
