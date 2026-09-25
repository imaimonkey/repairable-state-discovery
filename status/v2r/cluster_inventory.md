# V2R cluster inventory

2026-09-25T07:29:07.097507+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318870056960 available bytes; 82.21% used; 112480370 free inodes.

server1 `/home`: 318870056960 available bytes; 82.21% used; 112480370 free inodes.

server1 `/tmp`: 318870056960 available bytes; 82.21% used; 112480370 free inodes.

server1 `/var/tmp`: 318870056960 available bytes; 82.21% used; 112480370 free inodes.

server1 `/mnt/raid5`: 385897439232 available bytes; 98.23% used; 337558428 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22861242368 available bytes; 98.72% used; 110410502 free inodes.

server2 `/home`: 22861242368 available bytes; 98.72% used; 110410502 free inodes.

server2 `/tmp`: 22861242368 available bytes; 98.72% used; 110410502 free inodes.

server2 `/var/tmp`: 22861242368 available bytes; 98.72% used; 110410502 free inodes.

server2 `/mnt/raid5`: 343272378368 available bytes; 97.63% used; 445097486 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84446736384 available bytes; 95.29% used; 114156035 free inodes.

server3 `/home`: 84446736384 available bytes; 95.29% used; 114156035 free inodes.

server3 `/data`: 142394007552 available bytes; 98.03% used; 225812716 free inodes.

server3 `/tmp`: 84446736384 available bytes; 95.29% used; 114156035 free inodes.

server3 `/var/tmp`: 84446736384 available bytes; 95.29% used; 114156035 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105637912576 available bytes; 94.11% used; 114350360 free inodes.

server4 `/home`: 105637912576 available bytes; 94.11% used; 114350360 free inodes.

server4 `/data`: 249100165120 available bytes; 96.56% used; 225014549 free inodes.

server4 `/tmp`: 105637912576 available bytes; 94.11% used; 114350360 free inodes.

server4 `/var/tmp`: 105637912576 available bytes; 94.11% used; 114350360 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
