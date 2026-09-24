# V2R cluster inventory

2026-09-24T16:02:10.181351+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324024033280 available bytes; 81.92% used; 112481453 free inodes.

server1 `/home`: 324024033280 available bytes; 81.92% used; 112481453 free inodes.

server1 `/tmp`: 324024033280 available bytes; 81.92% used; 112481453 free inodes.

server1 `/var/tmp`: 324024033280 available bytes; 81.92% used; 112481453 free inodes.

server1 `/mnt/raid5`: 416636309504 available bytes; 98.09% used; 337656634 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57354915840 available bytes; 96.80% used; 110427183 free inodes.

server2 `/home`: 57354915840 available bytes; 96.80% used; 110427183 free inodes.

server2 `/tmp`: 57354915840 available bytes; 96.80% used; 110427183 free inodes.

server2 `/var/tmp`: 57354915840 available bytes; 96.80% used; 110427183 free inodes.

server2 `/mnt/raid5`: 501792997376 available bytes; 96.53% used; 445164899 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84855959552 available bytes; 95.26% used; 114182200 free inodes.

server3 `/home`: 84855959552 available bytes; 95.26% used; 114182200 free inodes.

server3 `/data`: 160068866048 available bytes; 97.79% used; 225805930 free inodes.

server3 `/tmp`: 84855959552 available bytes; 95.26% used; 114182200 free inodes.

server3 `/var/tmp`: 84855959552 available bytes; 95.26% used; 114182200 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105698172928 available bytes; 94.10% used; 114348610 free inodes.

server4 `/home`: 105698172928 available bytes; 94.10% used; 114348610 free inodes.

server4 `/data`: 89336598528 available bytes; 98.77% used; 225256335 free inodes.

server4 `/tmp`: 105698172928 available bytes; 94.10% used; 114348610 free inodes.

server4 `/var/tmp`: 105698172928 available bytes; 94.10% used; 114348610 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
