# V2R cluster inventory

2026-09-25T05:32:08.794187+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318874374144 available bytes; 82.21% used; 112480348 free inodes.

server1 `/home`: 318874374144 available bytes; 82.21% used; 112480348 free inodes.

server1 `/tmp`: 318874374144 available bytes; 82.21% used; 112480348 free inodes.

server1 `/var/tmp`: 318874374144 available bytes; 82.21% used; 112480348 free inodes.

server1 `/mnt/raid5`: 408488648704 available bytes; 98.13% used; 337568012 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22921097216 available bytes; 98.72% used; 110410447 free inodes.

server2 `/home`: 22921097216 available bytes; 98.72% used; 110410447 free inodes.

server2 `/tmp`: 22921097216 available bytes; 98.72% used; 110410447 free inodes.

server2 `/var/tmp`: 22921097216 available bytes; 98.72% used; 110410447 free inodes.

server2 `/mnt/raid5`: 475083362304 available bytes; 96.72% used; 445107931 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84314210304 available bytes; 95.29% used; 114156043 free inodes.

server3 `/home`: 84314210304 available bytes; 95.29% used; 114156043 free inodes.

server3 `/data`: 142781771776 available bytes; 98.03% used; 225814783 free inodes.

server3 `/tmp`: 84314210304 available bytes; 95.29% used; 114156043 free inodes.

server3 `/var/tmp`: 84314210304 available bytes; 95.29% used; 114156043 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105658343424 available bytes; 94.10% used; 114350392 free inodes.

server4 `/home`: 105658343424 available bytes; 94.10% used; 114350392 free inodes.

server4 `/data`: 26394046464 available bytes; 99.64% used; 224967992 free inodes.

server4 `/tmp`: 105658343424 available bytes; 94.10% used; 114350392 free inodes.

server4 `/var/tmp`: 105658343424 available bytes; 94.10% used; 114350392 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
