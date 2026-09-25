# V2R cluster inventory

2026-09-25T01:50:22.066629+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319025647616 available bytes; 82.20% used; 112480597 free inodes.

server1 `/home`: 319025647616 available bytes; 82.20% used; 112480597 free inodes.

server1 `/tmp`: 319025647616 available bytes; 82.20% used; 112480597 free inodes.

server1 `/var/tmp`: 319025647616 available bytes; 82.20% used; 112480597 free inodes.

server1 `/mnt/raid5`: 416444022784 available bytes; 98.09% used; 337610588 free inodes.
| server2 | True | ['2', '3', '6'] | [] |

server2 `/`: 23041024000 available bytes; 98.71% used; 110410780 free inodes.

server2 `/home`: 23041024000 available bytes; 98.71% used; 110410780 free inodes.

server2 `/tmp`: 23041024000 available bytes; 98.71% used; 110410780 free inodes.

server2 `/var/tmp`: 23041024000 available bytes; 98.71% used; 110410780 free inodes.

server2 `/mnt/raid5`: 490487881728 available bytes; 96.61% used; 445161034 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84353839104 available bytes; 95.29% used; 114156078 free inodes.

server3 `/home`: 84353839104 available bytes; 95.29% used; 114156078 free inodes.

server3 `/data`: 146349768704 available bytes; 97.98% used; 225811903 free inodes.

server3 `/tmp`: 84353839104 available bytes; 95.29% used; 114156078 free inodes.

server3 `/var/tmp`: 84353839104 available bytes; 95.29% used; 114156078 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105761484800 available bytes; 94.10% used; 114348274 free inodes.

server4 `/home`: 105761484800 available bytes; 94.10% used; 114348274 free inodes.

server4 `/data`: 53309501440 available bytes; 99.26% used; 225030544 free inodes.

server4 `/tmp`: 105761484800 available bytes; 94.10% used; 114348274 free inodes.

server4 `/var/tmp`: 105761484800 available bytes; 94.10% used; 114348274 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
