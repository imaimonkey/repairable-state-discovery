# V2R cluster inventory

2026-09-24T10:36:03.035125+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324408373248 available bytes; 81.90% used; 112489216 free inodes.

server1 `/home`: 324408373248 available bytes; 81.90% used; 112489216 free inodes.

server1 `/tmp`: 324408373248 available bytes; 81.90% used; 112489216 free inodes.

server1 `/var/tmp`: 324408373248 available bytes; 81.90% used; 112489216 free inodes.

server1 `/mnt/raid5`: 500001595392 available bytes; 97.71% used; 337697108 free inodes.
| server2 | True | ['5'] | [] |

server2 `/`: 57724211200 available bytes; 96.78% used; 110430549 free inodes.

server2 `/home`: 57724211200 available bytes; 96.78% used; 110430549 free inodes.

server2 `/tmp`: 57724211200 available bytes; 96.78% used; 110430549 free inodes.

server2 `/var/tmp`: 57724211200 available bytes; 96.78% used; 110430549 free inodes.

server2 `/mnt/raid5`: 512612069376 available bytes; 96.46% used; 445175079 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85790760960 available bytes; 95.21% used; 114199113 free inodes.

server3 `/home`: 85790760960 available bytes; 95.21% used; 114199113 free inodes.

server3 `/data`: 164187582464 available bytes; 97.73% used; 225818126 free inodes.

server3 `/tmp`: 85790760960 available bytes; 95.21% used; 114199113 free inodes.

server3 `/var/tmp`: 85790760960 available bytes; 95.21% used; 114199113 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105744318464 available bytes; 94.10% used; 114348969 free inodes.

server4 `/home`: 105744318464 available bytes; 94.10% used; 114348969 free inodes.

server4 `/data`: 153468571648 available bytes; 97.88% used; 225258370 free inodes.

server4 `/tmp`: 105744318464 available bytes; 94.10% used; 114348969 free inodes.

server4 `/var/tmp`: 105744318464 available bytes; 94.10% used; 114348969 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
