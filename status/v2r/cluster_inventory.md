# V2R cluster inventory

2026-09-26T07:19:54.611600+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318768103424 available bytes; 82.22% used; 112476289 free inodes.

server1 `/home`: 318768103424 available bytes; 82.22% used; 112476289 free inodes.

server1 `/tmp`: 318768103424 available bytes; 82.22% used; 112476289 free inodes.

server1 `/var/tmp`: 318768103424 available bytes; 82.22% used; 112476289 free inodes.

server1 `/mnt/raid5`: 219262369792 available bytes; 98.99% used; 337539295 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22320226304 available bytes; 98.75% used; 110403882 free inodes.

server2 `/home`: 22320226304 available bytes; 98.75% used; 110403882 free inodes.

server2 `/tmp`: 22320226304 available bytes; 98.75% used; 110403882 free inodes.

server2 `/var/tmp`: 22320226304 available bytes; 98.75% used; 110403882 free inodes.

server2 `/mnt/raid5`: 271011733504 available bytes; 98.13% used; 445027308 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82679767040 available bytes; 95.39% used; 114110895 free inodes.

server3 `/home`: 82679767040 available bytes; 95.39% used; 114110895 free inodes.

server3 `/data`: 123980984320 available bytes; 98.29% used; 225821253 free inodes.

server3 `/tmp`: 82679767040 available bytes; 95.39% used; 114110895 free inodes.

server3 `/var/tmp`: 82679767040 available bytes; 95.39% used; 114110895 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106074763264 available bytes; 94.08% used; 114348174 free inodes.

server4 `/home`: 106074763264 available bytes; 94.08% used; 114348174 free inodes.

server4 `/data`: 105869844480 available bytes; 98.54% used; 224922733 free inodes.

server4 `/tmp`: 106074763264 available bytes; 94.08% used; 114348174 free inodes.

server4 `/var/tmp`: 106074763264 available bytes; 94.08% used; 114348174 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
