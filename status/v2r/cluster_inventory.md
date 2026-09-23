# V2R cluster inventory

2026-09-23T23:28:41.064518+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325658730496 available bytes; 81.83% used; 112501520 free inodes.

server1 `/home`: 325658730496 available bytes; 81.83% used; 112501520 free inodes.

server1 `/tmp`: 325658730496 available bytes; 81.83% used; 112501520 free inodes.

server1 `/var/tmp`: 325658730496 available bytes; 81.83% used; 112501520 free inodes.

server1 `/mnt/raid5`: 1370771800064 available bytes; 93.71% used; 337739645 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41043984384 available bytes; 97.71% used; 110432573 free inodes.

server2 `/home`: 41043984384 available bytes; 97.71% used; 110432573 free inodes.

server2 `/tmp`: 41043984384 available bytes; 97.71% used; 110432573 free inodes.

server2 `/var/tmp`: 41043984384 available bytes; 97.71% used; 110432573 free inodes.

server2 `/mnt/raid5`: 534546550784 available bytes; 96.31% used; 445205548 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292850196480 available bytes; 83.66% used; 114212266 free inodes.

server3 `/home`: 292850196480 available bytes; 83.66% used; 114212266 free inodes.

server3 `/data`: 82315358208 available bytes; 98.86% used; 225845796 free inodes.

server3 `/tmp`: 292850196480 available bytes; 83.66% used; 114212266 free inodes.

server3 `/var/tmp`: 292850196480 available bytes; 83.66% used; 114212266 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106232270848 available bytes; 94.07% used; 114352403 free inodes.

server4 `/home`: 106232270848 available bytes; 94.07% used; 114352403 free inodes.

server4 `/data`: 293082468352 available bytes; 95.95% used; 225424351 free inodes.

server4 `/tmp`: 106232270848 available bytes; 94.07% used; 114352403 free inodes.

server4 `/var/tmp`: 106232270848 available bytes; 94.07% used; 114352403 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
