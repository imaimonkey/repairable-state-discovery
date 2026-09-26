# V2R cluster inventory

2026-09-26T15:46:54.235793+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318142140416 available bytes; 82.25% used; 112473930 free inodes.

server1 `/home`: 318142140416 available bytes; 82.25% used; 112473930 free inodes.

server1 `/tmp`: 318142140416 available bytes; 82.25% used; 112473930 free inodes.

server1 `/var/tmp`: 318142140416 available bytes; 82.25% used; 112473930 free inodes.

server1 `/mnt/raid5`: 654104363008 available bytes; 97.00% used; 337531411 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18023317504 available bytes; 98.99% used; 110367502 free inodes.

server2 `/home`: 18023317504 available bytes; 98.99% used; 110367502 free inodes.

server2 `/tmp`: 18023317504 available bytes; 98.99% used; 110367502 free inodes.

server2 `/var/tmp`: 18023317504 available bytes; 98.99% used; 110367502 free inodes.

server2 `/mnt/raid5`: 608944783360 available bytes; 95.79% used; 444972460 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82151702528 available bytes; 95.42% used; 114093400 free inodes.

server3 `/home`: 82151702528 available bytes; 95.42% used; 114093400 free inodes.

server3 `/data`: 1347152691200 available bytes; 81.38% used; 225809056 free inodes.

server3 `/tmp`: 82151702528 available bytes; 95.42% used; 114093400 free inodes.

server3 `/var/tmp`: 82151702528 available bytes; 95.42% used; 114093400 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105954430976 available bytes; 94.09% used; 114347852 free inodes.

server4 `/home`: 105954430976 available bytes; 94.09% used; 114347852 free inodes.

server4 `/data`: 410719924224 available bytes; 94.32% used; 224825359 free inodes.

server4 `/tmp`: 105954430976 available bytes; 94.09% used; 114347852 free inodes.

server4 `/var/tmp`: 105954430976 available bytes; 94.09% used; 114347852 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
