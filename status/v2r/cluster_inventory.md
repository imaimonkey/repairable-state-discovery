# V2R cluster inventory

2026-09-25T16:42:31.122723+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318683303936 available bytes; 82.22% used; 112476339 free inodes.

server1 `/home`: 318683303936 available bytes; 82.22% used; 112476339 free inodes.

server1 `/tmp`: 318683303936 available bytes; 82.22% used; 112476339 free inodes.

server1 `/var/tmp`: 318683303936 available bytes; 82.22% used; 112476339 free inodes.

server1 `/mnt/raid5`: 363878068224 available bytes; 98.33% used; 337544321 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23099121664 available bytes; 98.71% used; 110407930 free inodes.

server2 `/home`: 23099121664 available bytes; 98.71% used; 110407930 free inodes.

server2 `/tmp`: 23099121664 available bytes; 98.71% used; 110407930 free inodes.

server2 `/var/tmp`: 23099121664 available bytes; 98.71% used; 110407930 free inodes.

server2 `/mnt/raid5`: 317438664704 available bytes; 97.81% used; 445069567 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84394774528 available bytes; 95.29% used; 114152641 free inodes.

server3 `/home`: 84394774528 available bytes; 95.29% used; 114152641 free inodes.

server3 `/data`: 133789007872 available bytes; 98.15% used; 225805511 free inodes.

server3 `/tmp`: 84394774528 available bytes; 95.29% used; 114152641 free inodes.

server3 `/var/tmp`: 84394774528 available bytes; 95.29% used; 114152641 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105635770368 available bytes; 94.11% used; 114349643 free inodes.

server4 `/home`: 105635770368 available bytes; 94.11% used; 114349643 free inodes.

server4 `/data`: 230003515392 available bytes; 96.82% used; 224933744 free inodes.

server4 `/tmp`: 105635770368 available bytes; 94.11% used; 114349643 free inodes.

server4 `/var/tmp`: 105635770368 available bytes; 94.11% used; 114349643 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
