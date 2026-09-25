# V2R cluster inventory

2026-09-25T04:44:29.995629+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318914457600 available bytes; 82.21% used; 112480347 free inodes.

server1 `/home`: 318914457600 available bytes; 82.21% used; 112480347 free inodes.

server1 `/tmp`: 318914457600 available bytes; 82.21% used; 112480347 free inodes.

server1 `/var/tmp`: 318914457600 available bytes; 82.21% used; 112480347 free inodes.

server1 `/mnt/raid5`: 408691789824 available bytes; 98.13% used; 337589937 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22948466688 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22948466688 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22948466688 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22948466688 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 462579187712 available bytes; 96.80% used; 445109285 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84340154368 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84340154368 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 143281954816 available bytes; 98.02% used; 225815869 free inodes.

server3 `/tmp`: 84340154368 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84340154368 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105663897600 available bytes; 94.10% used; 114350594 free inodes.

server4 `/home`: 105663897600 available bytes; 94.10% used; 114350594 free inodes.

server4 `/data`: 31170166784 available bytes; 99.57% used; 224962180 free inodes.

server4 `/tmp`: 105663897600 available bytes; 94.10% used; 114350594 free inodes.

server4 `/var/tmp`: 105663897600 available bytes; 94.10% used; 114350594 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
