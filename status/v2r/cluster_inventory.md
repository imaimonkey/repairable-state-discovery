# V2R cluster inventory

2026-09-24T05:05:52.813197+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324599291904 available bytes; 81.89% used; 112492636 free inodes.

server1 `/home`: 324599291904 available bytes; 81.89% used; 112492636 free inodes.

server1 `/tmp`: 324599291904 available bytes; 81.89% used; 112492636 free inodes.

server1 `/var/tmp`: 324599291904 available bytes; 81.89% used; 112492636 free inodes.

server1 `/mnt/raid5`: 489212792832 available bytes; 97.76% used; 337724562 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40758484992 available bytes; 97.73% used; 110430394 free inodes.

server2 `/home`: 40758484992 available bytes; 97.73% used; 110430394 free inodes.

server2 `/tmp`: 40758484992 available bytes; 97.73% used; 110430394 free inodes.

server2 `/var/tmp`: 40758484992 available bytes; 97.73% used; 110430394 free inodes.

server2 `/mnt/raid5`: 522879508480 available bytes; 96.39% used; 445194777 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291604226048 available bytes; 83.73% used; 114152015 free inodes.

server3 `/home`: 291604226048 available bytes; 83.73% used; 114152015 free inodes.

server3 `/data`: 23287558144 available bytes; 99.68% used; 225840341 free inodes.

server3 `/tmp`: 291604226048 available bytes; 83.73% used; 114152015 free inodes.

server3 `/var/tmp`: 291604226048 available bytes; 83.73% used; 114152015 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105826725888 available bytes; 94.09% used; 114349383 free inodes.

server4 `/home`: 105826725888 available bytes; 94.09% used; 114349383 free inodes.

server4 `/data`: 252613566464 available bytes; 96.51% used; 225366790 free inodes.

server4 `/tmp`: 105826725888 available bytes; 94.09% used; 114349383 free inodes.

server4 `/var/tmp`: 105826725888 available bytes; 94.09% used; 114349383 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
