# V2R cluster inventory

2026-09-26T15:05:43.626714+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318166626304 available bytes; 82.25% used; 112473931 free inodes.

server1 `/home`: 318166626304 available bytes; 82.25% used; 112473931 free inodes.

server1 `/tmp`: 318166626304 available bytes; 82.25% used; 112473931 free inodes.

server1 `/var/tmp`: 318166626304 available bytes; 82.25% used; 112473931 free inodes.

server1 `/mnt/raid5`: 654242050048 available bytes; 97.00% used; 337531862 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 43081728 available bytes; 100.00% used; 110367049 free inodes.

server2 `/home`: 43081728 available bytes; 100.00% used; 110367049 free inodes.

server2 `/tmp`: 43081728 available bytes; 100.00% used; 110367049 free inodes.

server2 `/var/tmp`: 43081728 available bytes; 100.00% used; 110367049 free inodes.

server2 `/mnt/raid5`: 617637769216 available bytes; 95.73% used; 444973377 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82758291456 available bytes; 95.38% used; 114112145 free inodes.

server3 `/home`: 82758291456 available bytes; 95.38% used; 114112145 free inodes.

server3 `/data`: 1346926415872 available bytes; 81.38% used; 225810628 free inodes.

server3 `/tmp`: 82758291456 available bytes; 95.38% used; 114112145 free inodes.

server3 `/var/tmp`: 82758291456 available bytes; 95.38% used; 114112145 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105952993280 available bytes; 94.09% used; 114347839 free inodes.

server4 `/home`: 105952993280 available bytes; 94.09% used; 114347839 free inodes.

server4 `/data`: 410814967808 available bytes; 94.32% used; 224826184 free inodes.

server4 `/tmp`: 105952993280 available bytes; 94.09% used; 114347839 free inodes.

server4 `/var/tmp`: 105952993280 available bytes; 94.09% used; 114347839 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
