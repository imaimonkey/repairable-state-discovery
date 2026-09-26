# V2R cluster inventory

2026-09-26T02:48:37.659299+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318418964480 available bytes; 82.24% used; 112476265 free inodes.

server1 `/home`: 318418964480 available bytes; 82.24% used; 112476265 free inodes.

server1 `/tmp`: 318418964480 available bytes; 82.24% used; 112476265 free inodes.

server1 `/var/tmp`: 318418964480 available bytes; 82.24% used; 112476265 free inodes.

server1 `/mnt/raid5`: 331113246720 available bytes; 98.48% used; 337546022 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22936952832 available bytes; 98.72% used; 110406218 free inodes.

server2 `/home`: 22936952832 available bytes; 98.72% used; 110406218 free inodes.

server2 `/tmp`: 22936952832 available bytes; 98.72% used; 110406218 free inodes.

server2 `/var/tmp`: 22936952832 available bytes; 98.72% used; 110406218 free inodes.

server2 `/mnt/raid5`: 288440401920 available bytes; 98.01% used; 445053700 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84320153600 available bytes; 95.29% used; 114152372 free inodes.

server3 `/home`: 84320153600 available bytes; 95.29% used; 114152372 free inodes.

server3 `/data`: 124783616000 available bytes; 98.28% used; 225816686 free inodes.

server3 `/tmp`: 84320153600 available bytes; 95.29% used; 114152372 free inodes.

server3 `/var/tmp`: 84320153600 available bytes; 95.29% used; 114152372 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105919225856 available bytes; 94.09% used; 114347153 free inodes.

server4 `/home`: 105919225856 available bytes; 94.09% used; 114347153 free inodes.

server4 `/data`: 109770428416 available bytes; 98.48% used; 224915404 free inodes.

server4 `/tmp`: 105919225856 available bytes; 94.09% used; 114347153 free inodes.

server4 `/var/tmp`: 105919225856 available bytes; 94.09% used; 114347153 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
