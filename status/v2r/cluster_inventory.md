# V2R cluster inventory

2026-09-24T20:04:51.696972+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323990343680 available bytes; 81.93% used; 112481421 free inodes.

server1 `/home`: 323990343680 available bytes; 81.93% used; 112481421 free inodes.

server1 `/tmp`: 323990343680 available bytes; 81.93% used; 112481421 free inodes.

server1 `/var/tmp`: 323990343680 available bytes; 81.93% used; 112481421 free inodes.

server1 `/mnt/raid5`: 415541624832 available bytes; 98.09% used; 337628310 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30173941760 available bytes; 98.32% used; 110411376 free inodes.

server2 `/home`: 30173941760 available bytes; 98.32% used; 110411376 free inodes.

server2 `/tmp`: 30173941760 available bytes; 98.32% used; 110411376 free inodes.

server2 `/var/tmp`: 30173941760 available bytes; 98.32% used; 110411376 free inodes.

server2 `/mnt/raid5`: 493780512768 available bytes; 96.59% used; 445157554 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84401139712 available bytes; 95.29% used; 114156137 free inodes.

server3 `/home`: 84401139712 available bytes; 95.29% used; 114156137 free inodes.

server3 `/data`: 151847444480 available bytes; 97.90% used; 225798848 free inodes.

server3 `/tmp`: 84401139712 available bytes; 95.29% used; 114156137 free inodes.

server3 `/var/tmp`: 84401139712 available bytes; 95.29% used; 114156137 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105641594880 available bytes; 94.10% used; 114348421 free inodes.

server4 `/home`: 105641594880 available bytes; 94.10% used; 114348421 free inodes.

server4 `/data`: 89820901376 available bytes; 98.76% used; 225266350 free inodes.

server4 `/tmp`: 105641594880 available bytes; 94.10% used; 114348421 free inodes.

server4 `/var/tmp`: 105641594880 available bytes; 94.10% used; 114348421 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
