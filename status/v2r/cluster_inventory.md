# V2R cluster inventory

2026-09-23T21:41:17.320019+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325713969152 available bytes; 81.83% used; 112501425 free inodes.

server1 `/home`: 325713969152 available bytes; 81.83% used; 112501425 free inodes.

server1 `/tmp`: 325713969152 available bytes; 81.83% used; 112501425 free inodes.

server1 `/var/tmp`: 325713969152 available bytes; 81.83% used; 112501425 free inodes.

server1 `/mnt/raid5`: 1388131020800 available bytes; 93.63% used; 337739934 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41117003776 available bytes; 97.71% used; 110432674 free inodes.

server2 `/home`: 41117003776 available bytes; 97.71% used; 110432674 free inodes.

server2 `/tmp`: 41117003776 available bytes; 97.71% used; 110432674 free inodes.

server2 `/var/tmp`: 41117003776 available bytes; 97.71% used; 110432674 free inodes.

server2 `/mnt/raid5`: 538174173184 available bytes; 96.28% used; 445208494 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292647346176 available bytes; 83.67% used; 114189602 free inodes.

server3 `/home`: 292647346176 available bytes; 83.67% used; 114189602 free inodes.

server3 `/data`: 52266852352 available bytes; 99.28% used; 225848569 free inodes.

server3 `/tmp`: 292647346176 available bytes; 83.67% used; 114189602 free inodes.

server3 `/var/tmp`: 292647346176 available bytes; 83.67% used; 114189602 free inodes.
| server4 | True | ['0', '2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106474520576 available bytes; 94.06% used; 114355987 free inodes.

server4 `/home`: 106474520576 available bytes; 94.06% used; 114355987 free inodes.

server4 `/data`: 300258054144 available bytes; 95.85% used; 225448704 free inodes.

server4 `/tmp`: 106474520576 available bytes; 94.06% used; 114355987 free inodes.

server4 `/var/tmp`: 106474520576 available bytes; 94.06% used; 114355987 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
