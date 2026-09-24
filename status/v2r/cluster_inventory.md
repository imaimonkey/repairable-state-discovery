# V2R cluster inventory

2026-09-24T06:31:59.791881+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324507111424 available bytes; 81.90% used; 112491649 free inodes.

server1 `/home`: 324507111424 available bytes; 81.90% used; 112491649 free inodes.

server1 `/tmp`: 324507111424 available bytes; 81.90% used; 112491649 free inodes.

server1 `/var/tmp`: 324507111424 available bytes; 81.90% used; 112491649 free inodes.

server1 `/mnt/raid5`: 517577138176 available bytes; 97.63% used; 337723770 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57882566656 available bytes; 96.77% used; 110431203 free inodes.

server2 `/home`: 57882566656 available bytes; 96.77% used; 110431203 free inodes.

server2 `/tmp`: 57882566656 available bytes; 96.77% used; 110431203 free inodes.

server2 `/var/tmp`: 57882566656 available bytes; 96.77% used; 110431203 free inodes.

server2 `/mnt/raid5`: 520186814464 available bytes; 96.41% used; 445191848 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127199830016 available bytes; 92.90% used; 114197456 free inodes.

server3 `/home`: 127199830016 available bytes; 92.90% used; 114197456 free inodes.

server3 `/data`: 139455729664 available bytes; 98.07% used; 225835709 free inodes.

server3 `/tmp`: 127199830016 available bytes; 92.90% used; 114197456 free inodes.

server3 `/var/tmp`: 127199830016 available bytes; 92.90% used; 114197456 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105805369344 available bytes; 94.10% used; 114349268 free inodes.

server4 `/home`: 105805369344 available bytes; 94.10% used; 114349268 free inodes.

server4 `/data`: 327093841920 available bytes; 95.48% used; 225372883 free inodes.

server4 `/tmp`: 105805369344 available bytes; 94.10% used; 114349268 free inodes.

server4 `/var/tmp`: 105805369344 available bytes; 94.10% used; 114349268 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
