# V2R cluster inventory

2026-09-25T12:28:15.138470+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319123853312 available bytes; 82.20% used; 112477610 free inodes.

server1 `/home`: 319123853312 available bytes; 82.20% used; 112477610 free inodes.

server1 `/tmp`: 319123853312 available bytes; 82.20% used; 112477610 free inodes.

server1 `/var/tmp`: 319123853312 available bytes; 82.20% used; 112477610 free inodes.

server1 `/mnt/raid5`: 371392376832 available bytes; 98.30% used; 337548261 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 22901903360 available bytes; 98.72% used; 110409959 free inodes.

server2 `/home`: 22901903360 available bytes; 98.72% used; 110409959 free inodes.

server2 `/tmp`: 22901903360 available bytes; 98.72% used; 110409959 free inodes.

server2 `/var/tmp`: 22901903360 available bytes; 98.72% used; 110409959 free inodes.

server2 `/mnt/raid5`: 304441798656 available bytes; 97.90% used; 445079728 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84213768192 available bytes; 95.30% used; 114154978 free inodes.

server3 `/home`: 84213768192 available bytes; 95.30% used; 114154978 free inodes.

server3 `/data`: 142281203712 available bytes; 98.03% used; 225811238 free inodes.

server3 `/tmp`: 84213768192 available bytes; 95.30% used; 114154978 free inodes.

server3 `/var/tmp`: 84213768192 available bytes; 95.30% used; 114154978 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105666215936 available bytes; 94.10% used; 114349722 free inodes.

server4 `/home`: 105666215936 available bytes; 94.10% used; 114349722 free inodes.

server4 `/data`: 232028565504 available bytes; 96.79% used; 224964769 free inodes.

server4 `/tmp`: 105666215936 available bytes; 94.10% used; 114349722 free inodes.

server4 `/var/tmp`: 105666215936 available bytes; 94.10% used; 114349722 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
