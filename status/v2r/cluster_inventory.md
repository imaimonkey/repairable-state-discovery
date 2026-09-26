# V2R cluster inventory

2026-09-26T13:41:46.007823+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318154883072 available bytes; 82.25% used; 112474411 free inodes.

server1 `/home`: 318154883072 available bytes; 82.25% used; 112474411 free inodes.

server1 `/tmp`: 318154883072 available bytes; 82.25% used; 112474411 free inodes.

server1 `/var/tmp`: 318154883072 available bytes; 82.25% used; 112474411 free inodes.

server1 `/mnt/raid5`: 674755592192 available bytes; 96.90% used; 337535772 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 19071012864 available bytes; 98.94% used; 110378920 free inodes.

server2 `/home`: 19071012864 available bytes; 98.94% used; 110378920 free inodes.

server2 `/tmp`: 19071012864 available bytes; 98.94% used; 110378920 free inodes.

server2 `/var/tmp`: 19071012864 available bytes; 98.94% used; 110378920 free inodes.

server2 `/mnt/raid5`: 636239986688 available bytes; 95.60% used; 444976192 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82639937536 available bytes; 95.39% used; 114110801 free inodes.

server3 `/home`: 82639937536 available bytes; 95.39% used; 114110801 free inodes.

server3 `/data`: 1347495301120 available bytes; 81.38% used; 225822863 free inodes.

server3 `/tmp`: 82639937536 available bytes; 95.39% used; 114110801 free inodes.

server3 `/var/tmp`: 82639937536 available bytes; 95.39% used; 114110801 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105898270720 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105898270720 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 411509821440 available bytes; 94.31% used; 224827588 free inodes.

server4 `/tmp`: 105898270720 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105898270720 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
