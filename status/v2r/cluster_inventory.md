# V2R cluster inventory

2026-09-26T01:48:10.633558+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318526754816 available bytes; 82.23% used; 112476285 free inodes.

server1 `/home`: 318526754816 available bytes; 82.23% used; 112476285 free inodes.

server1 `/tmp`: 318526754816 available bytes; 82.23% used; 112476285 free inodes.

server1 `/var/tmp`: 318526754816 available bytes; 82.23% used; 112476285 free inodes.

server1 `/mnt/raid5`: 345255329792 available bytes; 98.42% used; 337546361 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22938353664 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22938353664 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22938353664 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22938353664 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 290177728512 available bytes; 97.99% used; 445055134 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84326195200 available bytes; 95.29% used; 114152364 free inodes.

server3 `/home`: 84326195200 available bytes; 95.29% used; 114152364 free inodes.

server3 `/data`: 124795179008 available bytes; 98.28% used; 225817714 free inodes.

server3 `/tmp`: 84326195200 available bytes; 95.29% used; 114152364 free inodes.

server3 `/var/tmp`: 84326195200 available bytes; 95.29% used; 114152364 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105434091520 available bytes; 94.12% used; 114348357 free inodes.

server4 `/home`: 105434091520 available bytes; 94.12% used; 114348357 free inodes.

server4 `/data`: 130909036544 available bytes; 98.19% used; 224915776 free inodes.

server4 `/tmp`: 105434091520 available bytes; 94.12% used; 114348357 free inodes.

server4 `/var/tmp`: 105434091520 available bytes; 94.12% used; 114348357 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
