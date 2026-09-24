# V2R cluster inventory

2026-09-24T04:35:21.521514+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324629905408 available bytes; 81.89% used; 112492945 free inodes.

server1 `/home`: 324629905408 available bytes; 81.89% used; 112492945 free inodes.

server1 `/tmp`: 324629905408 available bytes; 81.89% used; 112492945 free inodes.

server1 `/var/tmp`: 324629905408 available bytes; 81.89% used; 112492945 free inodes.

server1 `/mnt/raid5`: 455322755072 available bytes; 97.91% used; 337724656 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40779366400 available bytes; 97.73% used; 110430510 free inodes.

server2 `/home`: 40779366400 available bytes; 97.73% used; 110430510 free inodes.

server2 `/tmp`: 40779366400 available bytes; 97.73% used; 110430510 free inodes.

server2 `/var/tmp`: 40779366400 available bytes; 97.73% used; 110430510 free inodes.

server2 `/mnt/raid5`: 524656881664 available bytes; 96.37% used; 445195767 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292003061760 available bytes; 83.71% used; 114176138 free inodes.

server3 `/home`: 292003061760 available bytes; 83.71% used; 114176138 free inodes.

server3 `/data`: 24378695680 available bytes; 99.66% used; 225840838 free inodes.

server3 `/tmp`: 292003061760 available bytes; 83.71% used; 114176138 free inodes.

server3 `/var/tmp`: 292003061760 available bytes; 83.71% used; 114176138 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105844260864 available bytes; 94.09% used; 114349416 free inodes.

server4 `/home`: 105844260864 available bytes; 94.09% used; 114349416 free inodes.

server4 `/data`: 253400842240 available bytes; 96.50% used; 225366887 free inodes.

server4 `/tmp`: 105844260864 available bytes; 94.09% used; 114349416 free inodes.

server4 `/var/tmp`: 105844260864 available bytes; 94.09% used; 114349416 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
