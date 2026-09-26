# V2R cluster inventory

2026-09-26T09:57:18.501905+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318613139456 available bytes; 82.23% used; 112475043 free inodes.

server1 `/home`: 318613139456 available bytes; 82.23% used; 112475043 free inodes.

server1 `/tmp`: 318613139456 available bytes; 82.23% used; 112475043 free inodes.

server1 `/var/tmp`: 318613139456 available bytes; 82.23% used; 112475043 free inodes.

server1 `/mnt/raid5`: 218908635136 available bytes; 99.00% used; 337538522 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22302965760 available bytes; 98.76% used; 110402878 free inodes.

server2 `/home`: 22302965760 available bytes; 98.76% used; 110402878 free inodes.

server2 `/tmp`: 22302965760 available bytes; 98.76% used; 110402878 free inodes.

server2 `/var/tmp`: 22302965760 available bytes; 98.76% used; 110402878 free inodes.

server2 `/mnt/raid5`: 252619337728 available bytes; 98.25% used; 445022040 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82662633472 available bytes; 95.39% used; 114110816 free inodes.

server3 `/home`: 82662633472 available bytes; 95.39% used; 114110816 free inodes.

server3 `/data`: 123594203136 available bytes; 98.29% used; 225827348 free inodes.

server3 `/tmp`: 82662633472 available bytes; 95.39% used; 114110816 free inodes.

server3 `/var/tmp`: 82662633472 available bytes; 95.39% used; 114110816 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105931362304 available bytes; 94.09% used; 114348027 free inodes.

server4 `/home`: 105931362304 available bytes; 94.09% used; 114348027 free inodes.

server4 `/data`: 89242050560 available bytes; 98.77% used; 224882270 free inodes.

server4 `/tmp`: 105931362304 available bytes; 94.09% used; 114348027 free inodes.

server4 `/var/tmp`: 105931362304 available bytes; 94.09% used; 114348027 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
