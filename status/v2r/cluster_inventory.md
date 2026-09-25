# V2R cluster inventory

2026-09-25T21:49:49.678202+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318697746432 available bytes; 82.22% used; 112476286 free inodes.

server1 `/home`: 318697746432 available bytes; 82.22% used; 112476286 free inodes.

server1 `/tmp`: 318697746432 available bytes; 82.22% used; 112476286 free inodes.

server1 `/var/tmp`: 318697746432 available bytes; 82.22% used; 112476286 free inodes.

server1 `/mnt/raid5`: 360323350528 available bytes; 98.35% used; 337539152 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22898274304 available bytes; 98.72% used; 110405682 free inodes.

server2 `/home`: 22898274304 available bytes; 98.72% used; 110405682 free inodes.

server2 `/tmp`: 22898274304 available bytes; 98.72% used; 110405682 free inodes.

server2 `/var/tmp`: 22898274304 available bytes; 98.72% used; 110405682 free inodes.

server2 `/mnt/raid5`: 300697927680 available bytes; 97.92% used; 445054151 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84367925248 available bytes; 95.29% used; 114152626 free inodes.

server3 `/home`: 84367925248 available bytes; 95.29% used; 114152626 free inodes.

server3 `/data`: 125884784640 available bytes; 98.26% used; 225806661 free inodes.

server3 `/tmp`: 84367925248 available bytes; 95.29% used; 114152626 free inodes.

server3 `/var/tmp`: 84367925248 available bytes; 95.29% used; 114152626 free inodes.
| server4 | True | ['2', '3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105354858496 available bytes; 94.12% used; 114347242 free inodes.

server4 `/home`: 105354858496 available bytes; 94.12% used; 114347242 free inodes.

server4 `/data`: 208883212288 available bytes; 97.11% used; 224919204 free inodes.

server4 `/tmp`: 105354858496 available bytes; 94.12% used; 114347242 free inodes.

server4 `/var/tmp`: 105354858496 available bytes; 94.12% used; 114347242 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
