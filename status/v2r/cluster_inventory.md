# V2R cluster inventory

2026-09-26T16:03:40.554558+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318138925056 available bytes; 82.25% used; 112473906 free inodes.

server1 `/home`: 318138925056 available bytes; 82.25% used; 112473906 free inodes.

server1 `/tmp`: 318138925056 available bytes; 82.25% used; 112473906 free inodes.

server1 `/var/tmp`: 318138925056 available bytes; 82.25% used; 112473906 free inodes.

server1 `/mnt/raid5`: 654094159872 available bytes; 97.00% used; 337531404 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18031120384 available bytes; 98.99% used; 110367516 free inodes.

server2 `/home`: 18031120384 available bytes; 98.99% used; 110367516 free inodes.

server2 `/tmp`: 18031120384 available bytes; 98.99% used; 110367516 free inodes.

server2 `/var/tmp`: 18031120384 available bytes; 98.99% used; 110367516 free inodes.

server2 `/mnt/raid5`: 608447217664 available bytes; 95.80% used; 444971835 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81714692096 available bytes; 95.44% used; 114090104 free inodes.

server3 `/home`: 81714692096 available bytes; 95.44% used; 114090104 free inodes.

server3 `/data`: 1349393051648 available bytes; 81.35% used; 225831087 free inodes.

server3 `/tmp`: 81714692096 available bytes; 95.44% used; 114090104 free inodes.

server3 `/var/tmp`: 81714692096 available bytes; 95.44% used; 114090104 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105954095104 available bytes; 94.09% used; 114347852 free inodes.

server4 `/home`: 105954095104 available bytes; 94.09% used; 114347852 free inodes.

server4 `/data`: 410718859264 available bytes; 94.32% used; 224825373 free inodes.

server4 `/tmp`: 105954095104 available bytes; 94.09% used; 114347852 free inodes.

server4 `/var/tmp`: 105954095104 available bytes; 94.09% used; 114347852 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
