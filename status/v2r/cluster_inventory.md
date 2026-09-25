# V2R cluster inventory

2026-09-25T16:24:08.677446+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318673473536 available bytes; 82.22% used; 112476330 free inodes.

server1 `/home`: 318673473536 available bytes; 82.22% used; 112476330 free inodes.

server1 `/tmp`: 318673473536 available bytes; 82.22% used; 112476330 free inodes.

server1 `/var/tmp`: 318673473536 available bytes; 82.22% used; 112476330 free inodes.

server1 `/mnt/raid5`: 363881639936 available bytes; 98.33% used; 337544765 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23106932736 available bytes; 98.71% used; 110407932 free inodes.

server2 `/home`: 23106932736 available bytes; 98.71% used; 110407932 free inodes.

server2 `/tmp`: 23106932736 available bytes; 98.71% used; 110407932 free inodes.

server2 `/var/tmp`: 23106932736 available bytes; 98.71% used; 110407932 free inodes.

server2 `/mnt/raid5`: 318255108096 available bytes; 97.80% used; 445070400 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84401614848 available bytes; 95.29% used; 114152668 free inodes.

server3 `/home`: 84401614848 available bytes; 95.29% used; 114152668 free inodes.

server3 `/data`: 134858915840 available bytes; 98.14% used; 225805976 free inodes.

server3 `/tmp`: 84401614848 available bytes; 95.29% used; 114152668 free inodes.

server3 `/var/tmp`: 84401614848 available bytes; 95.29% used; 114152668 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105636323328 available bytes; 94.11% used; 114349650 free inodes.

server4 `/home`: 105636323328 available bytes; 94.11% used; 114349650 free inodes.

server4 `/data`: 230221611008 available bytes; 96.82% used; 224934307 free inodes.

server4 `/tmp`: 105636323328 available bytes; 94.11% used; 114349650 free inodes.

server4 `/var/tmp`: 105636323328 available bytes; 94.11% used; 114349650 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
