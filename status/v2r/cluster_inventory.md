# V2R cluster inventory

2026-09-26T14:41:18.770110+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318125301760 available bytes; 82.25% used; 112474358 free inodes.

server1 `/home`: 318125301760 available bytes; 82.25% used; 112474358 free inodes.

server1 `/tmp`: 318125301760 available bytes; 82.25% used; 112474358 free inodes.

server1 `/var/tmp`: 318125301760 available bytes; 82.25% used; 112474358 free inodes.

server1 `/mnt/raid5`: 673988894720 available bytes; 96.91% used; 337531918 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 14396588032 available bytes; 99.20% used; 110378815 free inodes.

server2 `/home`: 14396588032 available bytes; 99.20% used; 110378815 free inodes.

server2 `/tmp`: 14396588032 available bytes; 99.20% used; 110378815 free inodes.

server2 `/var/tmp`: 14396588032 available bytes; 99.20% used; 110378815 free inodes.

server2 `/mnt/raid5`: 634620768256 available bytes; 95.61% used; 444974414 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82628739072 available bytes; 95.39% used; 114110777 free inodes.

server3 `/home`: 82628739072 available bytes; 95.39% used; 114110777 free inodes.

server3 `/data`: 1346878423040 available bytes; 81.39% used; 225805090 free inodes.

server3 `/tmp`: 82628739072 available bytes; 95.39% used; 114110777 free inodes.

server3 `/var/tmp`: 82628739072 available bytes; 95.39% used; 114110777 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105886633984 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105886633984 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 411000168448 available bytes; 94.32% used; 224826640 free inodes.

server4 `/tmp`: 105886633984 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105886633984 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
