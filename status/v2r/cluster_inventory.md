# V2R cluster inventory

2026-09-25T21:02:27.022030+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318698737664 available bytes; 82.22% used; 112476320 free inodes.

server1 `/home`: 318698737664 available bytes; 82.22% used; 112476320 free inodes.

server1 `/tmp`: 318698737664 available bytes; 82.22% used; 112476320 free inodes.

server1 `/var/tmp`: 318698737664 available bytes; 82.22% used; 112476320 free inodes.

server1 `/mnt/raid5`: 368615428096 available bytes; 98.31% used; 337539515 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22888939520 available bytes; 98.72% used; 110405678 free inodes.

server2 `/home`: 22888939520 available bytes; 98.72% used; 110405678 free inodes.

server2 `/tmp`: 22888939520 available bytes; 98.72% used; 110405678 free inodes.

server2 `/var/tmp`: 22888939520 available bytes; 98.72% used; 110405678 free inodes.

server2 `/mnt/raid5`: 302347972608 available bytes; 97.91% used; 445056121 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84367368192 available bytes; 95.29% used; 114152622 free inodes.

server3 `/home`: 84367368192 available bytes; 95.29% used; 114152622 free inodes.

server3 `/data`: 126052679680 available bytes; 98.26% used; 225807476 free inodes.

server3 `/tmp`: 84367368192 available bytes; 95.29% used; 114152622 free inodes.

server3 `/var/tmp`: 84367368192 available bytes; 95.29% used; 114152622 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105570459648 available bytes; 94.11% used; 114348483 free inodes.

server4 `/home`: 105570459648 available bytes; 94.11% used; 114348483 free inodes.

server4 `/data`: 218876588032 available bytes; 96.98% used; 224921785 free inodes.

server4 `/tmp`: 105570459648 available bytes; 94.11% used; 114348483 free inodes.

server4 `/var/tmp`: 105570459648 available bytes; 94.11% used; 114348483 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
