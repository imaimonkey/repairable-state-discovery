# V2R cluster inventory

2026-09-26T00:16:31.771552+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318668869632 available bytes; 82.22% used; 112476297 free inodes.

server1 `/home`: 318668869632 available bytes; 82.22% used; 112476297 free inodes.

server1 `/tmp`: 318668869632 available bytes; 82.22% used; 112476297 free inodes.

server1 `/var/tmp`: 318668869632 available bytes; 82.22% used; 112476297 free inodes.

server1 `/mnt/raid5`: 359562694656 available bytes; 98.35% used; 337547050 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22947725312 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22947725312 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22947725312 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22947725312 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 295467958272 available bytes; 97.96% used; 445058357 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84341309440 available bytes; 95.29% used; 114152433 free inodes.

server3 `/home`: 84341309440 available bytes; 95.29% used; 114152433 free inodes.

server3 `/data`: 124945068032 available bytes; 98.27% used; 225819274 free inodes.

server3 `/tmp`: 84341309440 available bytes; 95.29% used; 114152433 free inodes.

server3 `/var/tmp`: 84341309440 available bytes; 95.29% used; 114152433 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105453670400 available bytes; 94.12% used; 114348398 free inodes.

server4 `/home`: 105453670400 available bytes; 94.12% used; 114348398 free inodes.

server4 `/data`: 178048409600 available bytes; 97.54% used; 224917551 free inodes.

server4 `/tmp`: 105453670400 available bytes; 94.12% used; 114348398 free inodes.

server4 `/var/tmp`: 105453670400 available bytes; 94.12% used; 114348398 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
