# V2R cluster inventory

2026-09-23T23:16:47.483218+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325665714176 available bytes; 81.83% used; 112501617 free inodes.

server1 `/home`: 325665714176 available bytes; 81.83% used; 112501617 free inodes.

server1 `/tmp`: 325665714176 available bytes; 81.83% used; 112501617 free inodes.

server1 `/var/tmp`: 325665714176 available bytes; 81.83% used; 112501617 free inodes.

server1 `/mnt/raid5`: 1387845410816 available bytes; 93.63% used; 337739862 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41050427392 available bytes; 97.71% used; 110432607 free inodes.

server2 `/home`: 41050427392 available bytes; 97.71% used; 110432607 free inodes.

server2 `/tmp`: 41050427392 available bytes; 97.71% used; 110432607 free inodes.

server2 `/var/tmp`: 41050427392 available bytes; 97.71% used; 110432607 free inodes.

server2 `/mnt/raid5`: 534906150912 available bytes; 96.30% used; 445205936 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292247646208 available bytes; 83.69% used; 114171241 free inodes.

server3 `/home`: 292247646208 available bytes; 83.69% used; 114171241 free inodes.

server3 `/data`: 82327056384 available bytes; 98.86% used; 225846019 free inodes.

server3 `/tmp`: 292247646208 available bytes; 83.69% used; 114171241 free inodes.

server3 `/var/tmp`: 292247646208 available bytes; 83.69% used; 114171241 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106258894848 available bytes; 94.07% used; 114352839 free inodes.

server4 `/home`: 106258894848 available bytes; 94.07% used; 114352839 free inodes.

server4 `/data`: 296955629568 available bytes; 95.90% used; 225428373 free inodes.

server4 `/tmp`: 106258894848 available bytes; 94.07% used; 114352839 free inodes.

server4 `/var/tmp`: 106258894848 available bytes; 94.07% used; 114352839 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
