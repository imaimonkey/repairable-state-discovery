# V2R cluster inventory

2026-09-27T01:37:40.868842+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315144499200 available bytes; 82.42% used; 112443373 free inodes.

server1 `/home`: 315144499200 available bytes; 82.42% used; 112443373 free inodes.

server1 `/tmp`: 315144499200 available bytes; 82.42% used; 112443373 free inodes.

server1 `/var/tmp`: 315144499200 available bytes; 82.42% used; 112443373 free inodes.

server1 `/mnt/raid5`: 637515661312 available bytes; 97.08% used; 337405522 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17628246016 available bytes; 99.02% used; 110364996 free inodes.

server2 `/home`: 17628246016 available bytes; 99.02% used; 110364996 free inodes.

server2 `/tmp`: 17628246016 available bytes; 99.02% used; 110364996 free inodes.

server2 `/var/tmp`: 17628246016 available bytes; 99.02% used; 110364996 free inodes.

server2 `/mnt/raid5`: 582466351104 available bytes; 95.98% used; 444886175 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78876352512 available bytes; 95.60% used; 114064286 free inodes.

server3 `/home`: 78876352512 available bytes; 95.60% used; 114064286 free inodes.

server3 `/data`: 1342368100352 available bytes; 81.45% used; 225763287 free inodes.

server3 `/tmp`: 78876352512 available bytes; 95.60% used; 114064286 free inodes.

server3 `/var/tmp`: 78876352512 available bytes; 95.60% used; 114064286 free inodes.
| server4 | True | ['0', '1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105869283328 available bytes; 94.09% used; 114347851 free inodes.

server4 `/home`: 105869283328 available bytes; 94.09% used; 114347851 free inodes.

server4 `/data`: 406534508544 available bytes; 94.38% used; 224782887 free inodes.

server4 `/tmp`: 105869283328 available bytes; 94.09% used; 114347851 free inodes.

server4 `/var/tmp`: 105869283328 available bytes; 94.09% used; 114347851 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
