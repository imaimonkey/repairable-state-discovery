# V2R cluster inventory

2026-09-26T15:39:16.802587+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318147530752 available bytes; 82.25% used; 112473949 free inodes.

server1 `/home`: 318147530752 available bytes; 82.25% used; 112473949 free inodes.

server1 `/tmp`: 318147530752 available bytes; 82.25% used; 112473949 free inodes.

server1 `/var/tmp`: 318147530752 available bytes; 82.25% used; 112473949 free inodes.

server1 `/mnt/raid5`: 654093074432 available bytes; 97.00% used; 337531405 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18024636416 available bytes; 98.99% used; 110367502 free inodes.

server2 `/home`: 18024636416 available bytes; 98.99% used; 110367502 free inodes.

server2 `/tmp`: 18024636416 available bytes; 98.99% used; 110367502 free inodes.

server2 `/var/tmp`: 18024636416 available bytes; 98.99% used; 110367502 free inodes.

server2 `/mnt/raid5`: 609148538880 available bytes; 95.79% used; 444972529 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82152816640 available bytes; 95.42% used; 114093400 free inodes.

server3 `/home`: 82152816640 available bytes; 95.42% used; 114093400 free inodes.

server3 `/data`: 1347153514496 available bytes; 81.38% used; 225809185 free inodes.

server3 `/tmp`: 82152816640 available bytes; 95.42% used; 114093400 free inodes.

server3 `/var/tmp`: 82152816640 available bytes; 95.42% used; 114093400 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105954607104 available bytes; 94.09% used; 114347852 free inodes.

server4 `/home`: 105954607104 available bytes; 94.09% used; 114347852 free inodes.

server4 `/data`: 410725232640 available bytes; 94.32% used; 224825358 free inodes.

server4 `/tmp`: 105954607104 available bytes; 94.09% used; 114347852 free inodes.

server4 `/var/tmp`: 105954607104 available bytes; 94.09% used; 114347852 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
