# V2R cluster inventory

2026-09-27T01:55:13.350048+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315162828800 available bytes; 82.42% used; 112443371 free inodes.

server1 `/home`: 315162828800 available bytes; 82.42% used; 112443371 free inodes.

server1 `/tmp`: 315162828800 available bytes; 82.42% used; 112443371 free inodes.

server1 `/var/tmp`: 315162828800 available bytes; 82.42% used; 112443371 free inodes.

server1 `/mnt/raid5`: 637480361984 available bytes; 97.08% used; 337405470 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17635373056 available bytes; 99.02% used; 110364998 free inodes.

server2 `/home`: 17635373056 available bytes; 99.02% used; 110364998 free inodes.

server2 `/tmp`: 17635373056 available bytes; 99.02% used; 110364998 free inodes.

server2 `/var/tmp`: 17635373056 available bytes; 99.02% used; 110364998 free inodes.

server2 `/mnt/raid5`: 581447983104 available bytes; 95.98% used; 444885803 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78716911616 available bytes; 95.61% used; 114062955 free inodes.

server3 `/home`: 78716911616 available bytes; 95.61% used; 114062955 free inodes.

server3 `/data`: 1338784518144 available bytes; 81.50% used; 225762805 free inodes.

server3 `/tmp`: 78716911616 available bytes; 95.61% used; 114062955 free inodes.

server3 `/var/tmp`: 78716911616 available bytes; 95.61% used; 114062955 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105860321280 available bytes; 94.09% used; 114347817 free inodes.

server4 `/home`: 105860321280 available bytes; 94.09% used; 114347817 free inodes.

server4 `/data`: 403704950784 available bytes; 94.42% used; 224782843 free inodes.

server4 `/tmp`: 105860321280 available bytes; 94.09% used; 114347817 free inodes.

server4 `/var/tmp`: 105860321280 available bytes; 94.09% used; 114347817 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
