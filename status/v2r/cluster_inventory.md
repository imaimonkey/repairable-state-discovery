# V2R cluster inventory

2026-09-25T16:02:41.453880+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318678339584 available bytes; 82.22% used; 112476513 free inodes.

server1 `/home`: 318678339584 available bytes; 82.22% used; 112476513 free inodes.

server1 `/tmp`: 318678339584 available bytes; 82.22% used; 112476513 free inodes.

server1 `/var/tmp`: 318678339584 available bytes; 82.22% used; 112476513 free inodes.

server1 `/mnt/raid5`: 363941687296 available bytes; 98.33% used; 337545218 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23117160448 available bytes; 98.71% used; 110407946 free inodes.

server2 `/home`: 23117160448 available bytes; 98.71% used; 110407946 free inodes.

server2 `/tmp`: 23117160448 available bytes; 98.71% used; 110407946 free inodes.

server2 `/var/tmp`: 23117160448 available bytes; 98.71% used; 110407946 free inodes.

server2 `/mnt/raid5`: 319150845952 available bytes; 97.79% used; 445071387 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84403343360 available bytes; 95.29% used; 114152682 free inodes.

server3 `/home`: 84403343360 available bytes; 95.29% used; 114152682 free inodes.

server3 `/data`: 138040053760 available bytes; 98.09% used; 225806476 free inodes.

server3 `/tmp`: 84403343360 available bytes; 95.29% used; 114152682 free inodes.

server3 `/var/tmp`: 84403343360 available bytes; 95.29% used; 114152682 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105636941824 available bytes; 94.11% used; 114349663 free inodes.

server4 `/home`: 105636941824 available bytes; 94.11% used; 114349663 free inodes.

server4 `/data`: 231292833792 available bytes; 96.80% used; 224943280 free inodes.

server4 `/tmp`: 105636941824 available bytes; 94.11% used; 114349663 free inodes.

server4 `/var/tmp`: 105636941824 available bytes; 94.11% used; 114349663 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
