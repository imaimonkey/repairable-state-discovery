# V2R cluster inventory

2026-09-23T15:19:10.423310+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['7'] | [] |

server2 `/`: 41433636864 available bytes; 97.69% used; 110435179 free inodes.

server2 `/home`: 41433636864 available bytes; 97.69% used; 110435179 free inodes.

server2 `/tmp`: 41433636864 available bytes; 97.69% used; 110435179 free inodes.

server2 `/var/tmp`: 41433636864 available bytes; 97.69% used; 110435179 free inodes.

server2 `/mnt/raid5`: 551111282688 available bytes; 96.19% used; 445224217 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 377643929600 available bytes; 78.93% used; 114304624 free inodes.

server3 `/home`: 377643929600 available bytes; 78.93% used; 114304624 free inodes.

server3 `/data`: 124968169472 available bytes; 98.27% used; 225841009 free inodes.

server3 `/tmp`: 377643929600 available bytes; 78.93% used; 114304624 free inodes.

server3 `/var/tmp`: 377643929600 available bytes; 78.93% used; 114304624 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111672868864 available bytes; 93.77% used; 114378451 free inodes.

server4 `/home`: 111672868864 available bytes; 93.77% used; 114378451 free inodes.

server4 `/data`: 38978887680 available bytes; 99.46% used; 225495241 free inodes.

server4 `/tmp`: 111672868864 available bytes; 93.77% used; 114378451 free inodes.

server4 `/var/tmp`: 111672868864 available bytes; 93.77% used; 114378451 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
