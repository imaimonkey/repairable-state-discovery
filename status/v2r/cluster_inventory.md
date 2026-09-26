# V2R cluster inventory

2026-09-26T01:11:30.522736+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318658273280 available bytes; 82.22% used; 112476294 free inodes.

server1 `/home`: 318658273280 available bytes; 82.22% used; 112476294 free inodes.

server1 `/tmp`: 318658273280 available bytes; 82.22% used; 112476294 free inodes.

server1 `/var/tmp`: 318658273280 available bytes; 82.22% used; 112476294 free inodes.

server1 `/mnt/raid5`: 345540292608 available bytes; 98.41% used; 337546640 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22939824128 available bytes; 98.72% used; 110406202 free inodes.

server2 `/home`: 22939824128 available bytes; 98.72% used; 110406202 free inodes.

server2 `/tmp`: 22939824128 available bytes; 98.72% used; 110406202 free inodes.

server2 `/var/tmp`: 22939824128 available bytes; 98.72% used; 110406202 free inodes.

server2 `/mnt/raid5`: 291251376128 available bytes; 97.99% used; 445056395 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340469760 available bytes; 95.29% used; 114152424 free inodes.

server3 `/home`: 84340469760 available bytes; 95.29% used; 114152424 free inodes.

server3 `/data`: 124932141056 available bytes; 98.27% used; 225818334 free inodes.

server3 `/tmp`: 84340469760 available bytes; 95.29% used; 114152424 free inodes.

server3 `/var/tmp`: 84340469760 available bytes; 95.29% used; 114152424 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105281445888 available bytes; 94.12% used; 114347079 free inodes.

server4 `/home`: 105281445888 available bytes; 94.12% used; 114347079 free inodes.

server4 `/data`: 141694189568 available bytes; 98.04% used; 224917324 free inodes.

server4 `/tmp`: 105281445888 available bytes; 94.12% used; 114347079 free inodes.

server4 `/var/tmp`: 105281445888 available bytes; 94.12% used; 114347079 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
