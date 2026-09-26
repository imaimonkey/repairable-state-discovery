# V2R cluster inventory

2026-09-26T15:33:10.801799+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318156689408 available bytes; 82.25% used; 112473900 free inodes.

server1 `/home`: 318156689408 available bytes; 82.25% used; 112473900 free inodes.

server1 `/tmp`: 318156689408 available bytes; 82.25% used; 112473900 free inodes.

server1 `/var/tmp`: 318156689408 available bytes; 82.25% used; 112473900 free inodes.

server1 `/mnt/raid5`: 654093864960 available bytes; 97.00% used; 337531434 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18026102784 available bytes; 98.99% used; 110367504 free inodes.

server2 `/home`: 18026102784 available bytes; 98.99% used; 110367504 free inodes.

server2 `/tmp`: 18026102784 available bytes; 98.99% used; 110367504 free inodes.

server2 `/var/tmp`: 18026102784 available bytes; 98.99% used; 110367504 free inodes.

server2 `/mnt/raid5`: 609326587904 available bytes; 95.79% used; 444972957 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82884333568 available bytes; 95.37% used; 114132242 free inodes.

server3 `/home`: 82884333568 available bytes; 95.37% used; 114132242 free inodes.

server3 `/data`: 1347176955904 available bytes; 81.38% used; 225809708 free inodes.

server3 `/tmp`: 82884333568 available bytes; 95.37% used; 114132242 free inodes.

server3 `/var/tmp`: 82884333568 available bytes; 95.37% used; 114132242 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105954672640 available bytes; 94.09% used; 114347840 free inodes.

server4 `/home`: 105954672640 available bytes; 94.09% used; 114347840 free inodes.

server4 `/data`: 410734964736 available bytes; 94.32% used; 224825849 free inodes.

server4 `/tmp`: 105954672640 available bytes; 94.09% used; 114347840 free inodes.

server4 `/var/tmp`: 105954672640 available bytes; 94.09% used; 114347840 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
