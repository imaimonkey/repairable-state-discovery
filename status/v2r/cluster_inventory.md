# V2R cluster inventory

2026-09-24T14:41:14.282185+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324051849216 available bytes; 81.92% used; 112481472 free inodes.

server1 `/home`: 324051849216 available bytes; 81.92% used; 112481472 free inodes.

server1 `/tmp`: 324051849216 available bytes; 81.92% used; 112481472 free inodes.

server1 `/var/tmp`: 324051849216 available bytes; 81.92% used; 112481472 free inodes.

server1 `/mnt/raid5`: 416864804864 available bytes; 98.09% used; 337666900 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57444556800 available bytes; 96.80% used; 110427997 free inodes.

server2 `/home`: 57444556800 available bytes; 96.80% used; 110427997 free inodes.

server2 `/tmp`: 57444556800 available bytes; 96.80% used; 110427997 free inodes.

server2 `/var/tmp`: 57444556800 available bytes; 96.80% used; 110427997 free inodes.

server2 `/mnt/raid5`: 504143085568 available bytes; 96.52% used; 445167730 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84479328256 available bytes; 95.29% used; 114158780 free inodes.

server3 `/home`: 84479328256 available bytes; 95.29% used; 114158780 free inodes.

server3 `/data`: 160759328768 available bytes; 97.78% used; 225807939 free inodes.

server3 `/tmp`: 84479328256 available bytes; 95.29% used; 114158780 free inodes.

server3 `/var/tmp`: 84479328256 available bytes; 95.29% used; 114158780 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105758466048 available bytes; 94.10% used; 114348683 free inodes.

server4 `/home`: 105758466048 available bytes; 94.10% used; 114348683 free inodes.

server4 `/data`: 69181788160 available bytes; 99.04% used; 225257005 free inodes.

server4 `/tmp`: 105758466048 available bytes; 94.10% used; 114348683 free inodes.

server4 `/var/tmp`: 105758466048 available bytes; 94.10% used; 114348683 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
