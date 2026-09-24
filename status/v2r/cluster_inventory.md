# V2R cluster inventory

2026-09-24T07:26:27.888934+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324453814272 available bytes; 81.90% used; 112491180 free inodes.

server1 `/home`: 324453814272 available bytes; 81.90% used; 112491180 free inodes.

server1 `/tmp`: 324453814272 available bytes; 81.90% used; 112491180 free inodes.

server1 `/var/tmp`: 324453814272 available bytes; 81.90% used; 112491180 free inodes.

server1 `/mnt/raid5`: 517411422208 available bytes; 97.63% used; 337722799 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57850691584 available bytes; 96.77% used; 110431109 free inodes.

server2 `/home`: 57850691584 available bytes; 96.77% used; 110431109 free inodes.

server2 `/tmp`: 57850691584 available bytes; 96.77% used; 110431109 free inodes.

server2 `/var/tmp`: 57850691584 available bytes; 96.77% used; 110431109 free inodes.

server2 `/mnt/raid5`: 518394486784 available bytes; 96.42% used; 445181069 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126780465152 available bytes; 92.93% used; 114174658 free inodes.

server3 `/home`: 126780465152 available bytes; 92.93% used; 114174658 free inodes.

server3 `/data`: 139009998848 available bytes; 98.08% used; 225834196 free inodes.

server3 `/tmp`: 126780465152 available bytes; 92.93% used; 114174658 free inodes.

server3 `/var/tmp`: 126780465152 available bytes; 92.93% used; 114174658 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780883456 available bytes; 94.10% used; 114349193 free inodes.

server4 `/home`: 105780883456 available bytes; 94.10% used; 114349193 free inodes.

server4 `/data`: 285862637568 available bytes; 96.05% used; 225366846 free inodes.

server4 `/tmp`: 105780883456 available bytes; 94.10% used; 114349193 free inodes.

server4 `/var/tmp`: 105780883456 available bytes; 94.10% used; 114349193 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
