# V2R cluster inventory

2026-09-23T21:15:04.909045+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325722206208 available bytes; 81.83% used; 112501444 free inodes.

server1 `/home`: 325722206208 available bytes; 81.83% used; 112501444 free inodes.

server1 `/tmp`: 325722206208 available bytes; 81.83% used; 112501444 free inodes.

server1 `/var/tmp`: 325722206208 available bytes; 81.83% used; 112501444 free inodes.

server1 `/mnt/raid5`: 1388133879808 available bytes; 93.63% used; 337739966 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41112641536 available bytes; 97.71% used; 110432694 free inodes.

server2 `/home`: 41112641536 available bytes; 97.71% used; 110432694 free inodes.

server2 `/tmp`: 41112641536 available bytes; 97.71% used; 110432694 free inodes.

server2 `/var/tmp`: 41112641536 available bytes; 97.71% used; 110432694 free inodes.

server2 `/mnt/raid5`: 538988756992 available bytes; 96.28% used; 445209179 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293273554944 available bytes; 83.63% used; 114228387 free inodes.

server3 `/home`: 293273554944 available bytes; 83.63% used; 114228387 free inodes.

server3 `/data`: 52307562496 available bytes; 99.28% used; 225849413 free inodes.

server3 `/tmp`: 293273554944 available bytes; 83.63% used; 114228387 free inodes.

server3 `/var/tmp`: 293273554944 available bytes; 83.63% used; 114228387 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106490892288 available bytes; 94.06% used; 114356034 free inodes.

server4 `/home`: 106490892288 available bytes; 94.06% used; 114356034 free inodes.

server4 `/data`: 300449247232 available bytes; 95.85% used; 225453986 free inodes.

server4 `/tmp`: 106490892288 available bytes; 94.06% used; 114356034 free inodes.

server4 `/var/tmp`: 106490892288 available bytes; 94.06% used; 114356034 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
