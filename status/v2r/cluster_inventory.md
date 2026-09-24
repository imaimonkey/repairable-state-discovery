# V2R cluster inventory

2026-09-24T04:28:59.485251+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324697976832 available bytes; 81.89% used; 112493173 free inodes.

server1 `/home`: 324697976832 available bytes; 81.89% used; 112493173 free inodes.

server1 `/tmp`: 324697976832 available bytes; 81.89% used; 112493173 free inodes.

server1 `/var/tmp`: 324697976832 available bytes; 81.89% used; 112493173 free inodes.

server1 `/mnt/raid5`: 445656977408 available bytes; 97.96% used; 337724689 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40783335424 available bytes; 97.72% used; 110430550 free inodes.

server2 `/home`: 40783335424 available bytes; 97.72% used; 110430550 free inodes.

server2 `/tmp`: 40783335424 available bytes; 97.72% used; 110430550 free inodes.

server2 `/var/tmp`: 40783335424 available bytes; 97.72% used; 110430550 free inodes.

server2 `/mnt/raid5`: 525407924224 available bytes; 96.37% used; 445195700 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292001701888 available bytes; 83.71% used; 114176140 free inodes.

server3 `/home`: 292001701888 available bytes; 83.71% used; 114176140 free inodes.

server3 `/data`: 28575547392 available bytes; 99.61% used; 225841024 free inodes.

server3 `/tmp`: 292001701888 available bytes; 83.71% used; 114176140 free inodes.

server3 `/var/tmp`: 292001701888 available bytes; 83.71% used; 114176140 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105844555776 available bytes; 94.09% used; 114349421 free inodes.

server4 `/home`: 105844555776 available bytes; 94.09% used; 114349421 free inodes.

server4 `/data`: 253409648640 available bytes; 96.50% used; 225366923 free inodes.

server4 `/tmp`: 105844555776 available bytes; 94.09% used; 114349421 free inodes.

server4 `/var/tmp`: 105844555776 available bytes; 94.09% used; 114349421 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
