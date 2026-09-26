# V2R cluster inventory

2026-09-26T15:07:15.173505+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318165471232 available bytes; 82.25% used; 112473929 free inodes.

server1 `/home`: 318165471232 available bytes; 82.25% used; 112473929 free inodes.

server1 `/tmp`: 318165471232 available bytes; 82.25% used; 112473929 free inodes.

server1 `/var/tmp`: 318165471232 available bytes; 82.25% used; 112473929 free inodes.

server1 `/mnt/raid5`: 654240780288 available bytes; 97.00% used; 337531860 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 42024960 available bytes; 100.00% used; 110367040 free inodes.

server2 `/home`: 42024960 available bytes; 100.00% used; 110367040 free inodes.

server2 `/tmp`: 42024960 available bytes; 100.00% used; 110367040 free inodes.

server2 `/var/tmp`: 42024960 available bytes; 100.00% used; 110367040 free inodes.

server2 `/mnt/raid5`: 615478812672 available bytes; 95.75% used; 444973145 free inodes.
| server3 | True | [] | [] |

server3 `/`: 83163168768 available bytes; 95.36% used; 114139295 free inodes.

server3 `/home`: 83163168768 available bytes; 95.36% used; 114139295 free inodes.

server3 `/data`: 1346925502464 available bytes; 81.38% used; 225810607 free inodes.

server3 `/tmp`: 83163168768 available bytes; 95.36% used; 114139295 free inodes.

server3 `/var/tmp`: 83163168768 available bytes; 95.36% used; 114139295 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105955168256 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105955168256 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 410813444096 available bytes; 94.32% used; 224826138 free inodes.

server4 `/tmp`: 105955168256 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105955168256 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
