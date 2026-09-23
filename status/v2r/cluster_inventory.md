# V2R cluster inventory

2026-09-23T22:07:29.443302+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325708013568 available bytes; 81.83% used; 112501413 free inodes.

server1 `/home`: 325708013568 available bytes; 81.83% used; 112501413 free inodes.

server1 `/tmp`: 325708013568 available bytes; 81.83% used; 112501413 free inodes.

server1 `/var/tmp`: 325708013568 available bytes; 81.83% used; 112501413 free inodes.

server1 `/mnt/raid5`: 1388115525632 available bytes; 93.63% used; 337739877 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41097822208 available bytes; 97.71% used; 110432655 free inodes.

server2 `/home`: 41097822208 available bytes; 97.71% used; 110432655 free inodes.

server2 `/tmp`: 41097822208 available bytes; 97.71% used; 110432655 free inodes.

server2 `/var/tmp`: 41097822208 available bytes; 97.71% used; 110432655 free inodes.

server2 `/mnt/raid5`: 537368698880 available bytes; 96.29% used; 445207693 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292730150912 available bytes; 83.66% used; 114201647 free inodes.

server3 `/home`: 292730150912 available bytes; 83.66% used; 114201647 free inodes.

server3 `/data`: 82450595840 available bytes; 98.86% used; 225847735 free inodes.

server3 `/tmp`: 292730150912 available bytes; 83.66% used; 114201647 free inodes.

server3 `/var/tmp`: 292730150912 available bytes; 83.66% used; 114201647 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106433236992 available bytes; 94.06% used; 114355355 free inodes.

server4 `/home`: 106433236992 available bytes; 94.06% used; 114355355 free inodes.

server4 `/data`: 300176883712 available bytes; 95.85% used; 225443050 free inodes.

server4 `/tmp`: 106433236992 available bytes; 94.06% used; 114355355 free inodes.

server4 `/var/tmp`: 106433236992 available bytes; 94.06% used; 114355355 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
