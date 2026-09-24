# V2R cluster inventory

2026-09-24T21:29:57.415291+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323953123328 available bytes; 81.93% used; 112481415 free inodes.

server1 `/home`: 323953123328 available bytes; 81.93% used; 112481415 free inodes.

server1 `/tmp`: 323953123328 available bytes; 81.93% used; 112481415 free inodes.

server1 `/var/tmp`: 323953123328 available bytes; 81.93% used; 112481415 free inodes.

server1 `/mnt/raid5`: 415498330112 available bytes; 98.09% used; 337627481 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30140596224 available bytes; 98.32% used; 110411342 free inodes.

server2 `/home`: 30140596224 available bytes; 98.32% used; 110411342 free inodes.

server2 `/tmp`: 30140596224 available bytes; 98.32% used; 110411342 free inodes.

server2 `/var/tmp`: 30140596224 available bytes; 98.32% used; 110411342 free inodes.

server2 `/mnt/raid5`: 490423791616 available bytes; 96.61% used; 445154995 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84383592448 available bytes; 95.29% used; 114156095 free inodes.

server3 `/home`: 84383592448 available bytes; 95.29% used; 114156095 free inodes.

server3 `/data`: 150306177024 available bytes; 97.92% used; 225803200 free inodes.

server3 `/tmp`: 84383592448 available bytes; 95.29% used; 114156095 free inodes.

server3 `/var/tmp`: 84383592448 available bytes; 95.29% used; 114156095 free inodes.
| server4 | True | ['1', '4', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105630212096 available bytes; 94.11% used; 114348350 free inodes.

server4 `/home`: 105630212096 available bytes; 94.11% used; 114348350 free inodes.

server4 `/data`: 83980652544 available bytes; 98.84% used; 225252958 free inodes.

server4 `/tmp`: 105630212096 available bytes; 94.11% used; 114348350 free inodes.

server4 `/var/tmp`: 105630212096 available bytes; 94.11% used; 114348350 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
