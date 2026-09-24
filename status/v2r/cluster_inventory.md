# V2R cluster inventory

2026-09-24T03:30:29.445399+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325352591360 available bytes; 81.85% used; 112498162 free inodes.

server1 `/home`: 325352591360 available bytes; 81.85% used; 112498162 free inodes.

server1 `/tmp`: 325352591360 available bytes; 81.85% used; 112498162 free inodes.

server1 `/var/tmp`: 325352591360 available bytes; 81.85% used; 112498162 free inodes.

server1 `/mnt/raid5`: 398923100160 available bytes; 98.17% used; 337733873 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40834445312 available bytes; 97.72% used; 110431098 free inodes.

server2 `/home`: 40834445312 available bytes; 97.72% used; 110431098 free inodes.

server2 `/tmp`: 40834445312 available bytes; 97.72% used; 110431098 free inodes.

server2 `/var/tmp`: 40834445312 available bytes; 97.72% used; 110431098 free inodes.

server2 `/mnt/raid5`: 527204446208 available bytes; 96.36% used; 445197936 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292365307904 available bytes; 83.68% used; 114200778 free inodes.

server3 `/home`: 292365307904 available bytes; 83.68% used; 114200778 free inodes.

server3 `/data`: 36015181824 available bytes; 99.50% used; 225843031 free inodes.

server3 `/tmp`: 292365307904 available bytes; 83.68% used; 114200778 free inodes.

server3 `/var/tmp`: 292365307904 available bytes; 83.68% used; 114200778 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105987047424 available bytes; 94.09% used; 114349606 free inodes.

server4 `/home`: 105987047424 available bytes; 94.09% used; 114349606 free inodes.

server4 `/data`: 282661670912 available bytes; 96.09% used; 225385554 free inodes.

server4 `/tmp`: 105987047424 available bytes; 94.09% used; 114349606 free inodes.

server4 `/var/tmp`: 105987047424 available bytes; 94.09% used; 114349606 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
