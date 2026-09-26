# V2R cluster inventory

2026-09-26T15:11:40.604152+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318164922368 available bytes; 82.25% used; 112473942 free inodes.

server1 `/home`: 318164922368 available bytes; 82.25% used; 112473942 free inodes.

server1 `/tmp`: 318164922368 available bytes; 82.25% used; 112473942 free inodes.

server1 `/var/tmp`: 318164922368 available bytes; 82.25% used; 112473942 free inodes.

server1 `/mnt/raid5`: 654233022464 available bytes; 97.00% used; 337531837 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 7273537536 available bytes; 99.59% used; 110367267 free inodes.

server2 `/home`: 7273537536 available bytes; 99.59% used; 110367267 free inodes.

server2 `/tmp`: 7273537536 available bytes; 99.59% used; 110367267 free inodes.

server2 `/var/tmp`: 7273537536 available bytes; 99.59% used; 110367267 free inodes.

server2 `/mnt/raid5`: 610226130944 available bytes; 95.78% used; 444973676 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82443751424 available bytes; 95.40% used; 114101906 free inodes.

server3 `/home`: 82443751424 available bytes; 95.40% used; 114101906 free inodes.

server3 `/data`: 1346909249536 available bytes; 81.39% used; 225810090 free inodes.

server3 `/tmp`: 82443751424 available bytes; 95.40% used; 114101906 free inodes.

server3 `/var/tmp`: 82443751424 available bytes; 95.40% used; 114101906 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105955074048 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105955074048 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 410810712064 available bytes; 94.32% used; 224826117 free inodes.

server4 `/tmp`: 105955074048 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105955074048 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
