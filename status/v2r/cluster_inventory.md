# V2R cluster inventory

2026-09-26T07:35:41.388750+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318769090560 available bytes; 82.22% used; 112476291 free inodes.

server1 `/home`: 318769090560 available bytes; 82.22% used; 112476291 free inodes.

server1 `/tmp`: 318769090560 available bytes; 82.22% used; 112476291 free inodes.

server1 `/var/tmp`: 318769090560 available bytes; 82.22% used; 112476291 free inodes.

server1 `/mnt/raid5`: 219225866240 available bytes; 98.99% used; 337539217 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22316924928 available bytes; 98.76% used; 110403927 free inodes.

server2 `/home`: 22316924928 available bytes; 98.76% used; 110403927 free inodes.

server2 `/tmp`: 22316924928 available bytes; 98.76% used; 110403927 free inodes.

server2 `/var/tmp`: 22316924928 available bytes; 98.76% used; 110403927 free inodes.

server2 `/mnt/raid5`: 270485757952 available bytes; 98.13% used; 445026574 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82680934400 available bytes; 95.39% used; 114110899 free inodes.

server3 `/home`: 82680934400 available bytes; 95.39% used; 114110899 free inodes.

server3 `/data`: 123976314880 available bytes; 98.29% used; 225820973 free inodes.

server3 `/tmp`: 82680934400 available bytes; 95.39% used; 114110899 free inodes.

server3 `/var/tmp`: 82680934400 available bytes; 95.39% used; 114110899 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106074308608 available bytes; 94.08% used; 114348172 free inodes.

server4 `/home`: 106074308608 available bytes; 94.08% used; 114348172 free inodes.

server4 `/data`: 105865367552 available bytes; 98.54% used; 224922701 free inodes.

server4 `/tmp`: 106074308608 available bytes; 94.08% used; 114348172 free inodes.

server4 `/var/tmp`: 106074308608 available bytes; 94.08% used; 114348172 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
