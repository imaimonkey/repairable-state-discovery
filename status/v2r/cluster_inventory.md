# V2R cluster inventory

2026-09-23T22:32:07.328042+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325694668800 available bytes; 81.83% used; 112501387 free inodes.

server1 `/home`: 325694668800 available bytes; 81.83% used; 112501387 free inodes.

server1 `/tmp`: 325694668800 available bytes; 81.83% used; 112501387 free inodes.

server1 `/var/tmp`: 325694668800 available bytes; 81.83% used; 112501387 free inodes.

server1 `/mnt/raid5`: 1388101177344 available bytes; 93.63% used; 337739838 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41081798656 available bytes; 97.71% used; 110432627 free inodes.

server2 `/home`: 41081798656 available bytes; 97.71% used; 110432627 free inodes.

server2 `/tmp`: 41081798656 available bytes; 97.71% used; 110432627 free inodes.

server2 `/var/tmp`: 41081798656 available bytes; 97.71% used; 110432627 free inodes.

server2 `/mnt/raid5`: 536046112768 available bytes; 96.30% used; 445206575 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293025943552 available bytes; 83.65% used; 114223250 free inodes.

server3 `/home`: 293025943552 available bytes; 83.65% used; 114223250 free inodes.

server3 `/data`: 82430656512 available bytes; 98.86% used; 225847337 free inodes.

server3 `/tmp`: 293025943552 available bytes; 83.65% used; 114223250 free inodes.

server3 `/var/tmp`: 293025943552 available bytes; 83.65% used; 114223250 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106368655360 available bytes; 94.06% used; 114354459 free inodes.

server4 `/home`: 106368655360 available bytes; 94.06% used; 114354459 free inodes.

server4 `/data`: 300068245504 available bytes; 95.85% used; 225436798 free inodes.

server4 `/tmp`: 106368655360 available bytes; 94.06% used; 114354459 free inodes.

server4 `/var/tmp`: 106368655360 available bytes; 94.06% used; 114354459 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
