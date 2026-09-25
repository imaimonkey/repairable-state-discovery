# V2R cluster inventory

2026-09-25T04:50:37.827905+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318908022784 available bytes; 82.21% used; 112480346 free inodes.

server1 `/home`: 318908022784 available bytes; 82.21% used; 112480346 free inodes.

server1 `/tmp`: 318908022784 available bytes; 82.21% used; 112480346 free inodes.

server1 `/var/tmp`: 318908022784 available bytes; 82.21% used; 112480346 free inodes.

server1 `/mnt/raid5`: 408675373056 available bytes; 98.13% used; 337589184 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22941655040 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22941655040 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22941655040 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22941655040 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 462392475648 available bytes; 96.80% used; 445109176 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84339171328 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84339171328 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 143126319104 available bytes; 98.02% used; 225815741 free inodes.

server3 `/tmp`: 84339171328 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84339171328 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105661681664 available bytes; 94.10% used; 114350497 free inodes.

server4 `/home`: 105661681664 available bytes; 94.10% used; 114350497 free inodes.

server4 `/data`: 27947769856 available bytes; 99.61% used; 224961781 free inodes.

server4 `/tmp`: 105661681664 available bytes; 94.10% used; 114350497 free inodes.

server4 `/var/tmp`: 105661681664 available bytes; 94.10% used; 114350497 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
