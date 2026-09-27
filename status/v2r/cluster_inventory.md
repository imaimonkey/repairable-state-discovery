# V2R cluster inventory

2026-09-27T00:23:44.553424+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315160780800 available bytes; 82.42% used; 112443485 free inodes.

server1 `/home`: 315160780800 available bytes; 82.42% used; 112443485 free inodes.

server1 `/tmp`: 315160780800 available bytes; 82.42% used; 112443485 free inodes.

server1 `/var/tmp`: 315160780800 available bytes; 82.42% used; 112443485 free inodes.

server1 `/mnt/raid5`: 637709533184 available bytes; 97.07% used; 337407931 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17639862272 available bytes; 99.02% used; 110365087 free inodes.

server2 `/home`: 17639862272 available bytes; 99.02% used; 110365087 free inodes.

server2 `/tmp`: 17639862272 available bytes; 99.02% used; 110365087 free inodes.

server2 `/var/tmp`: 17639862272 available bytes; 99.02% used; 110365087 free inodes.

server2 `/mnt/raid5`: 593397530624 available bytes; 95.90% used; 444957350 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 79507197952 available bytes; 95.56% used; 114068743 free inodes.

server3 `/home`: 79507197952 available bytes; 95.56% used; 114068743 free inodes.

server3 `/data`: 1349109645312 available bytes; 81.35% used; 225825660 free inodes.

server3 `/tmp`: 79507197952 available bytes; 95.56% used; 114068743 free inodes.

server3 `/var/tmp`: 79507197952 available bytes; 95.56% used; 114068743 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105879498752 available bytes; 94.09% used; 114347839 free inodes.

server4 `/home`: 105879498752 available bytes; 94.09% used; 114347839 free inodes.

server4 `/data`: 409330102272 available bytes; 94.34% used; 224821678 free inodes.

server4 `/tmp`: 105879498752 available bytes; 94.09% used; 114347839 free inodes.

server4 `/var/tmp`: 105879498752 available bytes; 94.09% used; 114347839 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
