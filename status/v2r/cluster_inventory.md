# V2R cluster inventory

2026-09-24T23:07:02.159350+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 320322240512 available bytes; 82.13% used; 112480847 free inodes.

server1 `/home`: 320322240512 available bytes; 82.13% used; 112480847 free inodes.

server1 `/tmp`: 320322240512 available bytes; 82.13% used; 112480847 free inodes.

server1 `/var/tmp`: 320322240512 available bytes; 82.13% used; 112480847 free inodes.

server1 `/mnt/raid5`: 415280496640 available bytes; 98.09% used; 337615904 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23123415040 available bytes; 98.71% used; 110410804 free inodes.

server2 `/home`: 23123415040 available bytes; 98.71% used; 110410804 free inodes.

server2 `/tmp`: 23123415040 available bytes; 98.71% used; 110410804 free inodes.

server2 `/var/tmp`: 23123415040 available bytes; 98.71% used; 110410804 free inodes.

server2 `/mnt/raid5`: 487390683136 available bytes; 96.63% used; 445151908 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84369682432 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84369682432 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 148660789248 available bytes; 97.95% used; 225801354 free inodes.

server3 `/tmp`: 84369682432 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84369682432 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105800650752 available bytes; 94.10% used; 114348311 free inodes.

server4 `/home`: 105800650752 available bytes; 94.10% used; 114348311 free inodes.

server4 `/data`: 61881360384 available bytes; 99.14% used; 225181213 free inodes.

server4 `/tmp`: 105800650752 available bytes; 94.10% used; 114348311 free inodes.

server4 `/var/tmp`: 105800650752 available bytes; 94.10% used; 114348311 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
