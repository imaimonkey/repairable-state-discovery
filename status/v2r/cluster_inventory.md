# V2R cluster inventory

2026-09-24T23:08:34.371596+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 320321081344 available bytes; 82.13% used; 112480848 free inodes.

server1 `/home`: 320321081344 available bytes; 82.13% used; 112480848 free inodes.

server1 `/tmp`: 320321081344 available bytes; 82.13% used; 112480848 free inodes.

server1 `/var/tmp`: 320321081344 available bytes; 82.13% used; 112480848 free inodes.

server1 `/mnt/raid5`: 415280926720 available bytes; 98.09% used; 337615725 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23122968576 available bytes; 98.71% used; 110410804 free inodes.

server2 `/home`: 23122968576 available bytes; 98.71% used; 110410804 free inodes.

server2 `/tmp`: 23122968576 available bytes; 98.71% used; 110410804 free inodes.

server2 `/var/tmp`: 23122968576 available bytes; 98.71% used; 110410804 free inodes.

server2 `/mnt/raid5`: 487345123328 available bytes; 96.63% used; 445151818 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84369600512 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84369600512 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 148634497024 available bytes; 97.95% used; 225801327 free inodes.

server3 `/tmp`: 84369600512 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84369600512 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105800617984 available bytes; 94.10% used; 114348311 free inodes.

server4 `/home`: 105800617984 available bytes; 94.10% used; 114348311 free inodes.

server4 `/data`: 61848051712 available bytes; 99.15% used; 225179070 free inodes.

server4 `/tmp`: 105800617984 available bytes; 94.10% used; 114348311 free inodes.

server4 `/var/tmp`: 105800617984 available bytes; 94.10% used; 114348311 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
