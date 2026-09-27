# V2R cluster inventory

2026-09-27T00:43:33.782462+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315146027008 available bytes; 82.42% used; 112443450 free inodes.

server1 `/home`: 315146027008 available bytes; 82.42% used; 112443450 free inodes.

server1 `/tmp`: 315146027008 available bytes; 82.42% used; 112443450 free inodes.

server1 `/var/tmp`: 315146027008 available bytes; 82.42% used; 112443450 free inodes.

server1 `/mnt/raid5`: 637609697280 available bytes; 97.08% used; 337406553 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17623134208 available bytes; 99.02% used; 110364997 free inodes.

server2 `/home`: 17623134208 available bytes; 99.02% used; 110364997 free inodes.

server2 `/tmp`: 17623134208 available bytes; 99.02% used; 110364997 free inodes.

server2 `/var/tmp`: 17623134208 available bytes; 99.02% used; 110364997 free inodes.

server2 `/mnt/raid5`: 584584216576 available bytes; 95.96% used; 444887609 free inodes.
| server3 | True | ['0', '3'] | [] |

server3 `/`: 79501340672 available bytes; 95.56% used; 114068708 free inodes.

server3 `/home`: 79501340672 available bytes; 95.56% used; 114068708 free inodes.

server3 `/data`: 1342828724224 available bytes; 81.44% used; 225764290 free inodes.

server3 `/tmp`: 79501340672 available bytes; 95.56% used; 114068708 free inodes.

server3 `/var/tmp`: 79501340672 available bytes; 95.56% used; 114068708 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105878974464 available bytes; 94.09% used; 114347835 free inodes.

server4 `/home`: 105878974464 available bytes; 94.09% used; 114347835 free inodes.

server4 `/data`: 406608678912 available bytes; 94.38% used; 224783002 free inodes.

server4 `/tmp`: 105878974464 available bytes; 94.09% used; 114347835 free inodes.

server4 `/var/tmp`: 105878974464 available bytes; 94.09% used; 114347835 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
