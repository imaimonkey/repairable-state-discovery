# V2R cluster inventory

2026-09-24T12:47:32.809505+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324038676480 available bytes; 81.92% used; 112481555 free inodes.

server1 `/home`: 324038676480 available bytes; 81.92% used; 112481555 free inodes.

server1 `/tmp`: 324038676480 available bytes; 81.92% used; 112481555 free inodes.

server1 `/var/tmp`: 324038676480 available bytes; 81.92% used; 112481555 free inodes.

server1 `/mnt/raid5`: 403355316224 available bytes; 98.15% used; 337680228 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57577910272 available bytes; 96.79% used; 110429161 free inodes.

server2 `/home`: 57577910272 available bytes; 96.79% used; 110429161 free inodes.

server2 `/tmp`: 57577910272 available bytes; 96.79% used; 110429161 free inodes.

server2 `/var/tmp`: 57577910272 available bytes; 96.79% used; 110429161 free inodes.

server2 `/mnt/raid5`: 507432484864 available bytes; 96.49% used; 445171230 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85691924480 available bytes; 95.22% used; 114197242 free inodes.

server3 `/home`: 85691924480 available bytes; 95.22% used; 114197242 free inodes.

server3 `/data`: 163123789824 available bytes; 97.75% used; 225814401 free inodes.

server3 `/tmp`: 85691924480 available bytes; 95.22% used; 114197242 free inodes.

server3 `/var/tmp`: 85691924480 available bytes; 95.22% used; 114197242 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779920896 available bytes; 94.10% used; 114348780 free inodes.

server4 `/home`: 105779920896 available bytes; 94.10% used; 114348780 free inodes.

server4 `/data`: 90046189568 available bytes; 98.76% used; 225257228 free inodes.

server4 `/tmp`: 105779920896 available bytes; 94.10% used; 114348780 free inodes.

server4 `/var/tmp`: 105779920896 available bytes; 94.10% used; 114348780 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
