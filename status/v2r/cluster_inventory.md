# V2R cluster inventory

2026-09-25T16:19:33.521573+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318672588800 available bytes; 82.22% used; 112476327 free inodes.

server1 `/home`: 318672588800 available bytes; 82.22% used; 112476327 free inodes.

server1 `/tmp`: 318672588800 available bytes; 82.22% used; 112476327 free inodes.

server1 `/var/tmp`: 318672588800 available bytes; 82.22% used; 112476327 free inodes.

server1 `/mnt/raid5`: 365257277440 available bytes; 98.32% used; 337544894 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23108751360 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23108751360 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23108751360 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23108751360 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 318662131712 available bytes; 97.80% used; 445070700 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 84402962432 available bytes; 95.29% used; 114152696 free inodes.

server3 `/home`: 84402962432 available bytes; 95.29% used; 114152696 free inodes.

server3 `/data`: 134867177472 available bytes; 98.14% used; 225806086 free inodes.

server3 `/tmp`: 84402962432 available bytes; 95.29% used; 114152696 free inodes.

server3 `/var/tmp`: 84402962432 available bytes; 95.29% used; 114152696 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105636433920 available bytes; 94.11% used; 114349647 free inodes.

server4 `/home`: 105636433920 available bytes; 94.11% used; 114349647 free inodes.

server4 `/data`: 230236549120 available bytes; 96.82% used; 224934404 free inodes.

server4 `/tmp`: 105636433920 available bytes; 94.11% used; 114349647 free inodes.

server4 `/var/tmp`: 105636433920 available bytes; 94.11% used; 114349647 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
