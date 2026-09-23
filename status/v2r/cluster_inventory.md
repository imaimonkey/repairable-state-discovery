# V2R cluster inventory

2026-09-23T23:25:36.432584+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325664169984 available bytes; 81.83% used; 112501543 free inodes.

server1 `/home`: 325664169984 available bytes; 81.83% used; 112501543 free inodes.

server1 `/tmp`: 325664169984 available bytes; 81.83% used; 112501543 free inodes.

server1 `/var/tmp`: 325664169984 available bytes; 81.83% used; 112501543 free inodes.

server1 `/mnt/raid5`: 1373530767360 available bytes; 93.70% used; 337739690 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41045200896 available bytes; 97.71% used; 110432582 free inodes.

server2 `/home`: 41045200896 available bytes; 97.71% used; 110432582 free inodes.

server2 `/tmp`: 41045200896 available bytes; 97.71% used; 110432582 free inodes.

server2 `/var/tmp`: 41045200896 available bytes; 97.71% used; 110432582 free inodes.

server2 `/mnt/raid5`: 534648401920 available bytes; 96.31% used; 445205871 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292861321216 available bytes; 83.66% used; 114213236 free inodes.

server3 `/home`: 292861321216 available bytes; 83.66% used; 114213236 free inodes.

server3 `/data`: 82317606912 available bytes; 98.86% used; 225845853 free inodes.

server3 `/tmp`: 292861321216 available bytes; 83.66% used; 114213236 free inodes.

server3 `/var/tmp`: 292861321216 available bytes; 83.66% used; 114213236 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106239385600 available bytes; 94.07% used; 114352518 free inodes.

server4 `/home`: 106239385600 available bytes; 94.07% used; 114352518 free inodes.

server4 `/data`: 293099249664 available bytes; 95.95% used; 225425251 free inodes.

server4 `/tmp`: 106239385600 available bytes; 94.07% used; 114352518 free inodes.

server4 `/var/tmp`: 106239385600 available bytes; 94.07% used; 114352518 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
