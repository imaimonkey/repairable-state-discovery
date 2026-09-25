# V2R cluster inventory

2026-09-25T18:29:33.327331+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318749847552 available bytes; 82.22% used; 112476346 free inodes.

server1 `/home`: 318749847552 available bytes; 82.22% used; 112476346 free inodes.

server1 `/tmp`: 318749847552 available bytes; 82.22% used; 112476346 free inodes.

server1 `/var/tmp`: 318749847552 available bytes; 82.22% used; 112476346 free inodes.

server1 `/mnt/raid5`: 371185311744 available bytes; 98.30% used; 337541827 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23105470464 available bytes; 98.71% used; 110407936 free inodes.

server2 `/home`: 23105470464 available bytes; 98.71% used; 110407936 free inodes.

server2 `/tmp`: 23105470464 available bytes; 98.71% used; 110407936 free inodes.

server2 `/var/tmp`: 23105470464 available bytes; 98.71% used; 110407936 free inodes.

server2 `/mnt/raid5`: 314012643328 available bytes; 97.83% used; 445066740 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84394442752 available bytes; 95.29% used; 114152621 free inodes.

server3 `/home`: 84394442752 available bytes; 95.29% used; 114152621 free inodes.

server3 `/data`: 131453100032 available bytes; 98.18% used; 225809812 free inodes.

server3 `/tmp`: 84394442752 available bytes; 95.29% used; 114152621 free inodes.

server3 `/var/tmp`: 84394442752 available bytes; 95.29% used; 114152621 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105615859712 available bytes; 94.11% used; 114349600 free inodes.

server4 `/home`: 105615859712 available bytes; 94.11% used; 114349600 free inodes.

server4 `/data`: 229696798720 available bytes; 96.83% used; 224931787 free inodes.

server4 `/tmp`: 105615859712 available bytes; 94.11% used; 114349600 free inodes.

server4 `/var/tmp`: 105615859712 available bytes; 94.11% used; 114349600 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
