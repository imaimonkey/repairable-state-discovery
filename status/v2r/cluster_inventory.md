# V2R cluster inventory

2026-09-25T15:03:01.827908+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319134978048 available bytes; 82.20% used; 112476955 free inodes.

server1 `/home`: 319134978048 available bytes; 82.20% used; 112476955 free inodes.

server1 `/tmp`: 319134978048 available bytes; 82.20% used; 112476955 free inodes.

server1 `/var/tmp`: 319134978048 available bytes; 82.20% used; 112476955 free inodes.

server1 `/mnt/raid5`: 364010790912 available bytes; 98.33% used; 337546254 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 19261718528 available bytes; 98.93% used; 110407893 free inodes.

server2 `/home`: 19261718528 available bytes; 98.93% used; 110407893 free inodes.

server2 `/tmp`: 19261718528 available bytes; 98.93% used; 110407893 free inodes.

server2 `/var/tmp`: 19261718528 available bytes; 98.93% used; 110407893 free inodes.

server2 `/mnt/raid5`: 320194867200 available bytes; 97.79% used; 445073813 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84426027008 available bytes; 95.29% used; 114153446 free inodes.

server3 `/home`: 84426027008 available bytes; 95.29% used; 114153446 free inodes.

server3 `/data`: 142189793280 available bytes; 98.03% used; 225808157 free inodes.

server3 `/tmp`: 84426027008 available bytes; 95.29% used; 114153446 free inodes.

server3 `/var/tmp`: 84426027008 available bytes; 95.29% used; 114153446 free inodes.
| server4 | True | ['2', '3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105636610048 available bytes; 94.11% used; 114349708 free inodes.

server4 `/home`: 105636610048 available bytes; 94.11% used; 114349708 free inodes.

server4 `/data`: 231410712576 available bytes; 96.80% used; 224944960 free inodes.

server4 `/tmp`: 105636610048 available bytes; 94.11% used; 114349708 free inodes.

server4 `/var/tmp`: 105636610048 available bytes; 94.11% used; 114349708 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
