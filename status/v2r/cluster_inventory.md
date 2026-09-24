# V2R cluster inventory

2026-09-24T05:48:25.467141+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324528738304 available bytes; 81.90% used; 112492063 free inodes.

server1 `/home`: 324528738304 available bytes; 81.90% used; 112492063 free inodes.

server1 `/tmp`: 324528738304 available bytes; 81.90% used; 112492063 free inodes.

server1 `/var/tmp`: 324528738304 available bytes; 81.90% used; 112492063 free inodes.

server1 `/mnt/raid5`: 517612900352 available bytes; 97.63% used; 337723913 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57906311168 available bytes; 96.77% used; 110431322 free inodes.

server2 `/home`: 57906311168 available bytes; 96.77% used; 110431322 free inodes.

server2 `/tmp`: 57906311168 available bytes; 96.77% used; 110431322 free inodes.

server2 `/var/tmp`: 57906311168 available bytes; 96.77% used; 110431322 free inodes.

server2 `/mnt/raid5`: 521810272256 available bytes; 96.39% used; 445193246 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126604742656 available bytes; 92.93% used; 114167050 free inodes.

server3 `/home`: 126604742656 available bytes; 92.93% used; 114167050 free inodes.

server3 `/data`: 185223213056 available bytes; 97.44% used; 225838671 free inodes.

server3 `/tmp`: 126604742656 available bytes; 92.93% used; 114167050 free inodes.

server3 `/var/tmp`: 126604742656 available bytes; 92.93% used; 114167050 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105816059904 available bytes; 94.10% used; 114349347 free inodes.

server4 `/home`: 105816059904 available bytes; 94.10% used; 114349347 free inodes.

server4 `/data`: 251481145344 available bytes; 96.52% used; 225358000 free inodes.

server4 `/tmp`: 105816059904 available bytes; 94.10% used; 114349347 free inodes.

server4 `/var/tmp`: 105816059904 available bytes; 94.10% used; 114349347 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
