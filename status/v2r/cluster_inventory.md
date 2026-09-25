# V2R cluster inventory

2026-09-25T02:02:40.577832+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319024164864 available bytes; 82.20% used; 112480576 free inodes.

server1 `/home`: 319024164864 available bytes; 82.20% used; 112480576 free inodes.

server1 `/tmp`: 319024164864 available bytes; 82.20% used; 112480576 free inodes.

server1 `/var/tmp`: 319024164864 available bytes; 82.20% used; 112480576 free inodes.

server1 `/mnt/raid5`: 416266792960 available bytes; 98.09% used; 337609129 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23026049024 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 23026049024 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 23026049024 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 23026049024 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 485894647808 available bytes; 96.64% used; 445118537 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 84352782336 available bytes; 95.29% used; 114156091 free inodes.

server3 `/home`: 84352782336 available bytes; 95.29% used; 114156091 free inodes.

server3 `/data`: 146058997760 available bytes; 97.98% used; 225811664 free inodes.

server3 `/tmp`: 84352782336 available bytes; 95.29% used; 114156091 free inodes.

server3 `/var/tmp`: 84352782336 available bytes; 95.29% used; 114156091 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105761079296 available bytes; 94.10% used; 114348250 free inodes.

server4 `/home`: 105761079296 available bytes; 94.10% used; 114348250 free inodes.

server4 `/data`: 50098106368 available bytes; 99.31% used; 225030340 free inodes.

server4 `/tmp`: 105761079296 available bytes; 94.10% used; 114348250 free inodes.

server4 `/var/tmp`: 105761079296 available bytes; 94.10% used; 114348250 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
