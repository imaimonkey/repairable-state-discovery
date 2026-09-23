# V2R cluster inventory

2026-09-23T22:40:55.120357+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325721395200 available bytes; 81.83% used; 112501558 free inodes.

server1 `/home`: 325721395200 available bytes; 81.83% used; 112501558 free inodes.

server1 `/tmp`: 325721395200 available bytes; 81.83% used; 112501558 free inodes.

server1 `/var/tmp`: 325721395200 available bytes; 81.83% used; 112501558 free inodes.

server1 `/mnt/raid5`: 1388120117248 available bytes; 93.63% used; 337739973 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41076338688 available bytes; 97.71% used; 110432622 free inodes.

server2 `/home`: 41076338688 available bytes; 97.71% used; 110432622 free inodes.

server2 `/tmp`: 41076338688 available bytes; 97.71% used; 110432622 free inodes.

server2 `/var/tmp`: 41076338688 available bytes; 97.71% used; 110432622 free inodes.

server2 `/mnt/raid5`: 536320909312 available bytes; 96.29% used; 445206440 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293026418688 available bytes; 83.65% used; 114223305 free inodes.

server3 `/home`: 293026418688 available bytes; 83.65% used; 114223305 free inodes.

server3 `/data`: 82452021248 available bytes; 98.86% used; 225847346 free inodes.

server3 `/tmp`: 293026418688 available bytes; 83.65% used; 114223305 free inodes.

server3 `/var/tmp`: 293026418688 available bytes; 83.65% used; 114223305 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106348830720 available bytes; 94.07% used; 114354143 free inodes.

server4 `/home`: 106348830720 available bytes; 94.07% used; 114354143 free inodes.

server4 `/data`: 300098764800 available bytes; 95.85% used; 225435534 free inodes.

server4 `/tmp`: 106348830720 available bytes; 94.07% used; 114354143 free inodes.

server4 `/var/tmp`: 106348830720 available bytes; 94.07% used; 114354143 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
