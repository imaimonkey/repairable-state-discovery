# V2R cluster inventory

2026-09-25T04:42:57.559557+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318914875392 available bytes; 82.21% used; 112480365 free inodes.

server1 `/home`: 318914875392 available bytes; 82.21% used; 112480365 free inodes.

server1 `/tmp`: 318914875392 available bytes; 82.21% used; 112480365 free inodes.

server1 `/var/tmp`: 318914875392 available bytes; 82.21% used; 112480365 free inodes.

server1 `/mnt/raid5`: 408693891072 available bytes; 98.13% used; 337590116 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22948941824 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22948941824 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22948941824 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22948941824 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 462639747072 available bytes; 96.80% used; 445109423 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340310016 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84340310016 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 143306694656 available bytes; 98.02% used; 225815907 free inodes.

server3 `/tmp`: 84340310016 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84340310016 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105663942656 available bytes; 94.10% used; 114350594 free inodes.

server4 `/home`: 105663942656 available bytes; 94.10% used; 114350594 free inodes.

server4 `/data`: 31172554752 available bytes; 99.57% used; 224962250 free inodes.

server4 `/tmp`: 105663942656 available bytes; 94.10% used; 114350594 free inodes.

server4 `/var/tmp`: 105663942656 available bytes; 94.10% used; 114350594 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
