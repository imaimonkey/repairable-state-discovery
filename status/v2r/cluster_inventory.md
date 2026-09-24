# V2R cluster inventory

2026-09-24T03:05:03.025671+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325369974784 available bytes; 81.85% used; 112498486 free inodes.

server1 `/home`: 325369974784 available bytes; 81.85% used; 112498486 free inodes.

server1 `/tmp`: 325369974784 available bytes; 81.85% used; 112498486 free inodes.

server1 `/var/tmp`: 325369974784 available bytes; 81.85% used; 112498486 free inodes.

server1 `/mnt/raid5`: 498374541312 available bytes; 97.71% used; 337732326 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40860348416 available bytes; 97.72% used; 110431288 free inodes.

server2 `/home`: 40860348416 available bytes; 97.72% used; 110431288 free inodes.

server2 `/tmp`: 40860348416 available bytes; 97.72% used; 110431288 free inodes.

server2 `/var/tmp`: 40860348416 available bytes; 97.72% used; 110431288 free inodes.

server2 `/mnt/raid5`: 527388246016 available bytes; 96.36% used; 445198424 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292478038016 available bytes; 83.68% used; 114205097 free inodes.

server3 `/home`: 292478038016 available bytes; 83.68% used; 114205097 free inodes.

server3 `/data`: 39698300928 available bytes; 99.45% used; 225845267 free inodes.

server3 `/tmp`: 292478038016 available bytes; 83.68% used; 114205097 free inodes.

server3 `/var/tmp`: 292478038016 available bytes; 83.68% used; 114205097 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105988239360 available bytes; 94.09% used; 114349629 free inodes.

server4 `/home`: 105988239360 available bytes; 94.09% used; 114349629 free inodes.

server4 `/data`: 289711730688 available bytes; 96.00% used; 225386869 free inodes.

server4 `/tmp`: 105988239360 available bytes; 94.09% used; 114349629 free inodes.

server4 `/var/tmp`: 105988239360 available bytes; 94.09% used; 114349629 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
