# V2R cluster inventory

2026-09-24T22:14:35.690417+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323948912640 available bytes; 81.93% used; 112481415 free inodes.

server1 `/home`: 323948912640 available bytes; 81.93% used; 112481415 free inodes.

server1 `/tmp`: 323948912640 available bytes; 81.93% used; 112481415 free inodes.

server1 `/var/tmp`: 323948912640 available bytes; 81.93% used; 112481415 free inodes.

server1 `/mnt/raid5`: 415405342720 available bytes; 98.09% used; 337622149 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30119501824 available bytes; 98.32% used; 110411304 free inodes.

server2 `/home`: 30119501824 available bytes; 98.32% used; 110411304 free inodes.

server2 `/tmp`: 30119501824 available bytes; 98.32% used; 110411304 free inodes.

server2 `/var/tmp`: 30119501824 available bytes; 98.32% used; 110411304 free inodes.

server2 `/mnt/raid5`: 488481615872 available bytes; 96.62% used; 445153642 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84382617600 available bytes; 95.29% used; 114156083 free inodes.

server3 `/home`: 84382617600 available bytes; 95.29% used; 114156083 free inodes.

server3 `/data`: 149541027840 available bytes; 97.93% used; 225802381 free inodes.

server3 `/tmp`: 84382617600 available bytes; 95.29% used; 114156083 free inodes.

server3 `/var/tmp`: 84382617600 available bytes; 95.29% used; 114156083 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105810784256 available bytes; 94.10% used; 114348328 free inodes.

server4 `/home`: 105810784256 available bytes; 94.10% used; 114348328 free inodes.

server4 `/data`: 73429573632 available bytes; 98.99% used; 225233909 free inodes.

server4 `/tmp`: 105810784256 available bytes; 94.10% used; 114348328 free inodes.

server4 `/var/tmp`: 105810784256 available bytes; 94.10% used; 114348328 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
