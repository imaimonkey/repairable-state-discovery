# V2R cluster inventory

2026-09-23T23:15:15.022490+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325665968128 available bytes; 81.83% used; 112501624 free inodes.

server1 `/home`: 325665968128 available bytes; 81.83% used; 112501624 free inodes.

server1 `/tmp`: 325665968128 available bytes; 81.83% used; 112501624 free inodes.

server1 `/var/tmp`: 325665968128 available bytes; 81.83% used; 112501624 free inodes.

server1 `/mnt/raid5`: 1387846828032 available bytes; 93.63% used; 337739865 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41052073984 available bytes; 97.71% used; 110432608 free inodes.

server2 `/home`: 41052073984 available bytes; 97.71% used; 110432608 free inodes.

server2 `/tmp`: 41052073984 available bytes; 97.71% used; 110432608 free inodes.

server2 `/var/tmp`: 41052073984 available bytes; 97.71% used; 110432608 free inodes.

server2 `/mnt/raid5`: 534942855168 available bytes; 96.30% used; 445206038 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292248039424 available bytes; 83.69% used; 114171241 free inodes.

server3 `/home`: 292248039424 available bytes; 83.69% used; 114171241 free inodes.

server3 `/data`: 82328231936 available bytes; 98.86% used; 225846036 free inodes.

server3 `/tmp`: 292248039424 available bytes; 83.69% used; 114171241 free inodes.

server3 `/var/tmp`: 292248039424 available bytes; 83.69% used; 114171241 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106262638592 available bytes; 94.07% used; 114352899 free inodes.

server4 `/home`: 106262638592 available bytes; 94.07% used; 114352899 free inodes.

server4 `/data`: 298022895616 available bytes; 95.88% used; 225428816 free inodes.

server4 `/tmp`: 106262638592 available bytes; 94.07% used; 114352899 free inodes.

server4 `/var/tmp`: 106262638592 available bytes; 94.07% used; 114352899 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
