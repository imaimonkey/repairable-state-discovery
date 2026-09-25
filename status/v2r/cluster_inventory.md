# V2R cluster inventory

2026-09-25T18:11:12.971285+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318762102784 available bytes; 82.22% used; 112476350 free inodes.

server1 `/home`: 318762102784 available bytes; 82.22% used; 112476350 free inodes.

server1 `/tmp`: 318762102784 available bytes; 82.22% used; 112476350 free inodes.

server1 `/var/tmp`: 318762102784 available bytes; 82.22% used; 112476350 free inodes.

server1 `/mnt/raid5`: 371217682432 available bytes; 98.30% used; 337542261 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23098687488 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23098687488 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23098687488 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23098687488 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 314538352640 available bytes; 97.83% used; 445067283 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84392390656 available bytes; 95.29% used; 114152617 free inodes.

server3 `/home`: 84392390656 available bytes; 95.29% used; 114152617 free inodes.

server3 `/data`: 131474784256 available bytes; 98.18% used; 225810249 free inodes.

server3 `/tmp`: 84392390656 available bytes; 95.29% used; 114152617 free inodes.

server3 `/var/tmp`: 84392390656 available bytes; 95.29% used; 114152617 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105616400384 available bytes; 94.11% used; 114349604 free inodes.

server4 `/home`: 105616400384 available bytes; 94.11% used; 114349604 free inodes.

server4 `/data`: 229733703680 available bytes; 96.82% used; 224932257 free inodes.

server4 `/tmp`: 105616400384 available bytes; 94.11% used; 114349604 free inodes.

server4 `/var/tmp`: 105616400384 available bytes; 94.11% used; 114349604 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
