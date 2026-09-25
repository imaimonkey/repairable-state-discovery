# V2R cluster inventory

2026-09-25T21:48:17.721882+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318698180608 available bytes; 82.22% used; 112476298 free inodes.

server1 `/home`: 318698180608 available bytes; 82.22% used; 112476298 free inodes.

server1 `/tmp`: 318698180608 available bytes; 82.22% used; 112476298 free inodes.

server1 `/var/tmp`: 318698180608 available bytes; 82.22% used; 112476298 free inodes.

server1 `/mnt/raid5`: 360321781760 available bytes; 98.35% used; 337539155 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22898401280 available bytes; 98.72% used; 110405682 free inodes.

server2 `/home`: 22898401280 available bytes; 98.72% used; 110405682 free inodes.

server2 `/tmp`: 22898401280 available bytes; 98.72% used; 110405682 free inodes.

server2 `/var/tmp`: 22898401280 available bytes; 98.72% used; 110405682 free inodes.

server2 `/mnt/raid5`: 300718338048 available bytes; 97.92% used; 445053870 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84368236544 available bytes; 95.29% used; 114152632 free inodes.

server3 `/home`: 84368236544 available bytes; 95.29% used; 114152632 free inodes.

server3 `/data`: 125886582784 available bytes; 98.26% used; 225806677 free inodes.

server3 `/tmp`: 84368236544 available bytes; 95.29% used; 114152632 free inodes.

server3 `/var/tmp`: 84368236544 available bytes; 95.29% used; 114152632 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105388474368 available bytes; 94.12% used; 114347329 free inodes.

server4 `/home`: 105388474368 available bytes; 94.12% used; 114347329 free inodes.

server4 `/data`: 215788978176 available bytes; 97.02% used; 224919244 free inodes.

server4 `/tmp`: 105388474368 available bytes; 94.12% used; 114347329 free inodes.

server4 `/var/tmp`: 105388474368 available bytes; 94.12% used; 114347329 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
