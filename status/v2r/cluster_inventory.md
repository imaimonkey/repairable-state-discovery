# V2R cluster inventory

2026-09-26T11:03:12.006659+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318213120000 available bytes; 82.25% used; 112474830 free inodes.

server1 `/home`: 318213120000 available bytes; 82.25% used; 112474830 free inodes.

server1 `/tmp`: 318213120000 available bytes; 82.25% used; 112474830 free inodes.

server1 `/var/tmp`: 318213120000 available bytes; 82.25% used; 112474830 free inodes.

server1 `/mnt/raid5`: 218756210688 available bytes; 99.00% used; 337538203 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19849367552 available bytes; 98.89% used; 110384895 free inodes.

server2 `/home`: 19849367552 available bytes; 98.89% used; 110384895 free inodes.

server2 `/tmp`: 19849367552 available bytes; 98.89% used; 110384895 free inodes.

server2 `/var/tmp`: 19849367552 available bytes; 98.89% used; 110384895 free inodes.

server2 `/mnt/raid5`: 242231611392 available bytes; 98.33% used; 444979107 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82661679104 available bytes; 95.39% used; 114110823 free inodes.

server3 `/home`: 82661679104 available bytes; 95.39% used; 114110823 free inodes.

server3 `/data`: 123565678592 available bytes; 98.29% used; 225825967 free inodes.

server3 `/tmp`: 82661679104 available bytes; 95.39% used; 114110823 free inodes.

server3 `/var/tmp`: 82661679104 available bytes; 95.39% used; 114110823 free inodes.
| server4 | True | ['3', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105926549504 available bytes; 94.09% used; 114347960 free inodes.

server4 `/home`: 105926549504 available bytes; 94.09% used; 114347960 free inodes.

server4 `/data`: 88887107584 available bytes; 98.77% used; 224880533 free inodes.

server4 `/tmp`: 105926549504 available bytes; 94.09% used; 114347960 free inodes.

server4 `/var/tmp`: 105926549504 available bytes; 94.09% used; 114347960 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
