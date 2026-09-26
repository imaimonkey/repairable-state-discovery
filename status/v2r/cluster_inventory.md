# V2R cluster inventory

2026-09-26T16:06:43.717570+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318129106944 available bytes; 82.25% used; 112473906 free inodes.

server1 `/home`: 318129106944 available bytes; 82.25% used; 112473906 free inodes.

server1 `/tmp`: 318129106944 available bytes; 82.25% used; 112473906 free inodes.

server1 `/var/tmp`: 318129106944 available bytes; 82.25% used; 112473906 free inodes.

server1 `/mnt/raid5`: 654094954496 available bytes; 97.00% used; 337531406 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18027012096 available bytes; 98.99% used; 110367514 free inodes.

server2 `/home`: 18027012096 available bytes; 98.99% used; 110367514 free inodes.

server2 `/tmp`: 18027012096 available bytes; 98.99% used; 110367514 free inodes.

server2 `/var/tmp`: 18027012096 available bytes; 98.99% used; 110367514 free inodes.

server2 `/mnt/raid5`: 607833481216 available bytes; 95.80% used; 444971770 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81582780416 available bytes; 95.45% used; 114077144 free inodes.

server3 `/home`: 81582780416 available bytes; 95.45% used; 114077144 free inodes.

server3 `/data`: 1349392543744 available bytes; 81.35% used; 225831030 free inodes.

server3 `/tmp`: 81582780416 available bytes; 95.45% used; 114077144 free inodes.

server3 `/var/tmp`: 81582780416 available bytes; 95.45% used; 114077144 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105953878016 available bytes; 94.09% used; 114347851 free inodes.

server4 `/home`: 105953878016 available bytes; 94.09% used; 114347851 free inodes.

server4 `/data`: 410716987392 available bytes; 94.32% used; 224825369 free inodes.

server4 `/tmp`: 105953878016 available bytes; 94.09% used; 114347851 free inodes.

server4 `/var/tmp`: 105953878016 available bytes; 94.09% used; 114347851 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
