# V2R cluster inventory

2026-09-25T16:27:13.134999+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318682202112 available bytes; 82.22% used; 112476344 free inodes.

server1 `/home`: 318682202112 available bytes; 82.22% used; 112476344 free inodes.

server1 `/tmp`: 318682202112 available bytes; 82.22% used; 112476344 free inodes.

server1 `/var/tmp`: 318682202112 available bytes; 82.22% used; 112476344 free inodes.

server1 `/mnt/raid5`: 371129782272 available bytes; 98.30% used; 337544775 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23106371584 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23106371584 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23106371584 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23106371584 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 317909528576 available bytes; 97.80% used; 445070246 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84400914432 available bytes; 95.29% used; 114152674 free inodes.

server3 `/home`: 84400914432 available bytes; 95.29% used; 114152674 free inodes.

server3 `/data`: 134856130560 available bytes; 98.14% used; 225805896 free inodes.

server3 `/tmp`: 84400914432 available bytes; 95.29% used; 114152674 free inodes.

server3 `/var/tmp`: 84400914432 available bytes; 95.29% used; 114152674 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105636212736 available bytes; 94.11% used; 114349646 free inodes.

server4 `/home`: 105636212736 available bytes; 94.11% used; 114349646 free inodes.

server4 `/data`: 230125109248 available bytes; 96.82% used; 224934183 free inodes.

server4 `/tmp`: 105636212736 available bytes; 94.11% used; 114349646 free inodes.

server4 `/var/tmp`: 105636212736 available bytes; 94.11% used; 114349646 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
