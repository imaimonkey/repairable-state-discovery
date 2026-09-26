# V2R cluster inventory

2026-09-26T13:43:21.098194+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318154452992 available bytes; 82.25% used; 112474411 free inodes.

server1 `/home`: 318154452992 available bytes; 82.25% used; 112474411 free inodes.

server1 `/tmp`: 318154452992 available bytes; 82.25% used; 112474411 free inodes.

server1 `/var/tmp`: 318154452992 available bytes; 82.25% used; 112474411 free inodes.

server1 `/mnt/raid5`: 674755956736 available bytes; 96.90% used; 337535774 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 19070832640 available bytes; 98.94% used; 110378920 free inodes.

server2 `/home`: 19070832640 available bytes; 98.94% used; 110378920 free inodes.

server2 `/tmp`: 19070832640 available bytes; 98.94% used; 110378920 free inodes.

server2 `/var/tmp`: 19070832640 available bytes; 98.94% used; 110378920 free inodes.

server2 `/mnt/raid5`: 635120791552 available bytes; 95.61% used; 444976014 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82639650816 available bytes; 95.39% used; 114110801 free inodes.

server3 `/home`: 82639650816 available bytes; 95.39% used; 114110801 free inodes.

server3 `/data`: 1347493441536 available bytes; 81.38% used; 225822842 free inodes.

server3 `/tmp`: 82639650816 available bytes; 95.39% used; 114110801 free inodes.

server3 `/var/tmp`: 82639650816 available bytes; 95.39% used; 114110801 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105898246144 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105898246144 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 411508695040 available bytes; 94.31% used; 224827587 free inodes.

server4 `/tmp`: 105898246144 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105898246144 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
