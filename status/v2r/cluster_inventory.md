# V2R cluster inventory

2026-09-24T07:18:15.898652+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324451704832 available bytes; 81.90% used; 112491253 free inodes.

server1 `/home`: 324451704832 available bytes; 81.90% used; 112491253 free inodes.

server1 `/tmp`: 324451704832 available bytes; 81.90% used; 112491253 free inodes.

server1 `/var/tmp`: 324451704832 available bytes; 81.90% used; 112491253 free inodes.

server1 `/mnt/raid5`: 517418663936 available bytes; 97.63% used; 337722818 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57851559936 available bytes; 96.77% used; 110431129 free inodes.

server2 `/home`: 57851559936 available bytes; 96.77% used; 110431129 free inodes.

server2 `/tmp`: 57851559936 available bytes; 96.77% used; 110431129 free inodes.

server2 `/var/tmp`: 57851559936 available bytes; 96.77% used; 110431129 free inodes.

server2 `/mnt/raid5`: 518641201152 available bytes; 96.42% used; 445181318 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 127139463168 available bytes; 92.91% used; 114198549 free inodes.

server3 `/home`: 127139463168 available bytes; 92.91% used; 114198549 free inodes.

server3 `/data`: 139050921984 available bytes; 98.08% used; 225834387 free inodes.

server3 `/tmp`: 127139463168 available bytes; 92.91% used; 114198549 free inodes.

server3 `/var/tmp`: 127139463168 available bytes; 92.91% used; 114198549 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105789800448 available bytes; 94.10% used; 114349211 free inodes.

server4 `/home`: 105789800448 available bytes; 94.10% used; 114349211 free inodes.

server4 `/data`: 291140534272 available bytes; 95.98% used; 225367138 free inodes.

server4 `/tmp`: 105789800448 available bytes; 94.10% used; 114349211 free inodes.

server4 `/var/tmp`: 105789800448 available bytes; 94.10% used; 114349211 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
