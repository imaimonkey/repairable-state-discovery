# V2R cluster inventory

2026-09-26T06:14:13.006809+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318778740736 available bytes; 82.22% used; 112476280 free inodes.

server1 `/home`: 318778740736 available bytes; 82.22% used; 112476280 free inodes.

server1 `/tmp`: 318778740736 available bytes; 82.22% used; 112476280 free inodes.

server1 `/var/tmp`: 318778740736 available bytes; 82.22% used; 112476280 free inodes.

server1 `/mnt/raid5`: 220188491776 available bytes; 98.99% used; 337539878 free inodes.
| server2 | True | [] | [] |

server2 `/`: 19802640384 available bytes; 98.90% used; 110401384 free inodes.

server2 `/home`: 19802640384 available bytes; 98.90% used; 110401384 free inodes.

server2 `/tmp`: 19802640384 available bytes; 98.90% used; 110401384 free inodes.

server2 `/var/tmp`: 19802640384 available bytes; 98.90% used; 110401384 free inodes.

server2 `/mnt/raid5`: 273501343744 available bytes; 98.11% used; 445029267 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82565107712 available bytes; 95.39% used; 114110907 free inodes.

server3 `/home`: 82565107712 available bytes; 95.39% used; 114110907 free inodes.

server3 `/data`: 123991826432 available bytes; 98.29% used; 225822548 free inodes.

server3 `/tmp`: 82565107712 available bytes; 95.39% used; 114110907 free inodes.

server3 `/var/tmp`: 82565107712 available bytes; 95.39% used; 114110907 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105990180864 available bytes; 94.09% used; 114347063 free inodes.

server4 `/home`: 105990180864 available bytes; 94.09% used; 114347063 free inodes.

server4 `/data`: 106644152320 available bytes; 98.53% used; 224923655 free inodes.

server4 `/tmp`: 105990180864 available bytes; 94.09% used; 114347063 free inodes.

server4 `/var/tmp`: 105990180864 available bytes; 94.09% used; 114347063 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
