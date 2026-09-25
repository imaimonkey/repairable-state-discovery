# V2R cluster inventory

2026-09-25T20:36:27.910554+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318707904512 available bytes; 82.22% used; 112476325 free inodes.

server1 `/home`: 318707904512 available bytes; 82.22% used; 112476325 free inodes.

server1 `/tmp`: 318707904512 available bytes; 82.22% used; 112476325 free inodes.

server1 `/var/tmp`: 318707904512 available bytes; 82.22% used; 112476325 free inodes.

server1 `/mnt/raid5`: 369381240832 available bytes; 98.31% used; 337540449 free inodes.
| server2 | True | ['4', '5', '6'] | [] |

server2 `/`: 23046324224 available bytes; 98.71% used; 110407144 free inodes.

server2 `/home`: 23046324224 available bytes; 98.71% used; 110407144 free inodes.

server2 `/tmp`: 23046324224 available bytes; 98.71% used; 110407144 free inodes.

server2 `/var/tmp`: 23046324224 available bytes; 98.71% used; 110407144 free inodes.

server2 `/mnt/raid5`: 303108808704 available bytes; 97.91% used; 445057162 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84381241344 available bytes; 95.29% used; 114152624 free inodes.

server3 `/home`: 84381241344 available bytes; 95.29% used; 114152624 free inodes.

server3 `/data`: 127171006464 available bytes; 98.24% used; 225807920 free inodes.

server3 `/tmp`: 84381241344 available bytes; 95.29% used; 114152624 free inodes.

server3 `/var/tmp`: 84381241344 available bytes; 95.29% used; 114152624 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105655898112 available bytes; 94.10% used; 114349549 free inodes.

server4 `/home`: 105655898112 available bytes; 94.10% used; 114349549 free inodes.

server4 `/data`: 228332339200 available bytes; 96.84% used; 224928551 free inodes.

server4 `/tmp`: 105655898112 available bytes; 94.10% used; 114349549 free inodes.

server4 `/var/tmp`: 105655898112 available bytes; 94.10% used; 114349549 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
