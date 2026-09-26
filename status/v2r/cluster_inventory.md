# V2R cluster inventory

2026-09-26T02:53:56.414837+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318417760256 available bytes; 82.24% used; 112476263 free inodes.

server1 `/home`: 318417760256 available bytes; 82.24% used; 112476263 free inodes.

server1 `/tmp`: 318417760256 available bytes; 82.24% used; 112476263 free inodes.

server1 `/var/tmp`: 318417760256 available bytes; 82.24% used; 112476263 free inodes.

server1 `/mnt/raid5`: 331103977472 available bytes; 98.48% used; 337546003 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22935900160 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22935900160 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22935900160 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22935900160 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 288307351552 available bytes; 98.01% used; 445053895 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84310589440 available bytes; 95.30% used; 114152367 free inodes.

server3 `/home`: 84310589440 available bytes; 95.30% used; 114152367 free inodes.

server3 `/data`: 125448679424 available bytes; 98.27% used; 225831308 free inodes.

server3 `/tmp`: 84310589440 available bytes; 95.30% used; 114152367 free inodes.

server3 `/var/tmp`: 84310589440 available bytes; 95.30% used; 114152367 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105919049728 available bytes; 94.09% used; 114347153 free inodes.

server4 `/home`: 105919049728 available bytes; 94.09% used; 114347153 free inodes.

server4 `/data`: 109770326016 available bytes; 98.48% used; 224915388 free inodes.

server4 `/tmp`: 105919049728 available bytes; 94.09% used; 114347153 free inodes.

server4 `/var/tmp`: 105919049728 available bytes; 94.09% used; 114347153 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
