# V2R cluster inventory

2026-09-26T01:06:55.810944+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318659534848 available bytes; 82.22% used; 112476294 free inodes.

server1 `/home`: 318659534848 available bytes; 82.22% used; 112476294 free inodes.

server1 `/tmp`: 318659534848 available bytes; 82.22% used; 112476294 free inodes.

server1 `/var/tmp`: 318659534848 available bytes; 82.22% used; 112476294 free inodes.

server1 `/mnt/raid5`: 345551704064 available bytes; 98.41% used; 337546660 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22941007872 available bytes; 98.72% used; 110406200 free inodes.

server2 `/home`: 22941007872 available bytes; 98.72% used; 110406200 free inodes.

server2 `/tmp`: 22941007872 available bytes; 98.72% used; 110406200 free inodes.

server2 `/var/tmp`: 22941007872 available bytes; 98.72% used; 110406200 free inodes.

server2 `/mnt/raid5`: 292799770624 available bytes; 97.98% used; 445056546 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84342034432 available bytes; 95.29% used; 114152426 free inodes.

server3 `/home`: 84342034432 available bytes; 95.29% used; 114152426 free inodes.

server3 `/data`: 124934434816 available bytes; 98.27% used; 225818405 free inodes.

server3 `/tmp`: 84342034432 available bytes; 95.29% used; 114152426 free inodes.

server3 `/var/tmp`: 84342034432 available bytes; 95.29% used; 114152426 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105281576960 available bytes; 94.12% used; 114347079 free inodes.

server4 `/home`: 105281576960 available bytes; 94.12% used; 114347079 free inodes.

server4 `/data`: 141767745536 available bytes; 98.04% used; 224917332 free inodes.

server4 `/tmp`: 105281576960 available bytes; 94.12% used; 114347079 free inodes.

server4 `/var/tmp`: 105281576960 available bytes; 94.12% used; 114347079 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
