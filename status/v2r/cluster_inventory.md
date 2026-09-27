# V2R cluster inventory

2026-09-27T01:51:23.264310+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315160006656 available bytes; 82.42% used; 112443365 free inodes.

server1 `/home`: 315160006656 available bytes; 82.42% used; 112443365 free inodes.

server1 `/tmp`: 315160006656 available bytes; 82.42% used; 112443365 free inodes.

server1 `/var/tmp`: 315160006656 available bytes; 82.42% used; 112443365 free inodes.

server1 `/mnt/raid5`: 637480804352 available bytes; 97.08% used; 337405470 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17636134912 available bytes; 99.02% used; 110364996 free inodes.

server2 `/home`: 17636134912 available bytes; 99.02% used; 110364996 free inodes.

server2 `/tmp`: 17636134912 available bytes; 99.02% used; 110364996 free inodes.

server2 `/var/tmp`: 17636134912 available bytes; 99.02% used; 110364996 free inodes.

server2 `/mnt/raid5`: 582089228288 available bytes; 95.98% used; 444886038 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78717550592 available bytes; 95.61% used; 114062953 free inodes.

server3 `/home`: 78717550592 available bytes; 95.61% used; 114062953 free inodes.

server3 `/data`: 1339816275968 available bytes; 81.48% used; 225762856 free inodes.

server3 `/tmp`: 78717550592 available bytes; 95.61% used; 114062953 free inodes.

server3 `/var/tmp`: 78717550592 available bytes; 95.61% used; 114062953 free inodes.
| server4 | True | ['0', '1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105868931072 available bytes; 94.09% used; 114347846 free inodes.

server4 `/home`: 105868931072 available bytes; 94.09% used; 114347846 free inodes.

server4 `/data`: 406911332352 available bytes; 94.38% used; 224782903 free inodes.

server4 `/tmp`: 105868931072 available bytes; 94.09% used; 114347846 free inodes.

server4 `/var/tmp`: 105868931072 available bytes; 94.09% used; 114347846 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
