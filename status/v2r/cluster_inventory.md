# V2R cluster inventory

2026-09-26T14:18:26.053926+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318129786880 available bytes; 82.25% used; 112474376 free inodes.

server1 `/home`: 318129786880 available bytes; 82.25% used; 112474376 free inodes.

server1 `/tmp`: 318129786880 available bytes; 82.25% used; 112474376 free inodes.

server1 `/var/tmp`: 318129786880 available bytes; 82.25% used; 112474376 free inodes.

server1 `/mnt/raid5`: 674015858688 available bytes; 96.91% used; 337531972 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 19066703872 available bytes; 98.94% used; 110378885 free inodes.

server2 `/home`: 19066703872 available bytes; 98.94% used; 110378885 free inodes.

server2 `/tmp`: 19066703872 available bytes; 98.94% used; 110378885 free inodes.

server2 `/var/tmp`: 19066703872 available bytes; 98.94% used; 110378885 free inodes.

server2 `/mnt/raid5`: 635261394944 available bytes; 95.61% used; 444974933 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82639953920 available bytes; 95.39% used; 114110784 free inodes.

server3 `/home`: 82639953920 available bytes; 95.39% used; 114110784 free inodes.

server3 `/data`: 1346892386304 available bytes; 81.39% used; 225805341 free inodes.

server3 `/tmp`: 82639953920 available bytes; 95.39% used; 114110784 free inodes.

server3 `/var/tmp`: 82639953920 available bytes; 95.39% used; 114110784 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105887162368 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105887162368 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 411023732736 available bytes; 94.32% used; 224826824 free inodes.

server4 `/tmp`: 105887162368 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105887162368 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
