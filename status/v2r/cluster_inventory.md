# V2R cluster inventory

2026-09-24T05:13:47.292022+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324592496640 available bytes; 81.89% used; 112492546 free inodes.

server1 `/home`: 324592496640 available bytes; 81.89% used; 112492546 free inodes.

server1 `/tmp`: 324592496640 available bytes; 81.89% used; 112492546 free inodes.

server1 `/var/tmp`: 324592496640 available bytes; 81.89% used; 112492546 free inodes.

server1 `/mnt/raid5`: 499558301696 available bytes; 97.71% used; 337724530 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40748511232 available bytes; 97.73% used; 110430362 free inodes.

server2 `/home`: 40748511232 available bytes; 97.73% used; 110430362 free inodes.

server2 `/tmp`: 40748511232 available bytes; 97.73% used; 110430362 free inodes.

server2 `/var/tmp`: 40748511232 available bytes; 97.73% used; 110430362 free inodes.

server2 `/mnt/raid5`: 522357313536 available bytes; 96.39% used; 445194406 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291652575232 available bytes; 83.72% used; 114161300 free inodes.

server3 `/home`: 291652575232 available bytes; 83.72% used; 114161300 free inodes.

server3 `/data`: 21167636480 available bytes; 99.71% used; 225840169 free inodes.

server3 `/tmp`: 291652575232 available bytes; 83.72% used; 114161300 free inodes.

server3 `/var/tmp`: 291652575232 available bytes; 83.72% used; 114161300 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105826340864 available bytes; 94.09% used; 114349379 free inodes.

server4 `/home`: 105826340864 available bytes; 94.09% used; 114349379 free inodes.

server4 `/data`: 252593057792 available bytes; 96.51% used; 225366776 free inodes.

server4 `/tmp`: 105826340864 available bytes; 94.09% used; 114349379 free inodes.

server4 `/var/tmp`: 105826340864 available bytes; 94.09% used; 114349379 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
