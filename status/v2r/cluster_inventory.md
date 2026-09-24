# V2R cluster inventory

2026-09-24T13:42:02.173208+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324028092416 available bytes; 81.92% used; 112481504 free inodes.

server1 `/home`: 324028092416 available bytes; 81.92% used; 112481504 free inodes.

server1 `/tmp`: 324028092416 available bytes; 81.92% used; 112481504 free inodes.

server1 `/var/tmp`: 324028092416 available bytes; 81.92% used; 112481504 free inodes.

server1 `/mnt/raid5`: 417002049536 available bytes; 98.09% used; 337673817 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57512472576 available bytes; 96.79% used; 110428595 free inodes.

server2 `/home`: 57512472576 available bytes; 96.79% used; 110428595 free inodes.

server2 `/tmp`: 57512472576 available bytes; 96.79% used; 110428595 free inodes.

server2 `/var/tmp`: 57512472576 available bytes; 96.79% used; 110428595 free inodes.

server2 `/mnt/raid5`: 506271764480 available bytes; 96.50% used; 445169460 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84700762112 available bytes; 95.27% used; 114165400 free inodes.

server3 `/home`: 84700762112 available bytes; 95.27% used; 114165400 free inodes.

server3 `/data`: 161181167616 available bytes; 97.77% used; 225802922 free inodes.

server3 `/tmp`: 84700762112 available bytes; 95.27% used; 114165400 free inodes.

server3 `/var/tmp`: 84700762112 available bytes; 95.27% used; 114165400 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105760870400 available bytes; 94.10% used; 114348733 free inodes.

server4 `/home`: 105760870400 available bytes; 94.10% used; 114348733 free inodes.

server4 `/data`: 90039336960 available bytes; 98.76% used; 225257164 free inodes.

server4 `/tmp`: 105760870400 available bytes; 94.10% used; 114348733 free inodes.

server4 `/var/tmp`: 105760870400 available bytes; 94.10% used; 114348733 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
