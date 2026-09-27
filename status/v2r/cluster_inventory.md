# V2R cluster inventory

2026-09-27T10:45:51.113494+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314429911040 available bytes; 82.46% used; 112440708 free inodes.

server1 `/home`: 314429911040 available bytes; 82.46% used; 112440708 free inodes.

server1 `/tmp`: 314429911040 available bytes; 82.46% used; 112440708 free inodes.

server1 `/var/tmp`: 314429911040 available bytes; 82.46% used; 112440708 free inodes.

server1 `/mnt/raid5`: 635410915328 available bytes; 97.09% used; 337424414 free inodes.
| server2 | True | ['1', '2', '7'] | [] |

server2 `/`: 16497971200 available bytes; 99.08% used; 110355942 free inodes.

server2 `/home`: 16497971200 available bytes; 99.08% used; 110355942 free inodes.

server2 `/tmp`: 16497971200 available bytes; 99.08% used; 110355942 free inodes.

server2 `/var/tmp`: 16497971200 available bytes; 99.08% used; 110355942 free inodes.

server2 `/mnt/raid5`: 571333939200 available bytes; 96.05% used; 444738426 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 78544334848 available bytes; 95.62% used; 114062823 free inodes.

server3 `/home`: 78544334848 available bytes; 95.62% used; 114062823 free inodes.

server3 `/data`: 1332059394048 available bytes; 81.59% used; 225760722 free inodes.

server3 `/tmp`: 78544334848 available bytes; 95.62% used; 114062823 free inodes.

server3 `/var/tmp`: 78544334848 available bytes; 95.62% used; 114062823 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111031513088 available bytes; 93.80% used; 114372822 free inodes.

server4 `/home`: 111031513088 available bytes; 93.80% used; 114372822 free inodes.

server4 `/data`: 363228815360 available bytes; 94.98% used; 224766858 free inodes.

server4 `/tmp`: 111031513088 available bytes; 93.80% used; 114372822 free inodes.

server4 `/var/tmp`: 111031513088 available bytes; 93.80% used; 114372822 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
