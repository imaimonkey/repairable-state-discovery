# V2R cluster inventory

2026-09-24T23:27:04.562195+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319013998592 available bytes; 82.20% used; 112480779 free inodes.

server1 `/home`: 319013998592 available bytes; 82.20% used; 112480779 free inodes.

server1 `/tmp`: 319013998592 available bytes; 82.20% used; 112480779 free inodes.

server1 `/var/tmp`: 319013998592 available bytes; 82.20% used; 112480779 free inodes.

server1 `/mnt/raid5`: 415239110656 available bytes; 98.10% used; 337613570 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23110955008 available bytes; 98.71% used; 110410804 free inodes.

server2 `/home`: 23110955008 available bytes; 98.71% used; 110410804 free inodes.

server2 `/tmp`: 23110955008 available bytes; 98.71% used; 110410804 free inodes.

server2 `/var/tmp`: 23110955008 available bytes; 98.71% used; 110410804 free inodes.

server2 `/mnt/raid5`: 486496903168 available bytes; 96.64% used; 445151393 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84369408000 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84369408000 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 148330729472 available bytes; 97.95% used; 225800963 free inodes.

server3 `/tmp`: 84369408000 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84369408000 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105799663616 available bytes; 94.10% used; 114348305 free inodes.

server4 `/home`: 105799663616 available bytes; 94.10% used; 114348305 free inodes.

server4 `/data`: 61389537280 available bytes; 99.15% used; 225151854 free inodes.

server4 `/tmp`: 105799663616 available bytes; 94.10% used; 114348305 free inodes.

server4 `/var/tmp`: 105799663616 available bytes; 94.10% used; 114348305 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
