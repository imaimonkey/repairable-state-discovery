# V2R cluster inventory

2026-09-24T12:53:44.882503+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324041060352 available bytes; 81.92% used; 112481557 free inodes.

server1 `/home`: 324041060352 available bytes; 81.92% used; 112481557 free inodes.

server1 `/tmp`: 324041060352 available bytes; 81.92% used; 112481557 free inodes.

server1 `/var/tmp`: 324041060352 available bytes; 81.92% used; 112481557 free inodes.

server1 `/mnt/raid5`: 396452954112 available bytes; 98.18% used; 337679478 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57566662656 available bytes; 96.79% used; 110429097 free inodes.

server2 `/home`: 57566662656 available bytes; 96.79% used; 110429097 free inodes.

server2 `/tmp`: 57566662656 available bytes; 96.79% used; 110429097 free inodes.

server2 `/var/tmp`: 57566662656 available bytes; 96.79% used; 110429097 free inodes.

server2 `/mnt/raid5`: 507777236992 available bytes; 96.49% used; 445171046 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85247959040 available bytes; 95.24% used; 114169221 free inodes.

server3 `/home`: 85247959040 available bytes; 95.24% used; 114169221 free inodes.

server3 `/data`: 163074068480 available bytes; 97.75% used; 225814195 free inodes.

server3 `/tmp`: 85247959040 available bytes; 95.24% used; 114169221 free inodes.

server3 `/var/tmp`: 85247959040 available bytes; 95.24% used; 114169221 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779650560 available bytes; 94.10% used; 114348776 free inodes.

server4 `/home`: 105779650560 available bytes; 94.10% used; 114348776 free inodes.

server4 `/data`: 90051678208 available bytes; 98.76% used; 225257227 free inodes.

server4 `/tmp`: 105779650560 available bytes; 94.10% used; 114348776 free inodes.

server4 `/var/tmp`: 105779650560 available bytes; 94.10% used; 114348776 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
