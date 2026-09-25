# V2R cluster inventory

2026-09-25T01:24:14.133769+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319078985728 available bytes; 82.20% used; 112480772 free inodes.

server1 `/home`: 319078985728 available bytes; 82.20% used; 112480772 free inodes.

server1 `/tmp`: 319078985728 available bytes; 82.20% used; 112480772 free inodes.

server1 `/var/tmp`: 319078985728 available bytes; 82.20% used; 112480772 free inodes.

server1 `/mnt/raid5`: 416499294208 available bytes; 98.09% used; 337613640 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 23051976704 available bytes; 98.71% used; 110410772 free inodes.

server2 `/home`: 23051976704 available bytes; 98.71% used; 110410772 free inodes.

server2 `/tmp`: 23051976704 available bytes; 98.71% used; 110410772 free inodes.

server2 `/var/tmp`: 23051976704 available bytes; 98.71% used; 110410772 free inodes.

server2 `/mnt/raid5`: 491307376640 available bytes; 96.61% used; 445161608 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84359159808 available bytes; 95.29% used; 114156085 free inodes.

server3 `/home`: 84359159808 available bytes; 95.29% used; 114156085 free inodes.

server3 `/data`: 146789212160 available bytes; 97.97% used; 225812416 free inodes.

server3 `/tmp`: 84359159808 available bytes; 95.29% used; 114156085 free inodes.

server3 `/var/tmp`: 84359159808 available bytes; 95.29% used; 114156085 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105779027968 available bytes; 94.10% used; 114348291 free inodes.

server4 `/home`: 105779027968 available bytes; 94.10% used; 114348291 free inodes.

server4 `/data`: 53319172096 available bytes; 99.26% used; 225030695 free inodes.

server4 `/tmp`: 105779027968 available bytes; 94.10% used; 114348291 free inodes.

server4 `/var/tmp`: 105779027968 available bytes; 94.10% used; 114348291 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
