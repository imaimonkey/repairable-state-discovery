# V2R cluster inventory

2026-09-25T19:12:23.166615+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318732660736 available bytes; 82.22% used; 112476334 free inodes.

server1 `/home`: 318732660736 available bytes; 82.22% used; 112476334 free inodes.

server1 `/tmp`: 318732660736 available bytes; 82.22% used; 112476334 free inodes.

server1 `/var/tmp`: 318732660736 available bytes; 82.22% used; 112476334 free inodes.

server1 `/mnt/raid5`: 371000004608 available bytes; 98.30% used; 337540901 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23104045056 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23104045056 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23104045056 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23104045056 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 312575893504 available bytes; 97.84% used; 445064990 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84383166464 available bytes; 95.29% used; 114152623 free inodes.

server3 `/home`: 84383166464 available bytes; 95.29% used; 114152623 free inodes.

server3 `/data`: 129294192640 available bytes; 98.21% used; 225808884 free inodes.

server3 `/tmp`: 84383166464 available bytes; 95.29% used; 114152623 free inodes.

server3 `/var/tmp`: 84383166464 available bytes; 95.29% used; 114152623 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105675481088 available bytes; 94.10% used; 114349590 free inodes.

server4 `/home`: 105675481088 available bytes; 94.10% used; 114349590 free inodes.

server4 `/data`: 229641793536 available bytes; 96.83% used; 224930966 free inodes.

server4 `/tmp`: 105675481088 available bytes; 94.10% used; 114349590 free inodes.

server4 `/var/tmp`: 105675481088 available bytes; 94.10% used; 114349590 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
