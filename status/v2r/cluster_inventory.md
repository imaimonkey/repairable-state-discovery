# V2R cluster inventory

2026-09-23T22:18:16.098363+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325705158656 available bytes; 81.83% used; 112501405 free inodes.

server1 `/home`: 325705158656 available bytes; 81.83% used; 112501405 free inodes.

server1 `/tmp`: 325705158656 available bytes; 81.83% used; 112501405 free inodes.

server1 `/var/tmp`: 325705158656 available bytes; 81.83% used; 112501405 free inodes.

server1 `/mnt/raid5`: 1375429615616 available bytes; 93.69% used; 337739860 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41092427776 available bytes; 97.71% used; 110432648 free inodes.

server2 `/home`: 41092427776 available bytes; 97.71% used; 110432648 free inodes.

server2 `/tmp`: 41092427776 available bytes; 97.71% used; 110432648 free inodes.

server2 `/var/tmp`: 41092427776 available bytes; 97.71% used; 110432648 free inodes.

server2 `/mnt/raid5`: 536498982912 available bytes; 96.29% used; 445207109 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293029961728 available bytes; 83.65% used; 114223240 free inodes.

server3 `/home`: 293029961728 available bytes; 83.65% used; 114223240 free inodes.

server3 `/data`: 82441039872 available bytes; 98.86% used; 225847557 free inodes.

server3 `/tmp`: 293029961728 available bytes; 83.65% used; 114223240 free inodes.

server3 `/var/tmp`: 293029961728 available bytes; 83.65% used; 114223240 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106408857600 available bytes; 94.06% used; 114354967 free inodes.

server4 `/home`: 106408857600 available bytes; 94.06% used; 114354967 free inodes.

server4 `/data`: 300117925888 available bytes; 95.85% used; 225439941 free inodes.

server4 `/tmp`: 106408857600 available bytes; 94.06% used; 114354967 free inodes.

server4 `/var/tmp`: 106408857600 available bytes; 94.06% used; 114354967 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
