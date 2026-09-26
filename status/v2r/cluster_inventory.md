# V2R cluster inventory

2026-09-26T09:03:50.014078+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318737350656 available bytes; 82.22% used; 112475808 free inodes.

server1 `/home`: 318737350656 available bytes; 82.22% used; 112475808 free inodes.

server1 `/tmp`: 318737350656 available bytes; 82.22% used; 112475808 free inodes.

server1 `/var/tmp`: 318737350656 available bytes; 82.22% used; 112475808 free inodes.

server1 `/mnt/raid5`: 219022573568 available bytes; 99.00% used; 337538772 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22316752896 available bytes; 98.76% used; 110403915 free inodes.

server2 `/home`: 22316752896 available bytes; 98.76% used; 110403915 free inodes.

server2 `/tmp`: 22316752896 available bytes; 98.76% used; 110403915 free inodes.

server2 `/var/tmp`: 22316752896 available bytes; 98.76% used; 110403915 free inodes.

server2 `/mnt/raid5`: 254438096896 available bytes; 98.24% used; 445023885 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82660515840 available bytes; 95.39% used; 114110812 free inodes.

server3 `/home`: 82660515840 available bytes; 95.39% used; 114110812 free inodes.

server3 `/data`: 123660820480 available bytes; 98.29% used; 225828223 free inodes.

server3 `/tmp`: 82660515840 available bytes; 95.39% used; 114110812 free inodes.

server3 `/var/tmp`: 82660515840 available bytes; 95.39% used; 114110812 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106046328832 available bytes; 94.08% used; 114348132 free inodes.

server4 `/home`: 106046328832 available bytes; 94.08% used; 114348132 free inodes.

server4 `/data`: 89350750208 available bytes; 98.77% used; 224883338 free inodes.

server4 `/tmp`: 106046328832 available bytes; 94.08% used; 114348132 free inodes.

server4 `/var/tmp`: 106046328832 available bytes; 94.08% used; 114348132 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
