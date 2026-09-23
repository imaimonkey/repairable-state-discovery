# V2R cluster inventory

2026-09-23T23:33:43.774167+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325645201408 available bytes; 81.83% used; 112501457 free inodes.

server1 `/home`: 325645201408 available bytes; 81.83% used; 112501457 free inodes.

server1 `/tmp`: 325645201408 available bytes; 81.83% used; 112501457 free inodes.

server1 `/var/tmp`: 325645201408 available bytes; 81.83% used; 112501457 free inodes.

server1 `/mnt/raid5`: 1367408644096 available bytes; 93.73% used; 337736319 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41034743808 available bytes; 97.71% used; 110432556 free inodes.

server2 `/home`: 41034743808 available bytes; 97.71% used; 110432556 free inodes.

server2 `/tmp`: 41034743808 available bytes; 97.71% used; 110432556 free inodes.

server2 `/var/tmp`: 41034743808 available bytes; 97.71% used; 110432556 free inodes.

server2 `/mnt/raid5`: 533832073216 available bytes; 96.31% used; 445205477 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292862550016 available bytes; 83.66% used; 114213543 free inodes.

server3 `/home`: 292862550016 available bytes; 83.66% used; 114213543 free inodes.

server3 `/data`: 82306158592 available bytes; 98.86% used; 225845706 free inodes.

server3 `/tmp`: 292862550016 available bytes; 83.66% used; 114213543 free inodes.

server3 `/var/tmp`: 292862550016 available bytes; 83.66% used; 114213543 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106212433920 available bytes; 94.07% used; 114352223 free inodes.

server4 `/home`: 106212433920 available bytes; 94.07% used; 114352223 free inodes.

server4 `/data`: 293059289088 available bytes; 95.95% used; 225422849 free inodes.

server4 `/tmp`: 106212433920 available bytes; 94.07% used; 114352223 free inodes.

server4 `/var/tmp`: 106212433920 available bytes; 94.07% used; 114352223 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
