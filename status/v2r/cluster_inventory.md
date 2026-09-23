# V2R cluster inventory

2026-09-23T21:47:26.597890+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325715234816 available bytes; 81.83% used; 112501391 free inodes.

server1 `/home`: 325715234816 available bytes; 81.83% used; 112501391 free inodes.

server1 `/tmp`: 325715234816 available bytes; 81.83% used; 112501391 free inodes.

server1 `/var/tmp`: 325715234816 available bytes; 81.83% used; 112501391 free inodes.

server1 `/mnt/raid5`: 1388125097984 available bytes; 93.63% used; 337739915 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41113341952 available bytes; 97.71% used; 110432653 free inodes.

server2 `/home`: 41113341952 available bytes; 97.71% used; 110432653 free inodes.

server2 `/tmp`: 41113341952 available bytes; 97.71% used; 110432653 free inodes.

server2 `/var/tmp`: 41113341952 available bytes; 97.71% used; 110432653 free inodes.

server2 `/mnt/raid5`: 537980403712 available bytes; 96.28% used; 445208042 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292122996736 available bytes; 83.70% used; 114160155 free inodes.

server3 `/home`: 292122996736 available bytes; 83.70% used; 114160155 free inodes.

server3 `/data`: 82472902656 available bytes; 98.86% used; 225848117 free inodes.

server3 `/tmp`: 292122996736 available bytes; 83.70% used; 114160155 free inodes.

server3 `/var/tmp`: 292122996736 available bytes; 83.70% used; 114160155 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106468052992 available bytes; 94.06% used; 114355882 free inodes.

server4 `/home`: 106468052992 available bytes; 94.06% used; 114355882 free inodes.

server4 `/data`: 300243447808 available bytes; 95.85% used; 225447528 free inodes.

server4 `/tmp`: 106468052992 available bytes; 94.06% used; 114355882 free inodes.

server4 `/var/tmp`: 106468052992 available bytes; 94.06% used; 114355882 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
