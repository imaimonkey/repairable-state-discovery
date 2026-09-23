# V2R cluster inventory

2026-09-23T21:44:22.012409+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325711704064 available bytes; 81.83% used; 112501314 free inodes.

server1 `/home`: 325711704064 available bytes; 81.83% used; 112501314 free inodes.

server1 `/tmp`: 325711704064 available bytes; 81.83% used; 112501314 free inodes.

server1 `/var/tmp`: 325711704064 available bytes; 81.83% used; 112501314 free inodes.

server1 `/mnt/raid5`: 1388127457280 available bytes; 93.63% used; 337739926 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41114959872 available bytes; 97.71% used; 110432663 free inodes.

server2 `/home`: 41114959872 available bytes; 97.71% used; 110432663 free inodes.

server2 `/tmp`: 41114959872 available bytes; 97.71% used; 110432663 free inodes.

server2 `/var/tmp`: 41114959872 available bytes; 97.71% used; 110432663 free inodes.

server2 `/mnt/raid5`: 538070069248 available bytes; 96.28% used; 445208172 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292631838720 available bytes; 83.67% used; 114187274 free inodes.

server3 `/home`: 292631838720 available bytes; 83.67% used; 114187274 free inodes.

server3 `/data`: 82484494336 available bytes; 98.86% used; 225848515 free inodes.

server3 `/tmp`: 292631838720 available bytes; 83.67% used; 114187274 free inodes.

server3 `/var/tmp`: 292631838720 available bytes; 83.67% used; 114187274 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106472402944 available bytes; 94.06% used; 114355943 free inodes.

server4 `/home`: 106472402944 available bytes; 94.06% used; 114355943 free inodes.

server4 `/data`: 300252831744 available bytes; 95.85% used; 225448120 free inodes.

server4 `/tmp`: 106472402944 available bytes; 94.06% used; 114355943 free inodes.

server4 `/var/tmp`: 106472402944 available bytes; 94.06% used; 114355943 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
