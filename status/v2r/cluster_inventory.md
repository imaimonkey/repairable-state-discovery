# V2R cluster inventory

2026-09-26T15:25:33.405219+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318157488128 available bytes; 82.25% used; 112473938 free inodes.

server1 `/home`: 318157488128 available bytes; 82.25% used; 112473938 free inodes.

server1 `/tmp`: 318157488128 available bytes; 82.25% used; 112473938 free inodes.

server1 `/var/tmp`: 318157488128 available bytes; 82.25% used; 112473938 free inodes.

server1 `/mnt/raid5`: 654124060672 available bytes; 97.00% used; 337531532 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18028670976 available bytes; 98.99% used; 110367501 free inodes.

server2 `/home`: 18028670976 available bytes; 98.99% used; 110367501 free inodes.

server2 `/tmp`: 18028670976 available bytes; 98.99% used; 110367501 free inodes.

server2 `/var/tmp`: 18028670976 available bytes; 98.99% used; 110367501 free inodes.

server2 `/mnt/raid5`: 609559244800 available bytes; 95.79% used; 444973294 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82449756160 available bytes; 95.40% used; 114101913 free inodes.

server3 `/home`: 82449756160 available bytes; 95.40% used; 114101913 free inodes.

server3 `/data`: 1347187785728 available bytes; 81.38% used; 225809911 free inodes.

server3 `/tmp`: 82449756160 available bytes; 95.40% used; 114101913 free inodes.

server3 `/var/tmp`: 82449756160 available bytes; 95.40% used; 114101913 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105954807808 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105954807808 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 410807980032 available bytes; 94.32% used; 224826003 free inodes.

server4 `/tmp`: 105954807808 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105954807808 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
