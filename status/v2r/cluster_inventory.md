# V2R cluster inventory

2026-09-23T22:02:28.197364+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325709987840 available bytes; 81.83% used; 112501413 free inodes.

server1 `/home`: 325709987840 available bytes; 81.83% used; 112501413 free inodes.

server1 `/tmp`: 325709987840 available bytes; 81.83% used; 112501413 free inodes.

server1 `/var/tmp`: 325709987840 available bytes; 81.83% used; 112501413 free inodes.

server1 `/mnt/raid5`: 1388119015424 available bytes; 93.63% used; 337739883 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41101750272 available bytes; 97.71% used; 110432652 free inodes.

server2 `/home`: 41101750272 available bytes; 97.71% used; 110432652 free inodes.

server2 `/tmp`: 41101750272 available bytes; 97.71% used; 110432652 free inodes.

server2 `/var/tmp`: 41101750272 available bytes; 97.71% used; 110432652 free inodes.

server2 `/mnt/raid5`: 536972664832 available bytes; 96.29% used; 445207462 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293045002240 available bytes; 83.65% used; 114223383 free inodes.

server3 `/home`: 293045002240 available bytes; 83.65% used; 114223383 free inodes.

server3 `/data`: 82454228992 available bytes; 98.86% used; 225847847 free inodes.

server3 `/tmp`: 293045002240 available bytes; 83.65% used; 114223383 free inodes.

server3 `/var/tmp`: 293045002240 available bytes; 83.65% used; 114223383 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106444787712 available bytes; 94.06% used; 114355539 free inodes.

server4 `/home`: 106444787712 available bytes; 94.06% used; 114355539 free inodes.

server4 `/data`: 300197695488 available bytes; 95.85% used; 225444553 free inodes.

server4 `/tmp`: 106444787712 available bytes; 94.06% used; 114355539 free inodes.

server4 `/var/tmp`: 106444787712 available bytes; 94.06% used; 114355539 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
