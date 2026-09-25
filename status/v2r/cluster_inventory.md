# V2R cluster inventory

2026-09-25T02:42:43.746208+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318958559232 available bytes; 82.21% used; 112480424 free inodes.

server1 `/home`: 318958559232 available bytes; 82.21% used; 112480424 free inodes.

server1 `/tmp`: 318958559232 available bytes; 82.21% used; 112480424 free inodes.

server1 `/var/tmp`: 318958559232 available bytes; 82.21% used; 112480424 free inodes.

server1 `/mnt/raid5`: 416187514880 available bytes; 98.09% used; 337604464 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23006580736 available bytes; 98.72% used; 110410439 free inodes.

server2 `/home`: 23006580736 available bytes; 98.72% used; 110410439 free inodes.

server2 `/tmp`: 23006580736 available bytes; 98.72% used; 110410439 free inodes.

server2 `/var/tmp`: 23006580736 available bytes; 98.72% used; 110410439 free inodes.

server2 `/mnt/raid5`: 482727849984 available bytes; 96.66% used; 445113234 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84350627840 available bytes; 95.29% used; 114156073 free inodes.

server3 `/home`: 84350627840 available bytes; 95.29% used; 114156073 free inodes.

server3 `/data`: 145387671552 available bytes; 97.99% used; 225811015 free inodes.

server3 `/tmp`: 84350627840 available bytes; 95.29% used; 114156073 free inodes.

server3 `/var/tmp`: 84350627840 available bytes; 95.29% used; 114156073 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105895501824 available bytes; 94.09% used; 114351001 free inodes.

server4 `/home`: 105895501824 available bytes; 94.09% used; 114351001 free inodes.

server4 `/data`: 0 available bytes; 100.00% used; 224968797 free inodes.

server4 `/tmp`: 105895501824 available bytes; 94.09% used; 114351001 free inodes.

server4 `/var/tmp`: 105895501824 available bytes; 94.09% used; 114351001 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
