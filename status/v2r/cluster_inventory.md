# V2R cluster inventory

2026-09-24T05:45:14.785181+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324526424064 available bytes; 81.90% used; 112492113 free inodes.

server1 `/home`: 324526424064 available bytes; 81.90% used; 112492113 free inodes.

server1 `/tmp`: 324526424064 available bytes; 81.90% used; 112492113 free inodes.

server1 `/var/tmp`: 324526424064 available bytes; 81.90% used; 112492113 free inodes.

server1 `/mnt/raid5`: 496971964416 available bytes; 97.72% used; 337723926 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57914421248 available bytes; 96.77% used; 110431332 free inodes.

server2 `/home`: 57914421248 available bytes; 96.77% used; 110431332 free inodes.

server2 `/tmp`: 57914421248 available bytes; 96.77% used; 110431332 free inodes.

server2 `/var/tmp`: 57914421248 available bytes; 96.77% used; 110431332 free inodes.

server2 `/mnt/raid5`: 521910247424 available bytes; 96.39% used; 445193539 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126795776000 available bytes; 92.92% used; 114175606 free inodes.

server3 `/home`: 126795776000 available bytes; 92.92% used; 114175606 free inodes.

server3 `/data`: 185236717568 available bytes; 97.44% used; 225839093 free inodes.

server3 `/tmp`: 126795776000 available bytes; 92.92% used; 114175606 free inodes.

server3 `/var/tmp`: 126795776000 available bytes; 92.92% used; 114175606 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105816244224 available bytes; 94.10% used; 114349351 free inodes.

server4 `/home`: 105816244224 available bytes; 94.10% used; 114349351 free inodes.

server4 `/data`: 251477778432 available bytes; 96.52% used; 225358018 free inodes.

server4 `/tmp`: 105816244224 available bytes; 94.10% used; 114349351 free inodes.

server4 `/var/tmp`: 105816244224 available bytes; 94.10% used; 114349351 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
