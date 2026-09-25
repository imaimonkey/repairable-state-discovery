# V2R cluster inventory

2026-09-25T12:19:19.828015+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319189499904 available bytes; 82.19% used; 112477801 free inodes.

server1 `/home`: 319189499904 available bytes; 82.19% used; 112477801 free inodes.

server1 `/tmp`: 319189499904 available bytes; 82.19% used; 112477801 free inodes.

server1 `/var/tmp`: 319189499904 available bytes; 82.19% used; 112477801 free inodes.

server1 `/mnt/raid5`: 368713170944 available bytes; 98.31% used; 337548272 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22902755328 available bytes; 98.72% used; 110409951 free inodes.

server2 `/home`: 22902755328 available bytes; 98.72% used; 110409951 free inodes.

server2 `/tmp`: 22902755328 available bytes; 98.72% used; 110409951 free inodes.

server2 `/var/tmp`: 22902755328 available bytes; 98.72% used; 110409951 free inodes.

server2 `/mnt/raid5`: 325266231296 available bytes; 97.75% used; 445080671 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84212162560 available bytes; 95.30% used; 114154978 free inodes.

server3 `/home`: 84212162560 available bytes; 95.30% used; 114154978 free inodes.

server3 `/data`: 142282309632 available bytes; 98.03% used; 225811310 free inodes.

server3 `/tmp`: 84212162560 available bytes; 95.30% used; 114154978 free inodes.

server3 `/var/tmp`: 84212162560 available bytes; 95.30% used; 114154978 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105666461696 available bytes; 94.10% used; 114349722 free inodes.

server4 `/home`: 105666461696 available bytes; 94.10% used; 114349722 free inodes.

server4 `/data`: 232045355008 available bytes; 96.79% used; 224965845 free inodes.

server4 `/tmp`: 105666461696 available bytes; 94.10% used; 114349722 free inodes.

server4 `/var/tmp`: 105666461696 available bytes; 94.10% used; 114349722 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
