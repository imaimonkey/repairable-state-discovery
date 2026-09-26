# V2R cluster inventory

2026-09-26T14:55:02.907004+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318118629376 available bytes; 82.25% used; 112474328 free inodes.

server1 `/home`: 318118629376 available bytes; 82.25% used; 112474328 free inodes.

server1 `/tmp`: 318118629376 available bytes; 82.25% used; 112474328 free inodes.

server1 `/var/tmp`: 318118629376 available bytes; 82.25% used; 112474328 free inodes.

server1 `/mnt/raid5`: 658385825792 available bytes; 96.98% used; 337531878 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 10546581504 available bytes; 99.41% used; 110367633 free inodes.

server2 `/home`: 10546581504 available bytes; 99.41% used; 110367633 free inodes.

server2 `/tmp`: 10546581504 available bytes; 99.41% used; 110367633 free inodes.

server2 `/var/tmp`: 10546581504 available bytes; 99.41% used; 110367633 free inodes.

server2 `/mnt/raid5`: 631817400320 available bytes; 95.63% used; 444973832 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82634596352 available bytes; 95.39% used; 114110773 free inodes.

server3 `/home`: 82634596352 available bytes; 95.39% used; 114110773 free inodes.

server3 `/data`: 1346841763840 available bytes; 81.39% used; 225804923 free inodes.

server3 `/tmp`: 82634596352 available bytes; 95.39% used; 114110773 free inodes.

server3 `/var/tmp`: 82634596352 available bytes; 95.39% used; 114110773 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105886384128 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105886384128 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 410836062208 available bytes; 94.32% used; 224826271 free inodes.

server4 `/tmp`: 105886384128 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105886384128 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
