# V2R cluster inventory

2026-09-25T04:57:41.323044+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318906736640 available bytes; 82.21% used; 112480355 free inodes.

server1 `/home`: 318906736640 available bytes; 82.21% used; 112480355 free inodes.

server1 `/tmp`: 318906736640 available bytes; 82.21% used; 112480355 free inodes.

server1 `/var/tmp`: 318906736640 available bytes; 82.21% used; 112480355 free inodes.

server1 `/mnt/raid5`: 408657039360 available bytes; 98.13% used; 337588336 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22938427392 available bytes; 98.72% used; 110410438 free inodes.

server2 `/home`: 22938427392 available bytes; 98.72% used; 110410438 free inodes.

server2 `/tmp`: 22938427392 available bytes; 98.72% used; 110410438 free inodes.

server2 `/var/tmp`: 22938427392 available bytes; 98.72% used; 110410438 free inodes.

server2 `/mnt/raid5`: 462182031360 available bytes; 96.81% used; 445108950 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84341460992 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84341460992 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 143003746304 available bytes; 98.02% used; 225815604 free inodes.

server3 `/tmp`: 84341460992 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84341460992 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105659457536 available bytes; 94.10% used; 114350405 free inodes.

server4 `/home`: 105659457536 available bytes; 94.10% used; 114350405 free inodes.

server4 `/data`: 27942473728 available bytes; 99.61% used; 224961309 free inodes.

server4 `/tmp`: 105659457536 available bytes; 94.10% used; 114350405 free inodes.

server4 `/var/tmp`: 105659457536 available bytes; 94.10% used; 114350405 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
