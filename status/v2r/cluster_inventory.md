# V2R cluster inventory

2026-09-24T13:03:03.723619+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324038057984 available bytes; 81.92% used; 112481558 free inodes.

server1 `/home`: 324038057984 available bytes; 81.92% used; 112481558 free inodes.

server1 `/tmp`: 324038057984 available bytes; 81.92% used; 112481558 free inodes.

server1 `/var/tmp`: 324038057984 available bytes; 81.92% used; 112481558 free inodes.

server1 `/mnt/raid5`: 417083183104 available bytes; 98.09% used; 337678384 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57557508096 available bytes; 96.79% used; 110429003 free inodes.

server2 `/home`: 57557508096 available bytes; 96.79% used; 110429003 free inodes.

server2 `/tmp`: 57557508096 available bytes; 96.79% used; 110429003 free inodes.

server2 `/var/tmp`: 57557508096 available bytes; 96.79% used; 110429003 free inodes.

server2 `/mnt/raid5`: 507471491072 available bytes; 96.49% used; 445170885 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85213794304 available bytes; 95.24% used; 114168903 free inodes.

server3 `/home`: 85213794304 available bytes; 95.24% used; 114168903 free inodes.

server3 `/data`: 163001044992 available bytes; 97.75% used; 225813687 free inodes.

server3 `/tmp`: 85213794304 available bytes; 95.24% used; 114168903 free inodes.

server3 `/var/tmp`: 85213794304 available bytes; 95.24% used; 114168903 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779224576 available bytes; 94.10% used; 114348761 free inodes.

server4 `/home`: 105779224576 available bytes; 94.10% used; 114348761 free inodes.

server4 `/data`: 90034843648 available bytes; 98.76% used; 225257179 free inodes.

server4 `/tmp`: 105779224576 available bytes; 94.10% used; 114348761 free inodes.

server4 `/var/tmp`: 105779224576 available bytes; 94.10% used; 114348761 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
