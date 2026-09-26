# V2R cluster inventory

2026-09-26T14:27:35.399071+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318132207616 available bytes; 82.25% used; 112474364 free inodes.

server1 `/home`: 318132207616 available bytes; 82.25% used; 112474364 free inodes.

server1 `/tmp`: 318132207616 available bytes; 82.25% used; 112474364 free inodes.

server1 `/var/tmp`: 318132207616 available bytes; 82.25% used; 112474364 free inodes.

server1 `/mnt/raid5`: 674014990336 available bytes; 96.91% used; 337531924 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 15752036352 available bytes; 99.12% used; 110378834 free inodes.

server2 `/home`: 15752036352 available bytes; 99.12% used; 110378834 free inodes.

server2 `/tmp`: 15752036352 available bytes; 99.12% used; 110378834 free inodes.

server2 `/var/tmp`: 15752036352 available bytes; 99.12% used; 110378834 free inodes.

server2 `/mnt/raid5`: 635015643136 available bytes; 95.61% used; 444974671 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82629234688 available bytes; 95.39% used; 114110776 free inodes.

server3 `/home`: 82629234688 available bytes; 95.39% used; 114110776 free inodes.

server3 `/data`: 1346886361088 available bytes; 81.39% used; 225805259 free inodes.

server3 `/tmp`: 82629234688 available bytes; 95.39% used; 114110776 free inodes.

server3 `/var/tmp`: 82629234688 available bytes; 95.39% used; 114110776 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105886965760 available bytes; 94.09% used; 114347844 free inodes.

server4 `/home`: 105886965760 available bytes; 94.09% used; 114347844 free inodes.

server4 `/data`: 411012689920 available bytes; 94.32% used; 224826756 free inodes.

server4 `/tmp`: 105886965760 available bytes; 94.09% used; 114347844 free inodes.

server4 `/var/tmp`: 105886965760 available bytes; 94.09% used; 114347844 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
