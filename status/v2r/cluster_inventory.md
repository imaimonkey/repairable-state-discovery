# V2R cluster inventory

2026-09-25T16:22:36.938257+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318671945728 available bytes; 82.22% used; 112476331 free inodes.

server1 `/home`: 318671945728 available bytes; 82.22% used; 112476331 free inodes.

server1 `/tmp`: 318671945728 available bytes; 82.22% used; 112476331 free inodes.

server1 `/var/tmp`: 318671945728 available bytes; 82.22% used; 112476331 free inodes.

server1 `/mnt/raid5`: 363886821376 available bytes; 98.33% used; 337544806 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23107653632 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23107653632 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23107653632 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23107653632 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 318040076288 available bytes; 97.80% used; 445070587 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84402036736 available bytes; 95.29% used; 114152668 free inodes.

server3 `/home`: 84402036736 available bytes; 95.29% used; 114152668 free inodes.

server3 `/data`: 134861414400 available bytes; 98.14% used; 225806015 free inodes.

server3 `/tmp`: 84402036736 available bytes; 95.29% used; 114152668 free inodes.

server3 `/var/tmp`: 84402036736 available bytes; 95.29% used; 114152668 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105636339712 available bytes; 94.11% used; 114349650 free inodes.

server4 `/home`: 105636339712 available bytes; 94.11% used; 114349650 free inodes.

server4 `/data`: 230228942848 available bytes; 96.82% used; 224934333 free inodes.

server4 `/tmp`: 105636339712 available bytes; 94.11% used; 114349650 free inodes.

server4 `/var/tmp`: 105636339712 available bytes; 94.11% used; 114349650 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
