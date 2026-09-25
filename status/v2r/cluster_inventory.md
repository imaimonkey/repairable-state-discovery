# V2R cluster inventory

2026-09-25T16:28:44.937584+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318681661440 available bytes; 82.22% used; 112476335 free inodes.

server1 `/home`: 318681661440 available bytes; 82.22% used; 112476335 free inodes.

server1 `/tmp`: 318681661440 available bytes; 82.22% used; 112476335 free inodes.

server1 `/var/tmp`: 318681661440 available bytes; 82.22% used; 112476335 free inodes.

server1 `/mnt/raid5`: 367096295424 available bytes; 98.32% used; 337544684 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23100071936 available bytes; 98.71% used; 110407934 free inodes.

server2 `/home`: 23100071936 available bytes; 98.71% used; 110407934 free inodes.

server2 `/tmp`: 23100071936 available bytes; 98.71% used; 110407934 free inodes.

server2 `/var/tmp`: 23100071936 available bytes; 98.71% used; 110407934 free inodes.

server2 `/mnt/raid5`: 317854699520 available bytes; 97.80% used; 445070125 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84404490240 available bytes; 95.29% used; 114152674 free inodes.

server3 `/home`: 84404490240 available bytes; 95.29% used; 114152674 free inodes.

server3 `/data`: 133810642944 available bytes; 98.15% used; 225805842 free inodes.

server3 `/tmp`: 84404490240 available bytes; 95.29% used; 114152674 free inodes.

server3 `/var/tmp`: 84404490240 available bytes; 95.29% used; 114152674 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105636167680 available bytes; 94.11% used; 114349645 free inodes.

server4 `/home`: 105636167680 available bytes; 94.11% used; 114349645 free inodes.

server4 `/data`: 230120816640 available bytes; 96.82% used; 224934148 free inodes.

server4 `/tmp`: 105636167680 available bytes; 94.11% used; 114349645 free inodes.

server4 `/var/tmp`: 105636167680 available bytes; 94.11% used; 114349645 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
