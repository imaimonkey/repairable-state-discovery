# V2R cluster inventory

2026-09-25T17:34:30.577678+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318671269888 available bytes; 82.22% used; 112476352 free inodes.

server1 `/home`: 318671269888 available bytes; 82.22% used; 112476352 free inodes.

server1 `/tmp`: 318671269888 available bytes; 82.22% used; 112476352 free inodes.

server1 `/var/tmp`: 318671269888 available bytes; 82.22% used; 112476352 free inodes.

server1 `/mnt/raid5`: 365673574400 available bytes; 98.32% used; 337543032 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23104757760 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23104757760 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23104757760 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23104757760 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 315355123712 available bytes; 97.82% used; 445067991 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84392914944 available bytes; 95.29% used; 114152611 free inodes.

server3 `/home`: 84392914944 available bytes; 95.29% used; 114152611 free inodes.

server3 `/data`: 132776665088 available bytes; 98.16% used; 225811130 free inodes.

server3 `/tmp`: 84392914944 available bytes; 95.29% used; 114152611 free inodes.

server3 `/var/tmp`: 84392914944 available bytes; 95.29% used; 114152611 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105617555456 available bytes; 94.11% used; 114349642 free inodes.

server4 `/home`: 105617555456 available bytes; 94.11% used; 114349642 free inodes.

server4 `/data`: 229861920768 available bytes; 96.82% used; 224932801 free inodes.

server4 `/tmp`: 105617555456 available bytes; 94.11% used; 114349642 free inodes.

server4 `/var/tmp`: 105617555456 available bytes; 94.11% used; 114349642 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
