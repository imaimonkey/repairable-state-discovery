# V2R cluster inventory

2026-09-26T16:32:38.970037+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318129938432 available bytes; 82.25% used; 112473837 free inodes.

server1 `/home`: 318129938432 available bytes; 82.25% used; 112473837 free inodes.

server1 `/tmp`: 318129938432 available bytes; 82.25% used; 112473837 free inodes.

server1 `/var/tmp`: 318129938432 available bytes; 82.25% used; 112473837 free inodes.

server1 `/mnt/raid5`: 654103404544 available bytes; 97.00% used; 337531410 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18030399488 available bytes; 98.99% used; 110367545 free inodes.

server2 `/home`: 18030399488 available bytes; 98.99% used; 110367545 free inodes.

server2 `/tmp`: 18030399488 available bytes; 98.99% used; 110367545 free inodes.

server2 `/var/tmp`: 18030399488 available bytes; 98.99% used; 110367545 free inodes.

server2 `/mnt/raid5`: 607628214272 available bytes; 95.80% used; 444971083 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82008166400 available bytes; 95.42% used; 114106873 free inodes.

server3 `/home`: 82008166400 available bytes; 95.42% used; 114106873 free inodes.

server3 `/data`: 1349329707008 available bytes; 81.35% used; 225830668 free inodes.

server3 `/tmp`: 82008166400 available bytes; 95.42% used; 114106873 free inodes.

server3 `/var/tmp`: 82008166400 available bytes; 95.42% used; 114106873 free inodes.
| server4 | True | ['0', '3', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105953460224 available bytes; 94.09% used; 114347865 free inodes.

server4 `/home`: 105953460224 available bytes; 94.09% used; 114347865 free inodes.

server4 `/data`: 410604773376 available bytes; 94.33% used; 224824680 free inodes.

server4 `/tmp`: 105953460224 available bytes; 94.09% used; 114347865 free inodes.

server4 `/var/tmp`: 105953460224 available bytes; 94.09% used; 114347865 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
