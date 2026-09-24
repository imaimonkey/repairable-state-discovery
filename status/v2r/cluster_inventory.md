# V2R cluster inventory

2026-09-24T19:52:30.932857+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323990048768 available bytes; 81.93% used; 112481461 free inodes.

server1 `/home`: 323990048768 available bytes; 81.93% used; 112481461 free inodes.

server1 `/tmp`: 323990048768 available bytes; 81.93% used; 112481461 free inodes.

server1 `/var/tmp`: 323990048768 available bytes; 81.93% used; 112481461 free inodes.

server1 `/mnt/raid5`: 415566180352 available bytes; 98.09% used; 337629751 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 36250779648 available bytes; 97.98% used; 110411484 free inodes.

server2 `/home`: 36250779648 available bytes; 97.98% used; 110411484 free inodes.

server2 `/tmp`: 36250779648 available bytes; 97.98% used; 110411484 free inodes.

server2 `/var/tmp`: 36250779648 available bytes; 97.98% used; 110411484 free inodes.

server2 `/mnt/raid5`: 494178230272 available bytes; 96.59% used; 445157912 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84400017408 available bytes; 95.29% used; 114156137 free inodes.

server3 `/home`: 84400017408 available bytes; 95.29% used; 114156137 free inodes.

server3 `/data`: 152046444544 available bytes; 97.90% used; 225799071 free inodes.

server3 `/tmp`: 84400017408 available bytes; 95.29% used; 114156137 free inodes.

server3 `/var/tmp`: 84400017408 available bytes; 95.29% used; 114156137 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105641988096 available bytes; 94.10% used; 114348426 free inodes.

server4 `/home`: 105641988096 available bytes; 94.10% used; 114348426 free inodes.

server4 `/data`: 89834291200 available bytes; 98.76% used; 225266363 free inodes.

server4 `/tmp`: 105641988096 available bytes; 94.10% used; 114348426 free inodes.

server4 `/var/tmp`: 105641988096 available bytes; 94.10% used; 114348426 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
