# V2R cluster inventory

2026-09-25T04:53:41.955059+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318906544128 available bytes; 82.21% used; 112480350 free inodes.

server1 `/home`: 318906544128 available bytes; 82.21% used; 112480350 free inodes.

server1 `/tmp`: 318906544128 available bytes; 82.21% used; 112480350 free inodes.

server1 `/var/tmp`: 318906544128 available bytes; 82.21% used; 112480350 free inodes.

server1 `/mnt/raid5`: 408667435008 available bytes; 98.13% used; 337588810 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22939901952 available bytes; 98.72% used; 110410438 free inodes.

server2 `/home`: 22939901952 available bytes; 98.72% used; 110410438 free inodes.

server2 `/tmp`: 22939901952 available bytes; 98.72% used; 110410438 free inodes.

server2 `/var/tmp`: 22939901952 available bytes; 98.72% used; 110410438 free inodes.

server2 `/mnt/raid5`: 462310559744 available bytes; 96.81% used; 445109208 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340568064 available bytes; 95.29% used; 114156078 free inodes.

server3 `/home`: 84340568064 available bytes; 95.29% used; 114156078 free inodes.

server3 `/data`: 143069069312 available bytes; 98.02% used; 225815683 free inodes.

server3 `/tmp`: 84340568064 available bytes; 95.29% used; 114156078 free inodes.

server3 `/var/tmp`: 84340568064 available bytes; 95.29% used; 114156078 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105659555840 available bytes; 94.10% used; 114350406 free inodes.

server4 `/home`: 105659555840 available bytes; 94.10% used; 114350406 free inodes.

server4 `/data`: 27944562688 available bytes; 99.61% used; 224961595 free inodes.

server4 `/tmp`: 105659555840 available bytes; 94.10% used; 114350406 free inodes.

server4 `/var/tmp`: 105659555840 available bytes; 94.10% used; 114350406 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
