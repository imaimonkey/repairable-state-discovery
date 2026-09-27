# V2R cluster inventory

2026-09-27T06:37:43.963906+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314498572288 available bytes; 82.46% used; 112440812 free inodes.

server1 `/home`: 314498572288 available bytes; 82.46% used; 112440812 free inodes.

server1 `/tmp`: 314498572288 available bytes; 82.46% used; 112440812 free inodes.

server1 `/var/tmp`: 314498572288 available bytes; 82.46% used; 112440812 free inodes.

server1 `/mnt/raid5`: 634679455744 available bytes; 97.09% used; 337400004 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17618665472 available bytes; 99.02% used; 110365003 free inodes.

server2 `/home`: 17618665472 available bytes; 99.02% used; 110365003 free inodes.

server2 `/tmp`: 17618665472 available bytes; 99.02% used; 110365003 free inodes.

server2 `/var/tmp`: 17618665472 available bytes; 99.02% used; 110365003 free inodes.

server2 `/mnt/raid5`: 572897255424 available bytes; 96.04% used; 444875928 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78575546368 available bytes; 95.62% used; 114062893 free inodes.

server3 `/home`: 78575546368 available bytes; 95.62% used; 114062893 free inodes.

server3 `/data`: 1333274935296 available bytes; 81.57% used; 225765291 free inodes.

server3 `/tmp`: 78575546368 available bytes; 95.62% used; 114062893 free inodes.

server3 `/var/tmp`: 78575546368 available bytes; 95.62% used; 114062893 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110997950464 available bytes; 93.81% used; 114372899 free inodes.

server4 `/home`: 110997950464 available bytes; 93.81% used; 114372899 free inodes.

server4 `/data`: 374455975936 available bytes; 94.82% used; 224771185 free inodes.

server4 `/tmp`: 110997950464 available bytes; 93.81% used; 114372899 free inodes.

server4 `/var/tmp`: 110997950464 available bytes; 93.81% used; 114372899 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
