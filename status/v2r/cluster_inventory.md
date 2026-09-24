# V2R cluster inventory

2026-09-24T12:12:59.089566+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 322648825856 available bytes; 82.00% used; 112464398 free inodes.

server1 `/home`: 322648825856 available bytes; 82.00% used; 112464398 free inodes.

server1 `/tmp`: 322648825856 available bytes; 82.00% used; 112464398 free inodes.

server1 `/var/tmp`: 322648825856 available bytes; 82.00% used; 112464398 free inodes.

server1 `/mnt/raid5`: 405238358016 available bytes; 98.14% used; 337684398 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57618841600 available bytes; 96.79% used; 110429574 free inodes.

server2 `/home`: 57618841600 available bytes; 96.79% used; 110429574 free inodes.

server2 `/tmp`: 57618841600 available bytes; 96.79% used; 110429574 free inodes.

server2 `/var/tmp`: 57618841600 available bytes; 96.79% used; 110429574 free inodes.

server2 `/mnt/raid5`: 509027590144 available bytes; 96.48% used; 445172221 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85268992000 available bytes; 95.24% used; 114168546 free inodes.

server3 `/home`: 85268992000 available bytes; 95.24% used; 114168546 free inodes.

server3 `/data`: 163501154304 available bytes; 97.74% used; 225815389 free inodes.

server3 `/tmp`: 85268992000 available bytes; 95.24% used; 114168546 free inodes.

server3 `/var/tmp`: 85268992000 available bytes; 95.24% used; 114168546 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105781399552 available bytes; 94.10% used; 114348816 free inodes.

server4 `/home`: 105781399552 available bytes; 94.10% used; 114348816 free inodes.

server4 `/data`: 90424864768 available bytes; 98.75% used; 225257322 free inodes.

server4 `/tmp`: 105781399552 available bytes; 94.10% used; 114348816 free inodes.

server4 `/var/tmp`: 105781399552 available bytes; 94.10% used; 114348816 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
