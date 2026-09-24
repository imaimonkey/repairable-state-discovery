# V2R cluster inventory

2026-09-24T07:29:10.650791+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324451655680 available bytes; 81.90% used; 112491152 free inodes.

server1 `/home`: 324451655680 available bytes; 81.90% used; 112491152 free inodes.

server1 `/tmp`: 324451655680 available bytes; 81.90% used; 112491152 free inodes.

server1 `/var/tmp`: 324451655680 available bytes; 81.90% used; 112491152 free inodes.

server1 `/mnt/raid5`: 517411737600 available bytes; 97.63% used; 337722800 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57844477952 available bytes; 96.77% used; 110431166 free inodes.

server2 `/home`: 57844477952 available bytes; 96.77% used; 110431166 free inodes.

server2 `/tmp`: 57844477952 available bytes; 96.77% used; 110431166 free inodes.

server2 `/var/tmp`: 57844477952 available bytes; 96.77% used; 110431166 free inodes.

server2 `/mnt/raid5`: 518312464384 available bytes; 96.42% used; 445180964 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 126453600256 available bytes; 92.94% used; 114160869 free inodes.

server3 `/home`: 126453600256 available bytes; 92.94% used; 114160869 free inodes.

server3 `/data`: 138803191808 available bytes; 98.08% used; 225834140 free inodes.

server3 `/tmp`: 126453600256 available bytes; 92.94% used; 114160869 free inodes.

server3 `/var/tmp`: 126453600256 available bytes; 92.94% used; 114160869 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105780805632 available bytes; 94.10% used; 114349193 free inodes.

server4 `/home`: 105780805632 available bytes; 94.10% used; 114349193 free inodes.

server4 `/data`: 285870059520 available bytes; 96.05% used; 225366893 free inodes.

server4 `/tmp`: 105780805632 available bytes; 94.10% used; 114349193 free inodes.

server4 `/var/tmp`: 105780805632 available bytes; 94.10% used; 114349193 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
