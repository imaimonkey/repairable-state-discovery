# V2R cluster inventory

2026-09-25T01:02:36.573617+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319077949440 available bytes; 82.20% used; 112480777 free inodes.

server1 `/home`: 319077949440 available bytes; 82.20% used; 112480777 free inodes.

server1 `/tmp`: 319077949440 available bytes; 82.20% used; 112480777 free inodes.

server1 `/var/tmp`: 319077949440 available bytes; 82.20% used; 112480777 free inodes.

server1 `/mnt/raid5`: 416790212608 available bytes; 98.09% used; 337616173 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23066681344 available bytes; 98.71% used; 110410764 free inodes.

server2 `/home`: 23066681344 available bytes; 98.71% used; 110410764 free inodes.

server2 `/tmp`: 23066681344 available bytes; 98.71% used; 110410764 free inodes.

server2 `/var/tmp`: 23066681344 available bytes; 98.71% used; 110410764 free inodes.

server2 `/mnt/raid5`: 497803268096 available bytes; 96.56% used; 445162484 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84354572288 available bytes; 95.29% used; 114156085 free inodes.

server3 `/home`: 84354572288 available bytes; 95.29% used; 114156085 free inodes.

server3 `/data`: 148345536512 available bytes; 97.95% used; 225812836 free inodes.

server3 `/tmp`: 84354572288 available bytes; 95.29% used; 114156085 free inodes.

server3 `/var/tmp`: 84354572288 available bytes; 95.29% used; 114156085 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105788084224 available bytes; 94.10% used; 114348302 free inodes.

server4 `/home`: 105788084224 available bytes; 94.10% used; 114348302 free inodes.

server4 `/data`: 55161077760 available bytes; 99.24% used; 225031053 free inodes.

server4 `/tmp`: 105788084224 available bytes; 94.10% used; 114348302 free inodes.

server4 `/var/tmp`: 105788084224 available bytes; 94.10% used; 114348302 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
