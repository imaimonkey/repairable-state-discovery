# V2R cluster inventory

2026-09-27T03:11:27.240156+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315084537856 available bytes; 82.42% used; 112443051 free inodes.

server1 `/home`: 315084537856 available bytes; 82.42% used; 112443051 free inodes.

server1 `/tmp`: 315084537856 available bytes; 82.42% used; 112443051 free inodes.

server1 `/var/tmp`: 315084537856 available bytes; 82.42% used; 112443051 free inodes.

server1 `/mnt/raid5`: 636792307712 available bytes; 97.08% used; 337401383 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17627279360 available bytes; 99.02% used; 110365007 free inodes.

server2 `/home`: 17627279360 available bytes; 99.02% used; 110365007 free inodes.

server2 `/tmp`: 17627279360 available bytes; 99.02% used; 110365007 free inodes.

server2 `/var/tmp`: 17627279360 available bytes; 99.02% used; 110365007 free inodes.

server2 `/mnt/raid5`: 579764813824 available bytes; 95.99% used; 444883436 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78706630656 available bytes; 95.61% used; 114062954 free inodes.

server3 `/home`: 78706630656 available bytes; 95.61% used; 114062954 free inodes.

server3 `/data`: 1336532869120 available bytes; 81.53% used; 225761710 free inodes.

server3 `/tmp`: 78706630656 available bytes; 95.61% used; 114062954 free inodes.

server3 `/var/tmp`: 78706630656 available bytes; 95.61% used; 114062954 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111028686848 available bytes; 93.80% used; 114372980 free inodes.

server4 `/home`: 111028686848 available bytes; 93.80% used; 114372980 free inodes.

server4 `/data`: 393632395264 available bytes; 94.56% used; 224781008 free inodes.

server4 `/tmp`: 111028686848 available bytes; 93.80% used; 114372980 free inodes.

server4 `/var/tmp`: 111028686848 available bytes; 93.80% used; 114372980 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
