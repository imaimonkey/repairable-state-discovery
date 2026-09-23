# V2R cluster inventory

2026-09-23T22:05:32.737682+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325708746752 available bytes; 81.83% used; 112501411 free inodes.

server1 `/home`: 325708746752 available bytes; 81.83% used; 112501411 free inodes.

server1 `/tmp`: 325708746752 available bytes; 81.83% used; 112501411 free inodes.

server1 `/var/tmp`: 325708746752 available bytes; 81.83% used; 112501411 free inodes.

server1 `/mnt/raid5`: 1367472549888 available bytes; 93.73% used; 337739888 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41098801152 available bytes; 97.71% used; 110432658 free inodes.

server2 `/home`: 41098801152 available bytes; 97.71% used; 110432658 free inodes.

server2 `/tmp`: 41098801152 available bytes; 97.71% used; 110432658 free inodes.

server2 `/var/tmp`: 41098801152 available bytes; 97.71% used; 110432658 free inodes.

server2 `/mnt/raid5`: 537429663744 available bytes; 96.29% used; 445207882 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292733394944 available bytes; 83.66% used; 114202039 free inodes.

server3 `/home`: 292733394944 available bytes; 83.66% used; 114202039 free inodes.

server3 `/data`: 82453843968 available bytes; 98.86% used; 225847768 free inodes.

server3 `/tmp`: 292733394944 available bytes; 83.66% used; 114202039 free inodes.

server3 `/var/tmp`: 292733394944 available bytes; 83.66% used; 114202039 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106437496832 available bytes; 94.06% used; 114355423 free inodes.

server4 `/home`: 106437496832 available bytes; 94.06% used; 114355423 free inodes.

server4 `/data`: 300186865664 available bytes; 95.85% used; 225443679 free inodes.

server4 `/tmp`: 106437496832 available bytes; 94.06% used; 114355423 free inodes.

server4 `/var/tmp`: 106437496832 available bytes; 94.06% used; 114355423 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
