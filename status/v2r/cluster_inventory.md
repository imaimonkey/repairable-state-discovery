# V2R cluster inventory

2026-09-24T22:42:18.054212+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323934371840 available bytes; 81.93% used; 112481412 free inodes.

server1 `/home`: 323934371840 available bytes; 81.93% used; 112481412 free inodes.

server1 `/tmp`: 323934371840 available bytes; 81.93% used; 112481412 free inodes.

server1 `/var/tmp`: 323934371840 available bytes; 81.93% used; 112481412 free inodes.

server1 `/mnt/raid5`: 415348019200 available bytes; 98.09% used; 337618886 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23176642560 available bytes; 98.71% used; 110410915 free inodes.

server2 `/home`: 23176642560 available bytes; 98.71% used; 110410915 free inodes.

server2 `/tmp`: 23176642560 available bytes; 98.71% used; 110410915 free inodes.

server2 `/var/tmp`: 23176642560 available bytes; 98.71% used; 110410915 free inodes.

server2 `/mnt/raid5`: 488167444480 available bytes; 96.63% used; 445152923 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84369825792 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84369825792 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 149081776128 available bytes; 97.94% used; 225801854 free inodes.

server3 `/tmp`: 84369825792 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84369825792 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['0', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105801572352 available bytes; 94.10% used; 114348322 free inodes.

server4 `/home`: 105801572352 available bytes; 94.10% used; 114348322 free inodes.

server4 `/data`: 65021349888 available bytes; 99.10% used; 225214360 free inodes.

server4 `/tmp`: 105801572352 available bytes; 94.10% used; 114348322 free inodes.

server4 `/var/tmp`: 105801572352 available bytes; 94.10% used; 114348322 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
