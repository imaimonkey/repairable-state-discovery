# V2R cluster inventory

2026-09-24T20:15:39.961233+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323988729856 available bytes; 81.93% used; 112481427 free inodes.

server1 `/home`: 323988729856 available bytes; 81.93% used; 112481427 free inodes.

server1 `/tmp`: 323988729856 available bytes; 81.93% used; 112481427 free inodes.

server1 `/var/tmp`: 323988729856 available bytes; 81.93% used; 112481427 free inodes.

server1 `/mnt/raid5`: 415521558528 available bytes; 98.09% used; 337627049 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30177349632 available bytes; 98.32% used; 110411376 free inodes.

server2 `/home`: 30177349632 available bytes; 98.32% used; 110411376 free inodes.

server2 `/tmp`: 30177349632 available bytes; 98.32% used; 110411376 free inodes.

server2 `/var/tmp`: 30177349632 available bytes; 98.32% used; 110411376 free inodes.

server2 `/mnt/raid5`: 492997296128 available bytes; 96.59% used; 445157261 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84398768128 available bytes; 95.29% used; 114156113 free inodes.

server3 `/home`: 84398768128 available bytes; 95.29% used; 114156113 free inodes.

server3 `/data`: 151662866432 available bytes; 97.90% used; 225798654 free inodes.

server3 `/tmp`: 84398768128 available bytes; 95.29% used; 114156113 free inodes.

server3 `/var/tmp`: 84398768128 available bytes; 95.29% used; 114156113 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105641123840 available bytes; 94.10% used; 114348411 free inodes.

server4 `/home`: 105641123840 available bytes; 94.10% used; 114348411 free inodes.

server4 `/data`: 89772191744 available bytes; 98.76% used; 225265889 free inodes.

server4 `/tmp`: 105641123840 available bytes; 94.10% used; 114348411 free inodes.

server4 `/var/tmp`: 105641123840 available bytes; 94.10% used; 114348411 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
