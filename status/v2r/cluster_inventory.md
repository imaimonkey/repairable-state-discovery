# V2R cluster inventory

2026-09-24T00:07:44.386011+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325574676480 available bytes; 81.84% used; 112500833 free inodes.

server1 `/home`: 325574676480 available bytes; 81.84% used; 112500833 free inodes.

server1 `/tmp`: 325574676480 available bytes; 81.84% used; 112500833 free inodes.

server1 `/var/tmp`: 325574676480 available bytes; 81.84% used; 112500833 free inodes.

server1 `/mnt/raid5`: 1235247583232 available bytes; 94.33% used; 337735295 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41009508352 available bytes; 97.71% used; 110432418 free inodes.

server2 `/home`: 41009508352 available bytes; 97.71% used; 110432418 free inodes.

server2 `/tmp`: 41009508352 available bytes; 97.71% used; 110432418 free inodes.

server2 `/var/tmp`: 41009508352 available bytes; 97.71% used; 110432418 free inodes.

server2 `/mnt/raid5`: 533372293120 available bytes; 96.31% used; 445203987 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292765106176 available bytes; 83.66% used; 114214255 free inodes.

server3 `/home`: 292765106176 available bytes; 83.66% used; 114214255 free inodes.

server3 `/data`: 82263445504 available bytes; 98.86% used; 225844641 free inodes.

server3 `/tmp`: 292765106176 available bytes; 83.66% used; 114214255 free inodes.

server3 `/var/tmp`: 292765106176 available bytes; 83.66% used; 114214255 free inodes.
| server4 | True | ['3', '4', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106121998336 available bytes; 94.08% used; 114351007 free inodes.

server4 `/home`: 106121998336 available bytes; 94.08% used; 114351007 free inodes.

server4 `/data`: 292918140928 available bytes; 95.95% used; 225414606 free inodes.

server4 `/tmp`: 106121998336 available bytes; 94.08% used; 114351007 free inodes.

server4 `/var/tmp`: 106121998336 available bytes; 94.08% used; 114351007 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
