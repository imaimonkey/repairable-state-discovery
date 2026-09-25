# V2R cluster inventory

2026-09-25T19:27:39.759554+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318735654912 available bytes; 82.22% used; 112476332 free inodes.

server1 `/home`: 318735654912 available bytes; 82.22% used; 112476332 free inodes.

server1 `/tmp`: 318735654912 available bytes; 82.22% used; 112476332 free inodes.

server1 `/var/tmp`: 318735654912 available bytes; 82.22% used; 112476332 free inodes.

server1 `/mnt/raid5`: 370866995200 available bytes; 98.30% used; 337540809 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23096041472 available bytes; 98.71% used; 110407936 free inodes.

server2 `/home`: 23096041472 available bytes; 98.71% used; 110407936 free inodes.

server2 `/tmp`: 23096041472 available bytes; 98.71% used; 110407936 free inodes.

server2 `/var/tmp`: 23096041472 available bytes; 98.71% used; 110407936 free inodes.

server2 `/mnt/raid5`: 312149995520 available bytes; 97.84% used; 445064627 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84382453760 available bytes; 95.29% used; 114152621 free inodes.

server3 `/home`: 84382453760 available bytes; 95.29% used; 114152621 free inodes.

server3 `/data`: 129277878272 available bytes; 98.21% used; 225808628 free inodes.

server3 `/tmp`: 84382453760 available bytes; 95.29% used; 114152621 free inodes.

server3 `/var/tmp`: 84382453760 available bytes; 95.29% used; 114152621 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105674874880 available bytes; 94.10% used; 114349584 free inodes.

server4 `/home`: 105674874880 available bytes; 94.10% used; 114349584 free inodes.

server4 `/data`: 229618450432 available bytes; 96.83% used; 224930016 free inodes.

server4 `/tmp`: 105674874880 available bytes; 94.10% used; 114349584 free inodes.

server4 `/var/tmp`: 105674874880 available bytes; 94.10% used; 114349584 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
