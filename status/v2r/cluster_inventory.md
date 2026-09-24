# V2R cluster inventory

2026-09-24T17:58:29.361635+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324004765696 available bytes; 81.92% used; 112481435 free inodes.

server1 `/home`: 324004765696 available bytes; 81.92% used; 112481435 free inodes.

server1 `/tmp`: 324004765696 available bytes; 81.92% used; 112481435 free inodes.

server1 `/var/tmp`: 324004765696 available bytes; 81.92% used; 112481435 free inodes.

server1 `/mnt/raid5`: 416388087808 available bytes; 98.09% used; 337643075 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 56898031616 available bytes; 96.83% used; 110412306 free inodes.

server2 `/home`: 56898031616 available bytes; 96.83% used; 110412306 free inodes.

server2 `/tmp`: 56898031616 available bytes; 96.83% used; 110412306 free inodes.

server2 `/var/tmp`: 56898031616 available bytes; 96.83% used; 110412306 free inodes.

server2 `/mnt/raid5`: 498000699392 available bytes; 96.56% used; 445161610 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84412203008 available bytes; 95.29% used; 114156136 free inodes.

server3 `/home`: 84412203008 available bytes; 95.29% used; 114156136 free inodes.

server3 `/data`: 151812673536 available bytes; 97.90% used; 225786288 free inodes.

server3 `/tmp`: 84412203008 available bytes; 95.29% used; 114156136 free inodes.

server3 `/var/tmp`: 84412203008 available bytes; 95.29% used; 114156136 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105672110080 available bytes; 94.10% used; 114348541 free inodes.

server4 `/home`: 105672110080 available bytes; 94.10% used; 114348541 free inodes.

server4 `/data`: 88690663424 available bytes; 98.77% used; 225253560 free inodes.

server4 `/tmp`: 105672110080 available bytes; 94.10% used; 114348541 free inodes.

server4 `/var/tmp`: 105672110080 available bytes; 94.10% used; 114348541 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
