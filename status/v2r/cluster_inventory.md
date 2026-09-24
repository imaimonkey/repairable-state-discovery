# V2R cluster inventory

2026-09-24T04:43:49.313183+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324621991936 available bytes; 81.89% used; 112492858 free inodes.

server1 `/home`: 324621991936 available bytes; 81.89% used; 112492858 free inodes.

server1 `/tmp`: 324621991936 available bytes; 81.89% used; 112492858 free inodes.

server1 `/var/tmp`: 324621991936 available bytes; 81.89% used; 112492858 free inodes.

server1 `/mnt/raid5`: 464991854592 available bytes; 97.87% used; 337724633 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40769249280 available bytes; 97.73% used; 110430476 free inodes.

server2 `/home`: 40769249280 available bytes; 97.73% used; 110430476 free inodes.

server2 `/tmp`: 40769249280 available bytes; 97.73% used; 110430476 free inodes.

server2 `/var/tmp`: 40769249280 available bytes; 97.73% used; 110430476 free inodes.

server2 `/mnt/raid5`: 524366872576 available bytes; 96.38% used; 445195350 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292401618944 available bytes; 83.68% used; 114200242 free inodes.

server3 `/home`: 292401618944 available bytes; 83.68% used; 114200242 free inodes.

server3 `/data`: 24360394752 available bytes; 99.66% used; 225840691 free inodes.

server3 `/tmp`: 292401618944 available bytes; 83.68% used; 114200242 free inodes.

server3 `/var/tmp`: 292401618944 available bytes; 83.68% used; 114200242 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105836253184 available bytes; 94.09% used; 114349396 free inodes.

server4 `/home`: 105836253184 available bytes; 94.09% used; 114349396 free inodes.

server4 `/data`: 253382733824 available bytes; 96.50% used; 225366864 free inodes.

server4 `/tmp`: 105836253184 available bytes; 94.09% used; 114349396 free inodes.

server4 `/var/tmp`: 105836253184 available bytes; 94.09% used; 114349396 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
