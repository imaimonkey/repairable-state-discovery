# V2R cluster inventory

2026-09-24T22:02:17.841964+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323947294720 available bytes; 81.93% used; 112481418 free inodes.

server1 `/home`: 323947294720 available bytes; 81.93% used; 112481418 free inodes.

server1 `/tmp`: 323947294720 available bytes; 81.93% used; 112481418 free inodes.

server1 `/var/tmp`: 323947294720 available bytes; 81.93% used; 112481418 free inodes.

server1 `/mnt/raid5`: 415426072576 available bytes; 98.09% used; 337623579 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30122008576 available bytes; 98.32% used; 110411302 free inodes.

server2 `/home`: 30122008576 available bytes; 98.32% used; 110411302 free inodes.

server2 `/tmp`: 30122008576 available bytes; 98.32% used; 110411302 free inodes.

server2 `/var/tmp`: 30122008576 available bytes; 98.32% used; 110411302 free inodes.

server2 `/mnt/raid5`: 468608663552 available bytes; 96.76% used; 445153884 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84379291648 available bytes; 95.29% used; 114156083 free inodes.

server3 `/home`: 84379291648 available bytes; 95.29% used; 114156083 free inodes.

server3 `/data`: 149760630784 available bytes; 97.93% used; 225802594 free inodes.

server3 `/tmp`: 84379291648 available bytes; 95.29% used; 114156083 free inodes.

server3 `/var/tmp`: 84379291648 available bytes; 95.29% used; 114156083 free inodes.
| server4 | True | ['1', '4', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105819533312 available bytes; 94.09% used; 114348340 free inodes.

server4 `/home`: 105819533312 available bytes; 94.09% used; 114348340 free inodes.

server4 `/data`: 75514671104 available bytes; 98.96% used; 225234815 free inodes.

server4 `/tmp`: 105819533312 available bytes; 94.09% used; 114348340 free inodes.

server4 `/var/tmp`: 105819533312 available bytes; 94.09% used; 114348340 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
