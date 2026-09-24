# V2R cluster inventory

2026-09-24T16:31:40.922314+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324022968320 available bytes; 81.92% used; 112481451 free inodes.

server1 `/home`: 324022968320 available bytes; 81.92% used; 112481451 free inodes.

server1 `/tmp`: 324022968320 available bytes; 81.92% used; 112481451 free inodes.

server1 `/var/tmp`: 324022968320 available bytes; 81.92% used; 112481451 free inodes.

server1 `/mnt/raid5`: 416574029824 available bytes; 98.09% used; 337653198 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57325182976 available bytes; 96.80% used; 110426867 free inodes.

server2 `/home`: 57325182976 available bytes; 96.80% used; 110426867 free inodes.

server2 `/tmp`: 57325182976 available bytes; 96.80% used; 110426867 free inodes.

server2 `/var/tmp`: 57325182976 available bytes; 96.80% used; 110426867 free inodes.

server2 `/mnt/raid5`: 500898754560 available bytes; 96.54% used; 445164507 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84386435072 available bytes; 95.29% used; 114164003 free inodes.

server3 `/home`: 84386435072 available bytes; 95.29% used; 114164003 free inodes.

server3 `/data`: 159344799744 available bytes; 97.80% used; 225788007 free inodes.

server3 `/tmp`: 84386435072 available bytes; 95.29% used; 114164003 free inodes.

server3 `/var/tmp`: 84386435072 available bytes; 95.29% used; 114164003 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105688662016 available bytes; 94.10% used; 114348602 free inodes.

server4 `/home`: 105688662016 available bytes; 94.10% used; 114348602 free inodes.

server4 `/data`: 89273978880 available bytes; 98.77% used; 225255745 free inodes.

server4 `/tmp`: 105688662016 available bytes; 94.10% used; 114348602 free inodes.

server4 `/var/tmp`: 105688662016 available bytes; 94.10% used; 114348602 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
