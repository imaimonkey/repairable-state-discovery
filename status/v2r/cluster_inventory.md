# V2R cluster inventory

2026-09-24T23:14:45.810464+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319572467712 available bytes; 82.17% used; 112480818 free inodes.

server1 `/home`: 319572467712 available bytes; 82.17% used; 112480818 free inodes.

server1 `/tmp`: 319572467712 available bytes; 82.17% used; 112480818 free inodes.

server1 `/var/tmp`: 319572467712 available bytes; 82.17% used; 112480818 free inodes.

server1 `/mnt/raid5`: 415270899712 available bytes; 98.10% used; 337615008 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23120531456 available bytes; 98.71% used; 110410810 free inodes.

server2 `/home`: 23120531456 available bytes; 98.71% used; 110410810 free inodes.

server2 `/tmp`: 23120531456 available bytes; 98.71% used; 110410810 free inodes.

server2 `/var/tmp`: 23120531456 available bytes; 98.71% used; 110410810 free inodes.

server2 `/mnt/raid5`: 487153774592 available bytes; 96.63% used; 445151792 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84371537920 available bytes; 95.29% used; 114156081 free inodes.

server3 `/home`: 84371537920 available bytes; 95.29% used; 114156081 free inodes.

server3 `/data`: 148552781824 available bytes; 97.95% used; 225801215 free inodes.

server3 `/tmp`: 84371537920 available bytes; 95.29% used; 114156081 free inodes.

server3 `/var/tmp`: 84371537920 available bytes; 95.29% used; 114156081 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105800151040 available bytes; 94.10% used; 114348306 free inodes.

server4 `/home`: 105800151040 available bytes; 94.10% used; 114348306 free inodes.

server4 `/data`: 61603811328 available bytes; 99.15% used; 225169811 free inodes.

server4 `/tmp`: 105800151040 available bytes; 94.10% used; 114348306 free inodes.

server4 `/var/tmp`: 105800151040 available bytes; 94.10% used; 114348306 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
