# V2R cluster inventory

2026-09-25T17:20:45.222361+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318679568384 available bytes; 82.22% used; 112476346 free inodes.

server1 `/home`: 318679568384 available bytes; 82.22% used; 112476346 free inodes.

server1 `/tmp`: 318679568384 available bytes; 82.22% used; 112476346 free inodes.

server1 `/var/tmp`: 318679568384 available bytes; 82.22% used; 112476346 free inodes.

server1 `/mnt/raid5`: 363849764864 available bytes; 98.33% used; 337543352 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23107284992 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23107284992 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23107284992 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23107284992 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 316309323776 available bytes; 97.81% used; 445068512 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84393713664 available bytes; 95.29% used; 114152612 free inodes.

server3 `/home`: 84393713664 available bytes; 95.29% used; 114152612 free inodes.

server3 `/data`: 132793081856 available bytes; 98.16% used; 225811495 free inodes.

server3 `/tmp`: 84393713664 available bytes; 95.29% used; 114152612 free inodes.

server3 `/var/tmp`: 84393713664 available bytes; 95.29% used; 114152612 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105617920000 available bytes; 94.11% used; 114349643 free inodes.

server4 `/home`: 105617920000 available bytes; 94.11% used; 114349643 free inodes.

server4 `/data`: 229872848896 available bytes; 96.82% used; 224932996 free inodes.

server4 `/tmp`: 105617920000 available bytes; 94.11% used; 114349643 free inodes.

server4 `/var/tmp`: 105617920000 available bytes; 94.11% used; 114349643 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
