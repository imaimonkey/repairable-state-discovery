# V2R cluster inventory

2026-09-27T00:13:04.577826+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315172782080 available bytes; 82.42% used; 112443685 free inodes.

server1 `/home`: 315172782080 available bytes; 82.42% used; 112443685 free inodes.

server1 `/tmp`: 315172782080 available bytes; 82.42% used; 112443685 free inodes.

server1 `/var/tmp`: 315172782080 available bytes; 82.42% used; 112443685 free inodes.

server1 `/mnt/raid5`: 637716508672 available bytes; 97.07% used; 337408130 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 17937248256 available bytes; 99.00% used; 110367421 free inodes.

server2 `/home`: 17937248256 available bytes; 99.00% used; 110367421 free inodes.

server2 `/tmp`: 17937248256 available bytes; 99.00% used; 110367421 free inodes.

server2 `/var/tmp`: 17937248256 available bytes; 99.00% used; 110367421 free inodes.

server2 `/mnt/raid5`: 593705521152 available bytes; 95.90% used; 444958058 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 79739912192 available bytes; 95.55% used; 114068852 free inodes.

server3 `/home`: 79739912192 available bytes; 95.55% used; 114068852 free inodes.

server3 `/data`: 1349113786368 available bytes; 81.35% used; 225825886 free inodes.

server3 `/tmp`: 79739912192 available bytes; 95.55% used; 114068852 free inodes.

server3 `/var/tmp`: 79739912192 available bytes; 95.55% used; 114068852 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105879818240 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105879818240 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409569894400 available bytes; 94.34% used; 224823737 free inodes.

server4 `/tmp`: 105879818240 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105879818240 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
