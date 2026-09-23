# V2R cluster inventory

2026-09-23T22:42:53.933943+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325747970048 available bytes; 81.83% used; 112501731 free inodes.

server1 `/home`: 325747970048 available bytes; 81.83% used; 112501731 free inodes.

server1 `/tmp`: 325747970048 available bytes; 81.83% used; 112501731 free inodes.

server1 `/var/tmp`: 325747970048 available bytes; 81.83% used; 112501731 free inodes.

server1 `/mnt/raid5`: 1388119183360 available bytes; 93.63% used; 337739974 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41074515968 available bytes; 97.71% used; 110432625 free inodes.

server2 `/home`: 41074515968 available bytes; 97.71% used; 110432625 free inodes.

server2 `/tmp`: 41074515968 available bytes; 97.71% used; 110432625 free inodes.

server2 `/var/tmp`: 41074515968 available bytes; 97.71% used; 110432625 free inodes.

server2 `/mnt/raid5`: 536288018432 available bytes; 96.29% used; 445206534 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 293066686464 available bytes; 83.65% used; 114223170 free inodes.

server3 `/home`: 293066686464 available bytes; 83.65% used; 114223170 free inodes.

server3 `/data`: 82450341888 available bytes; 98.86% used; 225847278 free inodes.

server3 `/tmp`: 293066686464 available bytes; 83.65% used; 114223170 free inodes.

server3 `/var/tmp`: 293066686464 available bytes; 83.65% used; 114223170 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106344321024 available bytes; 94.07% used; 114354069 free inodes.

server4 `/home`: 106344321024 available bytes; 94.07% used; 114354069 free inodes.

server4 `/data`: 300119293952 available bytes; 95.85% used; 225435319 free inodes.

server4 `/tmp`: 106344321024 available bytes; 94.07% used; 114354069 free inodes.

server4 `/var/tmp`: 106344321024 available bytes; 94.07% used; 114354069 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
