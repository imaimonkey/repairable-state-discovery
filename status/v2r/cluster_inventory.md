# V2R cluster inventory

2026-09-25T02:24:16.690345+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318970462208 available bytes; 82.21% used; 112480503 free inodes.

server1 `/home`: 318970462208 available bytes; 82.21% used; 112480503 free inodes.

server1 `/tmp`: 318970462208 available bytes; 82.21% used; 112480503 free inodes.

server1 `/var/tmp`: 318970462208 available bytes; 82.21% used; 112480503 free inodes.

server1 `/mnt/raid5`: 416224071680 available bytes; 98.09% used; 337606616 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23017738240 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 23017738240 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 23017738240 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 23017738240 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 483602571264 available bytes; 96.66% used; 445113959 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84355665920 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84355665920 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 145698037760 available bytes; 97.99% used; 225811167 free inodes.

server3 `/tmp`: 84355665920 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84355665920 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['1', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105896013824 available bytes; 94.09% used; 114350978 free inodes.

server4 `/home`: 105896013824 available bytes; 94.09% used; 114350978 free inodes.

server4 `/data`: 35432587264 available bytes; 99.51% used; 224970012 free inodes.

server4 `/tmp`: 105896013824 available bytes; 94.09% used; 114350978 free inodes.

server4 `/var/tmp`: 105896013824 available bytes; 94.09% used; 114350978 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
