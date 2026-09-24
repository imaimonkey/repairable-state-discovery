# V2R cluster inventory

2026-09-24T22:06:54.570783+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323949846528 available bytes; 81.93% used; 112481426 free inodes.

server1 `/home`: 323949846528 available bytes; 81.93% used; 112481426 free inodes.

server1 `/tmp`: 323949846528 available bytes; 81.93% used; 112481426 free inodes.

server1 `/var/tmp`: 323949846528 available bytes; 81.93% used; 112481426 free inodes.

server1 `/mnt/raid5`: 415416803328 available bytes; 98.09% used; 337623043 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30120542208 available bytes; 98.32% used; 110411302 free inodes.

server2 `/home`: 30120542208 available bytes; 98.32% used; 110411302 free inodes.

server2 `/tmp`: 30120542208 available bytes; 98.32% used; 110411302 free inodes.

server2 `/var/tmp`: 30120542208 available bytes; 98.32% used; 110411302 free inodes.

server2 `/mnt/raid5`: 489268297728 available bytes; 96.62% used; 445154017 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84379389952 available bytes; 95.29% used; 114156081 free inodes.

server3 `/home`: 84379389952 available bytes; 95.29% used; 114156081 free inodes.

server3 `/data`: 149672816640 available bytes; 97.93% used; 225802510 free inodes.

server3 `/tmp`: 84379389952 available bytes; 95.29% used; 114156081 free inodes.

server3 `/var/tmp`: 84379389952 available bytes; 95.29% used; 114156081 free inodes.
| server4 | True | ['1', '4', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105819389952 available bytes; 94.09% used; 114348338 free inodes.

server4 `/home`: 105819389952 available bytes; 94.09% used; 114348338 free inodes.

server4 `/data`: 73865592832 available bytes; 98.98% used; 225234515 free inodes.

server4 `/tmp`: 105819389952 available bytes; 94.09% used; 114348338 free inodes.

server4 `/var/tmp`: 105819389952 available bytes; 94.09% used; 114348338 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
