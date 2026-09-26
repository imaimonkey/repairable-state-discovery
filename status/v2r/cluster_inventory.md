# V2R cluster inventory

2026-09-26T01:13:59.784681+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318657765376 available bytes; 82.22% used; 112476294 free inodes.

server1 `/home`: 318657765376 available bytes; 82.22% used; 112476294 free inodes.

server1 `/tmp`: 318657765376 available bytes; 82.22% used; 112476294 free inodes.

server1 `/var/tmp`: 318657765376 available bytes; 82.22% used; 112476294 free inodes.

server1 `/mnt/raid5`: 345536081920 available bytes; 98.41% used; 337546634 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22938796032 available bytes; 98.72% used; 110406202 free inodes.

server2 `/home`: 22938796032 available bytes; 98.72% used; 110406202 free inodes.

server2 `/tmp`: 22938796032 available bytes; 98.72% used; 110406202 free inodes.

server2 `/var/tmp`: 22938796032 available bytes; 98.72% used; 110406202 free inodes.

server2 `/mnt/raid5`: 291186114560 available bytes; 97.99% used; 445056332 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84341882880 available bytes; 95.29% used; 114152426 free inodes.

server3 `/home`: 84341882880 available bytes; 95.29% used; 114152426 free inodes.

server3 `/data`: 124935544832 available bytes; 98.27% used; 225818302 free inodes.

server3 `/tmp`: 84341882880 available bytes; 95.29% used; 114152426 free inodes.

server3 `/var/tmp`: 84341882880 available bytes; 95.29% used; 114152426 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105281372160 available bytes; 94.12% used; 114347079 free inodes.

server4 `/home`: 105281372160 available bytes; 94.12% used; 114347079 free inodes.

server4 `/data`: 141691269120 available bytes; 98.04% used; 224917308 free inodes.

server4 `/tmp`: 105281372160 available bytes; 94.12% used; 114347079 free inodes.

server4 `/var/tmp`: 105281372160 available bytes; 94.12% used; 114347079 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
