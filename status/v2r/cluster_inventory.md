# V2R cluster inventory

2026-09-25T16:54:44.670434+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318681546752 available bytes; 82.22% used; 112476339 free inodes.

server1 `/home`: 318681546752 available bytes; 82.22% used; 112476339 free inodes.

server1 `/tmp`: 318681546752 available bytes; 82.22% used; 112476339 free inodes.

server1 `/var/tmp`: 318681546752 available bytes; 82.22% used; 112476339 free inodes.

server1 `/mnt/raid5`: 364368695296 available bytes; 98.33% used; 337544001 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23107788800 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23107788800 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23107788800 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23107788800 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 317094060032 available bytes; 97.81% used; 445069573 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84396630016 available bytes; 95.29% used; 114152623 free inodes.

server3 `/home`: 84396630016 available bytes; 95.29% used; 114152623 free inodes.

server3 `/data`: 133777461248 available bytes; 98.15% used; 225805239 free inodes.

server3 `/tmp`: 84396630016 available bytes; 95.29% used; 114152623 free inodes.

server3 `/var/tmp`: 84396630016 available bytes; 95.29% used; 114152623 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105635438592 available bytes; 94.11% used; 114349641 free inodes.

server4 `/home`: 105635438592 available bytes; 94.11% used; 114349641 free inodes.

server4 `/data`: 229982715904 available bytes; 96.82% used; 224933490 free inodes.

server4 `/tmp`: 105635438592 available bytes; 94.11% used; 114349641 free inodes.

server4 `/var/tmp`: 105635438592 available bytes; 94.11% used; 114349641 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
