# V2R cluster inventory

2026-09-25T08:12:08.859286+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318839218176 available bytes; 82.21% used; 112480355 free inodes.

server1 `/home`: 318839218176 available bytes; 82.21% used; 112480355 free inodes.

server1 `/tmp`: 318839218176 available bytes; 82.21% used; 112480355 free inodes.

server1 `/var/tmp`: 318839218176 available bytes; 82.21% used; 112480355 free inodes.

server1 `/mnt/raid5`: 379202727936 available bytes; 98.26% used; 337557618 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22842224640 available bytes; 98.73% used; 110410483 free inodes.

server2 `/home`: 22842224640 available bytes; 98.73% used; 110410483 free inodes.

server2 `/tmp`: 22842224640 available bytes; 98.73% used; 110410483 free inodes.

server2 `/var/tmp`: 22842224640 available bytes; 98.73% used; 110410483 free inodes.

server2 `/mnt/raid5`: 333292085248 available bytes; 97.70% used; 445094733 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84436566016 available bytes; 95.29% used; 114156049 free inodes.

server3 `/home`: 84436566016 available bytes; 95.29% used; 114156049 free inodes.

server3 `/data`: 142387077120 available bytes; 98.03% used; 225811995 free inodes.

server3 `/tmp`: 84436566016 available bytes; 95.29% used; 114156049 free inodes.

server3 `/var/tmp`: 84436566016 available bytes; 95.29% used; 114156049 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105625174016 available bytes; 94.11% used; 114350335 free inodes.

server4 `/home`: 105625174016 available bytes; 94.11% used; 114350335 free inodes.

server4 `/data`: 249010302976 available bytes; 96.56% used; 225008074 free inodes.

server4 `/tmp`: 105625174016 available bytes; 94.11% used; 114350335 free inodes.

server4 `/var/tmp`: 105625174016 available bytes; 94.11% used; 114350335 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
