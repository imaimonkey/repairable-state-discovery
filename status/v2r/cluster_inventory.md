# V2R cluster inventory

2026-09-24T10:00:19.889075+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324428288000 available bytes; 81.90% used; 112489541 free inodes.

server1 `/home`: 324428288000 available bytes; 81.90% used; 112489541 free inodes.

server1 `/tmp`: 324428288000 available bytes; 81.90% used; 112489541 free inodes.

server1 `/var/tmp`: 324428288000 available bytes; 81.90% used; 112489541 free inodes.

server1 `/mnt/raid5`: 500704624640 available bytes; 97.70% used; 337701342 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57755045888 available bytes; 96.78% used; 110430740 free inodes.

server2 `/home`: 57755045888 available bytes; 96.78% used; 110430740 free inodes.

server2 `/tmp`: 57755045888 available bytes; 96.78% used; 110430740 free inodes.

server2 `/var/tmp`: 57755045888 available bytes; 96.78% used; 110430740 free inodes.

server2 `/mnt/raid5`: 513118810112 available bytes; 96.45% used; 445176755 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 85313368064 available bytes; 95.24% used; 114170451 free inodes.

server3 `/home`: 85313368064 available bytes; 95.24% used; 114170451 free inodes.

server3 `/data`: 164501676032 available bytes; 97.73% used; 225819272 free inodes.

server3 `/tmp`: 85313368064 available bytes; 95.24% used; 114170451 free inodes.

server3 `/var/tmp`: 85313368064 available bytes; 95.24% used; 114170451 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105748111360 available bytes; 94.10% used; 114349034 free inodes.

server4 `/home`: 105748111360 available bytes; 94.10% used; 114349034 free inodes.

server4 `/data`: 154567970816 available bytes; 97.86% used; 225273210 free inodes.

server4 `/tmp`: 105748111360 available bytes; 94.10% used; 114349034 free inodes.

server4 `/var/tmp`: 105748111360 available bytes; 94.10% used; 114349034 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
