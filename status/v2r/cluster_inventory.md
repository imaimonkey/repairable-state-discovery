# V2R cluster inventory

2026-09-24T01:43:06.366759+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325457108992 available bytes; 81.84% used; 112499480 free inodes.

server1 `/home`: 325457108992 available bytes; 81.84% used; 112499480 free inodes.

server1 `/tmp`: 325457108992 available bytes; 81.84% used; 112499480 free inodes.

server1 `/var/tmp`: 325457108992 available bytes; 81.84% used; 112499480 free inodes.

server1 `/mnt/raid5`: 843327561728 available bytes; 96.13% used; 337733861 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40935161856 available bytes; 97.72% used; 110431891 free inodes.

server2 `/home`: 40935161856 available bytes; 97.72% used; 110431891 free inodes.

server2 `/tmp`: 40935161856 available bytes; 97.72% used; 110431891 free inodes.

server2 `/var/tmp`: 40935161856 available bytes; 97.72% used; 110431891 free inodes.

server2 `/mnt/raid5`: 530396598272 available bytes; 96.34% used; 445201067 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292713709568 available bytes; 83.67% used; 114211036 free inodes.

server3 `/home`: 292713709568 available bytes; 83.67% used; 114211036 free inodes.

server3 `/data`: 71399288832 available bytes; 99.01% used; 225842020 free inodes.

server3 `/tmp`: 292713709568 available bytes; 83.67% used; 114211036 free inodes.

server3 `/var/tmp`: 292713709568 available bytes; 83.67% used; 114211036 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105954033664 available bytes; 94.09% used; 114348616 free inodes.

server4 `/home`: 105954033664 available bytes; 94.09% used; 114348616 free inodes.

server4 `/data`: 289766490112 available bytes; 96.00% used; 225388487 free inodes.

server4 `/tmp`: 105954033664 available bytes; 94.09% used; 114348616 free inodes.

server4 `/var/tmp`: 105954033664 available bytes; 94.09% used; 114348616 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
