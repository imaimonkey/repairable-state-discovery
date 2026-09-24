# V2R cluster inventory

2026-09-24T04:13:08.038048+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324708646912 available bytes; 81.89% used; 112493403 free inodes.

server1 `/home`: 324708646912 available bytes; 81.89% used; 112493403 free inodes.

server1 `/tmp`: 324708646912 available bytes; 81.89% used; 112493403 free inodes.

server1 `/var/tmp`: 324708646912 available bytes; 81.89% used; 112493403 free inodes.

server1 `/mnt/raid5`: 426302631936 available bytes; 98.04% used; 337724745 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40799576064 available bytes; 97.72% used; 110430780 free inodes.

server2 `/home`: 40799576064 available bytes; 97.72% used; 110430780 free inodes.

server2 `/tmp`: 40799576064 available bytes; 97.72% used; 110430780 free inodes.

server2 `/var/tmp`: 40799576064 available bytes; 97.72% used; 110430780 free inodes.

server2 `/mnt/raid5`: 525899968512 available bytes; 96.37% used; 445196608 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292029198336 available bytes; 83.70% used; 114176989 free inodes.

server3 `/home`: 292029198336 available bytes; 83.70% used; 114176989 free inodes.

server3 `/data`: 31727251456 available bytes; 99.56% used; 225841808 free inodes.

server3 `/tmp`: 292029198336 available bytes; 83.70% used; 114176989 free inodes.

server3 `/var/tmp`: 292029198336 available bytes; 83.70% used; 114176989 free inodes.
| server4 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105790652416 available bytes; 94.10% used; 114349462 free inodes.

server4 `/home`: 105790652416 available bytes; 94.10% used; 114349462 free inodes.

server4 `/data`: 256717176832 available bytes; 96.45% used; 225381832 free inodes.

server4 `/tmp`: 105790652416 available bytes; 94.10% used; 114349462 free inodes.

server4 `/var/tmp`: 105790652416 available bytes; 94.10% used; 114349462 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
