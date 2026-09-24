# V2R cluster inventory

2026-09-24T16:59:36.102201+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324023091200 available bytes; 81.92% used; 112481449 free inodes.

server1 `/home`: 324023091200 available bytes; 81.92% used; 112481449 free inodes.

server1 `/tmp`: 324023091200 available bytes; 81.92% used; 112481449 free inodes.

server1 `/var/tmp`: 324023091200 available bytes; 81.92% used; 112481449 free inodes.

server1 `/mnt/raid5`: 416513216512 available bytes; 98.09% used; 337649936 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57068060672 available bytes; 96.82% used; 110418031 free inodes.

server2 `/home`: 57068060672 available bytes; 96.82% used; 110418031 free inodes.

server2 `/tmp`: 57068060672 available bytes; 96.82% used; 110418031 free inodes.

server2 `/var/tmp`: 57068060672 available bytes; 96.82% used; 110418031 free inodes.

server2 `/mnt/raid5`: 499495628800 available bytes; 96.55% used; 445163373 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84419518464 available bytes; 95.29% used; 114156150 free inodes.

server3 `/home`: 84419518464 available bytes; 95.29% used; 114156150 free inodes.

server3 `/data`: 159157297152 available bytes; 97.80% used; 225787413 free inodes.

server3 `/tmp`: 84419518464 available bytes; 95.29% used; 114156150 free inodes.

server3 `/var/tmp`: 84419518464 available bytes; 95.29% used; 114156150 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105682534400 available bytes; 94.10% used; 114348574 free inodes.

server4 `/home`: 105682534400 available bytes; 94.10% used; 114348574 free inodes.

server4 `/data`: 89174888448 available bytes; 98.77% used; 225254945 free inodes.

server4 `/tmp`: 105682534400 available bytes; 94.10% used; 114348574 free inodes.

server4 `/var/tmp`: 105682534400 available bytes; 94.10% used; 114348574 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
