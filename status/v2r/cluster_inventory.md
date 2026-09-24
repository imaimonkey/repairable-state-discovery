# V2R cluster inventory

2026-09-24T17:10:32.194381+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324008751104 available bytes; 81.92% used; 112481441 free inodes.

server1 `/home`: 324008751104 available bytes; 81.92% used; 112481441 free inodes.

server1 `/tmp`: 324008751104 available bytes; 81.92% used; 112481441 free inodes.

server1 `/var/tmp`: 324008751104 available bytes; 81.92% used; 112481441 free inodes.

server1 `/mnt/raid5`: 416492449792 available bytes; 98.09% used; 337648662 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57053683712 available bytes; 96.82% used; 110417901 free inodes.

server2 `/home`: 57053683712 available bytes; 96.82% used; 110417901 free inodes.

server2 `/tmp`: 57053683712 available bytes; 96.82% used; 110417901 free inodes.

server2 `/var/tmp`: 57053683712 available bytes; 96.82% used; 110417901 free inodes.

server2 `/mnt/raid5`: 499680882688 available bytes; 96.55% used; 445163060 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84409733120 available bytes; 95.29% used; 114156152 free inodes.

server3 `/home`: 84409733120 available bytes; 95.29% used; 114156152 free inodes.

server3 `/data`: 159062384640 available bytes; 97.80% used; 225787208 free inodes.

server3 `/tmp`: 84409733120 available bytes; 95.29% used; 114156152 free inodes.

server3 `/var/tmp`: 84409733120 available bytes; 95.29% used; 114156152 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105682112512 available bytes; 94.10% used; 114348569 free inodes.

server4 `/home`: 105682112512 available bytes; 94.10% used; 114348569 free inodes.

server4 `/data`: 89162194944 available bytes; 98.77% used; 225254656 free inodes.

server4 `/tmp`: 105682112512 available bytes; 94.10% used; 114348569 free inodes.

server4 `/var/tmp`: 105682112512 available bytes; 94.10% used; 114348569 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
