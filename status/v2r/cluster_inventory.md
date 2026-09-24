# V2R cluster inventory

2026-09-24T07:29:33.977283+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324452782080 available bytes; 81.90% used; 112491152 free inodes.

server1 `/home`: 324452782080 available bytes; 81.90% used; 112491152 free inodes.

server1 `/tmp`: 324452782080 available bytes; 81.90% used; 112491152 free inodes.

server1 `/var/tmp`: 324452782080 available bytes; 81.90% used; 112491152 free inodes.

server1 `/mnt/raid5`: 517411491840 available bytes; 97.63% used; 337722794 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57844477952 available bytes; 96.77% used; 110431166 free inodes.

server2 `/home`: 57844477952 available bytes; 96.77% used; 110431166 free inodes.

server2 `/tmp`: 57844477952 available bytes; 96.77% used; 110431166 free inodes.

server2 `/var/tmp`: 57844477952 available bytes; 96.77% used; 110431166 free inodes.

server2 `/mnt/raid5`: 518296645632 available bytes; 96.42% used; 445180947 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126421254144 available bytes; 92.95% used; 114158817 free inodes.

server3 `/home`: 126421254144 available bytes; 92.95% used; 114158817 free inodes.

server3 `/data`: 138802909184 available bytes; 98.08% used; 225834126 free inodes.

server3 `/tmp`: 126421254144 available bytes; 92.95% used; 114158817 free inodes.

server3 `/var/tmp`: 126421254144 available bytes; 92.95% used; 114158817 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780789248 available bytes; 94.10% used; 114349193 free inodes.

server4 `/home`: 105780789248 available bytes; 94.10% used; 114349193 free inodes.

server4 `/data`: 285869592576 available bytes; 96.05% used; 225366893 free inodes.

server4 `/tmp`: 105780789248 available bytes; 94.10% used; 114349193 free inodes.

server4 `/var/tmp`: 105780789248 available bytes; 94.10% used; 114349193 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
