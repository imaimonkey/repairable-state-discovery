# V2R cluster inventory

2026-09-23T23:03:59.590899+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325740900352 available bytes; 81.83% used; 112501689 free inodes.

server1 `/home`: 325740900352 available bytes; 81.83% used; 112501689 free inodes.

server1 `/tmp`: 325740900352 available bytes; 81.83% used; 112501689 free inodes.

server1 `/var/tmp`: 325740900352 available bytes; 81.83% used; 112501689 free inodes.

server1 `/mnt/raid5`: 1388003942400 available bytes; 93.63% used; 337739787 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41059536896 available bytes; 97.71% used; 110432609 free inodes.

server2 `/home`: 41059536896 available bytes; 97.71% used; 110432609 free inodes.

server2 `/tmp`: 41059536896 available bytes; 97.71% used; 110432609 free inodes.

server2 `/var/tmp`: 41059536896 available bytes; 97.71% used; 110432609 free inodes.

server2 `/mnt/raid5`: 535269388288 available bytes; 96.30% used; 445205854 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292863938560 available bytes; 83.66% used; 114210987 free inodes.

server3 `/home`: 292863938560 available bytes; 83.66% used; 114210987 free inodes.

server3 `/data`: 82344337408 available bytes; 98.86% used; 225846576 free inodes.

server3 `/tmp`: 292863938560 available bytes; 83.66% used; 114210987 free inodes.

server3 `/var/tmp`: 292863938560 available bytes; 83.66% used; 114210987 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106288123904 available bytes; 94.07% used; 114353307 free inodes.

server4 `/home`: 106288123904 available bytes; 94.07% used; 114353307 free inodes.

server4 `/data`: 300063051776 available bytes; 95.85% used; 225431339 free inodes.

server4 `/tmp`: 106288123904 available bytes; 94.07% used; 114353307 free inodes.

server4 `/var/tmp`: 106288123904 available bytes; 94.07% used; 114353307 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
