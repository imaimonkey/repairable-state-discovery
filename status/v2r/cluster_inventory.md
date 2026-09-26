# V2R cluster inventory

2026-09-26T03:12:16.249731+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318416691200 available bytes; 82.24% used; 112476252 free inodes.

server1 `/home`: 318416691200 available bytes; 82.24% used; 112476252 free inodes.

server1 `/tmp`: 318416691200 available bytes; 82.24% used; 112476252 free inodes.

server1 `/var/tmp`: 318416691200 available bytes; 82.24% used; 112476252 free inodes.

server1 `/mnt/raid5`: 331055206400 available bytes; 98.48% used; 337545897 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22938816512 available bytes; 98.72% used; 110406208 free inodes.

server2 `/home`: 22938816512 available bytes; 98.72% used; 110406208 free inodes.

server2 `/tmp`: 22938816512 available bytes; 98.72% used; 110406208 free inodes.

server2 `/var/tmp`: 22938816512 available bytes; 98.72% used; 110406208 free inodes.

server2 `/mnt/raid5`: 287745839104 available bytes; 98.01% used; 445052987 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84312006656 available bytes; 95.30% used; 114152352 free inodes.

server3 `/home`: 84312006656 available bytes; 95.30% used; 114152352 free inodes.

server3 `/data`: 125437886464 available bytes; 98.27% used; 225830919 free inodes.

server3 `/tmp`: 84312006656 available bytes; 95.30% used; 114152352 free inodes.

server3 `/var/tmp`: 84312006656 available bytes; 95.30% used; 114152352 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105918394368 available bytes; 94.09% used; 114347138 free inodes.

server4 `/home`: 105918394368 available bytes; 94.09% used; 114347138 free inodes.

server4 `/data`: 109092134912 available bytes; 98.49% used; 224914854 free inodes.

server4 `/tmp`: 105918394368 available bytes; 94.09% used; 114347138 free inodes.

server4 `/var/tmp`: 105918394368 available bytes; 94.09% used; 114347138 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
