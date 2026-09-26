# V2R cluster inventory

2026-09-26T03:13:04.935480+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318418145280 available bytes; 82.24% used; 112476252 free inodes.

server1 `/home`: 318418145280 available bytes; 82.24% used; 112476252 free inodes.

server1 `/tmp`: 318418145280 available bytes; 82.24% used; 112476252 free inodes.

server1 `/var/tmp`: 318418145280 available bytes; 82.24% used; 112476252 free inodes.

server1 `/mnt/raid5`: 331051044864 available bytes; 98.48% used; 337545887 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22939643904 available bytes; 98.72% used; 110406210 free inodes.

server2 `/home`: 22939643904 available bytes; 98.72% used; 110406210 free inodes.

server2 `/tmp`: 22939643904 available bytes; 98.72% used; 110406210 free inodes.

server2 `/var/tmp`: 22939643904 available bytes; 98.72% used; 110406210 free inodes.

server2 `/mnt/raid5`: 287730589696 available bytes; 98.01% used; 445053060 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84311941120 available bytes; 95.30% used; 114152352 free inodes.

server3 `/home`: 84311941120 available bytes; 95.30% used; 114152352 free inodes.

server3 `/data`: 125437284352 available bytes; 98.27% used; 225830899 free inodes.

server3 `/tmp`: 84311941120 available bytes; 95.30% used; 114152352 free inodes.

server3 `/var/tmp`: 84311941120 available bytes; 95.30% used; 114152352 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105918377984 available bytes; 94.09% used; 114347138 free inodes.

server4 `/home`: 105918377984 available bytes; 94.09% used; 114347138 free inodes.

server4 `/data`: 109092102144 available bytes; 98.49% used; 224914854 free inodes.

server4 `/tmp`: 105918377984 available bytes; 94.09% used; 114347138 free inodes.

server4 `/var/tmp`: 105918377984 available bytes; 94.09% used; 114347138 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
