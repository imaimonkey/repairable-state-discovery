# V2R cluster inventory

2026-09-25T16:21:05.214492+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318672248832 available bytes; 82.22% used; 112476327 free inodes.

server1 `/home`: 318672248832 available bytes; 82.22% used; 112476327 free inodes.

server1 `/tmp`: 318672248832 available bytes; 82.22% used; 112476327 free inodes.

server1 `/var/tmp`: 318672248832 available bytes; 82.22% used; 112476327 free inodes.

server1 `/mnt/raid5`: 363886051328 available bytes; 98.33% used; 337544835 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23108104192 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23108104192 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23108104192 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23108104192 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 318633385984 available bytes; 97.80% used; 445070779 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84402409472 available bytes; 95.29% used; 114152674 free inodes.

server3 `/home`: 84402409472 available bytes; 95.29% used; 114152674 free inodes.

server3 `/data`: 134864224256 available bytes; 98.14% used; 225806045 free inodes.

server3 `/tmp`: 84402409472 available bytes; 95.29% used; 114152674 free inodes.

server3 `/var/tmp`: 84402409472 available bytes; 95.29% used; 114152674 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105636384768 available bytes; 94.11% used; 114349650 free inodes.

server4 `/home`: 105636384768 available bytes; 94.11% used; 114349650 free inodes.

server4 `/data`: 230232268800 available bytes; 96.82% used; 224934357 free inodes.

server4 `/tmp`: 105636384768 available bytes; 94.11% used; 114349650 free inodes.

server4 `/var/tmp`: 105636384768 available bytes; 94.11% used; 114349650 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
