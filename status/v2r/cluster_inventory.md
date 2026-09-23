# V2R cluster inventory

2026-09-23T22:01:19.541838+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325710651392 available bytes; 81.83% used; 112501416 free inodes.

server1 `/home`: 325710651392 available bytes; 81.83% used; 112501416 free inodes.

server1 `/tmp`: 325710651392 available bytes; 81.83% used; 112501416 free inodes.

server1 `/var/tmp`: 325710651392 available bytes; 81.83% used; 112501416 free inodes.

server1 `/mnt/raid5`: 1388122034176 available bytes; 93.63% used; 337739894 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41102196736 available bytes; 97.71% used; 110432653 free inodes.

server2 `/home`: 41102196736 available bytes; 97.71% used; 110432653 free inodes.

server2 `/tmp`: 41102196736 available bytes; 97.71% used; 110432653 free inodes.

server2 `/var/tmp`: 41102196736 available bytes; 97.71% used; 110432653 free inodes.

server2 `/mnt/raid5`: 537548939264 available bytes; 96.29% used; 445207616 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293045284864 available bytes; 83.65% used; 114223410 free inodes.

server3 `/home`: 293045284864 available bytes; 83.65% used; 114223410 free inodes.

server3 `/data`: 82455949312 available bytes; 98.86% used; 225847871 free inodes.

server3 `/tmp`: 293045284864 available bytes; 83.65% used; 114223410 free inodes.

server3 `/var/tmp`: 293045284864 available bytes; 83.65% used; 114223410 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106447298560 available bytes; 94.06% used; 114355581 free inodes.

server4 `/home`: 106447298560 available bytes; 94.06% used; 114355581 free inodes.

server4 `/data`: 300202987520 available bytes; 95.85% used; 225444854 free inodes.

server4 `/tmp`: 106447298560 available bytes; 94.06% used; 114355581 free inodes.

server4 `/var/tmp`: 106447298560 available bytes; 94.06% used; 114355581 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
