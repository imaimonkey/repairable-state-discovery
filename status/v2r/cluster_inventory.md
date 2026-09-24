# V2R cluster inventory

2026-09-24T21:28:25.014314+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323951874048 available bytes; 81.93% used; 112481415 free inodes.

server1 `/home`: 323951874048 available bytes; 81.93% used; 112481415 free inodes.

server1 `/tmp`: 323951874048 available bytes; 81.93% used; 112481415 free inodes.

server1 `/var/tmp`: 323951874048 available bytes; 81.93% used; 112481415 free inodes.

server1 `/mnt/raid5`: 415501094912 available bytes; 98.09% used; 337627654 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30141075456 available bytes; 98.32% used; 110411341 free inodes.

server2 `/home`: 30141075456 available bytes; 98.32% used; 110411341 free inodes.

server2 `/tmp`: 30141075456 available bytes; 98.32% used; 110411341 free inodes.

server2 `/var/tmp`: 30141075456 available bytes; 98.32% used; 110411341 free inodes.

server2 `/mnt/raid5`: 490461876224 available bytes; 96.61% used; 445154950 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84382748672 available bytes; 95.29% used; 114156093 free inodes.

server3 `/home`: 84382748672 available bytes; 95.29% used; 114156093 free inodes.

server3 `/data`: 150336409600 available bytes; 97.92% used; 225803222 free inodes.

server3 `/tmp`: 84382748672 available bytes; 95.29% used; 114156093 free inodes.

server3 `/var/tmp`: 84382748672 available bytes; 95.29% used; 114156093 free inodes.
| server4 | True | ['1', '4', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105632010240 available bytes; 94.11% used; 114348356 free inodes.

server4 `/home`: 105632010240 available bytes; 94.11% used; 114348356 free inodes.

server4 `/data`: 84498472960 available bytes; 98.83% used; 225253121 free inodes.

server4 `/tmp`: 105632010240 available bytes; 94.11% used; 114348356 free inodes.

server4 `/var/tmp`: 105632010240 available bytes; 94.11% used; 114348356 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
