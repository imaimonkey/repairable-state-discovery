# V2R cluster inventory

2026-09-24T22:13:03.445987+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323949494272 available bytes; 81.93% used; 112481417 free inodes.

server1 `/home`: 323949494272 available bytes; 81.93% used; 112481417 free inodes.

server1 `/tmp`: 323949494272 available bytes; 81.93% used; 112481417 free inodes.

server1 `/var/tmp`: 323949494272 available bytes; 81.93% used; 112481417 free inodes.

server1 `/mnt/raid5`: 415407697920 available bytes; 98.09% used; 337622322 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30118580224 available bytes; 98.32% used; 110411302 free inodes.

server2 `/home`: 30118580224 available bytes; 98.32% used; 110411302 free inodes.

server2 `/tmp`: 30118580224 available bytes; 98.32% used; 110411302 free inodes.

server2 `/var/tmp`: 30118580224 available bytes; 98.32% used; 110411302 free inodes.

server2 `/mnt/raid5`: 489076547584 available bytes; 96.62% used; 445153812 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84378419200 available bytes; 95.29% used; 114156081 free inodes.

server3 `/home`: 84378419200 available bytes; 95.29% used; 114156081 free inodes.

server3 `/data`: 149566869504 available bytes; 97.93% used; 225802406 free inodes.

server3 `/tmp`: 84378419200 available bytes; 95.29% used; 114156081 free inodes.

server3 `/var/tmp`: 84378419200 available bytes; 95.29% used; 114156081 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105810833408 available bytes; 94.10% used; 114348329 free inodes.

server4 `/home`: 105810833408 available bytes; 94.10% used; 114348329 free inodes.

server4 `/data`: 73431621632 available bytes; 98.99% used; 225233996 free inodes.

server4 `/tmp`: 105810833408 available bytes; 94.10% used; 114348329 free inodes.

server4 `/var/tmp`: 105810833408 available bytes; 94.10% used; 114348329 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
