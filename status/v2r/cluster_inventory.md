# V2R cluster inventory

2026-09-25T17:39:05.644636+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318671261696 available bytes; 82.22% used; 112476352 free inodes.

server1 `/home`: 318671261696 available bytes; 82.22% used; 112476352 free inodes.

server1 `/tmp`: 318671261696 available bytes; 82.22% used; 112476352 free inodes.

server1 `/var/tmp`: 318671261696 available bytes; 82.22% used; 112476352 free inodes.

server1 `/mnt/raid5`: 363769556992 available bytes; 98.33% used; 337542883 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23097700352 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23097700352 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23097700352 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23097700352 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 315215953920 available bytes; 97.82% used; 445067673 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84391886848 available bytes; 95.29% used; 114152611 free inodes.

server3 `/home`: 84391886848 available bytes; 95.29% used; 114152611 free inodes.

server3 `/data`: 132544462848 available bytes; 98.17% used; 225811022 free inodes.

server3 `/tmp`: 84391886848 available bytes; 95.29% used; 114152611 free inodes.

server3 `/var/tmp`: 84391886848 available bytes; 95.29% used; 114152611 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105617412096 available bytes; 94.11% used; 114349641 free inodes.

server4 `/home`: 105617412096 available bytes; 94.11% used; 114349641 free inodes.

server4 `/data`: 229859074048 available bytes; 96.82% used; 224932735 free inodes.

server4 `/tmp`: 105617412096 available bytes; 94.11% used; 114349641 free inodes.

server4 `/var/tmp`: 105617412096 available bytes; 94.11% used; 114349641 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
