# V2R cluster inventory

2026-09-25T15:56:32.174383+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318678994944 available bytes; 82.22% used; 112476508 free inodes.

server1 `/home`: 318678994944 available bytes; 82.22% used; 112476508 free inodes.

server1 `/tmp`: 318678994944 available bytes; 82.22% used; 112476508 free inodes.

server1 `/var/tmp`: 318678994944 available bytes; 82.22% used; 112476508 free inodes.

server1 `/mnt/raid5`: 363938283520 available bytes; 98.33% used; 337545353 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23116054528 available bytes; 98.71% used; 110407946 free inodes.

server2 `/home`: 23116054528 available bytes; 98.71% used; 110407946 free inodes.

server2 `/tmp`: 23116054528 available bytes; 98.71% used; 110407946 free inodes.

server2 `/var/tmp`: 23116054528 available bytes; 98.71% used; 110407946 free inodes.

server2 `/mnt/raid5`: 319282511872 available bytes; 97.79% used; 445071552 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84412653568 available bytes; 95.29% used; 114152920 free inodes.

server3 `/home`: 84412653568 available bytes; 95.29% used; 114152920 free inodes.

server3 `/data`: 142184509440 available bytes; 98.03% used; 225806698 free inodes.

server3 `/tmp`: 84412653568 available bytes; 95.29% used; 114152920 free inodes.

server3 `/var/tmp`: 84412653568 available bytes; 95.29% used; 114152920 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105637154816 available bytes; 94.11% used; 114349667 free inodes.

server4 `/home`: 105637154816 available bytes; 94.11% used; 114349667 free inodes.

server4 `/data`: 231294001152 available bytes; 96.80% used; 224943441 free inodes.

server4 `/tmp`: 105637154816 available bytes; 94.11% used; 114349667 free inodes.

server4 `/var/tmp`: 105637154816 available bytes; 94.11% used; 114349667 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
