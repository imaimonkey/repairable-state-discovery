# V2R cluster inventory

2026-09-24T07:18:40.965802+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324451438592 available bytes; 81.90% used; 112491249 free inodes.

server1 `/home`: 324451438592 available bytes; 81.90% used; 112491249 free inodes.

server1 `/tmp`: 324451438592 available bytes; 81.90% used; 112491249 free inodes.

server1 `/var/tmp`: 324451438592 available bytes; 81.90% used; 112491249 free inodes.

server1 `/mnt/raid5`: 517419241472 available bytes; 97.63% used; 337722820 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57851551744 available bytes; 96.77% used; 110431129 free inodes.

server2 `/home`: 57851551744 available bytes; 96.77% used; 110431129 free inodes.

server2 `/tmp`: 57851547648 available bytes; 96.77% used; 110431129 free inodes.

server2 `/var/tmp`: 57851547648 available bytes; 96.77% used; 110431129 free inodes.

server2 `/mnt/raid5`: 518628409344 available bytes; 96.42% used; 445181304 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127139364864 available bytes; 92.91% used; 114198549 free inodes.

server3 `/home`: 127139364864 available bytes; 92.91% used; 114198549 free inodes.

server3 `/data`: 139047809024 available bytes; 98.08% used; 225834370 free inodes.

server3 `/tmp`: 127139364864 available bytes; 92.91% used; 114198549 free inodes.

server3 `/var/tmp`: 127139364864 available bytes; 92.91% used; 114198549 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105789779968 available bytes; 94.10% used; 114349211 free inodes.

server4 `/home`: 105789779968 available bytes; 94.10% used; 114349211 free inodes.

server4 `/data`: 290847809536 available bytes; 95.98% used; 225367124 free inodes.

server4 `/tmp`: 105789779968 available bytes; 94.10% used; 114349211 free inodes.

server4 `/var/tmp`: 105789779968 available bytes; 94.10% used; 114349211 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
