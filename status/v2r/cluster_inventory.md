# V2R cluster inventory

2026-09-24T12:45:43.757212+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324039577600 available bytes; 81.92% used; 112481557 free inodes.

server1 `/home`: 324039577600 available bytes; 81.92% used; 112481557 free inodes.

server1 `/tmp`: 324039577600 available bytes; 81.92% used; 112481557 free inodes.

server1 `/var/tmp`: 324039577600 available bytes; 81.92% used; 112481557 free inodes.

server1 `/mnt/raid5`: 403367690240 available bytes; 98.15% used; 337680458 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57579704320 available bytes; 96.79% used; 110429177 free inodes.

server2 `/home`: 57579704320 available bytes; 96.79% used; 110429177 free inodes.

server2 `/tmp`: 57579704320 available bytes; 96.79% used; 110429177 free inodes.

server2 `/var/tmp`: 57579704320 available bytes; 96.79% used; 110429177 free inodes.

server2 `/mnt/raid5`: 508024029184 available bytes; 96.49% used; 445171416 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85279535104 available bytes; 95.24% used; 114172034 free inodes.

server3 `/home`: 85279535104 available bytes; 95.24% used; 114172034 free inodes.

server3 `/data`: 163140317184 available bytes; 97.75% used; 225814435 free inodes.

server3 `/tmp`: 85279535104 available bytes; 95.24% used; 114172034 free inodes.

server3 `/var/tmp`: 85279535104 available bytes; 95.24% used; 114172034 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105780039680 available bytes; 94.10% used; 114348784 free inodes.

server4 `/home`: 105780039680 available bytes; 94.10% used; 114348784 free inodes.

server4 `/data`: 90048344064 available bytes; 98.76% used; 225257236 free inodes.

server4 `/tmp`: 105780039680 available bytes; 94.10% used; 114348784 free inodes.

server4 `/var/tmp`: 105780039680 available bytes; 94.10% used; 114348784 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
