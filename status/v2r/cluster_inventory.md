# V2R cluster inventory

2026-09-24T03:39:53.330160+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324740579328 available bytes; 81.88% used; 112493772 free inodes.

server1 `/home`: 324740579328 available bytes; 81.88% used; 112493772 free inodes.

server1 `/tmp`: 324740579328 available bytes; 81.88% used; 112493772 free inodes.

server1 `/var/tmp`: 324740579328 available bytes; 81.88% used; 112493772 free inodes.

server1 `/mnt/raid5`: 402131169280 available bytes; 98.16% used; 337724847 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40829247488 available bytes; 97.72% used; 110431032 free inodes.

server2 `/home`: 40829247488 available bytes; 97.72% used; 110431032 free inodes.

server2 `/tmp`: 40829247488 available bytes; 97.72% used; 110431032 free inodes.

server2 `/var/tmp`: 40829247488 available bytes; 97.72% used; 110431032 free inodes.

server2 `/mnt/raid5`: 526920081408 available bytes; 96.36% used; 445197499 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 291966218240 available bytes; 83.71% used; 114174462 free inodes.

server3 `/home`: 291966218240 available bytes; 83.71% used; 114174462 free inodes.

server3 `/data`: 36002304000 available bytes; 99.50% used; 225842804 free inodes.

server3 `/tmp`: 291966218240 available bytes; 83.71% used; 114174462 free inodes.

server3 `/var/tmp`: 291966218240 available bytes; 83.71% used; 114174462 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105793044480 available bytes; 94.10% used; 114349571 free inodes.

server4 `/home`: 105793044480 available bytes; 94.10% used; 114349571 free inodes.

server4 `/data`: 278988718080 available bytes; 96.14% used; 225384446 free inodes.

server4 `/tmp`: 105793044480 available bytes; 94.10% used; 114349571 free inodes.

server4 `/var/tmp`: 105793044480 available bytes; 94.10% used; 114349571 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
