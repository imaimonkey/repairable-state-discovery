# V2R cluster inventory

2026-09-27T08:19:47.401920+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314469773312 available bytes; 82.46% used; 112440802 free inodes.

server1 `/home`: 314469773312 available bytes; 82.46% used; 112440802 free inodes.

server1 `/tmp`: 314469773312 available bytes; 82.46% used; 112440802 free inodes.

server1 `/var/tmp`: 314469773312 available bytes; 82.46% used; 112440802 free inodes.

server1 `/mnt/raid5`: 634647351296 available bytes; 97.09% used; 337400004 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 17608228864 available bytes; 99.02% used; 110365014 free inodes.

server2 `/home`: 17608228864 available bytes; 99.02% used; 110365014 free inodes.

server2 `/tmp`: 17608228864 available bytes; 99.02% used; 110365014 free inodes.

server2 `/var/tmp`: 17608228864 available bytes; 99.02% used; 110365014 free inodes.

server2 `/mnt/raid5`: 578248671232 available bytes; 96.00% used; 444873167 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78571315200 available bytes; 95.62% used; 114062868 free inodes.

server3 `/home`: 78571315200 available bytes; 95.62% used; 114062868 free inodes.

server3 `/data`: 1332707368960 available bytes; 81.58% used; 225763464 free inodes.

server3 `/tmp`: 78571315200 available bytes; 95.62% used; 114062868 free inodes.

server3 `/var/tmp`: 78571315200 available bytes; 95.62% used; 114062868 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111052455936 available bytes; 93.80% used; 114372881 free inodes.

server4 `/home`: 111052455936 available bytes; 93.80% used; 114372881 free inodes.

server4 `/data`: 368333602816 available bytes; 94.91% used; 224770894 free inodes.

server4 `/tmp`: 111052455936 available bytes; 93.80% used; 114372881 free inodes.

server4 `/var/tmp`: 111052455936 available bytes; 93.80% used; 114372881 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
