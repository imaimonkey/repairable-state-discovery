# V2R cluster inventory

2026-09-25T20:47:09.745227+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318709026816 available bytes; 82.22% used; 112476326 free inodes.

server1 `/home`: 318709026816 available bytes; 82.22% used; 112476326 free inodes.

server1 `/tmp`: 318709026816 available bytes; 82.22% used; 112476326 free inodes.

server1 `/var/tmp`: 318709026816 available bytes; 82.22% used; 112476326 free inodes.

server1 `/mnt/raid5`: 368642621440 available bytes; 98.31% used; 337539571 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] |

server2 `/`: 22945824768 available bytes; 98.72% used; 110406238 free inodes.

server2 `/home`: 22945824768 available bytes; 98.72% used; 110406238 free inodes.

server2 `/tmp`: 22945824768 available bytes; 98.72% used; 110406238 free inodes.

server2 `/var/tmp`: 22945824768 available bytes; 98.72% used; 110406238 free inodes.

server2 `/mnt/raid5`: 302797488128 available bytes; 97.91% used; 445056831 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84372422656 available bytes; 95.29% used; 114152620 free inodes.

server3 `/home`: 84372422656 available bytes; 95.29% used; 114152620 free inodes.

server3 `/data`: 127103893504 available bytes; 98.24% used; 225807747 free inodes.

server3 `/tmp`: 84372422656 available bytes; 95.29% used; 114152620 free inodes.

server3 `/var/tmp`: 84372422656 available bytes; 95.29% used; 114152620 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105655603200 available bytes; 94.10% used; 114349549 free inodes.

server4 `/home`: 105655603200 available bytes; 94.10% used; 114349549 free inodes.

server4 `/data`: 228181307392 available bytes; 96.85% used; 224928296 free inodes.

server4 `/tmp`: 105655603200 available bytes; 94.10% used; 114349549 free inodes.

server4 `/var/tmp`: 105655603200 available bytes; 94.10% used; 114349549 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
