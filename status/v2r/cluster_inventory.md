# V2R cluster inventory

2026-09-23T21:28:57.707529+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325719183360 available bytes; 81.83% used; 112501436 free inodes.

server1 `/home`: 325719183360 available bytes; 81.83% used; 112501436 free inodes.

server1 `/tmp`: 325719183360 available bytes; 81.83% used; 112501436 free inodes.

server1 `/var/tmp`: 325719183360 available bytes; 81.83% used; 112501436 free inodes.

server1 `/mnt/raid5`: 1388135833600 available bytes; 93.63% used; 337739954 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41126244352 available bytes; 97.71% used; 110432685 free inodes.

server2 `/home`: 41126244352 available bytes; 97.71% used; 110432685 free inodes.

server2 `/tmp`: 41126244352 available bytes; 97.71% used; 110432685 free inodes.

server2 `/var/tmp`: 41126244352 available bytes; 97.71% used; 110432685 free inodes.

server2 `/mnt/raid5`: 538555355136 available bytes; 96.28% used; 445208643 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293245718528 available bytes; 83.64% used; 114227973 free inodes.

server3 `/home`: 293245718528 available bytes; 83.64% used; 114227973 free inodes.

server3 `/data`: 52279234560 available bytes; 99.28% used; 225848813 free inodes.

server3 `/tmp`: 293245718528 available bytes; 83.64% used; 114227973 free inodes.

server3 `/var/tmp`: 293245718528 available bytes; 83.64% used; 114227973 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106481664000 available bytes; 94.06% used; 114356004 free inodes.

server4 `/home`: 106481664000 available bytes; 94.06% used; 114356004 free inodes.

server4 `/data`: 300333490176 available bytes; 95.85% used; 225451147 free inodes.

server4 `/tmp`: 106481664000 available bytes; 94.06% used; 114356004 free inodes.

server4 `/var/tmp`: 106481664000 available bytes; 94.06% used; 114356004 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
