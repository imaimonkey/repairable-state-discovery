# V2R cluster inventory

2026-09-23T21:59:23.672998+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325710958592 available bytes; 81.83% used; 112501408 free inodes.

server1 `/home`: 325710958592 available bytes; 81.83% used; 112501408 free inodes.

server1 `/tmp`: 325710958592 available bytes; 81.83% used; 112501408 free inodes.

server1 `/var/tmp`: 325710958592 available bytes; 81.83% used; 112501408 free inodes.

server1 `/mnt/raid5`: 1388116316160 available bytes; 93.63% used; 337739900 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41103564800 available bytes; 97.71% used; 110432651 free inodes.

server2 `/home`: 41103564800 available bytes; 97.71% used; 110432651 free inodes.

server2 `/tmp`: 41103564800 available bytes; 97.71% used; 110432651 free inodes.

server2 `/var/tmp`: 41103564800 available bytes; 97.71% used; 110432651 free inodes.

server2 `/mnt/raid5`: 536552026112 available bytes; 96.29% used; 445207667 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293040246784 available bytes; 83.65% used; 114223126 free inodes.

server3 `/home`: 293040246784 available bytes; 83.65% used; 114223126 free inodes.

server3 `/data`: 82457706496 available bytes; 98.86% used; 225847903 free inodes.

server3 `/tmp`: 293040246784 available bytes; 83.65% used; 114223126 free inodes.

server3 `/var/tmp`: 293040246784 available bytes; 83.65% used; 114223126 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106450472960 available bytes; 94.06% used; 114355645 free inodes.

server4 `/home`: 106450472960 available bytes; 94.06% used; 114355645 free inodes.

server4 `/data`: 300206964736 available bytes; 95.85% used; 225445261 free inodes.

server4 `/tmp`: 106450472960 available bytes; 94.06% used; 114355645 free inodes.

server4 `/var/tmp`: 106450472960 available bytes; 94.06% used; 114355645 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
