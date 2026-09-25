# V2R cluster inventory

2026-09-25T17:06:57.990572+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318680993792 available bytes; 82.22% used; 112476347 free inodes.

server1 `/home`: 318680993792 available bytes; 82.22% used; 112476347 free inodes.

server1 `/tmp`: 318680993792 available bytes; 82.22% used; 112476347 free inodes.

server1 `/var/tmp`: 318680993792 available bytes; 82.22% used; 112476347 free inodes.

server1 `/mnt/raid5`: 367187435520 available bytes; 98.32% used; 337543726 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23100682240 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23100682240 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23100682240 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23100682240 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 316708192256 available bytes; 97.81% used; 445068996 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84395081728 available bytes; 95.29% used; 114152611 free inodes.

server3 `/home`: 84395081728 available bytes; 95.29% used; 114152611 free inodes.

server3 `/data`: 132802662400 available bytes; 98.16% used; 225811882 free inodes.

server3 `/tmp`: 84395081728 available bytes; 95.29% used; 114152611 free inodes.

server3 `/var/tmp`: 84395081728 available bytes; 95.29% used; 114152611 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105626718208 available bytes; 94.11% used; 114349641 free inodes.

server4 `/home`: 105626718208 available bytes; 94.11% used; 114349641 free inodes.

server4 `/data`: 229949571072 available bytes; 96.82% used; 224933250 free inodes.

server4 `/tmp`: 105626718208 available bytes; 94.11% used; 114349641 free inodes.

server4 `/var/tmp`: 105626718208 available bytes; 94.11% used; 114349641 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
