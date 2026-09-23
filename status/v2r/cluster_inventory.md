# V2R cluster inventory

2026-09-23T22:50:35.929980+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325746860032 available bytes; 81.83% used; 112501729 free inodes.

server1 `/home`: 325746860032 available bytes; 81.83% used; 112501729 free inodes.

server1 `/tmp`: 325746860032 available bytes; 81.83% used; 112501729 free inodes.

server1 `/var/tmp`: 325746860032 available bytes; 81.83% used; 112501729 free inodes.

server1 `/mnt/raid5`: 1388113174528 available bytes; 93.63% used; 337739960 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41070755840 available bytes; 97.71% used; 110432620 free inodes.

server2 `/home`: 41070755840 available bytes; 97.71% used; 110432620 free inodes.

server2 `/tmp`: 41070755840 available bytes; 97.71% used; 110432620 free inodes.

server2 `/var/tmp`: 41070755840 available bytes; 97.71% used; 110432620 free inodes.

server2 `/mnt/raid5`: 536053559296 available bytes; 96.30% used; 445206153 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292536840192 available bytes; 83.68% used; 114192874 free inodes.

server3 `/home`: 292536840192 available bytes; 83.68% used; 114192874 free inodes.

server3 `/data`: 82363527168 available bytes; 98.86% used; 225846816 free inodes.

server3 `/tmp`: 292536840192 available bytes; 83.68% used; 114192874 free inodes.

server3 `/var/tmp`: 292536840192 available bytes; 83.68% used; 114192874 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106318585856 available bytes; 94.07% used; 114353795 free inodes.

server4 `/home`: 106318585856 available bytes; 94.07% used; 114353795 free inodes.

server4 `/data`: 300098990080 available bytes; 95.85% used; 225433880 free inodes.

server4 `/tmp`: 106318585856 available bytes; 94.07% used; 114353795 free inodes.

server4 `/var/tmp`: 106318585856 available bytes; 94.07% used; 114353795 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
