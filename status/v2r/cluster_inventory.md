# V2R cluster inventory

2026-09-26T10:20:28.442140+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318241665024 available bytes; 82.25% used; 112474925 free inodes.

server1 `/home`: 318241665024 available bytes; 82.25% used; 112474925 free inodes.

server1 `/tmp`: 318241665024 available bytes; 82.25% used; 112474925 free inodes.

server1 `/var/tmp`: 318241665024 available bytes; 82.25% used; 112474925 free inodes.

server1 `/mnt/raid5`: 218852872192 available bytes; 99.00% used; 337538403 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19846025216 available bytes; 98.89% used; 110384907 free inodes.

server2 `/home`: 19846025216 available bytes; 98.89% used; 110384907 free inodes.

server2 `/tmp`: 19846025216 available bytes; 98.89% used; 110384907 free inodes.

server2 `/var/tmp`: 19846025216 available bytes; 98.89% used; 110384907 free inodes.

server2 `/mnt/raid5`: 243829755904 available bytes; 98.32% used; 444979820 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82659524608 available bytes; 95.39% used; 114110829 free inodes.

server3 `/home`: 82659524608 available bytes; 95.39% used; 114110829 free inodes.

server3 `/data`: 123587510272 available bytes; 98.29% used; 225826954 free inodes.

server3 `/tmp`: 82659524608 available bytes; 95.39% used; 114110829 free inodes.

server3 `/var/tmp`: 82659524608 available bytes; 95.39% used; 114110829 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105930674176 available bytes; 94.09% used; 114348032 free inodes.

server4 `/home`: 105930674176 available bytes; 94.09% used; 114348032 free inodes.

server4 `/data`: 89112285184 available bytes; 98.77% used; 224881911 free inodes.

server4 `/tmp`: 105930674176 available bytes; 94.09% used; 114348032 free inodes.

server4 `/var/tmp`: 105930674176 available bytes; 94.09% used; 114348032 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
