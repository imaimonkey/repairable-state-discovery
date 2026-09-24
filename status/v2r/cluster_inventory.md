# V2R cluster inventory

2026-09-24T02:05:28.653364+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325445623808 available bytes; 81.84% used; 112499267 free inodes.

server1 `/home`: 325445623808 available bytes; 81.84% used; 112499267 free inodes.

server1 `/tmp`: 325445623808 available bytes; 81.84% used; 112499267 free inodes.

server1 `/var/tmp`: 325445623808 available bytes; 81.84% used; 112499267 free inodes.

server1 `/mnt/raid5`: 752127414272 available bytes; 96.55% used; 337733570 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40911159296 available bytes; 97.72% used; 110431712 free inodes.

server2 `/home`: 40911159296 available bytes; 97.72% used; 110431712 free inodes.

server2 `/tmp`: 40911159296 available bytes; 97.72% used; 110431712 free inodes.

server2 `/var/tmp`: 40911159296 available bytes; 97.72% used; 110431712 free inodes.

server2 `/mnt/raid5`: 529774972928 available bytes; 96.34% used; 445200512 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292682784768 available bytes; 83.67% used; 114210523 free inodes.

server3 `/home`: 292682784768 available bytes; 83.67% used; 114210523 free inodes.

server3 `/data`: 60188983296 available bytes; 99.17% used; 225841535 free inodes.

server3 `/tmp`: 292682784768 available bytes; 83.67% used; 114210523 free inodes.

server3 `/var/tmp`: 292682784768 available bytes; 83.67% used; 114210523 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105938128896 available bytes; 94.09% used; 114348463 free inodes.

server4 `/home`: 105938128896 available bytes; 94.09% used; 114348463 free inodes.

server4 `/data`: 289766031360 available bytes; 96.00% used; 225388478 free inodes.

server4 `/tmp`: 105938128896 available bytes; 94.09% used; 114348463 free inodes.

server4 `/var/tmp`: 105938128896 available bytes; 94.09% used; 114348463 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
