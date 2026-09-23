# V2R cluster inventory

2026-09-23T15:30:08.717566+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['7'] | [] |

server2 `/`: 41430872064 available bytes; 97.69% used; 110435179 free inodes.

server2 `/home`: 41430872064 available bytes; 97.69% used; 110435179 free inodes.

server2 `/tmp`: 41430872064 available bytes; 97.69% used; 110435179 free inodes.

server2 `/var/tmp`: 41430872064 available bytes; 97.69% used; 110435179 free inodes.

server2 `/mnt/raid5`: 550771073024 available bytes; 96.19% used; 445223770 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] |

server3 `/`: 377614819328 available bytes; 78.93% used; 114304185 free inodes.

server3 `/home`: 377614819328 available bytes; 78.93% used; 114304185 free inodes.

server3 `/data`: 124958535680 available bytes; 98.27% used; 225840810 free inodes.

server3 `/tmp`: 377614819328 available bytes; 78.93% used; 114304185 free inodes.

server3 `/var/tmp`: 377614819328 available bytes; 78.93% used; 114304185 free inodes.
| server4 | True | ['1', '2', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111538724864 available bytes; 93.78% used; 114375948 free inodes.

server4 `/home`: 111538724864 available bytes; 93.78% used; 114375948 free inodes.

server4 `/data`: 38878789632 available bytes; 99.46% used; 225495090 free inodes.

server4 `/tmp`: 111538724864 available bytes; 93.78% used; 114375948 free inodes.

server4 `/var/tmp`: 111538724864 available bytes; 93.78% used; 114375948 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
