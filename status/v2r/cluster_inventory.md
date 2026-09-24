# V2R cluster inventory

2026-09-24T07:14:01.569459+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324454002688 available bytes; 81.90% used; 112491283 free inodes.

server1 `/home`: 324454002688 available bytes; 81.90% used; 112491283 free inodes.

server1 `/tmp`: 324454002688 available bytes; 81.90% used; 112491283 free inodes.

server1 `/var/tmp`: 324454002688 available bytes; 81.90% used; 112491283 free inodes.

server1 `/mnt/raid5`: 500718469120 available bytes; 97.70% used; 337722816 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57853190144 available bytes; 96.77% used; 110431141 free inodes.

server2 `/home`: 57853190144 available bytes; 96.77% used; 110431141 free inodes.

server2 `/tmp`: 57853190144 available bytes; 96.77% used; 110431141 free inodes.

server2 `/var/tmp`: 57853190144 available bytes; 96.77% used; 110431141 free inodes.

server2 `/mnt/raid5`: 518773506048 available bytes; 96.42% used; 445181564 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127145340928 available bytes; 92.90% used; 114199321 free inodes.

server3 `/home`: 127145340928 available bytes; 92.90% used; 114199321 free inodes.

server3 `/data`: 139091091456 available bytes; 98.08% used; 225834470 free inodes.

server3 `/tmp`: 127145340928 available bytes; 92.90% used; 114199321 free inodes.

server3 `/var/tmp`: 127145340928 available bytes; 92.90% used; 114199321 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105789915136 available bytes; 94.10% used; 114349211 free inodes.

server4 `/home`: 105789915136 available bytes; 94.10% used; 114349211 free inodes.

server4 `/data`: 294179442688 available bytes; 95.93% used; 225367277 free inodes.

server4 `/tmp`: 105789915136 available bytes; 94.10% used; 114349211 free inodes.

server4 `/var/tmp`: 105789915136 available bytes; 94.10% used; 114349211 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
