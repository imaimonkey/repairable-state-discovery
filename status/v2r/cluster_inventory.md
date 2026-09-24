# V2R cluster inventory

2026-09-24T06:56:49.606276+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324482478080 available bytes; 81.90% used; 112491407 free inodes.

server1 `/home`: 324482478080 available bytes; 81.90% used; 112491407 free inodes.

server1 `/tmp`: 324482478080 available bytes; 81.90% used; 112491407 free inodes.

server1 `/var/tmp`: 324482478080 available bytes; 81.90% used; 112491407 free inodes.

server1 `/mnt/raid5`: 517424246784 available bytes; 97.63% used; 337722848 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57862709248 available bytes; 96.77% used; 110431183 free inodes.

server2 `/home`: 57862709248 available bytes; 96.77% used; 110431183 free inodes.

server2 `/tmp`: 57862709248 available bytes; 96.77% used; 110431183 free inodes.

server2 `/var/tmp`: 57862709248 available bytes; 96.77% used; 110431183 free inodes.

server2 `/mnt/raid5`: 519427629056 available bytes; 96.41% used; 445191127 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126766178304 available bytes; 92.93% used; 114175142 free inodes.

server3 `/home`: 126766178304 available bytes; 92.93% used; 114175142 free inodes.

server3 `/data`: 139236950016 available bytes; 98.08% used; 225834824 free inodes.

server3 `/tmp`: 126766178304 available bytes; 92.93% used; 114175142 free inodes.

server3 `/var/tmp`: 126766178304 available bytes; 92.93% used; 114175142 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105799061504 available bytes; 94.10% used; 114349219 free inodes.

server4 `/home`: 105799061504 available bytes; 94.10% used; 114349219 free inodes.

server4 `/data`: 306063421440 available bytes; 95.77% used; 225367885 free inodes.

server4 `/tmp`: 105799061504 available bytes; 94.10% used; 114349219 free inodes.

server4 `/var/tmp`: 105799061504 available bytes; 94.10% used; 114349219 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
