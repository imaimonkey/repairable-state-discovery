# V2R cluster inventory

2026-09-26T13:49:27.014033+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318152474624 available bytes; 82.25% used; 112474409 free inodes.

server1 `/home`: 318152474624 available bytes; 82.25% used; 112474409 free inodes.

server1 `/tmp`: 318152474624 available bytes; 82.25% used; 112474409 free inodes.

server1 `/var/tmp`: 318152474624 available bytes; 82.25% used; 112474409 free inodes.

server1 `/mnt/raid5`: 674755166208 available bytes; 96.90% used; 337535768 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 19078803456 available bytes; 98.94% used; 110378924 free inodes.

server2 `/home`: 19078803456 available bytes; 98.94% used; 110378924 free inodes.

server2 `/tmp`: 19078803456 available bytes; 98.94% used; 110378924 free inodes.

server2 `/var/tmp`: 19078803456 available bytes; 98.94% used; 110378924 free inodes.

server2 `/mnt/raid5`: 636032598016 available bytes; 95.61% used; 444975989 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82639933440 available bytes; 95.39% used; 114110803 free inodes.

server3 `/home`: 82639933440 available bytes; 95.39% used; 114110803 free inodes.

server3 `/data`: 1347488104448 available bytes; 81.38% used; 225822780 free inodes.

server3 `/tmp`: 82639933440 available bytes; 95.39% used; 114110803 free inodes.

server3 `/var/tmp`: 82639933440 available bytes; 95.39% used; 114110803 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105898164224 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105898164224 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 411443724288 available bytes; 94.31% used; 224827549 free inodes.

server4 `/tmp`: 105898164224 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105898164224 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
