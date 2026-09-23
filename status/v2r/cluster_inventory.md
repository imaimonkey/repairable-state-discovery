# V2R cluster inventory

2026-09-23T22:21:20.758793+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325708398592 available bytes; 81.83% used; 112501403 free inodes.

server1 `/home`: 325708398592 available bytes; 81.83% used; 112501403 free inodes.

server1 `/tmp`: 325708398592 available bytes; 81.83% used; 112501403 free inodes.

server1 `/var/tmp`: 325708398592 available bytes; 81.83% used; 112501403 free inodes.

server1 `/mnt/raid5`: 1388103110656 available bytes; 93.63% used; 337739849 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41091457024 available bytes; 97.71% used; 110432646 free inodes.

server2 `/home`: 41091457024 available bytes; 97.71% used; 110432646 free inodes.

server2 `/tmp`: 41091457024 available bytes; 97.71% used; 110432646 free inodes.

server2 `/var/tmp`: 41091457024 available bytes; 97.71% used; 110432646 free inodes.

server2 `/mnt/raid5`: 536420397056 available bytes; 96.29% used; 445207266 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292712861696 available bytes; 83.67% used; 114201909 free inodes.

server3 `/home`: 292712861696 available bytes; 83.67% used; 114201909 free inodes.

server3 `/data`: 82437992448 available bytes; 98.86% used; 225847505 free inodes.

server3 `/tmp`: 292710764544 available bytes; 83.67% used; 114201909 free inodes.

server3 `/var/tmp`: 292710764544 available bytes; 83.67% used; 114201909 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106402091008 available bytes; 94.06% used; 114354859 free inodes.

server4 `/home`: 106402091008 available bytes; 94.06% used; 114354859 free inodes.

server4 `/data`: 300105129984 available bytes; 95.85% used; 225439140 free inodes.

server4 `/tmp`: 106402091008 available bytes; 94.06% used; 114354859 free inodes.

server4 `/var/tmp`: 106402091008 available bytes; 94.06% used; 114354859 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
