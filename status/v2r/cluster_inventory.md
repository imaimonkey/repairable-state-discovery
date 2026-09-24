# V2R cluster inventory

2026-09-24T22:11:31.219152+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323949539328 available bytes; 81.93% used; 112481417 free inodes.

server1 `/home`: 323949539328 available bytes; 81.93% used; 112481417 free inodes.

server1 `/tmp`: 323949539328 available bytes; 81.93% used; 112481417 free inodes.

server1 `/var/tmp`: 323949539328 available bytes; 81.93% used; 112481417 free inodes.

server1 `/mnt/raid5`: 415410368512 available bytes; 98.09% used; 337622506 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30119018496 available bytes; 98.32% used; 110411302 free inodes.

server2 `/home`: 30119018496 available bytes; 98.32% used; 110411302 free inodes.

server2 `/tmp`: 30119018496 available bytes; 98.32% used; 110411302 free inodes.

server2 `/var/tmp`: 30119018496 available bytes; 98.32% used; 110411302 free inodes.

server2 `/mnt/raid5`: 488572932096 available bytes; 96.62% used; 445153718 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84378566656 available bytes; 95.29% used; 114156081 free inodes.

server3 `/home`: 84378566656 available bytes; 95.29% used; 114156081 free inodes.

server3 `/data`: 149587087360 available bytes; 97.93% used; 225802434 free inodes.

server3 `/tmp`: 84378566656 available bytes; 95.29% used; 114156081 free inodes.

server3 `/var/tmp`: 84378566656 available bytes; 95.29% used; 114156081 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105819262976 available bytes; 94.09% used; 114348329 free inodes.

server4 `/home`: 105819262976 available bytes; 94.09% used; 114348329 free inodes.

server4 `/data`: 73428783104 available bytes; 98.99% used; 225234048 free inodes.

server4 `/tmp`: 105819262976 available bytes; 94.09% used; 114348329 free inodes.

server4 `/var/tmp`: 105819262976 available bytes; 94.09% used; 114348329 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
