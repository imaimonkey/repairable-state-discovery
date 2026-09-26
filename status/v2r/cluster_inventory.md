# V2R cluster inventory

2026-09-26T06:32:32.846966+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318770028544 available bytes; 82.22% used; 112476274 free inodes.

server1 `/home`: 318770028544 available bytes; 82.22% used; 112476274 free inodes.

server1 `/tmp`: 318770028544 available bytes; 82.22% used; 112476274 free inodes.

server1 `/var/tmp`: 318770028544 available bytes; 82.22% used; 112476274 free inodes.

server1 `/mnt/raid5`: 219673956352 available bytes; 98.99% used; 337539781 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22314672128 available bytes; 98.76% used; 110403832 free inodes.

server2 `/home`: 22314672128 available bytes; 98.76% used; 110403832 free inodes.

server2 `/tmp`: 22314672128 available bytes; 98.76% used; 110403832 free inodes.

server2 `/var/tmp`: 22314672128 available bytes; 98.76% used; 110403832 free inodes.

server2 `/mnt/raid5`: 272938590208 available bytes; 98.11% used; 445028405 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82565001216 available bytes; 95.39% used; 114110885 free inodes.

server3 `/home`: 82565001216 available bytes; 95.39% used; 114110885 free inodes.

server3 `/data`: 123993976832 available bytes; 98.29% used; 225822255 free inodes.

server3 `/tmp`: 82565001216 available bytes; 95.39% used; 114110885 free inodes.

server3 `/var/tmp`: 82565001216 available bytes; 95.39% used; 114110885 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105905696768 available bytes; 94.09% used; 114346888 free inodes.

server4 `/home`: 105905696768 available bytes; 94.09% used; 114346888 free inodes.

server4 `/data`: 106557820928 available bytes; 98.53% used; 224923430 free inodes.

server4 `/tmp`: 105905696768 available bytes; 94.09% used; 114346888 free inodes.

server4 `/var/tmp`: 105905696768 available bytes; 94.09% used; 114346888 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
