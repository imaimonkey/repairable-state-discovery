# V2R cluster inventory

2026-09-24T23:16:18.002247+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319023366144 available bytes; 82.20% used; 112480809 free inodes.

server1 `/home`: 319023366144 available bytes; 82.20% used; 112480809 free inodes.

server1 `/tmp`: 319023366144 available bytes; 82.20% used; 112480809 free inodes.

server1 `/var/tmp`: 319023366144 available bytes; 82.20% used; 112480809 free inodes.

server1 `/mnt/raid5`: 415263989760 available bytes; 98.10% used; 337614819 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23120224256 available bytes; 98.71% used; 110410812 free inodes.

server2 `/home`: 23120224256 available bytes; 98.71% used; 110410812 free inodes.

server2 `/tmp`: 23120224256 available bytes; 98.71% used; 110410812 free inodes.

server2 `/var/tmp`: 23120224256 available bytes; 98.71% used; 110410812 free inodes.

server2 `/mnt/raid5`: 487108251648 available bytes; 96.63% used; 445151664 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84374593536 available bytes; 95.29% used; 114156083 free inodes.

server3 `/home`: 84374593536 available bytes; 95.29% used; 114156083 free inodes.

server3 `/data`: 148515889152 available bytes; 97.95% used; 225801192 free inodes.

server3 `/tmp`: 84374593536 available bytes; 95.29% used; 114156083 free inodes.

server3 `/var/tmp`: 84374593536 available bytes; 95.29% used; 114156083 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105800097792 available bytes; 94.10% used; 114348306 free inodes.

server4 `/home`: 105800097792 available bytes; 94.10% used; 114348306 free inodes.

server4 `/data`: 61577216000 available bytes; 99.15% used; 225167488 free inodes.

server4 `/tmp`: 105800097792 available bytes; 94.10% used; 114348306 free inodes.

server4 `/var/tmp`: 105800097792 available bytes; 94.10% used; 114348306 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
