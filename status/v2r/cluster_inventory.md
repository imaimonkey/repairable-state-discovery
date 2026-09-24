# V2R cluster inventory

2026-09-24T05:43:07.291393+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324528271360 available bytes; 81.90% used; 112492132 free inodes.

server1 `/home`: 324528271360 available bytes; 81.90% used; 112492132 free inodes.

server1 `/tmp`: 324528271360 available bytes; 81.90% used; 112492132 free inodes.

server1 `/var/tmp`: 324528271360 available bytes; 81.90% used; 112492132 free inodes.

server1 `/mnt/raid5`: 517628518400 available bytes; 97.63% used; 337723939 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57915170816 available bytes; 96.77% used; 110431338 free inodes.

server2 `/home`: 57915170816 available bytes; 96.77% used; 110431338 free inodes.

server2 `/tmp`: 57915170816 available bytes; 96.77% used; 110431338 free inodes.

server2 `/var/tmp`: 57915170816 available bytes; 96.77% used; 110431338 free inodes.

server2 `/mnt/raid5`: 521976926208 available bytes; 96.39% used; 445193606 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 126959169536 available bytes; 92.92% used; 114191271 free inodes.

server3 `/home`: 126959169536 available bytes; 92.92% used; 114191271 free inodes.

server3 `/data`: 185241645056 available bytes; 97.44% used; 225839129 free inodes.

server3 `/tmp`: 126959169536 available bytes; 92.92% used; 114191271 free inodes.

server3 `/var/tmp`: 126959169536 available bytes; 92.92% used; 114191271 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105816338432 available bytes; 94.10% used; 114349351 free inodes.

server4 `/home`: 105816338432 available bytes; 94.10% used; 114349351 free inodes.

server4 `/data`: 251474063360 available bytes; 96.52% used; 225358017 free inodes.

server4 `/tmp`: 105816338432 available bytes; 94.10% used; 114349351 free inodes.

server4 `/var/tmp`: 105816338432 available bytes; 94.10% used; 114349351 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
