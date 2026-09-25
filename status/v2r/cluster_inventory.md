# V2R cluster inventory

2026-09-25T15:55:00.557341+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318679326720 available bytes; 82.22% used; 112476515 free inodes.

server1 `/home`: 318679326720 available bytes; 82.22% used; 112476515 free inodes.

server1 `/tmp`: 318679326720 available bytes; 82.22% used; 112476515 free inodes.

server1 `/var/tmp`: 318679326720 available bytes; 82.22% used; 112476515 free inodes.

server1 `/mnt/raid5`: 363942510592 available bytes; 98.33% used; 337545389 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23102881792 available bytes; 98.71% used; 110407944 free inodes.

server2 `/home`: 23102881792 available bytes; 98.71% used; 110407944 free inodes.

server2 `/tmp`: 23102881792 available bytes; 98.71% used; 110407944 free inodes.

server2 `/var/tmp`: 23102881792 available bytes; 98.71% used; 110407944 free inodes.

server2 `/mnt/raid5`: 319324282880 available bytes; 97.79% used; 445071681 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 84427284480 available bytes; 95.29% used; 114153473 free inodes.

server3 `/home`: 84427284480 available bytes; 95.29% used; 114153473 free inodes.

server3 `/data`: 142185742336 available bytes; 98.03% used; 225806734 free inodes.

server3 `/tmp`: 84427284480 available bytes; 95.29% used; 114153473 free inodes.

server3 `/var/tmp`: 84427284480 available bytes; 95.29% used; 114153473 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105637224448 available bytes; 94.11% used; 114349677 free inodes.

server4 `/home`: 105637224448 available bytes; 94.11% used; 114349677 free inodes.

server4 `/data`: 231305068544 available bytes; 96.80% used; 224943556 free inodes.

server4 `/tmp`: 105637224448 available bytes; 94.11% used; 114349677 free inodes.

server4 `/var/tmp`: 105637224448 available bytes; 94.11% used; 114349677 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
