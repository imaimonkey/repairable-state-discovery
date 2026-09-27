# V2R cluster inventory

2026-09-27T07:17:19.817873+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314477961216 available bytes; 82.46% used; 112440786 free inodes.

server1 `/home`: 314477961216 available bytes; 82.46% used; 112440786 free inodes.

server1 `/tmp`: 314477961216 available bytes; 82.46% used; 112440786 free inodes.

server1 `/var/tmp`: 314477961216 available bytes; 82.46% used; 112440786 free inodes.

server1 `/mnt/raid5`: 634660933632 available bytes; 97.09% used; 337400004 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17609302016 available bytes; 99.02% used; 110364996 free inodes.

server2 `/home`: 17609302016 available bytes; 99.02% used; 110364996 free inodes.

server2 `/tmp`: 17609302016 available bytes; 99.02% used; 110364996 free inodes.

server2 `/var/tmp`: 17609302016 available bytes; 99.02% used; 110364996 free inodes.

server2 `/mnt/raid5`: 571758223360 available bytes; 96.05% used; 444874714 free inodes.
| server3 | True | ['3'] | [] | reference_compatible=True |

server3 `/`: 78572097536 available bytes; 95.62% used; 114062884 free inodes.

server3 `/home`: 78572097536 available bytes; 95.62% used; 114062884 free inodes.

server3 `/data`: 1333165887488 available bytes; 81.58% used; 225764365 free inodes.

server3 `/tmp`: 78572097536 available bytes; 95.62% used; 114062884 free inodes.

server3 `/var/tmp`: 78572097536 available bytes; 95.62% used; 114062884 free inodes.
| server4 | True | ['5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111070871552 available bytes; 93.80% used; 114372891 free inodes.

server4 `/home`: 111070871552 available bytes; 93.80% used; 114372891 free inodes.

server4 `/data`: 374365884416 available bytes; 94.83% used; 224771170 free inodes.

server4 `/tmp`: 111070871552 available bytes; 93.80% used; 114372891 free inodes.

server4 `/var/tmp`: 111070871552 available bytes; 93.80% used; 114372891 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
