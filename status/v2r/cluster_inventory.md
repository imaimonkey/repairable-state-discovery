# V2R cluster inventory

2026-09-24T07:07:49.142441+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324478361600 available bytes; 81.90% used; 112491308 free inodes.

server1 `/home`: 324478361600 available bytes; 81.90% used; 112491308 free inodes.

server1 `/tmp`: 324478361600 available bytes; 81.90% used; 112491308 free inodes.

server1 `/var/tmp`: 324478361600 available bytes; 81.90% used; 112491308 free inodes.

server1 `/mnt/raid5`: 517431402496 available bytes; 97.63% used; 337722837 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57861013504 available bytes; 96.77% used; 110431161 free inodes.

server2 `/home`: 57861013504 available bytes; 96.77% used; 110431161 free inodes.

server2 `/tmp`: 57861013504 available bytes; 96.77% used; 110431161 free inodes.

server2 `/var/tmp`: 57861013504 available bytes; 96.77% used; 110431161 free inodes.

server2 `/mnt/raid5`: 518956179456 available bytes; 96.41% used; 445181491 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127167569920 available bytes; 92.90% used; 114199243 free inodes.

server3 `/home`: 127167569920 available bytes; 92.90% used; 114199243 free inodes.

server3 `/data`: 139144003584 available bytes; 98.08% used; 225834613 free inodes.

server3 `/tmp`: 127167569920 available bytes; 92.90% used; 114199243 free inodes.

server3 `/var/tmp`: 127167569920 available bytes; 92.90% used; 114199243 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105790177280 available bytes; 94.10% used; 114349211 free inodes.

server4 `/home`: 105790177280 available bytes; 94.10% used; 114349211 free inodes.

server4 `/data`: 298428416000 available bytes; 95.88% used; 225367496 free inodes.

server4 `/tmp`: 105790177280 available bytes; 94.10% used; 114349211 free inodes.

server4 `/var/tmp`: 105790177280 available bytes; 94.10% used; 114349211 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
