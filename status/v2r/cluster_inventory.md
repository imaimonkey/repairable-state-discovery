# V2R cluster inventory

2026-09-27T08:49:56.338669+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314468745216 available bytes; 82.46% used; 112440736 free inodes.

server1 `/home`: 314468745216 available bytes; 82.46% used; 112440736 free inodes.

server1 `/tmp`: 314468745216 available bytes; 82.46% used; 112440736 free inodes.

server1 `/var/tmp`: 314468745216 available bytes; 82.46% used; 112440736 free inodes.

server1 `/mnt/raid5`: 634583138304 available bytes; 97.09% used; 337400007 free inodes.
| server2 | True | ['1', '2', '7'] | [] |

server2 `/`: 17602306048 available bytes; 99.02% used; 110364820 free inodes.

server2 `/home`: 17602306048 available bytes; 99.02% used; 110364820 free inodes.

server2 `/tmp`: 17602306048 available bytes; 99.02% used; 110364820 free inodes.

server2 `/var/tmp`: 17602306048 available bytes; 99.02% used; 110364820 free inodes.

server2 `/mnt/raid5`: 575514800128 available bytes; 96.02% used; 444750072 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 78571831296 available bytes; 95.62% used; 114062868 free inodes.

server3 `/home`: 78571831296 available bytes; 95.62% used; 114062868 free inodes.

server3 `/data`: 1332596994048 available bytes; 81.58% used; 225763058 free inodes.

server3 `/tmp`: 78571831296 available bytes; 95.62% used; 114062868 free inodes.

server3 `/var/tmp`: 78571831296 available bytes; 95.62% used; 114062868 free inodes.
| server4 | True | ['4', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111051636736 available bytes; 93.80% used; 114372888 free inodes.

server4 `/home`: 111051636736 available bytes; 93.80% used; 114372888 free inodes.

server4 `/data`: 366095831040 available bytes; 94.94% used; 224769437 free inodes.

server4 `/tmp`: 111051636736 available bytes; 93.80% used; 114372888 free inodes.

server4 `/var/tmp`: 111051636736 available bytes; 93.80% used; 114372888 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
