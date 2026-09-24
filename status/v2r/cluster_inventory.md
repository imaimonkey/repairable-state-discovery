# V2R cluster inventory

2026-09-24T16:00:37.576838+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324024213504 available bytes; 81.92% used; 112481453 free inodes.

server1 `/home`: 324024213504 available bytes; 81.92% used; 112481453 free inodes.

server1 `/tmp`: 324024213504 available bytes; 81.92% used; 112481453 free inodes.

server1 `/var/tmp`: 324024213504 available bytes; 81.92% used; 112481453 free inodes.

server1 `/mnt/raid5`: 416689147904 available bytes; 98.09% used; 337657602 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57355329536 available bytes; 96.80% used; 110427197 free inodes.

server2 `/home`: 57355329536 available bytes; 96.80% used; 110427197 free inodes.

server2 `/tmp`: 57355329536 available bytes; 96.80% used; 110427197 free inodes.

server2 `/var/tmp`: 57355329536 available bytes; 96.80% used; 110427197 free inodes.

server2 `/mnt/raid5`: 501840273408 available bytes; 96.53% used; 445164969 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84856434688 available bytes; 95.26% used; 114182202 free inodes.

server3 `/home`: 84856434688 available bytes; 95.26% used; 114182202 free inodes.

server3 `/data`: 160080687104 available bytes; 97.79% used; 225805966 free inodes.

server3 `/tmp`: 84856434688 available bytes; 95.26% used; 114182202 free inodes.

server3 `/var/tmp`: 84856434688 available bytes; 95.26% used; 114182202 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105698197504 available bytes; 94.10% used; 114348610 free inodes.

server4 `/home`: 105698197504 available bytes; 94.10% used; 114348610 free inodes.

server4 `/data`: 89339260928 available bytes; 98.77% used; 225256350 free inodes.

server4 `/tmp`: 105698197504 available bytes; 94.10% used; 114348610 free inodes.

server4 `/var/tmp`: 105698197504 available bytes; 94.10% used; 114348610 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
