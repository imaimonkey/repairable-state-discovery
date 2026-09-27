# V2R cluster inventory

2026-09-27T02:39:26.238506+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315079712768 available bytes; 82.42% used; 112443408 free inodes.

server1 `/home`: 315079712768 available bytes; 82.42% used; 112443408 free inodes.

server1 `/tmp`: 315079712768 available bytes; 82.42% used; 112443408 free inodes.

server1 `/var/tmp`: 315079712768 available bytes; 82.42% used; 112443408 free inodes.

server1 `/mnt/raid5`: 637202923520 available bytes; 97.08% used; 337401568 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17626820608 available bytes; 99.02% used; 110365002 free inodes.

server2 `/home`: 17626820608 available bytes; 99.02% used; 110365002 free inodes.

server2 `/tmp`: 17626820608 available bytes; 99.02% used; 110365002 free inodes.

server2 `/var/tmp`: 17626820608 available bytes; 99.02% used; 110365002 free inodes.

server2 `/mnt/raid5`: 580695158784 available bytes; 95.99% used; 444884345 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78707838976 available bytes; 95.61% used; 114062953 free inodes.

server3 `/home`: 78707838976 available bytes; 95.61% used; 114062953 free inodes.

server3 `/data`: 1337679708160 available bytes; 81.51% used; 225762219 free inodes.

server3 `/tmp`: 78707838976 available bytes; 95.61% used; 114062953 free inodes.

server3 `/var/tmp`: 78707838976 available bytes; 95.61% used; 114062953 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111036121088 available bytes; 93.80% used; 114373249 free inodes.

server4 `/home`: 111036121088 available bytes; 93.80% used; 114373249 free inodes.

server4 `/data`: 397015752704 available bytes; 94.51% used; 224781455 free inodes.

server4 `/tmp`: 111036121088 available bytes; 93.80% used; 114373249 free inodes.

server4 `/var/tmp`: 111036121088 available bytes; 93.80% used; 114373249 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
