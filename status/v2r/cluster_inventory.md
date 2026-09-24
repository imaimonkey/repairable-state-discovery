# V2R cluster inventory

2026-09-24T05:02:45.470234+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324612407296 available bytes; 81.89% used; 112492668 free inodes.

server1 `/home`: 324612407296 available bytes; 81.89% used; 112492668 free inodes.

server1 `/tmp`: 324612407296 available bytes; 81.89% used; 112492668 free inodes.

server1 `/var/tmp`: 324612407296 available bytes; 81.89% used; 112492668 free inodes.

server1 `/mnt/raid5`: 463724740608 available bytes; 97.87% used; 337724570 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40759726080 available bytes; 97.73% used; 110430406 free inodes.

server2 `/home`: 40759726080 available bytes; 97.73% used; 110430406 free inodes.

server2 `/tmp`: 40759726080 available bytes; 97.73% used; 110430406 free inodes.

server2 `/var/tmp`: 40759726080 available bytes; 97.73% used; 110430406 free inodes.

server2 `/mnt/raid5`: 523505438720 available bytes; 96.38% used; 445194884 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291657756672 available bytes; 83.72% used; 114160937 free inodes.

server3 `/home`: 291657756672 available bytes; 83.72% used; 114160937 free inodes.

server3 `/data`: 23293792256 available bytes; 99.68% used; 225840380 free inodes.

server3 `/tmp`: 291657756672 available bytes; 83.72% used; 114160937 free inodes.

server3 `/var/tmp`: 291657756672 available bytes; 83.72% used; 114160937 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105826861056 available bytes; 94.09% used; 114349383 free inodes.

server4 `/home`: 105826861056 available bytes; 94.09% used; 114349383 free inodes.

server4 `/data`: 252699963392 available bytes; 96.51% used; 225366800 free inodes.

server4 `/tmp`: 105826861056 available bytes; 94.09% used; 114349383 free inodes.

server4 `/var/tmp`: 105826861056 available bytes; 94.09% used; 114349383 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
