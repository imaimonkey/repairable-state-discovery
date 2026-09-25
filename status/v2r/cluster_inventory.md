# V2R cluster inventory

2026-09-25T02:08:49.410060+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319022870528 available bytes; 82.20% used; 112480581 free inodes.

server1 `/home`: 319022870528 available bytes; 82.20% used; 112480581 free inodes.

server1 `/tmp`: 319022870528 available bytes; 82.20% used; 112480581 free inodes.

server1 `/var/tmp`: 319022870528 available bytes; 82.20% used; 112480581 free inodes.

server1 `/mnt/raid5`: 416256475136 available bytes; 98.09% used; 337608422 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23024521216 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 23024521216 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 23024521216 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 23024521216 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 484061040640 available bytes; 96.66% used; 445114444 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84351746048 available bytes; 95.29% used; 114156074 free inodes.

server3 `/home`: 84351746048 available bytes; 95.29% used; 114156074 free inodes.

server3 `/data`: 145963233280 available bytes; 97.98% used; 225811554 free inodes.

server3 `/tmp`: 84351746048 available bytes; 95.29% used; 114156074 free inodes.

server3 `/var/tmp`: 84351746048 available bytes; 95.29% used; 114156074 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105752481792 available bytes; 94.10% used; 114348242 free inodes.

server4 `/home`: 105752481792 available bytes; 94.10% used; 114348242 free inodes.

server4 `/data`: 45032759296 available bytes; 99.38% used; 225019857 free inodes.

server4 `/tmp`: 105752481792 available bytes; 94.10% used; 114348242 free inodes.

server4 `/var/tmp`: 105752481792 available bytes; 94.10% used; 114348242 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
