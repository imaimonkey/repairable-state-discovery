# V2R cluster inventory

2026-09-27T01:59:47.725536+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315162890240 available bytes; 82.42% used; 112443359 free inodes.

server1 `/home`: 315162890240 available bytes; 82.42% used; 112443359 free inodes.

server1 `/tmp`: 315162890240 available bytes; 82.42% used; 112443359 free inodes.

server1 `/var/tmp`: 315162890240 available bytes; 82.42% used; 112443359 free inodes.

server1 `/mnt/raid5`: 637479616512 available bytes; 97.08% used; 337405470 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17636401152 available bytes; 99.02% used; 110364998 free inodes.

server2 `/home`: 17636401152 available bytes; 99.02% used; 110364998 free inodes.

server2 `/tmp`: 17636401152 available bytes; 99.02% used; 110364998 free inodes.

server2 `/var/tmp`: 17636401152 available bytes; 99.02% used; 110364998 free inodes.

server2 `/mnt/raid5`: 581857325056 available bytes; 95.98% used; 444885681 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78715756544 available bytes; 95.61% used; 114062955 free inodes.

server3 `/home`: 78715756544 available bytes; 95.61% used; 114062955 free inodes.

server3 `/data`: 1338781614080 available bytes; 81.50% used; 225762761 free inodes.

server3 `/tmp`: 78715756544 available bytes; 95.61% used; 114062955 free inodes.

server3 `/var/tmp`: 78715756544 available bytes; 95.61% used; 114062955 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105860046848 available bytes; 94.09% used; 114347780 free inodes.

server4 `/home`: 105860046848 available bytes; 94.09% used; 114347780 free inodes.

server4 `/data`: 403700834304 available bytes; 94.42% used; 224782804 free inodes.

server4 `/tmp`: 105860046848 available bytes; 94.09% used; 114347780 free inodes.

server4 `/var/tmp`: 105860046848 available bytes; 94.09% used; 114347780 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
