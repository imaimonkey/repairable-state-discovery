# V2R cluster inventory

2026-09-25T21:55:56.370243+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318696091648 available bytes; 82.22% used; 112476286 free inodes.

server1 `/home`: 318696091648 available bytes; 82.22% used; 112476286 free inodes.

server1 `/tmp`: 318696091648 available bytes; 82.22% used; 112476286 free inodes.

server1 `/var/tmp`: 318696091648 available bytes; 82.22% used; 112476286 free inodes.

server1 `/mnt/raid5`: 360315678720 available bytes; 98.35% used; 337539112 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22905847808 available bytes; 98.72% used; 110405684 free inodes.

server2 `/home`: 22905847808 available bytes; 98.72% used; 110405684 free inodes.

server2 `/tmp`: 22905847808 available bytes; 98.72% used; 110405684 free inodes.

server2 `/var/tmp`: 22905847808 available bytes; 98.72% used; 110405684 free inodes.

server2 `/mnt/raid5`: 300388925440 available bytes; 97.92% used; 445053681 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84366692352 available bytes; 95.29% used; 114152622 free inodes.

server3 `/home`: 84366692352 available bytes; 95.29% used; 114152622 free inodes.

server3 `/data`: 125885104128 available bytes; 98.26% used; 225806557 free inodes.

server3 `/tmp`: 84366692352 available bytes; 95.29% used; 114152622 free inodes.

server3 `/var/tmp`: 84366692352 available bytes; 95.29% used; 114152622 free inodes.
| server4 | True | ['0', '3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105321107456 available bytes; 94.12% used; 114347156 free inodes.

server4 `/home`: 105321107456 available bytes; 94.12% used; 114347156 free inodes.

server4 `/data`: 208820199424 available bytes; 97.11% used; 224919185 free inodes.

server4 `/tmp`: 105321107456 available bytes; 94.12% used; 114347156 free inodes.

server4 `/var/tmp`: 105321107456 available bytes; 94.12% used; 114347156 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
