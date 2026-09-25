# V2R cluster inventory

2026-09-25T23:39:23.268664+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318673248256 available bytes; 82.22% used; 112476314 free inodes.

server1 `/home`: 318673248256 available bytes; 82.22% used; 112476314 free inodes.

server1 `/tmp`: 318673248256 available bytes; 82.22% used; 112476314 free inodes.

server1 `/var/tmp`: 318673248256 available bytes; 82.22% used; 112476314 free inodes.

server1 `/mnt/raid5`: 360097349632 available bytes; 98.35% used; 337538610 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22950977536 available bytes; 98.72% used; 110406238 free inodes.

server2 `/home`: 22950977536 available bytes; 98.72% used; 110406238 free inodes.

server2 `/tmp`: 22950977536 available bytes; 98.72% used; 110406238 free inodes.

server2 `/var/tmp`: 22950977536 available bytes; 98.72% used; 110406238 free inodes.

server2 `/mnt/raid5`: 296732565504 available bytes; 97.95% used; 445050569 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84352131072 available bytes; 95.29% used; 114152440 free inodes.

server3 `/home`: 84352131072 available bytes; 95.29% used; 114152440 free inodes.

server3 `/data`: 124802945024 available bytes; 98.28% used; 225811347 free inodes.

server3 `/tmp`: 84352131072 available bytes; 95.29% used; 114152440 free inodes.

server3 `/var/tmp`: 84352131072 available bytes; 95.29% used; 114152440 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105082859520 available bytes; 94.14% used; 114346616 free inodes.

server4 `/home`: 105082859520 available bytes; 94.14% used; 114346616 free inodes.

server4 `/data`: 178220621824 available bytes; 97.54% used; 224917593 free inodes.

server4 `/tmp`: 105082859520 available bytes; 94.14% used; 114346616 free inodes.

server4 `/var/tmp`: 105082859520 available bytes; 94.14% used; 114346616 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
