# V2R cluster inventory

2026-09-23T12:02:06.411763+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['6'] | [] |

server2 `/`: 41817743360 available bytes; 97.67% used; 110436697 free inodes.

server2 `/home`: 41817743360 available bytes; 97.67% used; 110436697 free inodes.

server2 `/tmp`: 41817743360 available bytes; 97.67% used; 110436697 free inodes.

server2 `/var/tmp`: 41817743360 available bytes; 97.67% used; 110436697 free inodes.

server2 `/mnt/raid5`: 557590306816 available bytes; 96.15% used; 445231363 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 380037103616 available bytes; 78.79% used; 114346185 free inodes.

server3 `/home`: 380037103616 available bytes; 78.79% used; 114346185 free inodes.

server3 `/data`: 137494499328 available bytes; 98.10% used; 225864246 free inodes.

server3 `/tmp`: 380037103616 available bytes; 78.79% used; 114346185 free inodes.

server3 `/var/tmp`: 380037103616 available bytes; 78.79% used; 114346185 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111605137408 available bytes; 93.77% used; 114379003 free inodes.

server4 `/home`: 111605137408 available bytes; 93.77% used; 114379003 free inodes.

server4 `/data`: 65721548800 available bytes; 99.09% used; 225411578 free inodes.

server4 `/tmp`: 111605137408 available bytes; 93.77% used; 114379003 free inodes.

server4 `/var/tmp`: 111605137408 available bytes; 93.77% used; 114379003 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
