# V2R cluster inventory

2026-09-26T03:03:06.426634+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318416850944 available bytes; 82.24% used; 112476267 free inodes.

server1 `/home`: 318416850944 available bytes; 82.24% used; 112476267 free inodes.

server1 `/tmp`: 318416850944 available bytes; 82.24% used; 112476267 free inodes.

server1 `/var/tmp`: 318416850944 available bytes; 82.24% used; 112476267 free inodes.

server1 `/mnt/raid5`: 331075371008 available bytes; 98.48% used; 337545945 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22940581888 available bytes; 98.72% used; 110406212 free inodes.

server2 `/home`: 22940581888 available bytes; 98.72% used; 110406212 free inodes.

server2 `/tmp`: 22940581888 available bytes; 98.72% used; 110406212 free inodes.

server2 `/var/tmp`: 22940581888 available bytes; 98.72% used; 110406212 free inodes.

server2 `/mnt/raid5`: 288009289728 available bytes; 98.01% used; 445053358 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84308615168 available bytes; 95.30% used; 114152368 free inodes.

server3 `/home`: 84308615168 available bytes; 95.30% used; 114152368 free inodes.

server3 `/data`: 125440385024 available bytes; 98.27% used; 225831121 free inodes.

server3 `/tmp`: 84308615168 available bytes; 95.30% used; 114152368 free inodes.

server3 `/var/tmp`: 84308615168 available bytes; 95.30% used; 114152368 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105885188096 available bytes; 94.09% used; 114347063 free inodes.

server4 `/home`: 105885188096 available bytes; 94.09% used; 114347063 free inodes.

server4 `/data`: 109659811840 available bytes; 98.48% used; 224915301 free inodes.

server4 `/tmp`: 105885188096 available bytes; 94.09% used; 114347063 free inodes.

server4 `/var/tmp`: 105885188096 available bytes; 94.09% used; 114347063 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
