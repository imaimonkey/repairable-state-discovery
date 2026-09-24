# V2R cluster inventory

2026-09-24T11:49:35.965417+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324330844160 available bytes; 81.91% used; 112488695 free inodes.

server1 `/home`: 324330844160 available bytes; 81.91% used; 112488695 free inodes.

server1 `/tmp`: 324330844160 available bytes; 81.91% used; 112488695 free inodes.

server1 `/var/tmp`: 324330844160 available bytes; 81.91% used; 112488695 free inodes.

server1 `/mnt/raid5`: 421923524608 available bytes; 98.06% used; 337686991 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57640448000 available bytes; 96.78% used; 110429804 free inodes.

server2 `/home`: 57640448000 available bytes; 96.78% used; 110429804 free inodes.

server2 `/tmp`: 57640448000 available bytes; 96.78% used; 110429804 free inodes.

server2 `/var/tmp`: 57640448000 available bytes; 96.78% used; 110429804 free inodes.

server2 `/mnt/raid5`: 510039728128 available bytes; 96.48% used; 445172856 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85339701248 available bytes; 95.24% used; 114173345 free inodes.

server3 `/home`: 85339701248 available bytes; 95.24% used; 114173345 free inodes.

server3 `/data`: 163658338304 available bytes; 97.74% used; 225815879 free inodes.

server3 `/tmp`: 85339701248 available bytes; 95.24% used; 114173345 free inodes.

server3 `/var/tmp`: 85339701248 available bytes; 95.24% used; 114173345 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105727569920 available bytes; 94.10% used; 114348834 free inodes.

server4 `/home`: 105727569920 available bytes; 94.10% used; 114348834 free inodes.

server4 `/data`: 115388628992 available bytes; 98.41% used; 225257934 free inodes.

server4 `/tmp`: 105727569920 available bytes; 94.10% used; 114348834 free inodes.

server4 `/var/tmp`: 105727569920 available bytes; 94.10% used; 114348834 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
