# V2R cluster inventory

2026-09-25T15:58:05.200889+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318678605824 available bytes; 82.22% used; 112476507 free inodes.

server1 `/home`: 318678605824 available bytes; 82.22% used; 112476507 free inodes.

server1 `/tmp`: 318678605824 available bytes; 82.22% used; 112476507 free inodes.

server1 `/var/tmp`: 318678605824 available bytes; 82.22% used; 112476507 free inodes.

server1 `/mnt/raid5`: 369332396032 available bytes; 98.31% used; 337545385 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23115747328 available bytes; 98.71% used; 110407946 free inodes.

server2 `/home`: 23115747328 available bytes; 98.71% used; 110407946 free inodes.

server2 `/tmp`: 23115747328 available bytes; 98.71% used; 110407946 free inodes.

server2 `/var/tmp`: 23115747328 available bytes; 98.71% used; 110407946 free inodes.

server2 `/mnt/raid5`: 318706728960 available bytes; 97.80% used; 445071685 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84403802112 available bytes; 95.29% used; 114152684 free inodes.

server3 `/home`: 84403802112 available bytes; 95.29% used; 114152684 free inodes.

server3 `/data`: 140112023552 available bytes; 98.06% used; 225806614 free inodes.

server3 `/tmp`: 84403802112 available bytes; 95.29% used; 114152684 free inodes.

server3 `/var/tmp`: 84403802112 available bytes; 95.29% used; 114152684 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105637101568 available bytes; 94.11% used; 114349665 free inodes.

server4 `/home`: 105637101568 available bytes; 94.11% used; 114349665 free inodes.

server4 `/data`: 231292567552 available bytes; 96.80% used; 224943412 free inodes.

server4 `/tmp`: 105637101568 available bytes; 94.11% used; 114349665 free inodes.

server4 `/var/tmp`: 105637101568 available bytes; 94.11% used; 114349665 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
