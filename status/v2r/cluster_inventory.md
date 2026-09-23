# V2R cluster inventory

2026-09-23T22:38:17.009685+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325695590400 available bytes; 81.83% used; 112501390 free inodes.

server1 `/home`: 325695590400 available bytes; 81.83% used; 112501390 free inodes.

server1 `/tmp`: 325695590400 available bytes; 81.83% used; 112501390 free inodes.

server1 `/var/tmp`: 325695590400 available bytes; 81.83% used; 112501390 free inodes.

server1 `/mnt/raid5`: 1388125261824 available bytes; 93.63% used; 337739986 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41083367424 available bytes; 97.71% used; 110432628 free inodes.

server2 `/home`: 41083367424 available bytes; 97.71% used; 110432628 free inodes.

server2 `/tmp`: 41083367424 available bytes; 97.71% used; 110432628 free inodes.

server2 `/var/tmp`: 41083367424 available bytes; 97.71% used; 110432628 free inodes.

server2 `/mnt/raid5`: 536405794816 available bytes; 96.29% used; 445206635 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292733210624 available bytes; 83.66% used; 114202004 free inodes.

server3 `/home`: 292733210624 available bytes; 83.66% used; 114202004 free inodes.

server3 `/data`: 82432159744 available bytes; 98.86% used; 225847213 free inodes.

server3 `/tmp`: 292733210624 available bytes; 83.66% used; 114202004 free inodes.

server3 `/var/tmp`: 292733210624 available bytes; 83.66% used; 114202004 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106355101696 available bytes; 94.06% used; 114354243 free inodes.

server4 `/home`: 106355101696 available bytes; 94.06% used; 114354243 free inodes.

server4 `/data`: 300087099392 available bytes; 95.85% used; 225435832 free inodes.

server4 `/tmp`: 106355101696 available bytes; 94.06% used; 114354243 free inodes.

server4 `/var/tmp`: 106355101696 available bytes; 94.06% used; 114354243 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
