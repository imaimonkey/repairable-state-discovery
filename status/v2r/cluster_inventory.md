# V2R cluster inventory

2026-09-25T05:05:20.663373+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318900445184 available bytes; 82.21% used; 112480332 free inodes.

server1 `/home`: 318900445184 available bytes; 82.21% used; 112480332 free inodes.

server1 `/tmp`: 318900445184 available bytes; 82.21% used; 112480332 free inodes.

server1 `/var/tmp`: 318900445184 available bytes; 82.21% used; 112480332 free inodes.

server1 `/mnt/raid5`: 408616525824 available bytes; 98.13% used; 337571411 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22931542016 available bytes; 98.72% used; 110410438 free inodes.

server2 `/home`: 22931542016 available bytes; 98.72% used; 110410438 free inodes.

server2 `/tmp`: 22931542016 available bytes; 98.72% used; 110410438 free inodes.

server2 `/var/tmp`: 22931542016 available bytes; 98.72% used; 110410438 free inodes.

server2 `/mnt/raid5`: 461947375616 available bytes; 96.81% used; 445109247 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84340289536 available bytes; 95.29% used; 114156078 free inodes.

server3 `/home`: 84340289536 available bytes; 95.29% used; 114156078 free inodes.

server3 `/data`: 142870650880 available bytes; 98.03% used; 225815452 free inodes.

server3 `/tmp`: 84340289536 available bytes; 95.29% used; 114156078 free inodes.

server3 `/var/tmp`: 84340289536 available bytes; 95.29% used; 114156078 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105659203584 available bytes; 94.10% used; 114350405 free inodes.

server4 `/home`: 105659203584 available bytes; 94.10% used; 114350405 free inodes.

server4 `/data`: 27936100352 available bytes; 99.61% used; 224960940 free inodes.

server4 `/tmp`: 105659203584 available bytes; 94.10% used; 114350405 free inodes.

server4 `/var/tmp`: 105659203584 available bytes; 94.10% used; 114350405 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
