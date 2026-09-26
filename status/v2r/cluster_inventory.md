# V2R cluster inventory

2026-09-26T00:33:19.894335+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318652096512 available bytes; 82.22% used; 112476300 free inodes.

server1 `/home`: 318652096512 available bytes; 82.22% used; 112476300 free inodes.

server1 `/tmp`: 318652096512 available bytes; 82.22% used; 112476300 free inodes.

server1 `/var/tmp`: 318652096512 available bytes; 82.22% used; 112476300 free inodes.

server1 `/mnt/raid5`: 345627705344 available bytes; 98.41% used; 337546826 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22943195136 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22943195136 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22943195136 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22943195136 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 294991953920 available bytes; 97.96% used; 445057807 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84339867648 available bytes; 95.29% used; 114152441 free inodes.

server3 `/home`: 84339867648 available bytes; 95.29% used; 114152441 free inodes.

server3 `/data`: 124944322560 available bytes; 98.27% used; 225818991 free inodes.

server3 `/tmp`: 84339867648 available bytes; 95.29% used; 114152441 free inodes.

server3 `/var/tmp`: 84339867648 available bytes; 95.29% used; 114152441 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105349697536 available bytes; 94.12% used; 114347253 free inodes.

server4 `/home`: 105349697536 available bytes; 94.12% used; 114347253 free inodes.

server4 `/data`: 169381621760 available bytes; 97.66% used; 224917436 free inodes.

server4 `/tmp`: 105349697536 available bytes; 94.12% used; 114347253 free inodes.

server4 `/var/tmp`: 105349697536 available bytes; 94.12% used; 114347253 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
