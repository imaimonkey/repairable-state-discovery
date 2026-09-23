# V2R cluster inventory

2026-09-23T23:24:50.952073+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325664788480 available bytes; 81.83% used; 112501553 free inodes.

server1 `/home`: 325664788480 available bytes; 81.83% used; 112501553 free inodes.

server1 `/tmp`: 325664788480 available bytes; 81.83% used; 112501553 free inodes.

server1 `/var/tmp`: 325664788480 available bytes; 81.83% used; 112501553 free inodes.

server1 `/mnt/raid5`: 1374003240960 available bytes; 93.70% used; 337739710 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41045819392 available bytes; 97.71% used; 110432587 free inodes.

server2 `/home`: 41045819392 available bytes; 97.71% used; 110432587 free inodes.

server2 `/tmp`: 41045819392 available bytes; 97.71% used; 110432587 free inodes.

server2 `/var/tmp`: 41045819392 available bytes; 97.71% used; 110432587 free inodes.

server2 `/mnt/raid5`: 534656442368 available bytes; 96.31% used; 445205577 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292860227584 available bytes; 83.66% used; 114212799 free inodes.

server3 `/home`: 292860227584 available bytes; 83.66% used; 114212799 free inodes.

server3 `/data`: 82318901248 available bytes; 98.86% used; 225845875 free inodes.

server3 `/tmp`: 292860227584 available bytes; 83.66% used; 114212799 free inodes.

server3 `/var/tmp`: 292860227584 available bytes; 83.66% used; 114212799 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106241134592 available bytes; 94.07% used; 114352546 free inodes.

server4 `/home`: 106241134592 available bytes; 94.07% used; 114352546 free inodes.

server4 `/data`: 293103603712 available bytes; 95.95% used; 225425504 free inodes.

server4 `/tmp`: 106241134592 available bytes; 94.07% used; 114352546 free inodes.

server4 `/var/tmp`: 106241134592 available bytes; 94.07% used; 114352546 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
