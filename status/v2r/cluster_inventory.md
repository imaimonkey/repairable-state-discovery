# V2R cluster inventory

2026-09-26T01:10:56.823356+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318658392064 available bytes; 82.22% used; 112476294 free inodes.

server1 `/home`: 318658392064 available bytes; 82.22% used; 112476294 free inodes.

server1 `/tmp`: 318658392064 available bytes; 82.22% used; 112476294 free inodes.

server1 `/var/tmp`: 318658392064 available bytes; 82.22% used; 112476294 free inodes.

server1 `/mnt/raid5`: 345541185536 available bytes; 98.41% used; 337546640 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22939930624 available bytes; 98.72% used; 110406202 free inodes.

server2 `/home`: 22939930624 available bytes; 98.72% used; 110406202 free inodes.

server2 `/tmp`: 22939930624 available bytes; 98.72% used; 110406202 free inodes.

server2 `/var/tmp`: 22939930624 available bytes; 98.72% used; 110406202 free inodes.

server2 `/mnt/raid5`: 291274231808 available bytes; 97.99% used; 445056443 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84340678656 available bytes; 95.29% used; 114152424 free inodes.

server3 `/home`: 84340678656 available bytes; 95.29% used; 114152424 free inodes.

server3 `/data`: 124932497408 available bytes; 98.27% used; 225818353 free inodes.

server3 `/tmp`: 84340678656 available bytes; 95.29% used; 114152424 free inodes.

server3 `/var/tmp`: 84340678656 available bytes; 95.29% used; 114152424 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105281458176 available bytes; 94.12% used; 114347079 free inodes.

server4 `/home`: 105281458176 available bytes; 94.12% used; 114347079 free inodes.

server4 `/data`: 141764329472 available bytes; 98.04% used; 224917328 free inodes.

server4 `/tmp`: 105281458176 available bytes; 94.12% used; 114347079 free inodes.

server4 `/var/tmp`: 105281458176 available bytes; 94.12% used; 114347079 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
