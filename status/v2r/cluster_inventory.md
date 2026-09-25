# V2R cluster inventory

2026-09-25T03:07:20.003487+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318941429760 available bytes; 82.21% used; 112480388 free inodes.

server1 `/home`: 318941429760 available bytes; 82.21% used; 112480388 free inodes.

server1 `/tmp`: 318941429760 available bytes; 82.21% used; 112480388 free inodes.

server1 `/var/tmp`: 318941429760 available bytes; 82.21% used; 112480388 free inodes.

server1 `/mnt/raid5`: 416131964928 available bytes; 98.09% used; 337601589 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22992769024 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22992769024 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22992769024 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22992769024 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 465881612288 available bytes; 96.78% used; 445112585 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84344438784 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84344438784 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 144918921216 available bytes; 98.00% used; 225810339 free inodes.

server3 `/tmp`: 84344438784 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84344438784 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105693044736 available bytes; 94.10% used; 114350903 free inodes.

server4 `/home`: 105693044736 available bytes; 94.10% used; 114350903 free inodes.

server4 `/data`: 50255425536 available bytes; 99.31% used; 224967426 free inodes.

server4 `/tmp`: 105693044736 available bytes; 94.10% used; 114350903 free inodes.

server4 `/var/tmp`: 105693044736 available bytes; 94.10% used; 114350903 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
