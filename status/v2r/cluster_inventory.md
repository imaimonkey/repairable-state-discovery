# V2R cluster inventory

2026-09-24T12:14:32.333006+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324063031296 available bytes; 81.92% used; 112481785 free inodes.

server1 `/home`: 324063031296 available bytes; 81.92% used; 112481785 free inodes.

server1 `/tmp`: 324063031296 available bytes; 81.92% used; 112481785 free inodes.

server1 `/var/tmp`: 324063031296 available bytes; 81.92% used; 112481785 free inodes.

server1 `/mnt/raid5`: 405226885120 available bytes; 98.14% used; 337684212 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57617367040 available bytes; 96.79% used; 110429558 free inodes.

server2 `/home`: 57617367040 available bytes; 96.79% used; 110429558 free inodes.

server2 `/tmp`: 57617367040 available bytes; 96.79% used; 110429558 free inodes.

server2 `/var/tmp`: 57617367040 available bytes; 96.79% used; 110429558 free inodes.

server2 `/mnt/raid5`: 508986716160 available bytes; 96.48% used; 445172376 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85133672448 available bytes; 95.25% used; 114164776 free inodes.

server3 `/home`: 85133672448 available bytes; 95.25% used; 114164776 free inodes.

server3 `/data`: 163484131328 available bytes; 97.74% used; 225815044 free inodes.

server3 `/tmp`: 85133672448 available bytes; 95.25% used; 114164776 free inodes.

server3 `/var/tmp`: 85133672448 available bytes; 95.25% used; 114164776 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105781366784 available bytes; 94.10% used; 114348816 free inodes.

server4 `/home`: 105781366784 available bytes; 94.10% used; 114348816 free inodes.

server4 `/data`: 90423083008 available bytes; 98.75% used; 225257325 free inodes.

server4 `/tmp`: 105781366784 available bytes; 94.10% used; 114348816 free inodes.

server4 `/var/tmp`: 105781366784 available bytes; 94.10% used; 114348816 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
