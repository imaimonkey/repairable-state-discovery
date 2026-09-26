# V2R cluster inventory

2026-09-26T03:10:44.561912+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318416871424 available bytes; 82.24% used; 112476258 free inodes.

server1 `/home`: 318416871424 available bytes; 82.24% used; 112476258 free inodes.

server1 `/tmp`: 318416871424 available bytes; 82.24% used; 112476258 free inodes.

server1 `/var/tmp`: 318416871424 available bytes; 82.24% used; 112476258 free inodes.

server1 `/mnt/raid5`: 331059195904 available bytes; 98.48% used; 337545917 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22939209728 available bytes; 98.72% used; 110406208 free inodes.

server2 `/home`: 22939209728 available bytes; 98.72% used; 110406208 free inodes.

server2 `/tmp`: 22939209728 available bytes; 98.72% used; 110406208 free inodes.

server2 `/var/tmp`: 22939209728 available bytes; 98.72% used; 110406208 free inodes.

server2 `/mnt/raid5`: 287259254784 available bytes; 98.02% used; 445053142 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84308131840 available bytes; 95.30% used; 114152358 free inodes.

server3 `/home`: 84308131840 available bytes; 95.30% used; 114152358 free inodes.

server3 `/data`: 125438763008 available bytes; 98.27% used; 225830960 free inodes.

server3 `/tmp`: 84308131840 available bytes; 95.30% used; 114152358 free inodes.

server3 `/var/tmp`: 84308131840 available bytes; 95.30% used; 114152358 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105920450560 available bytes; 94.09% used; 114347147 free inodes.

server4 `/home`: 105920450560 available bytes; 94.09% used; 114347147 free inodes.

server4 `/data`: 109092925440 available bytes; 98.49% used; 224914863 free inodes.

server4 `/tmp`: 105920450560 available bytes; 94.09% used; 114347147 free inodes.

server4 `/var/tmp`: 105920450560 available bytes; 94.09% used; 114347147 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
