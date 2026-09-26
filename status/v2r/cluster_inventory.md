# V2R cluster inventory

2026-09-26T14:35:12.757564+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318131535872 available bytes; 82.25% used; 112474374 free inodes.

server1 `/home`: 318131535872 available bytes; 82.25% used; 112474374 free inodes.

server1 `/tmp`: 318131535872 available bytes; 82.25% used; 112474374 free inodes.

server1 `/var/tmp`: 318131535872 available bytes; 82.25% used; 112474374 free inodes.

server1 `/mnt/raid5`: 674019012608 available bytes; 96.91% used; 337531928 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 15070900224 available bytes; 99.16% used; 110378828 free inodes.

server2 `/home`: 15070900224 available bytes; 99.16% used; 110378828 free inodes.

server2 `/tmp`: 15070900224 available bytes; 99.16% used; 110378828 free inodes.

server2 `/var/tmp`: 15070900224 available bytes; 99.16% used; 110378828 free inodes.

server2 `/mnt/raid5`: 634783154176 available bytes; 95.61% used; 444974320 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82629615616 available bytes; 95.39% used; 114110776 free inodes.

server3 `/home`: 82629615616 available bytes; 95.39% used; 114110776 free inodes.

server3 `/data`: 1346878681088 available bytes; 81.39% used; 225805166 free inodes.

server3 `/tmp`: 82629615616 available bytes; 95.39% used; 114110776 free inodes.

server3 `/var/tmp`: 82629615616 available bytes; 95.39% used; 114110776 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105886822400 available bytes; 94.09% used; 114347845 free inodes.

server4 `/home`: 105886822400 available bytes; 94.09% used; 114347845 free inodes.

server4 `/data`: 411003080704 available bytes; 94.32% used; 224826699 free inodes.

server4 `/tmp`: 105886822400 available bytes; 94.09% used; 114347845 free inodes.

server4 `/var/tmp`: 105886822400 available bytes; 94.09% used; 114347845 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
