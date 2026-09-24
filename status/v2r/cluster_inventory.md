# V2R cluster inventory

2026-09-24T12:58:24.684916+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324040126464 available bytes; 81.92% used; 112481551 free inodes.

server1 `/home`: 324040126464 available bytes; 81.92% used; 112481551 free inodes.

server1 `/tmp`: 324040126464 available bytes; 81.92% used; 112481551 free inodes.

server1 `/var/tmp`: 324040126464 available bytes; 81.92% used; 112481551 free inodes.

server1 `/mnt/raid5`: 417089990656 available bytes; 98.09% used; 337678923 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57561665536 available bytes; 96.79% used; 110429048 free inodes.

server2 `/home`: 57561665536 available bytes; 96.79% used; 110429048 free inodes.

server2 `/tmp`: 57561665536 available bytes; 96.79% used; 110429048 free inodes.

server2 `/var/tmp`: 57561665536 available bytes; 96.79% used; 110429048 free inodes.

server2 `/mnt/raid5`: 507631554560 available bytes; 96.49% used; 445170670 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85242810368 available bytes; 95.24% used; 114169164 free inodes.

server3 `/home`: 85242810368 available bytes; 95.24% used; 114169164 free inodes.

server3 `/data`: 163038965760 available bytes; 97.75% used; 225813784 free inodes.

server3 `/tmp`: 85242810368 available bytes; 95.24% used; 114169164 free inodes.

server3 `/var/tmp`: 85242810368 available bytes; 95.24% used; 114169164 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779445760 available bytes; 94.10% used; 114348765 free inodes.

server4 `/home`: 105779445760 available bytes; 94.10% used; 114348765 free inodes.

server4 `/data`: 90021388288 available bytes; 98.76% used; 225257176 free inodes.

server4 `/tmp`: 105779445760 available bytes; 94.10% used; 114348765 free inodes.

server4 `/var/tmp`: 105779445760 available bytes; 94.10% used; 114348765 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
