# V2R cluster inventory

2026-09-26T12:28:33.991089+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318174167040 available bytes; 82.25% used; 112474424 free inodes.

server1 `/home`: 318174167040 available bytes; 82.25% used; 112474424 free inodes.

server1 `/tmp`: 318174167040 available bytes; 82.25% used; 112474424 free inodes.

server1 `/var/tmp`: 318174167040 available bytes; 82.25% used; 112474424 free inodes.

server1 `/mnt/raid5`: 218556825600 available bytes; 99.00% used; 337537759 free inodes.
| server2 | True | [] | [] |

server2 `/`: 19758678016 available bytes; 98.90% used; 110381998 free inodes.

server2 `/home`: 19758678016 available bytes; 98.90% used; 110381998 free inodes.

server2 `/tmp`: 19758678016 available bytes; 98.90% used; 110381998 free inodes.

server2 `/var/tmp`: 19758678016 available bytes; 98.90% used; 110381998 free inodes.

server2 `/mnt/raid5`: 240360734720 available bytes; 98.34% used; 444980157 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82652229632 available bytes; 95.39% used; 114110833 free inodes.

server3 `/home`: 82652229632 available bytes; 95.39% used; 114110833 free inodes.

server3 `/data`: 123411382272 available bytes; 98.29% used; 225823754 free inodes.

server3 `/tmp`: 82652229632 available bytes; 95.39% used; 114110833 free inodes.

server3 `/var/tmp`: 82652229632 available bytes; 95.39% used; 114110833 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105899773952 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105899773952 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 88552390656 available bytes; 98.78% used; 224878833 free inodes.

server4 `/tmp`: 105899773952 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105899773952 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
