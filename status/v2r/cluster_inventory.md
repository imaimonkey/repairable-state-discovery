# V2R cluster inventory

2026-09-25T18:57:05.394153+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318739861504 available bytes; 82.22% used; 112476333 free inodes.

server1 `/home`: 318739861504 available bytes; 82.22% used; 112476333 free inodes.

server1 `/tmp`: 318739861504 available bytes; 82.22% used; 112476333 free inodes.

server1 `/var/tmp`: 318739861504 available bytes; 82.22% used; 112476333 free inodes.

server1 `/mnt/raid5`: 371039703040 available bytes; 98.30% used; 337541030 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23096131584 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23096131584 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23096131584 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23096131584 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 313174417408 available bytes; 97.84% used; 445065715 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84382965760 available bytes; 95.29% used; 114152621 free inodes.

server3 `/home`: 84382965760 available bytes; 95.29% used; 114152621 free inodes.

server3 `/data`: 131371888640 available bytes; 98.18% used; 225809176 free inodes.

server3 `/tmp`: 84382965760 available bytes; 95.29% used; 114152621 free inodes.

server3 `/var/tmp`: 84382965760 available bytes; 95.29% used; 114152621 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105606651904 available bytes; 94.11% used; 114349596 free inodes.

server4 `/home`: 105606651904 available bytes; 94.11% used; 114349596 free inodes.

server4 `/data`: 229682860032 available bytes; 96.83% used; 224931360 free inodes.

server4 `/tmp`: 105606651904 available bytes; 94.11% used; 114349596 free inodes.

server4 `/var/tmp`: 105606651904 available bytes; 94.11% used; 114349596 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
