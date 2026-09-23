# V2R cluster inventory

2026-09-23T22:36:44.622647+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325696036864 available bytes; 81.83% used; 112501393 free inodes.

server1 `/home`: 325696036864 available bytes; 81.83% used; 112501393 free inodes.

server1 `/tmp`: 325696036864 available bytes; 81.83% used; 112501393 free inodes.

server1 `/var/tmp`: 325696036864 available bytes; 81.83% used; 112501393 free inodes.

server1 `/mnt/raid5`: 1388099223552 available bytes; 93.63% used; 337739824 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41083707392 available bytes; 97.71% used; 110432629 free inodes.

server2 `/home`: 41083707392 available bytes; 97.71% used; 110432629 free inodes.

server2 `/tmp`: 41083707392 available bytes; 97.71% used; 110432629 free inodes.

server2 `/var/tmp`: 41083707392 available bytes; 97.71% used; 110432629 free inodes.

server2 `/mnt/raid5`: 536437628928 available bytes; 96.29% used; 445206355 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292794884096 available bytes; 83.66% used; 114211656 free inodes.

server3 `/home`: 292794884096 available bytes; 83.66% used; 114211656 free inodes.

server3 `/data`: 82431352832 available bytes; 98.86% used; 225847245 free inodes.

server3 `/tmp`: 292794884096 available bytes; 83.66% used; 114211656 free inodes.

server3 `/var/tmp`: 292794884096 available bytes; 83.66% used; 114211656 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106358128640 available bytes; 94.06% used; 114354291 free inodes.

server4 `/home`: 106358128640 available bytes; 94.06% used; 114354291 free inodes.

server4 `/data`: 300065226752 available bytes; 95.85% used; 225435944 free inodes.

server4 `/tmp`: 106358128640 available bytes; 94.06% used; 114354291 free inodes.

server4 `/var/tmp`: 106358128640 available bytes; 94.06% used; 114354291 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
