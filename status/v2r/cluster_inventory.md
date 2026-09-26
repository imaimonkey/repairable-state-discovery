# V2R cluster inventory

2026-09-26T15:37:45.369994+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318150680576 available bytes; 82.25% used; 112473958 free inodes.

server1 `/home`: 318150680576 available bytes; 82.25% used; 112473958 free inodes.

server1 `/tmp`: 318150680576 available bytes; 82.25% used; 112473958 free inodes.

server1 `/var/tmp`: 318150680576 available bytes; 82.25% used; 112473958 free inodes.

server1 `/mnt/raid5`: 654093463552 available bytes; 97.00% used; 337531405 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18025025536 available bytes; 98.99% used; 110367502 free inodes.

server2 `/home`: 18025025536 available bytes; 98.99% used; 110367502 free inodes.

server2 `/tmp`: 18025025536 available bytes; 98.99% used; 110367502 free inodes.

server2 `/var/tmp`: 18025025536 available bytes; 98.99% used; 110367502 free inodes.

server2 `/mnt/raid5`: 608125976576 available bytes; 95.80% used; 444972695 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82163400704 available bytes; 95.41% used; 114094199 free inodes.

server3 `/home`: 82163400704 available bytes; 95.41% used; 114094199 free inodes.

server3 `/data`: 1347155116032 available bytes; 81.38% used; 225809210 free inodes.

server3 `/tmp`: 82163400704 available bytes; 95.41% used; 114094199 free inodes.

server3 `/var/tmp`: 82163400704 available bytes; 95.41% used; 114094199 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105954635776 available bytes; 94.09% used; 114347852 free inodes.

server4 `/home`: 105954635776 available bytes; 94.09% used; 114347852 free inodes.

server4 `/data`: 410724384768 available bytes; 94.32% used; 224825365 free inodes.

server4 `/tmp`: 105954635776 available bytes; 94.09% used; 114347852 free inodes.

server4 `/var/tmp`: 105954635776 available bytes; 94.09% used; 114347852 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
