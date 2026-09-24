# V2R cluster inventory

2026-09-24T07:32:17.179955+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324451426304 available bytes; 81.90% used; 112491123 free inodes.

server1 `/home`: 324451426304 available bytes; 81.90% used; 112491123 free inodes.

server1 `/tmp`: 324451426304 available bytes; 81.90% used; 112491123 free inodes.

server1 `/var/tmp`: 324451426304 available bytes; 81.90% used; 112491123 free inodes.

server1 `/mnt/raid5`: 517409931264 available bytes; 97.63% used; 337722784 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57842216960 available bytes; 96.77% used; 110431158 free inodes.

server2 `/home`: 57842216960 available bytes; 96.77% used; 110431158 free inodes.

server2 `/tmp`: 57842216960 available bytes; 96.77% used; 110431158 free inodes.

server2 `/var/tmp`: 57842216960 available bytes; 96.77% used; 110431158 free inodes.

server2 `/mnt/raid5`: 518193291264 available bytes; 96.42% used; 445180664 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 126365523968 available bytes; 92.95% used; 114149779 free inodes.

server3 `/home`: 126365523968 available bytes; 92.95% used; 114149779 free inodes.

server3 `/data`: 138730496000 available bytes; 98.08% used; 225831992 free inodes.

server3 `/tmp`: 126365523968 available bytes; 92.95% used; 114149779 free inodes.

server3 `/var/tmp`: 126365523968 available bytes; 92.95% used; 114149779 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105780645888 available bytes; 94.10% used; 114349185 free inodes.

server4 `/home`: 105780645888 available bytes; 94.10% used; 114349185 free inodes.

server4 `/data`: 285813444608 available bytes; 96.05% used; 225366883 free inodes.

server4 `/tmp`: 105780645888 available bytes; 94.10% used; 114349185 free inodes.

server4 `/var/tmp`: 105780645888 available bytes; 94.10% used; 114349185 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
