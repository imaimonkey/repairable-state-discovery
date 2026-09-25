# V2R cluster inventory

2026-09-25T07:27:35.246242+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318871298048 available bytes; 82.21% used; 112480382 free inodes.

server1 `/home`: 318871298048 available bytes; 82.21% used; 112480382 free inodes.

server1 `/tmp`: 318871298048 available bytes; 82.21% used; 112480382 free inodes.

server1 `/var/tmp`: 318871298048 available bytes; 82.21% used; 112480382 free inodes.

server1 `/mnt/raid5`: 385908092928 available bytes; 98.23% used; 337558439 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22860775424 available bytes; 98.72% used; 110410510 free inodes.

server2 `/home`: 22860775424 available bytes; 98.72% used; 110410510 free inodes.

server2 `/tmp`: 22860775424 available bytes; 98.72% used; 110410510 free inodes.

server2 `/var/tmp`: 22860775424 available bytes; 98.72% used; 110410510 free inodes.

server2 `/mnt/raid5`: 343316889600 available bytes; 97.63% used; 445097537 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84448829440 available bytes; 95.29% used; 114156031 free inodes.

server3 `/home`: 84448829440 available bytes; 95.29% used; 114156031 free inodes.

server3 `/data`: 142394667008 available bytes; 98.03% used; 225812753 free inodes.

server3 `/tmp`: 84448829440 available bytes; 95.29% used; 114156031 free inodes.

server3 `/var/tmp`: 84448829440 available bytes; 95.29% used; 114156031 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105637961728 available bytes; 94.11% used; 114350361 free inodes.

server4 `/home`: 105637961728 available bytes; 94.11% used; 114350361 free inodes.

server4 `/data`: 249098760192 available bytes; 96.56% used; 225014715 free inodes.

server4 `/tmp`: 105637961728 available bytes; 94.11% used; 114350361 free inodes.

server4 `/var/tmp`: 105637961728 available bytes; 94.11% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
