# V2R cluster inventory

2026-09-26T00:42:29.734174+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318650499072 available bytes; 82.22% used; 112476302 free inodes.

server1 `/home`: 318650499072 available bytes; 82.22% used; 112476302 free inodes.

server1 `/tmp`: 318650499072 available bytes; 82.22% used; 112476302 free inodes.

server1 `/var/tmp`: 318650499072 available bytes; 82.22% used; 112476302 free inodes.

server1 `/mnt/raid5`: 345611993088 available bytes; 98.41% used; 337546788 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22940971008 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22940971008 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22940971008 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22940971008 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 294722326528 available bytes; 97.96% used; 445057287 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84342779904 available bytes; 95.29% used; 114152439 free inodes.

server3 `/home`: 84342779904 available bytes; 95.29% used; 114152439 free inodes.

server3 `/data`: 124944166912 available bytes; 98.27% used; 225818828 free inodes.

server3 `/tmp`: 84342779904 available bytes; 95.29% used; 114152439 free inodes.

server3 `/var/tmp`: 84342779904 available bytes; 95.29% used; 114152439 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105349431296 available bytes; 94.12% used; 114347253 free inodes.

server4 `/home`: 105349431296 available bytes; 94.12% used; 114347253 free inodes.

server4 `/data`: 148674310144 available bytes; 97.95% used; 224917381 free inodes.

server4 `/tmp`: 105349431296 available bytes; 94.12% used; 114347253 free inodes.

server4 `/var/tmp`: 105349431296 available bytes; 94.12% used; 114347253 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
