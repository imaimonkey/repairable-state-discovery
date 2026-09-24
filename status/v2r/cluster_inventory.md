# V2R cluster inventory

2026-09-24T00:16:32.501523+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325559148544 available bytes; 81.84% used; 112500738 free inodes.

server1 `/home`: 325559148544 available bytes; 81.84% used; 112500738 free inodes.

server1 `/tmp`: 325559148544 available bytes; 81.84% used; 112500738 free inodes.

server1 `/var/tmp`: 325559148544 available bytes; 81.84% used; 112500738 free inodes.

server1 `/mnt/raid5`: 1198521896960 available bytes; 94.50% used; 337735133 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41008922624 available bytes; 97.71% used; 110432395 free inodes.

server2 `/home`: 41008922624 available bytes; 97.71% used; 110432395 free inodes.

server2 `/tmp`: 41008922624 available bytes; 97.71% used; 110432395 free inodes.

server2 `/var/tmp`: 41008922624 available bytes; 97.71% used; 110432395 free inodes.

server2 `/mnt/raid5`: 533207498752 available bytes; 96.32% used; 445203888 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292594696192 available bytes; 83.67% used; 114206619 free inodes.

server3 `/home`: 292594696192 available bytes; 83.67% used; 114206619 free inodes.

server3 `/data`: 82250653696 available bytes; 98.86% used; 225844458 free inodes.

server3 `/tmp`: 292594696192 available bytes; 83.67% used; 114206619 free inodes.

server3 `/var/tmp`: 292594696192 available bytes; 83.67% used; 114206619 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106102943744 available bytes; 94.08% used; 114350703 free inodes.

server4 `/home`: 106102943744 available bytes; 94.08% used; 114350703 free inodes.

server4 `/data`: 292912254976 available bytes; 95.95% used; 225414568 free inodes.

server4 `/tmp`: 106102943744 available bytes; 94.08% used; 114350703 free inodes.

server4 `/var/tmp`: 106102943744 available bytes; 94.08% used; 114350703 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
