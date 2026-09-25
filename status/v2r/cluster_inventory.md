# V2R cluster inventory

2026-09-25T17:55:54.386448+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318661611520 available bytes; 82.22% used; 112476341 free inodes.

server1 `/home`: 318661611520 available bytes; 82.22% used; 112476341 free inodes.

server1 `/tmp`: 318661611520 available bytes; 82.22% used; 112476341 free inodes.

server1 `/var/tmp`: 318661611520 available bytes; 82.22% used; 112476341 free inodes.

server1 `/mnt/raid5`: 371230633984 available bytes; 98.30% used; 337542594 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23106318336 available bytes; 98.71% used; 110407930 free inodes.

server2 `/home`: 23106318336 available bytes; 98.71% used; 110407930 free inodes.

server2 `/tmp`: 23106318336 available bytes; 98.71% used; 110407930 free inodes.

server2 `/var/tmp`: 23106318336 available bytes; 98.71% used; 110407930 free inodes.

server2 `/mnt/raid5`: 315298168832 available bytes; 97.82% used; 445067995 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84391178240 available bytes; 95.29% used; 114152615 free inodes.

server3 `/home`: 84391178240 available bytes; 95.29% used; 114152615 free inodes.

server3 `/data`: 132526469120 available bytes; 98.17% used; 225810627 free inodes.

server3 `/tmp`: 84391178240 available bytes; 95.29% used; 114152615 free inodes.

server3 `/var/tmp`: 84391178240 available bytes; 95.29% used; 114152615 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105616809984 available bytes; 94.11% used; 114349604 free inodes.

server4 `/home`: 105616809984 available bytes; 94.11% used; 114349604 free inodes.

server4 `/data`: 229738549248 available bytes; 96.82% used; 224932492 free inodes.

server4 `/tmp`: 105616809984 available bytes; 94.11% used; 114349604 free inodes.

server4 `/var/tmp`: 105616809984 available bytes; 94.11% used; 114349604 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
