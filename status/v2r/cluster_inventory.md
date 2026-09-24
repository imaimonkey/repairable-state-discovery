# V2R cluster inventory

2026-09-24T17:30:41.284364+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324004409344 available bytes; 81.92% used; 112481446 free inodes.

server1 `/home`: 324004409344 available bytes; 81.92% used; 112481446 free inodes.

server1 `/tmp`: 324004409344 available bytes; 81.92% used; 112481446 free inodes.

server1 `/var/tmp`: 324004409344 available bytes; 81.92% used; 112481446 free inodes.

server1 `/mnt/raid5`: 416443969536 available bytes; 98.09% used; 337646307 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 56919216128 available bytes; 96.82% used; 110412521 free inodes.

server2 `/home`: 56919216128 available bytes; 96.82% used; 110412521 free inodes.

server2 `/tmp`: 56919216128 available bytes; 96.82% used; 110412521 free inodes.

server2 `/var/tmp`: 56919216128 available bytes; 96.82% used; 110412521 free inodes.

server2 `/mnt/raid5`: 498779041792 available bytes; 96.55% used; 445162452 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84409896960 available bytes; 95.29% used; 114156148 free inodes.

server3 `/home`: 84409896960 available bytes; 95.29% used; 114156148 free inodes.

server3 `/data`: 158939000832 available bytes; 97.80% used; 225786825 free inodes.

server3 `/tmp`: 84409896960 available bytes; 95.29% used; 114156148 free inodes.

server3 `/var/tmp`: 84409896960 available bytes; 95.29% used; 114156148 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105681526784 available bytes; 94.10% used; 114348570 free inodes.

server4 `/home`: 105681526784 available bytes; 94.10% used; 114348570 free inodes.

server4 `/data`: 89074307072 available bytes; 98.77% used; 225254117 free inodes.

server4 `/tmp`: 105681526784 available bytes; 94.10% used; 114348570 free inodes.

server4 `/var/tmp`: 105681526784 available bytes; 94.10% used; 114348570 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
