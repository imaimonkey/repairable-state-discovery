# V2R cluster inventory

2026-09-23T22:57:50.159078+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325747240960 available bytes; 81.83% used; 112501733 free inodes.

server1 `/home`: 325747240960 available bytes; 81.83% used; 112501733 free inodes.

server1 `/tmp`: 325747240960 available bytes; 81.83% used; 112501733 free inodes.

server1 `/var/tmp`: 325747240960 available bytes; 81.83% used; 112501733 free inodes.

server1 `/mnt/raid5`: 1388001865728 available bytes; 93.63% used; 337739804 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41062182912 available bytes; 97.71% used; 110432612 free inodes.

server2 `/home`: 41062182912 available bytes; 97.71% used; 110432612 free inodes.

server2 `/tmp`: 41062182912 available bytes; 97.71% used; 110432612 free inodes.

server2 `/var/tmp`: 41062182912 available bytes; 97.71% used; 110432612 free inodes.

server2 `/mnt/raid5`: 535487066112 available bytes; 96.30% used; 445206185 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292536864768 available bytes; 83.68% used; 114192878 free inodes.

server3 `/home`: 292536864768 available bytes; 83.68% used; 114192878 free inodes.

server3 `/data`: 82354798592 available bytes; 98.86% used; 225846706 free inodes.

server3 `/tmp`: 292536864768 available bytes; 83.68% used; 114192878 free inodes.

server3 `/var/tmp`: 292536864768 available bytes; 83.68% used; 114192878 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106302111744 available bytes; 94.07% used; 114353531 free inodes.

server4 `/home`: 106302111744 available bytes; 94.07% used; 114353531 free inodes.

server4 `/data`: 300085346304 available bytes; 95.85% used; 225432501 free inodes.

server4 `/tmp`: 106302111744 available bytes; 94.07% used; 114353531 free inodes.

server4 `/var/tmp`: 106302111744 available bytes; 94.07% used; 114353531 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
