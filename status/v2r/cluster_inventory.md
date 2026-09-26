# V2R cluster inventory

2026-09-26T17:30:35.158201+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315596484608 available bytes; 82.39% used; 112445882 free inodes.

server1 `/home`: 315596484608 available bytes; 82.39% used; 112445882 free inodes.

server1 `/tmp`: 315596484608 available bytes; 82.39% used; 112445882 free inodes.

server1 `/var/tmp`: 315596484608 available bytes; 82.39% used; 112445882 free inodes.

server1 `/mnt/raid5`: 645852082176 available bytes; 97.04% used; 337467116 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 18030845952 available bytes; 98.99% used; 110367628 free inodes.

server2 `/home`: 18030845952 available bytes; 98.99% used; 110367628 free inodes.

server2 `/tmp`: 18030845952 available bytes; 98.99% used; 110367628 free inodes.

server2 `/var/tmp`: 18030845952 available bytes; 98.99% used; 110367628 free inodes.

server2 `/mnt/raid5`: 606054506496 available bytes; 95.81% used; 444969487 free inodes.
| server3 | True | [] | [] |

server3 `/`: 81275695104 available bytes; 95.46% used; 114065401 free inodes.

server3 `/home`: 81275695104 available bytes; 95.46% used; 114065401 free inodes.

server3 `/data`: 1349213179904 available bytes; 81.35% used; 225836143 free inodes.

server3 `/tmp`: 81275695104 available bytes; 95.46% used; 114065401 free inodes.

server3 `/var/tmp`: 81275695104 available bytes; 95.46% used; 114065401 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105952092160 available bytes; 94.09% used; 114347878 free inodes.

server4 `/home`: 105952092160 available bytes; 94.09% used; 114347878 free inodes.

server4 `/data`: 410448351232 available bytes; 94.33% used; 224824484 free inodes.

server4 `/tmp`: 105952092160 available bytes; 94.09% used; 114347878 free inodes.

server4 `/var/tmp`: 105952092160 available bytes; 94.09% used; 114347878 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
