# V2R cluster inventory

2026-09-26T16:25:01.590897+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318130159616 available bytes; 82.25% used; 112473895 free inodes.

server1 `/home`: 318130159616 available bytes; 82.25% used; 112473895 free inodes.

server1 `/tmp`: 318130159616 available bytes; 82.25% used; 112473895 free inodes.

server1 `/var/tmp`: 318130159616 available bytes; 82.25% used; 112473895 free inodes.

server1 `/mnt/raid5`: 654103293952 available bytes; 97.00% used; 337531408 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18031112192 available bytes; 98.99% used; 110367524 free inodes.

server2 `/home`: 18031112192 available bytes; 98.99% used; 110367524 free inodes.

server2 `/tmp`: 18031112192 available bytes; 98.99% used; 110367524 free inodes.

server2 `/var/tmp`: 18031112192 available bytes; 98.99% used; 110367524 free inodes.

server2 `/mnt/raid5`: 607872135168 available bytes; 95.80% used; 444971496 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81572982784 available bytes; 95.45% used; 114077209 free inodes.

server3 `/home`: 81572982784 available bytes; 95.45% used; 114077209 free inodes.

server3 `/data`: 1349334560768 available bytes; 81.35% used; 225830756 free inodes.

server3 `/tmp`: 81572982784 available bytes; 95.45% used; 114077209 free inodes.

server3 `/var/tmp`: 81572982784 available bytes; 95.45% used; 114077209 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105953611776 available bytes; 94.09% used; 114347852 free inodes.

server4 `/home`: 105953611776 available bytes; 94.09% used; 114347852 free inodes.

server4 `/data`: 410693636096 available bytes; 94.32% used; 224824689 free inodes.

server4 `/tmp`: 105953611776 available bytes; 94.09% used; 114347852 free inodes.

server4 `/var/tmp`: 105953611776 available bytes; 94.09% used; 114347852 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
