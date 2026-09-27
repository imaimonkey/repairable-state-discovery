# V2R cluster inventory

2026-09-27T01:49:51.917090+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315160596480 available bytes; 82.42% used; 112443365 free inodes.

server1 `/home`: 315160596480 available bytes; 82.42% used; 112443365 free inodes.

server1 `/tmp`: 315160596480 available bytes; 82.42% used; 112443365 free inodes.

server1 `/var/tmp`: 315160596480 available bytes; 82.42% used; 112443365 free inodes.

server1 `/mnt/raid5`: 637479305216 available bytes; 97.08% used; 337405468 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17636704256 available bytes; 99.02% used; 110364998 free inodes.

server2 `/home`: 17636704256 available bytes; 99.02% used; 110364998 free inodes.

server2 `/tmp`: 17636704256 available bytes; 99.02% used; 110364998 free inodes.

server2 `/var/tmp`: 17636704256 available bytes; 99.02% used; 110364998 free inodes.

server2 `/mnt/raid5`: 582144442368 available bytes; 95.98% used; 444886219 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78717968384 available bytes; 95.61% used; 114062957 free inodes.

server3 `/home`: 78717968384 available bytes; 95.61% used; 114062957 free inodes.

server3 `/data`: 1339827716096 available bytes; 81.48% used; 225762884 free inodes.

server3 `/tmp`: 78717968384 available bytes; 95.61% used; 114062957 free inodes.

server3 `/var/tmp`: 78717968384 available bytes; 95.61% used; 114062957 free inodes.
| server4 | True | ['0', '1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105868972032 available bytes; 94.09% used; 114347846 free inodes.

server4 `/home`: 105868972032 available bytes; 94.09% used; 114347846 free inodes.

server4 `/data`: 406913036288 available bytes; 94.38% used; 224782903 free inodes.

server4 `/tmp`: 105868972032 available bytes; 94.09% used; 114347846 free inodes.

server4 `/var/tmp`: 105868972032 available bytes; 94.09% used; 114347846 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
