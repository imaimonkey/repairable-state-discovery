# V2R cluster inventory

2026-09-24T07:21:48.139761+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324449017856 available bytes; 81.90% used; 112491216 free inodes.

server1 `/home`: 324449017856 available bytes; 81.90% used; 112491216 free inodes.

server1 `/tmp`: 324449017856 available bytes; 81.90% used; 112491216 free inodes.

server1 `/var/tmp`: 324449017856 available bytes; 81.90% used; 112491216 free inodes.

server1 `/mnt/raid5`: 517416423424 available bytes; 97.63% used; 337722820 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57851940864 available bytes; 96.77% used; 110431123 free inodes.

server2 `/home`: 57851940864 available bytes; 96.77% used; 110431123 free inodes.

server2 `/tmp`: 57851940864 available bytes; 96.77% used; 110431123 free inodes.

server2 `/var/tmp`: 57851940864 available bytes; 96.77% used; 110431123 free inodes.

server2 `/mnt/raid5`: 518537707520 available bytes; 96.42% used; 445181194 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127141625856 available bytes; 92.91% used; 114197780 free inodes.

server3 `/home`: 127141625856 available bytes; 92.91% used; 114197780 free inodes.

server3 `/data`: 139052949504 available bytes; 98.08% used; 225834305 free inodes.

server3 `/tmp`: 127141625856 available bytes; 92.91% used; 114197780 free inodes.

server3 `/var/tmp`: 127141625856 available bytes; 92.91% used; 114197780 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105781051392 available bytes; 94.10% used; 114349193 free inodes.

server4 `/home`: 105781051392 available bytes; 94.10% used; 114349193 free inodes.

server4 `/data`: 288712499200 available bytes; 96.01% used; 225366989 free inodes.

server4 `/tmp`: 105781051392 available bytes; 94.10% used; 114349193 free inodes.

server4 `/var/tmp`: 105781051392 available bytes; 94.10% used; 114349193 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
