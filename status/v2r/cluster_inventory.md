# V2R cluster inventory

2026-09-24T07:01:29.999280+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324483448832 available bytes; 81.90% used; 112491365 free inodes.

server1 `/home`: 324483444736 available bytes; 81.90% used; 112491365 free inodes.

server1 `/tmp`: 324483436544 available bytes; 81.90% used; 112491365 free inodes.

server1 `/var/tmp`: 324483432448 available bytes; 81.90% used; 112491365 free inodes.

server1 `/mnt/raid5`: 517422772224 available bytes; 97.63% used; 337722844 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57862840320 available bytes; 96.77% used; 110431179 free inodes.

server2 `/home`: 57862840320 available bytes; 96.77% used; 110431179 free inodes.

server2 `/tmp`: 57862840320 available bytes; 96.77% used; 110431179 free inodes.

server2 `/var/tmp`: 57862840320 available bytes; 96.77% used; 110431179 free inodes.

server2 `/mnt/raid5`: 519272357888 available bytes; 96.41% used; 445191075 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126756581376 available bytes; 92.93% used; 114175146 free inodes.

server3 `/home`: 126756581376 available bytes; 92.93% used; 114175146 free inodes.

server3 `/data`: 139191824384 available bytes; 98.08% used; 225834732 free inodes.

server3 `/tmp`: 126756581376 available bytes; 92.93% used; 114175146 free inodes.

server3 `/var/tmp`: 126756581376 available bytes; 92.93% used; 114175146 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105790357504 available bytes; 94.10% used; 114349211 free inodes.

server4 `/home`: 105790357504 available bytes; 94.10% used; 114349211 free inodes.

server4 `/data`: 302802317312 available bytes; 95.82% used; 225367720 free inodes.

server4 `/tmp`: 105790357504 available bytes; 94.10% used; 114349211 free inodes.

server4 `/var/tmp`: 105790357504 available bytes; 94.10% used; 114349211 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
