# V2R cluster inventory

2026-09-24T15:02:59.839600+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324046102528 available bytes; 81.92% used; 112481467 free inodes.

server1 `/home`: 324046102528 available bytes; 81.92% used; 112481467 free inodes.

server1 `/tmp`: 324046102528 available bytes; 81.92% used; 112481467 free inodes.

server1 `/var/tmp`: 324046102528 available bytes; 81.92% used; 112481467 free inodes.

server1 `/mnt/raid5`: 416831229952 available bytes; 98.09% used; 337664363 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57424633856 available bytes; 96.80% used; 110427773 free inodes.

server2 `/home`: 57424633856 available bytes; 96.80% used; 110427773 free inodes.

server2 `/tmp`: 57424633856 available bytes; 96.80% used; 110427773 free inodes.

server2 `/var/tmp`: 57424633856 available bytes; 96.80% used; 110427773 free inodes.

server2 `/mnt/raid5`: 503495454720 available bytes; 96.52% used; 445166851 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84851118080 available bytes; 95.26% used; 114183718 free inodes.

server3 `/home`: 84851118080 available bytes; 95.26% used; 114183718 free inodes.

server3 `/data`: 160581398528 available bytes; 97.78% used; 225807489 free inodes.

server3 `/tmp`: 84851118080 available bytes; 95.26% used; 114183718 free inodes.

server3 `/var/tmp`: 84851118080 available bytes; 95.26% used; 114183718 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105719386112 available bytes; 94.10% used; 114348643 free inodes.

server4 `/home`: 105719386112 available bytes; 94.10% used; 114348643 free inodes.

server4 `/data`: 68790927360 available bytes; 99.05% used; 225256977 free inodes.

server4 `/tmp`: 105719386112 available bytes; 94.10% used; 114348643 free inodes.

server4 `/var/tmp`: 105719386112 available bytes; 94.10% used; 114348643 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
