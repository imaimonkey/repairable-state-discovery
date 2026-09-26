# V2R cluster inventory

2026-09-26T18:33:06.409597+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315565531136 available bytes; 82.40% used; 112445743 free inodes.

server1 `/home`: 315565531136 available bytes; 82.40% used; 112445743 free inodes.

server1 `/tmp`: 315565531136 available bytes; 82.40% used; 112445743 free inodes.

server1 `/var/tmp`: 315565531136 available bytes; 82.40% used; 112445743 free inodes.

server1 `/mnt/raid5`: 645856137216 available bytes; 97.04% used; 337467122 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18023755776 available bytes; 98.99% used; 110367616 free inodes.

server2 `/home`: 18023755776 available bytes; 98.99% used; 110367616 free inodes.

server2 `/tmp`: 18023755776 available bytes; 98.99% used; 110367616 free inodes.

server2 `/var/tmp`: 18023755776 available bytes; 98.99% used; 110367616 free inodes.

server2 `/mnt/raid5`: 603990122496 available bytes; 95.83% used; 444967745 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81277222912 available bytes; 95.46% used; 114065373 free inodes.

server3 `/home`: 81277222912 available bytes; 95.46% used; 114065373 free inodes.

server3 `/data`: 1349267939328 available bytes; 81.35% used; 225834813 free inodes.

server3 `/tmp`: 81277222912 available bytes; 95.46% used; 114065373 free inodes.

server3 `/var/tmp`: 81277222912 available bytes; 95.46% used; 114065373 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105938583552 available bytes; 94.09% used; 114347834 free inodes.

server4 `/home`: 105938583552 available bytes; 94.09% used; 114347834 free inodes.

server4 `/data`: 410352201728 available bytes; 94.33% used; 224824176 free inodes.

server4 `/tmp`: 105938583552 available bytes; 94.09% used; 114347834 free inodes.

server4 `/var/tmp`: 105938583552 available bytes; 94.09% used; 114347834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
