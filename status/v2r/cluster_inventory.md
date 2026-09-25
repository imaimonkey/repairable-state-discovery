# V2R cluster inventory

2026-09-25T21:10:05.214141+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318699450368 available bytes; 82.22% used; 112476314 free inodes.

server1 `/home`: 318699450368 available bytes; 82.22% used; 112476314 free inodes.

server1 `/tmp`: 318699450368 available bytes; 82.22% used; 112476314 free inodes.

server1 `/var/tmp`: 318699450368 available bytes; 82.22% used; 112476314 free inodes.

server1 `/mnt/raid5`: 368480100352 available bytes; 98.31% used; 337539459 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22888747008 available bytes; 98.72% used; 110405686 free inodes.

server2 `/home`: 22888747008 available bytes; 98.72% used; 110405686 free inodes.

server2 `/tmp`: 22888747008 available bytes; 98.72% used; 110405686 free inodes.

server2 `/var/tmp`: 22888747008 available bytes; 98.72% used; 110405686 free inodes.

server2 `/mnt/raid5`: 302125187072 available bytes; 97.91% used; 445055765 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84365692928 available bytes; 95.29% used; 114152630 free inodes.

server3 `/home`: 84365692928 available bytes; 95.29% used; 114152630 free inodes.

server3 `/data`: 125909143552 available bytes; 98.26% used; 225807325 free inodes.

server3 `/tmp`: 84365692928 available bytes; 95.29% used; 114152630 free inodes.

server3 `/var/tmp`: 84365692928 available bytes; 95.29% used; 114152630 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105389641728 available bytes; 94.12% used; 114347333 free inodes.

server4 `/home`: 105389641728 available bytes; 94.12% used; 114347333 free inodes.

server4 `/data`: 218507337728 available bytes; 96.98% used; 224920838 free inodes.

server4 `/tmp`: 105389641728 available bytes; 94.12% used; 114347333 free inodes.

server4 `/var/tmp`: 105389641728 available bytes; 94.12% used; 114347333 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
