# V2R cluster inventory

2026-09-25T22:52:27.746399+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318694858752 available bytes; 82.22% used; 112476297 free inodes.

server1 `/home`: 318694858752 available bytes; 82.22% used; 112476297 free inodes.

server1 `/tmp`: 318694858752 available bytes; 82.22% used; 112476297 free inodes.

server1 `/var/tmp`: 318694858752 available bytes; 82.22% used; 112476297 free inodes.

server1 `/mnt/raid5`: 360197439488 available bytes; 98.35% used; 337538843 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22946770944 available bytes; 98.72% used; 110406230 free inodes.

server2 `/home`: 22946770944 available bytes; 98.72% used; 110406230 free inodes.

server2 `/tmp`: 22946770944 available bytes; 98.72% used; 110406230 free inodes.

server2 `/var/tmp`: 22946770944 available bytes; 98.72% used; 110406230 free inodes.

server2 `/mnt/raid5`: 298321063936 available bytes; 97.94% used; 445052055 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84351148032 available bytes; 95.29% used; 114152434 free inodes.

server3 `/home`: 84351148032 available bytes; 95.29% used; 114152434 free inodes.

server3 `/data`: 124822683648 available bytes; 98.27% used; 225805583 free inodes.

server3 `/tmp`: 84351148032 available bytes; 95.29% used; 114152434 free inodes.

server3 `/var/tmp`: 84351148032 available bytes; 95.29% used; 114152434 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105235361792 available bytes; 94.13% used; 114346964 free inodes.

server4 `/home`: 105235361792 available bytes; 94.13% used; 114346964 free inodes.

server4 `/data`: 192136646656 available bytes; 97.34% used; 224917671 free inodes.

server4 `/tmp`: 105235361792 available bytes; 94.13% used; 114346964 free inodes.

server4 `/var/tmp`: 105235361792 available bytes; 94.13% used; 114346964 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
