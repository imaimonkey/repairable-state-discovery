# V2R cluster inventory

2026-09-24T23:11:40.329857+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 320268959744 available bytes; 82.13% used; 112480845 free inodes.

server1 `/home`: 320268959744 available bytes; 82.13% used; 112480845 free inodes.

server1 `/tmp`: 320268959744 available bytes; 82.13% used; 112480845 free inodes.

server1 `/var/tmp`: 320268959744 available bytes; 82.13% used; 112480845 free inodes.

server1 `/mnt/raid5`: 415274151936 available bytes; 98.09% used; 337615359 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23121203200 available bytes; 98.71% used; 110410804 free inodes.

server2 `/home`: 23121203200 available bytes; 98.71% used; 110410804 free inodes.

server2 `/tmp`: 23121203200 available bytes; 98.71% used; 110410804 free inodes.

server2 `/var/tmp`: 23121203200 available bytes; 98.71% used; 110410804 free inodes.

server2 `/mnt/raid5`: 487252463616 available bytes; 96.63% used; 445152000 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84372176896 available bytes; 95.29% used; 114156081 free inodes.

server3 `/home`: 84372176896 available bytes; 95.29% used; 114156081 free inodes.

server3 `/data`: 148601380864 available bytes; 97.95% used; 225801273 free inodes.

server3 `/tmp`: 84372176896 available bytes; 95.29% used; 114156081 free inodes.

server3 `/var/tmp`: 84372176896 available bytes; 95.29% used; 114156081 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105800253440 available bytes; 94.10% used; 114348309 free inodes.

server4 `/home`: 105800253440 available bytes; 94.10% used; 114348309 free inodes.

server4 `/data`: 61794455552 available bytes; 99.15% used; 225174283 free inodes.

server4 `/tmp`: 105800253440 available bytes; 94.10% used; 114348309 free inodes.

server4 `/var/tmp`: 105800253440 available bytes; 94.10% used; 114348309 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
