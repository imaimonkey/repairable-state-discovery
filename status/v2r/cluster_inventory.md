# V2R cluster inventory

2026-09-25T02:41:10.685786+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318958850048 available bytes; 82.21% used; 112480424 free inodes.

server1 `/home`: 318958850048 available bytes; 82.21% used; 112480424 free inodes.

server1 `/tmp`: 318958850048 available bytes; 82.21% used; 112480424 free inodes.

server1 `/var/tmp`: 318958850048 available bytes; 82.21% used; 112480424 free inodes.

server1 `/mnt/raid5`: 416193814528 available bytes; 98.09% used; 337604651 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23007154176 available bytes; 98.72% used; 110410439 free inodes.

server2 `/home`: 23007154176 available bytes; 98.72% used; 110410439 free inodes.

server2 `/tmp`: 23007154176 available bytes; 98.72% used; 110410439 free inodes.

server2 `/var/tmp`: 23007154176 available bytes; 98.72% used; 110410439 free inodes.

server2 `/mnt/raid5`: 482770579456 available bytes; 96.66% used; 445113384 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84350644224 available bytes; 95.29% used; 114156073 free inodes.

server3 `/home`: 84350644224 available bytes; 95.29% used; 114156073 free inodes.

server3 `/data`: 145414455296 available bytes; 97.99% used; 225811039 free inodes.

server3 `/tmp`: 84350644224 available bytes; 95.29% used; 114156073 free inodes.

server3 `/var/tmp`: 84350644224 available bytes; 95.29% used; 114156073 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105895546880 available bytes; 94.09% used; 114351001 free inodes.

server4 `/home`: 105895546880 available bytes; 94.09% used; 114351001 free inodes.

server4 `/data`: 0 available bytes; 100.00% used; 224968801 free inodes.

server4 `/tmp`: 105895546880 available bytes; 94.09% used; 114351001 free inodes.

server4 `/var/tmp`: 105895546880 available bytes; 94.09% used; 114351001 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
