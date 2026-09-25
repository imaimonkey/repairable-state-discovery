# V2R cluster inventory

2026-09-25T06:26:00.386171+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318880907264 available bytes; 82.21% used; 112480350 free inodes.

server1 `/home`: 318880907264 available bytes; 82.21% used; 112480350 free inodes.

server1 `/tmp`: 318880907264 available bytes; 82.21% used; 112480350 free inodes.

server1 `/var/tmp`: 318880907264 available bytes; 82.21% used; 112480350 free inodes.

server1 `/mnt/raid5`: 401441984512 available bytes; 98.16% used; 337561539 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22895116288 available bytes; 98.72% used; 110410532 free inodes.

server2 `/home`: 22895116288 available bytes; 98.72% used; 110410532 free inodes.

server2 `/tmp`: 22895116288 available bytes; 98.72% used; 110410532 free inodes.

server2 `/var/tmp`: 22895116288 available bytes; 98.72% used; 110410532 free inodes.

server2 `/mnt/raid5`: 370149347328 available bytes; 97.44% used; 445099746 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84319719424 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84319719424 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 142531756032 available bytes; 98.03% used; 225813859 free inodes.

server3 `/tmp`: 84319719424 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84319719424 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105648361472 available bytes; 94.10% used; 114350390 free inodes.

server4 `/home`: 105648361472 available bytes; 94.10% used; 114350390 free inodes.

server4 `/data`: 254602256384 available bytes; 96.48% used; 225021452 free inodes.

server4 `/tmp`: 105648361472 available bytes; 94.10% used; 114350390 free inodes.

server4 `/var/tmp`: 105648361472 available bytes; 94.10% used; 114350390 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
