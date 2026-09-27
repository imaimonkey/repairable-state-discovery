# V2R cluster inventory

2026-09-27T00:25:16.046895+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315159429120 available bytes; 82.42% used; 112443460 free inodes.

server1 `/home`: 315159429120 available bytes; 82.42% used; 112443460 free inodes.

server1 `/tmp`: 315159429120 available bytes; 82.42% used; 112443460 free inodes.

server1 `/var/tmp`: 315159429120 available bytes; 82.42% used; 112443460 free inodes.

server1 `/mnt/raid5`: 637707345920 available bytes; 97.07% used; 337407904 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17639354368 available bytes; 99.02% used; 110365093 free inodes.

server2 `/home`: 17639354368 available bytes; 99.02% used; 110365093 free inodes.

server2 `/tmp`: 17639354368 available bytes; 99.02% used; 110365093 free inodes.

server2 `/var/tmp`: 17639354368 available bytes; 99.02% used; 110365093 free inodes.

server2 `/mnt/raid5`: 593356742656 available bytes; 95.90% used; 444957308 free inodes.
| server3 | True | ['2', '3'] | [] |

server3 `/`: 79498723328 available bytes; 95.56% used; 114068715 free inodes.

server3 `/home`: 79498723328 available bytes; 95.56% used; 114068715 free inodes.

server3 `/data`: 1349106274304 available bytes; 81.35% used; 225825614 free inodes.

server3 `/tmp`: 79498723328 available bytes; 95.56% used; 114068715 free inodes.

server3 `/var/tmp`: 79498723328 available bytes; 95.56% used; 114068715 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105818554368 available bytes; 94.09% used; 114347829 free inodes.

server4 `/home`: 105818554368 available bytes; 94.09% used; 114347829 free inodes.

server4 `/data`: 409277616128 available bytes; 94.34% used; 224820917 free inodes.

server4 `/tmp`: 105818554368 available bytes; 94.09% used; 114347829 free inodes.

server4 `/var/tmp`: 105818554368 available bytes; 94.09% used; 114347829 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
