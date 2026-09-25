# V2R cluster inventory

2026-09-25T18:05:06.077062+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318762217472 available bytes; 82.22% used; 112476342 free inodes.

server1 `/home`: 318762217472 available bytes; 82.22% used; 112476342 free inodes.

server1 `/tmp`: 318762217472 available bytes; 82.22% used; 112476342 free inodes.

server1 `/var/tmp`: 318762217472 available bytes; 82.22% used; 112476342 free inodes.

server1 `/mnt/raid5`: 371225096192 available bytes; 98.30% used; 337542400 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23105339392 available bytes; 98.71% used; 110407932 free inodes.

server2 `/home`: 23105339392 available bytes; 98.71% used; 110407932 free inodes.

server2 `/tmp`: 23105339392 available bytes; 98.71% used; 110407932 free inodes.

server2 `/var/tmp`: 23105339392 available bytes; 98.71% used; 110407932 free inodes.

server2 `/mnt/raid5`: 314732179456 available bytes; 97.83% used; 445067784 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84392325120 available bytes; 95.29% used; 114152615 free inodes.

server3 `/home`: 84392325120 available bytes; 95.29% used; 114152615 free inodes.

server3 `/data`: 131474169856 available bytes; 98.18% used; 225810371 free inodes.

server3 `/tmp`: 84392325120 available bytes; 95.29% used; 114152615 free inodes.

server3 `/var/tmp`: 84392325120 available bytes; 95.29% used; 114152615 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105616564224 available bytes; 94.11% used; 114349604 free inodes.

server4 `/home`: 105616564224 available bytes; 94.11% used; 114349604 free inodes.

server4 `/data`: 229742395392 available bytes; 96.82% used; 224932357 free inodes.

server4 `/tmp`: 105616564224 available bytes; 94.11% used; 114349604 free inodes.

server4 `/var/tmp`: 105616564224 available bytes; 94.11% used; 114349604 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
