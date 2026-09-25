# V2R cluster inventory

2026-09-25T01:04:09.689728+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319077908480 available bytes; 82.20% used; 112480777 free inodes.

server1 `/home`: 319077908480 available bytes; 82.20% used; 112480777 free inodes.

server1 `/tmp`: 319077908480 available bytes; 82.20% used; 112480777 free inodes.

server1 `/var/tmp`: 319077908480 available bytes; 82.20% used; 112480777 free inodes.

server1 `/mnt/raid5`: 416784613376 available bytes; 98.09% used; 337615985 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 23066529792 available bytes; 98.71% used; 110410768 free inodes.

server2 `/home`: 23066529792 available bytes; 98.71% used; 110410768 free inodes.

server2 `/tmp`: 23066529792 available bytes; 98.71% used; 110410768 free inodes.

server2 `/var/tmp`: 23066529792 available bytes; 98.71% used; 110410768 free inodes.

server2 `/mnt/raid5`: 498356240384 available bytes; 96.56% used; 445162332 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84354076672 available bytes; 95.29% used; 114156085 free inodes.

server3 `/home`: 84354076672 available bytes; 95.29% used; 114156085 free inodes.

server3 `/data`: 148319158272 available bytes; 97.95% used; 225812795 free inodes.

server3 `/tmp`: 84354076672 available bytes; 95.29% used; 114156085 free inodes.

server3 `/var/tmp`: 84354076672 available bytes; 95.29% used; 114156085 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105788039168 available bytes; 94.10% used; 114348301 free inodes.

server4 `/home`: 105788039168 available bytes; 94.10% used; 114348301 free inodes.

server4 `/data`: 54609281024 available bytes; 99.25% used; 225031009 free inodes.

server4 `/tmp`: 105788039168 available bytes; 94.10% used; 114348301 free inodes.

server4 `/var/tmp`: 105788039168 available bytes; 94.10% used; 114348301 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
