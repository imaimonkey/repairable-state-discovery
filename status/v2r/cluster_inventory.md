# V2R cluster inventory

2026-09-27T01:47:36.060929+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315160829952 available bytes; 82.42% used; 112443365 free inodes.

server1 `/home`: 315160829952 available bytes; 82.42% used; 112443365 free inodes.

server1 `/tmp`: 315160829952 available bytes; 82.42% used; 112443365 free inodes.

server1 `/var/tmp`: 315160829952 available bytes; 82.42% used; 112443365 free inodes.

server1 `/mnt/raid5`: 637483528192 available bytes; 97.08% used; 337405485 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17635532800 available bytes; 99.02% used; 110364996 free inodes.

server2 `/home`: 17635532800 available bytes; 99.02% used; 110364996 free inodes.

server2 `/tmp`: 17635532800 available bytes; 99.02% used; 110364996 free inodes.

server2 `/var/tmp`: 17635532800 available bytes; 99.02% used; 110364996 free inodes.

server2 `/mnt/raid5`: 582183759872 available bytes; 95.98% used; 444885639 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78726397952 available bytes; 95.61% used; 114063254 free inodes.

server3 `/home`: 78726397952 available bytes; 95.61% used; 114063254 free inodes.

server3 `/data`: 1341903982592 available bytes; 81.45% used; 225762974 free inodes.

server3 `/tmp`: 78726397952 available bytes; 95.61% used; 114063254 free inodes.

server3 `/var/tmp`: 78726397952 available bytes; 95.61% used; 114063254 free inodes.
| server4 | True | ['0', '1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105869025280 available bytes; 94.09% used; 114347846 free inodes.

server4 `/home`: 105869025280 available bytes; 94.09% used; 114347846 free inodes.

server4 `/data`: 406915407872 available bytes; 94.38% used; 224782924 free inodes.

server4 `/tmp`: 105869025280 available bytes; 94.09% used; 114347846 free inodes.

server4 `/var/tmp`: 105869025280 available bytes; 94.09% used; 114347846 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
