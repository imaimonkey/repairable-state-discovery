# V2R cluster inventory

2026-09-26T16:38:45.018803+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318129471488 available bytes; 82.25% used; 112473836 free inodes.

server1 `/home`: 318129471488 available bytes; 82.25% used; 112473836 free inodes.

server1 `/tmp`: 318129471488 available bytes; 82.25% used; 112473836 free inodes.

server1 `/var/tmp`: 318129471488 available bytes; 82.25% used; 112473836 free inodes.

server1 `/mnt/raid5`: 654103625728 available bytes; 97.00% used; 337531410 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18025553920 available bytes; 98.99% used; 110367553 free inodes.

server2 `/home`: 18025553920 available bytes; 98.99% used; 110367553 free inodes.

server2 `/tmp`: 18025553920 available bytes; 98.99% used; 110367553 free inodes.

server2 `/var/tmp`: 18025553920 available bytes; 98.99% used; 110367553 free inodes.

server2 `/mnt/raid5`: 607462641664 available bytes; 95.80% used; 444970893 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 81569468416 available bytes; 95.45% used; 114086240 free inodes.

server3 `/home`: 81569468416 available bytes; 95.45% used; 114086240 free inodes.

server3 `/data`: 1349271392256 available bytes; 81.35% used; 225830515 free inodes.

server3 `/tmp`: 81569468416 available bytes; 95.45% used; 114086240 free inodes.

server3 `/var/tmp`: 81569468416 available bytes; 95.45% used; 114086240 free inodes.
| server4 | True | ['0', '2', '3', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105953378304 available bytes; 94.09% used; 114347873 free inodes.

server4 `/home`: 105953378304 available bytes; 94.09% used; 114347873 free inodes.

server4 `/data`: 410603864064 available bytes; 94.33% used; 224824665 free inodes.

server4 `/tmp`: 105953378304 available bytes; 94.09% used; 114347873 free inodes.

server4 `/var/tmp`: 105953378304 available bytes; 94.09% used; 114347873 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
