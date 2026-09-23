# V2R cluster inventory

2026-09-23T23:36:23.198445+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325614567424 available bytes; 81.84% used; 112501250 free inodes.

server1 `/home`: 325614567424 available bytes; 81.84% used; 112501250 free inodes.

server1 `/tmp`: 325614567424 available bytes; 81.84% used; 112501250 free inodes.

server1 `/var/tmp`: 325614567424 available bytes; 81.84% used; 112501250 free inodes.

server1 `/mnt/raid5`: 1366868996096 available bytes; 93.73% used; 337736137 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41033707520 available bytes; 97.71% used; 110432547 free inodes.

server2 `/home`: 41033707520 available bytes; 97.71% used; 110432547 free inodes.

server2 `/tmp`: 41033707520 available bytes; 97.71% used; 110432547 free inodes.

server2 `/var/tmp`: 41033707520 available bytes; 97.71% used; 110432547 free inodes.

server2 `/mnt/raid5`: 534258970624 available bytes; 96.31% used; 445205015 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292841918464 available bytes; 83.66% used; 114214314 free inodes.

server3 `/home`: 292841918464 available bytes; 83.66% used; 114214314 free inodes.

server3 `/data`: 82308124672 available bytes; 98.86% used; 225845650 free inodes.

server3 `/tmp`: 292841918464 available bytes; 83.66% used; 114214314 free inodes.

server3 `/var/tmp`: 292841918464 available bytes; 83.66% used; 114214314 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106206593024 available bytes; 94.07% used; 114352131 free inodes.

server4 `/home`: 106206593024 available bytes; 94.07% used; 114352131 free inodes.

server4 `/data`: 293022908416 available bytes; 95.95% used; 225422007 free inodes.

server4 `/tmp`: 106206593024 available bytes; 94.07% used; 114352131 free inodes.

server4 `/var/tmp`: 106206593024 available bytes; 94.07% used; 114352131 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
