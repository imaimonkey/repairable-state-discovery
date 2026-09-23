# V2R cluster inventory

2026-09-23T11:52:39.427285+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['6'] | [] |

server2 `/`: 41820225536 available bytes; 97.67% used; 110436697 free inodes.

server2 `/home`: 41820225536 available bytes; 97.67% used; 110436697 free inodes.

server2 `/tmp`: 41820225536 available bytes; 97.67% used; 110436697 free inodes.

server2 `/var/tmp`: 41820225536 available bytes; 97.67% used; 110436697 free inodes.

server2 `/mnt/raid5`: 558430904320 available bytes; 96.14% used; 445231546 free inodes.
| server3 | True | ['1', '3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 380102963200 available bytes; 78.79% used; 114347676 free inodes.

server3 `/home`: 380102963200 available bytes; 78.79% used; 114347676 free inodes.

server3 `/data`: 137461051392 available bytes; 98.10% used; 225865034 free inodes.

server3 `/tmp`: 380102963200 available bytes; 78.79% used; 114347676 free inodes.

server3 `/var/tmp`: 380102963200 available bytes; 78.79% used; 114347676 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111605297152 available bytes; 93.77% used; 114379004 free inodes.

server4 `/home`: 111605297152 available bytes; 93.77% used; 114379004 free inodes.

server4 `/data`: 67428208640 available bytes; 99.07% used; 225411870 free inodes.

server4 `/tmp`: 111605297152 available bytes; 93.77% used; 114379004 free inodes.

server4 `/var/tmp`: 111605297152 available bytes; 93.77% used; 114379004 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
