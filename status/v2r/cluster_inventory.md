# V2R cluster inventory

2026-09-25T11:48:23.825132+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319050588160 available bytes; 82.20% used; 112478818 free inodes.

server1 `/home`: 319050588160 available bytes; 82.20% used; 112478818 free inodes.

server1 `/tmp`: 319050588160 available bytes; 82.20% used; 112478818 free inodes.

server1 `/var/tmp`: 319050588160 available bytes; 82.20% used; 112478818 free inodes.

server1 `/mnt/raid5`: 364346671104 available bytes; 98.33% used; 337549172 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 22906417152 available bytes; 98.72% used; 110409976 free inodes.

server2 `/home`: 22906417152 available bytes; 98.72% used; 110409976 free inodes.

server2 `/tmp`: 22906417152 available bytes; 98.72% used; 110409976 free inodes.

server2 `/var/tmp`: 22906417152 available bytes; 98.72% used; 110409976 free inodes.

server2 `/mnt/raid5`: 326559150080 available bytes; 97.74% used; 445082705 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84214591488 available bytes; 95.30% used; 114154984 free inodes.

server3 `/home`: 84214591488 available bytes; 95.30% used; 114154984 free inodes.

server3 `/data`: 142045077504 available bytes; 98.04% used; 225813356 free inodes.

server3 `/tmp`: 84214591488 available bytes; 95.30% used; 114154984 free inodes.

server3 `/var/tmp`: 84214591488 available bytes; 95.30% used; 114154984 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105602580480 available bytes; 94.11% used; 114350231 free inodes.

server4 `/home`: 105602580480 available bytes; 94.11% used; 114350231 free inodes.

server4 `/data`: 232577523712 available bytes; 96.79% used; 224974697 free inodes.

server4 `/tmp`: 105602580480 available bytes; 94.11% used; 114350231 free inodes.

server4 `/var/tmp`: 105602580480 available bytes; 94.11% used; 114350231 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
