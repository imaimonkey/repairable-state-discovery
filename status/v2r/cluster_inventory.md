# V2R cluster inventory

2026-09-24T22:03:50.038508+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323947163648 available bytes; 81.93% used; 112481424 free inodes.

server1 `/home`: 323947163648 available bytes; 81.93% used; 112481424 free inodes.

server1 `/tmp`: 323947163648 available bytes; 81.93% used; 112481424 free inodes.

server1 `/var/tmp`: 323947163648 available bytes; 81.93% used; 112481424 free inodes.

server1 `/mnt/raid5`: 415422992384 available bytes; 98.09% used; 337623394 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30121775104 available bytes; 98.32% used; 110411302 free inodes.

server2 `/home`: 30121775104 available bytes; 98.32% used; 110411302 free inodes.

server2 `/tmp`: 30121775104 available bytes; 98.32% used; 110411302 free inodes.

server2 `/var/tmp`: 30121775104 available bytes; 98.32% used; 110411302 free inodes.

server2 `/mnt/raid5`: 489341816832 available bytes; 96.62% used; 445153823 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84378857472 available bytes; 95.29% used; 114156081 free inodes.

server3 `/home`: 84378857472 available bytes; 95.29% used; 114156081 free inodes.

server3 `/data`: 149734244352 available bytes; 97.93% used; 225802570 free inodes.

server3 `/tmp`: 84378857472 available bytes; 95.29% used; 114156081 free inodes.

server3 `/var/tmp`: 84378857472 available bytes; 95.29% used; 114156081 free inodes.
| server4 | True | ['1', '4', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105819488256 available bytes; 94.09% used; 114348339 free inodes.

server4 `/home`: 105819488256 available bytes; 94.09% used; 114348339 free inodes.

server4 `/data`: 74875539456 available bytes; 98.97% used; 225234718 free inodes.

server4 `/tmp`: 105819488256 available bytes; 94.09% used; 114348339 free inodes.

server4 `/var/tmp`: 105819488256 available bytes; 94.09% used; 114348339 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
