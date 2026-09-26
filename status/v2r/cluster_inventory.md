# V2R cluster inventory

2026-09-26T23:21:14.665585+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315470327808 available bytes; 82.40% used; 112445701 free inodes.

server1 `/home`: 315470327808 available bytes; 82.40% used; 112445701 free inodes.

server1 `/tmp`: 315470327808 available bytes; 82.40% used; 112445701 free inodes.

server1 `/var/tmp`: 315470327808 available bytes; 82.40% used; 112445701 free inodes.

server1 `/mnt/raid5`: 645842141184 available bytes; 97.04% used; 337467045 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17946132480 available bytes; 99.00% used; 110367452 free inodes.

server2 `/home`: 17946132480 available bytes; 99.00% used; 110367452 free inodes.

server2 `/tmp`: 17946132480 available bytes; 99.00% used; 110367452 free inodes.

server2 `/var/tmp`: 17946132480 available bytes; 99.00% used; 110367452 free inodes.

server2 `/mnt/raid5`: 595332440064 available bytes; 95.89% used; 444959695 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 81084452864 available bytes; 95.48% used; 114069877 free inodes.

server3 `/home`: 81084452864 available bytes; 95.48% used; 114069877 free inodes.

server3 `/data`: 1349231927296 available bytes; 81.35% used; 225826483 free inodes.

server3 `/tmp`: 81084452864 available bytes; 95.48% used; 114069877 free inodes.

server3 `/var/tmp`: 81084452864 available bytes; 95.48% used; 114069877 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105897906176 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105897906176 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409603358720 available bytes; 94.34% used; 224823792 free inodes.

server4 `/tmp`: 105897906176 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105897906176 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
