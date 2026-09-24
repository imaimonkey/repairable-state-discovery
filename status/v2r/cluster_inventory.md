# V2R cluster inventory

2026-09-24T17:15:13.504367+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324008112128 available bytes; 81.92% used; 112481439 free inodes.

server1 `/home`: 324008112128 available bytes; 81.92% used; 112481439 free inodes.

server1 `/tmp`: 324008112128 available bytes; 81.92% used; 112481439 free inodes.

server1 `/var/tmp`: 324008112128 available bytes; 81.92% used; 112481439 free inodes.

server1 `/mnt/raid5`: 416480149504 available bytes; 98.09% used; 337648117 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57049092096 available bytes; 96.82% used; 110417852 free inodes.

server2 `/home`: 57049092096 available bytes; 96.82% used; 110417852 free inodes.

server2 `/tmp`: 57049092096 available bytes; 96.82% used; 110417852 free inodes.

server2 `/var/tmp`: 57049092096 available bytes; 96.82% used; 110417852 free inodes.

server2 `/mnt/raid5`: 499533848576 available bytes; 96.55% used; 445162767 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84409049088 available bytes; 95.29% used; 114156150 free inodes.

server3 `/home`: 84409049088 available bytes; 95.29% used; 114156150 free inodes.

server3 `/data`: 159035858944 available bytes; 97.80% used; 225787109 free inodes.

server3 `/tmp`: 84409049088 available bytes; 95.29% used; 114156150 free inodes.

server3 `/var/tmp`: 84409049088 available bytes; 95.29% used; 114156150 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105681993728 available bytes; 94.10% used; 114348569 free inodes.

server4 `/home`: 105681993728 available bytes; 94.10% used; 114348569 free inodes.

server4 `/data`: 89151283200 available bytes; 98.77% used; 225254583 free inodes.

server4 `/tmp`: 105681993728 available bytes; 94.10% used; 114348569 free inodes.

server4 `/var/tmp`: 105681993728 available bytes; 94.10% used; 114348569 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
