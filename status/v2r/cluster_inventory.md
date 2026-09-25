# V2R cluster inventory

2026-09-25T12:25:11.468031+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319125032960 available bytes; 82.20% used; 112477609 free inodes.

server1 `/home`: 319125032960 available bytes; 82.20% used; 112477609 free inodes.

server1 `/tmp`: 319125032960 available bytes; 82.20% used; 112477609 free inodes.

server1 `/var/tmp`: 319125032960 available bytes; 82.20% used; 112477609 free inodes.

server1 `/mnt/raid5`: 364257198080 available bytes; 98.33% used; 337548190 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 22902960128 available bytes; 98.72% used; 110409959 free inodes.

server2 `/home`: 22902960128 available bytes; 98.72% used; 110409959 free inodes.

server2 `/tmp`: 22902960128 available bytes; 98.72% used; 110409959 free inodes.

server2 `/var/tmp`: 22902960128 available bytes; 98.72% used; 110409959 free inodes.

server2 `/mnt/raid5`: 325181947904 available bytes; 97.75% used; 445079990 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84210880512 available bytes; 95.30% used; 114154978 free inodes.

server3 `/home`: 84210880512 available bytes; 95.30% used; 114154978 free inodes.

server3 `/data`: 142277885952 available bytes; 98.03% used; 225811289 free inodes.

server3 `/tmp`: 84210880512 available bytes; 95.30% used; 114154978 free inodes.

server3 `/var/tmp`: 84210880512 available bytes; 95.30% used; 114154978 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105666285568 available bytes; 94.10% used; 114349722 free inodes.

server4 `/home`: 105666285568 available bytes; 94.10% used; 114349722 free inodes.

server4 `/data`: 232030187520 available bytes; 96.79% used; 224965163 free inodes.

server4 `/tmp`: 105666285568 available bytes; 94.10% used; 114349722 free inodes.

server4 `/var/tmp`: 105666285568 available bytes; 94.10% used; 114349722 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
