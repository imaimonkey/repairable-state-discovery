# V2R cluster inventory

2026-09-24T11:52:43.697497+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324293509120 available bytes; 81.91% used; 112488519 free inodes.

server1 `/home`: 324293509120 available bytes; 81.91% used; 112488519 free inodes.

server1 `/tmp`: 324293509120 available bytes; 81.91% used; 112488519 free inodes.

server1 `/var/tmp`: 324293509120 available bytes; 81.91% used; 112488519 free inodes.

server1 `/mnt/raid5`: 417438162944 available bytes; 98.09% used; 337686565 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57637351424 available bytes; 96.78% used; 110429772 free inodes.

server2 `/home`: 57637351424 available bytes; 96.78% used; 110429772 free inodes.

server2 `/tmp`: 57637351424 available bytes; 96.78% used; 110429772 free inodes.

server2 `/var/tmp`: 57637351424 available bytes; 96.78% used; 110429772 free inodes.

server2 `/mnt/raid5`: 509938061312 available bytes; 96.48% used; 445172540 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85338374144 available bytes; 95.24% used; 114173309 free inodes.

server3 `/home`: 85338374144 available bytes; 95.24% used; 114173309 free inodes.

server3 `/data`: 163639406592 available bytes; 97.74% used; 225815818 free inodes.

server3 `/tmp`: 85338374144 available bytes; 95.24% used; 114173309 free inodes.

server3 `/var/tmp`: 85338374144 available bytes; 95.24% used; 114173309 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105727451136 available bytes; 94.10% used; 114348834 free inodes.

server4 `/home`: 105727451136 available bytes; 94.10% used; 114348834 free inodes.

server4 `/data`: 115383128064 available bytes; 98.41% used; 225257910 free inodes.

server4 `/tmp`: 105727451136 available bytes; 94.10% used; 114348834 free inodes.

server4 `/var/tmp`: 105727451136 available bytes; 94.10% used; 114348834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
