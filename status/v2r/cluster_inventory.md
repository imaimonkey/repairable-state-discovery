# V2R cluster inventory

2026-09-24T08:20:33.228173+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324403916800 available bytes; 81.90% used; 112490544 free inodes.

server1 `/home`: 324403916800 available bytes; 81.90% used; 112490544 free inodes.

server1 `/tmp`: 324403916800 available bytes; 81.90% used; 112490544 free inodes.

server1 `/var/tmp`: 324403916800 available bytes; 81.90% used; 112490544 free inodes.

server1 `/mnt/raid5`: 510274260992 available bytes; 97.66% used; 337721299 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57811357696 available bytes; 96.77% used; 110431022 free inodes.

server2 `/home`: 57811357696 available bytes; 96.77% used; 110431022 free inodes.

server2 `/tmp`: 57811357696 available bytes; 96.77% used; 110431022 free inodes.

server2 `/var/tmp`: 57811357696 available bytes; 96.77% used; 110431022 free inodes.

server2 `/mnt/raid5`: 516440956928 available bytes; 96.43% used; 445179829 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85899874304 available bytes; 95.21% used; 114200261 free inodes.

server3 `/home`: 85899874304 available bytes; 95.21% used; 114200261 free inodes.

server3 `/data`: 175143534592 available bytes; 97.58% used; 225823173 free inodes.

server3 `/tmp`: 85899874304 available bytes; 95.21% used; 114200261 free inodes.

server3 `/var/tmp`: 85899874304 available bytes; 95.21% used; 114200261 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105778204672 available bytes; 94.10% used; 114349144 free inodes.

server4 `/home`: 105778204672 available bytes; 94.10% used; 114349144 free inodes.

server4 `/data`: 280474464256 available bytes; 96.12% used; 225350816 free inodes.

server4 `/tmp`: 105778204672 available bytes; 94.10% used; 114349144 free inodes.

server4 `/var/tmp`: 105778204672 available bytes; 94.10% used; 114349144 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
