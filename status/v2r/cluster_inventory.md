# V2R cluster inventory

2026-09-24T13:32:40.703814+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324027408384 available bytes; 81.92% used; 112481513 free inodes.

server1 `/home`: 324027408384 available bytes; 81.92% used; 112481513 free inodes.

server1 `/tmp`: 324027408384 available bytes; 81.92% used; 112481513 free inodes.

server1 `/var/tmp`: 324027408384 available bytes; 81.92% used; 112481513 free inodes.

server1 `/mnt/raid5`: 417023123456 available bytes; 98.09% used; 337674897 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57523216384 available bytes; 96.79% used; 110428702 free inodes.

server2 `/home`: 57523216384 available bytes; 96.79% used; 110428702 free inodes.

server2 `/tmp`: 57523216384 available bytes; 96.79% used; 110428702 free inodes.

server2 `/var/tmp`: 57523216384 available bytes; 96.79% used; 110428702 free inodes.

server2 `/mnt/raid5`: 506551906304 available bytes; 96.50% used; 445169563 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84704604160 available bytes; 95.27% used; 114165426 free inodes.

server3 `/home`: 84704604160 available bytes; 95.27% used; 114165426 free inodes.

server3 `/data`: 161250127872 available bytes; 97.77% used; 225803118 free inodes.

server3 `/tmp`: 84704604160 available bytes; 95.27% used; 114165426 free inodes.

server3 `/var/tmp`: 84704604160 available bytes; 95.27% used; 114165426 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105769607168 available bytes; 94.10% used; 114348737 free inodes.

server4 `/home`: 105769607168 available bytes; 94.10% used; 114348737 free inodes.

server4 `/data`: 90044190720 available bytes; 98.76% used; 225257180 free inodes.

server4 `/tmp`: 105769607168 available bytes; 94.10% used; 114348737 free inodes.

server4 `/var/tmp`: 105769607168 available bytes; 94.10% used; 114348737 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
