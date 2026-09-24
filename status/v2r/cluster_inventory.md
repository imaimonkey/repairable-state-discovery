# V2R cluster inventory

2026-09-24T22:05:22.309613+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323950018560 available bytes; 81.93% used; 112481426 free inodes.

server1 `/home`: 323950018560 available bytes; 81.93% used; 112481426 free inodes.

server1 `/tmp`: 323950018560 available bytes; 81.93% used; 112481426 free inodes.

server1 `/var/tmp`: 323950018560 available bytes; 81.93% used; 112481426 free inodes.

server1 `/mnt/raid5`: 415420026880 available bytes; 98.09% used; 337623219 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30121279488 available bytes; 98.32% used; 110411302 free inodes.

server2 `/home`: 30121279488 available bytes; 98.32% used; 110411302 free inodes.

server2 `/tmp`: 30121279488 available bytes; 98.32% used; 110411302 free inodes.

server2 `/var/tmp`: 30121279488 available bytes; 98.32% used; 110411302 free inodes.

server2 `/mnt/raid5`: 488772001792 available bytes; 96.62% used; 445154159 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84379787264 available bytes; 95.29% used; 114156083 free inodes.

server3 `/home`: 84379787264 available bytes; 95.29% used; 114156083 free inodes.

server3 `/data`: 149708423168 available bytes; 97.93% used; 225802547 free inodes.

server3 `/tmp`: 84379787264 available bytes; 95.29% used; 114156083 free inodes.

server3 `/var/tmp`: 84379787264 available bytes; 95.29% used; 114156083 free inodes.
| server4 | True | ['1', '4', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105819430912 available bytes; 94.09% used; 114348339 free inodes.

server4 `/home`: 105819430912 available bytes; 94.09% used; 114348339 free inodes.

server4 `/data`: 74404945920 available bytes; 98.97% used; 225234552 free inodes.

server4 `/tmp`: 105819430912 available bytes; 94.09% used; 114348339 free inodes.

server4 `/var/tmp`: 105819430912 available bytes; 94.09% used; 114348339 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
