# V2R cluster inventory

2026-09-25T21:03:58.667267+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318698536960 available bytes; 82.22% used; 112476316 free inodes.

server1 `/home`: 318698536960 available bytes; 82.22% used; 112476316 free inodes.

server1 `/tmp`: 318698536960 available bytes; 82.22% used; 112476316 free inodes.

server1 `/var/tmp`: 318698536960 available bytes; 82.22% used; 112476316 free inodes.

server1 `/mnt/raid5`: 368609505280 available bytes; 98.31% used; 337539504 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22888996864 available bytes; 98.72% used; 110405680 free inodes.

server2 `/home`: 22888996864 available bytes; 98.72% used; 110405680 free inodes.

server2 `/tmp`: 22888996864 available bytes; 98.72% used; 110405680 free inodes.

server2 `/var/tmp`: 22888996864 available bytes; 98.72% used; 110405680 free inodes.

server2 `/mnt/raid5`: 302302392320 available bytes; 97.91% used; 445056061 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84367155200 available bytes; 95.29% used; 114152622 free inodes.

server3 `/home`: 84367155200 available bytes; 95.29% used; 114152622 free inodes.

server3 `/data`: 126048124928 available bytes; 98.26% used; 225807457 free inodes.

server3 `/tmp`: 84367155200 available bytes; 95.29% used; 114152622 free inodes.

server3 `/var/tmp`: 84367155200 available bytes; 95.29% used; 114152622 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105422127104 available bytes; 94.12% used; 114347432 free inodes.

server4 `/home`: 105422127104 available bytes; 94.12% used; 114347432 free inodes.

server4 `/data`: 218524807168 available bytes; 96.98% used; 224921709 free inodes.

server4 `/tmp`: 105422127104 available bytes; 94.12% used; 114347432 free inodes.

server4 `/var/tmp`: 105422127104 available bytes; 94.12% used; 114347432 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
