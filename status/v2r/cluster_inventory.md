# V2R cluster inventory

2026-09-24T23:44:03.318764+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319013392384 available bytes; 82.20% used; 112480782 free inodes.

server1 `/home`: 319013392384 available bytes; 82.20% used; 112480782 free inodes.

server1 `/tmp`: 319013392384 available bytes; 82.20% used; 112480782 free inodes.

server1 `/var/tmp`: 319013392384 available bytes; 82.20% used; 112480782 free inodes.

server1 `/mnt/raid5`: 415199604736 available bytes; 98.10% used; 337611592 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23103582208 available bytes; 98.71% used; 110410812 free inodes.

server2 `/home`: 23103582208 available bytes; 98.71% used; 110410812 free inodes.

server2 `/tmp`: 23103582208 available bytes; 98.71% used; 110410812 free inodes.

server2 `/var/tmp`: 23103582208 available bytes; 98.71% used; 110410812 free inodes.

server2 `/mnt/raid5`: 486043299840 available bytes; 96.64% used; 445150919 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84360679424 available bytes; 95.29% used; 114156079 free inodes.

server3 `/home`: 84360679424 available bytes; 95.29% used; 114156079 free inodes.

server3 `/data`: 147971645440 available bytes; 97.95% used; 225800663 free inodes.

server3 `/tmp`: 84360679424 available bytes; 95.29% used; 114156079 free inodes.

server3 `/var/tmp`: 84360679424 available bytes; 95.29% used; 114156079 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105799172096 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105799172096 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 61030260736 available bytes; 99.16% used; 225126954 free inodes.

server4 `/tmp`: 105799172096 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105799172096 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
