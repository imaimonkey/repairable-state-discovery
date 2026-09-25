# V2R cluster inventory

2026-09-25T03:39:40.205925+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318939701248 available bytes; 82.21% used; 112480356 free inodes.

server1 `/home`: 318939701248 available bytes; 82.21% used; 112480356 free inodes.

server1 `/tmp`: 318939701248 available bytes; 82.21% used; 112480356 free inodes.

server1 `/var/tmp`: 318939701248 available bytes; 82.21% used; 112480356 free inodes.

server1 `/mnt/raid5`: 416063217664 available bytes; 98.09% used; 337597801 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22982422528 available bytes; 98.72% used; 110410446 free inodes.

server2 `/home`: 22982422528 available bytes; 98.72% used; 110410446 free inodes.

server2 `/tmp`: 22982422528 available bytes; 98.72% used; 110410446 free inodes.

server2 `/var/tmp`: 22982422528 available bytes; 98.72% used; 110410446 free inodes.

server2 `/mnt/raid5`: 464589103104 available bytes; 96.79% used; 445111449 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84341174272 available bytes; 95.29% used; 114156065 free inodes.

server3 `/home`: 84341174272 available bytes; 95.29% used; 114156065 free inodes.

server3 `/data`: 144436264960 available bytes; 98.00% used; 225817315 free inodes.

server3 `/tmp`: 84341174272 available bytes; 95.29% used; 114156065 free inodes.

server3 `/var/tmp`: 84341174272 available bytes; 95.29% used; 114156065 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105683582976 available bytes; 94.10% used; 114350896 free inodes.

server4 `/home`: 105683582976 available bytes; 94.10% used; 114350896 free inodes.

server4 `/data`: 39226822656 available bytes; 99.46% used; 224965767 free inodes.

server4 `/tmp`: 105683582976 available bytes; 94.10% used; 114350896 free inodes.

server4 `/var/tmp`: 105683582976 available bytes; 94.10% used; 114350896 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
