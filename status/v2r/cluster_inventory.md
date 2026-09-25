# V2R cluster inventory

2026-09-25T20:56:20.268952+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318698758144 available bytes; 82.22% used; 112476323 free inodes.

server1 `/home`: 318698758144 available bytes; 82.22% used; 112476323 free inodes.

server1 `/tmp`: 318698758144 available bytes; 82.22% used; 112476323 free inodes.

server1 `/var/tmp`: 318698758144 available bytes; 82.22% used; 112476323 free inodes.

server1 `/mnt/raid5`: 368625188864 available bytes; 98.31% used; 337539547 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] |

server2 `/`: 22894448640 available bytes; 98.72% used; 110405678 free inodes.

server2 `/home`: 22894448640 available bytes; 98.72% used; 110405678 free inodes.

server2 `/tmp`: 22894448640 available bytes; 98.72% used; 110405678 free inodes.

server2 `/var/tmp`: 22894448640 available bytes; 98.72% used; 110405678 free inodes.

server2 `/mnt/raid5`: 302532059136 available bytes; 97.91% used; 445056329 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84362354688 available bytes; 95.29% used; 114152622 free inodes.

server3 `/home`: 84362354688 available bytes; 95.29% used; 114152622 free inodes.

server3 `/data`: 127098814464 available bytes; 98.24% used; 225807614 free inodes.

server3 `/tmp`: 84362354688 available bytes; 95.29% used; 114152622 free inodes.

server3 `/var/tmp`: 84362354688 available bytes; 95.29% used; 114152622 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105655246848 available bytes; 94.10% used; 114349534 free inodes.

server4 `/home`: 105655246848 available bytes; 94.10% used; 114349534 free inodes.

server4 `/data`: 227910311936 available bytes; 96.85% used; 224926672 free inodes.

server4 `/tmp`: 105655246848 available bytes; 94.10% used; 114349534 free inodes.

server4 `/var/tmp`: 105655246848 available bytes; 94.10% used; 114349534 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
