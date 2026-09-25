# V2R cluster inventory

2026-09-25T22:11:12.682374+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318692921344 available bytes; 82.22% used; 112476301 free inodes.

server1 `/home`: 318692921344 available bytes; 82.22% used; 112476301 free inodes.

server1 `/tmp`: 318692921344 available bytes; 82.22% used; 112476301 free inodes.

server1 `/var/tmp`: 318692921344 available bytes; 82.22% used; 112476301 free inodes.

server1 `/mnt/raid5`: 360282378240 available bytes; 98.35% used; 337539032 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22948679680 available bytes; 98.72% used; 110406242 free inodes.

server2 `/home`: 22948679680 available bytes; 98.72% used; 110406242 free inodes.

server2 `/tmp`: 22948679680 available bytes; 98.72% used; 110406242 free inodes.

server2 `/var/tmp`: 22948679680 available bytes; 98.72% used; 110406242 free inodes.

server2 `/mnt/raid5`: 299862749184 available bytes; 97.93% used; 445053625 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84358750208 available bytes; 95.29% used; 114152630 free inodes.

server3 `/home`: 84358750208 available bytes; 95.29% used; 114152630 free inodes.

server3 `/data`: 125876649984 available bytes; 98.26% used; 225806295 free inodes.

server3 `/tmp`: 84358750208 available bytes; 95.29% used; 114152630 free inodes.

server3 `/var/tmp`: 84358750208 available bytes; 95.29% used; 114152630 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105312206848 available bytes; 94.12% used; 114347146 free inodes.

server4 `/home`: 105312206848 available bytes; 94.12% used; 114347146 free inodes.

server4 `/data`: 208744828928 available bytes; 97.12% used; 224919045 free inodes.

server4 `/tmp`: 105312206848 available bytes; 94.12% used; 114347146 free inodes.

server4 `/var/tmp`: 105312206848 available bytes; 94.12% used; 114347146 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
