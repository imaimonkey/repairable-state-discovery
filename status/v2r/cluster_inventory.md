# V2R cluster inventory

2026-09-24T22:31:30.786870+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323944759296 available bytes; 81.93% used; 112481420 free inodes.

server1 `/home`: 323944759296 available bytes; 81.93% used; 112481420 free inodes.

server1 `/tmp`: 323944759296 available bytes; 81.93% used; 112481420 free inodes.

server1 `/var/tmp`: 323944759296 available bytes; 81.93% used; 112481420 free inodes.

server1 `/mnt/raid5`: 415369453568 available bytes; 98.09% used; 337620168 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23207665664 available bytes; 98.71% used; 110410937 free inodes.

server2 `/home`: 23207665664 available bytes; 98.71% used; 110410937 free inodes.

server2 `/tmp`: 23207665664 available bytes; 98.71% used; 110410937 free inodes.

server2 `/var/tmp`: 23207665664 available bytes; 98.71% used; 110410937 free inodes.

server2 `/mnt/raid5`: 488495075328 available bytes; 96.62% used; 445152990 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84379598848 available bytes; 95.29% used; 114156083 free inodes.

server3 `/home`: 84379598848 available bytes; 95.29% used; 114156083 free inodes.

server3 `/data`: 149275844608 available bytes; 97.94% used; 225802047 free inodes.

server3 `/tmp`: 84379598848 available bytes; 95.29% used; 114156083 free inodes.

server3 `/var/tmp`: 84379598848 available bytes; 95.29% used; 114156083 free inodes.
| server4 | True | ['0', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105801785344 available bytes; 94.10% used; 114348326 free inodes.

server4 `/home`: 105801785344 available bytes; 94.10% used; 114348326 free inodes.

server4 `/data`: 73275973632 available bytes; 98.99% used; 225225595 free inodes.

server4 `/tmp`: 105801785344 available bytes; 94.10% used; 114348326 free inodes.

server4 `/var/tmp`: 105801785344 available bytes; 94.10% used; 114348326 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
