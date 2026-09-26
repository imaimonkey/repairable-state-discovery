# V2R cluster inventory

2026-09-26T01:06:22.233890+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318658990080 available bytes; 82.22% used; 112476292 free inodes.

server1 `/home`: 318658990080 available bytes; 82.22% used; 112476292 free inodes.

server1 `/tmp`: 318658990080 available bytes; 82.22% used; 112476292 free inodes.

server1 `/var/tmp`: 318658990080 available bytes; 82.22% used; 112476292 free inodes.

server1 `/mnt/raid5`: 345552347136 available bytes; 98.41% used; 337546660 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22940061696 available bytes; 98.72% used; 110406200 free inodes.

server2 `/home`: 22940061696 available bytes; 98.72% used; 110406200 free inodes.

server2 `/tmp`: 22940061696 available bytes; 98.72% used; 110406200 free inodes.

server2 `/var/tmp`: 22940061696 available bytes; 98.72% used; 110406200 free inodes.

server2 `/mnt/raid5`: 293889060864 available bytes; 97.97% used; 445056579 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84337790976 available bytes; 95.29% used; 114152424 free inodes.

server3 `/home`: 84337790976 available bytes; 95.29% used; 114152424 free inodes.

server3 `/data`: 124934832128 available bytes; 98.27% used; 225818423 free inodes.

server3 `/tmp`: 84337790976 available bytes; 95.29% used; 114152424 free inodes.

server3 `/var/tmp`: 84337790976 available bytes; 95.29% used; 114152424 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105281589248 available bytes; 94.12% used; 114347079 free inodes.

server4 `/home`: 105281589248 available bytes; 94.12% used; 114347079 free inodes.

server4 `/data`: 141769007104 available bytes; 98.04% used; 224917333 free inodes.

server4 `/tmp`: 105281589248 available bytes; 94.12% used; 114347079 free inodes.

server4 `/var/tmp`: 105281589248 available bytes; 94.12% used; 114347079 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
