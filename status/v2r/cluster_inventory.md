# V2R cluster inventory

2026-09-26T22:03:29.841451+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315470938112 available bytes; 82.40% used; 112445684 free inodes.

server1 `/home`: 315470938112 available bytes; 82.40% used; 112445684 free inodes.

server1 `/tmp`: 315470938112 available bytes; 82.40% used; 112445684 free inodes.

server1 `/var/tmp`: 315470938112 available bytes; 82.40% used; 112445684 free inodes.

server1 `/mnt/raid5`: 645854461952 available bytes; 97.04% used; 337467237 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17949859840 available bytes; 99.00% used; 110367515 free inodes.

server2 `/home`: 17949859840 available bytes; 99.00% used; 110367515 free inodes.

server2 `/tmp`: 17949859840 available bytes; 99.00% used; 110367515 free inodes.

server2 `/var/tmp`: 17949859840 available bytes; 99.00% used; 110367515 free inodes.

server2 `/mnt/raid5`: 597809176576 available bytes; 95.87% used; 444961828 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81081311232 available bytes; 95.48% used; 114069855 free inodes.

server3 `/home`: 81081311232 available bytes; 95.48% used; 114069855 free inodes.

server3 `/data`: 1349262675968 available bytes; 81.35% used; 225827339 free inodes.

server3 `/tmp`: 81081311232 available bytes; 95.48% used; 114069855 free inodes.

server3 `/var/tmp`: 81081311232 available bytes; 95.48% used; 114069855 free inodes.
| server4 | True | ['2', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105899868160 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105899868160 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409654980608 available bytes; 94.34% used; 224823821 free inodes.

server4 `/tmp`: 105899868160 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105899868160 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
