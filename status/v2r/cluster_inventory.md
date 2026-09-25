# V2R cluster inventory

2026-09-25T23:04:18.106639+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318693150720 available bytes; 82.22% used; 112476299 free inodes.

server1 `/home`: 318693150720 available bytes; 82.22% used; 112476299 free inodes.

server1 `/tmp`: 318693150720 available bytes; 82.22% used; 112476299 free inodes.

server1 `/var/tmp`: 318693150720 available bytes; 82.22% used; 112476299 free inodes.

server1 `/mnt/raid5`: 360170979328 available bytes; 98.35% used; 337538780 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 22952587264 available bytes; 98.72% used; 110406230 free inodes.

server2 `/home`: 22952587264 available bytes; 98.72% used; 110406230 free inodes.

server2 `/tmp`: 22952587264 available bytes; 98.72% used; 110406230 free inodes.

server2 `/var/tmp`: 22952587264 available bytes; 98.72% used; 110406230 free inodes.

server2 `/mnt/raid5`: 297964339200 available bytes; 97.94% used; 445051659 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84354621440 available bytes; 95.29% used; 114152436 free inodes.

server3 `/home`: 84354621440 available bytes; 95.29% used; 114152436 free inodes.

server3 `/data`: 124758642688 available bytes; 98.28% used; 225805363 free inodes.

server3 `/tmp`: 84354621440 available bytes; 95.29% used; 114152436 free inodes.

server3 `/var/tmp`: 84354621440 available bytes; 95.29% used; 114152436 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105159491584 available bytes; 94.13% used; 114346790 free inodes.

server4 `/home`: 105159491584 available bytes; 94.13% used; 114346790 free inodes.

server4 `/data`: 185227591680 available bytes; 97.44% used; 224917657 free inodes.

server4 `/tmp`: 105159491584 available bytes; 94.13% used; 114346790 free inodes.

server4 `/var/tmp`: 105159491584 available bytes; 94.13% used; 114346790 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
