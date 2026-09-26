# V2R cluster inventory

2026-09-26T11:21:30.494949+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318208819200 available bytes; 82.25% used; 112474810 free inodes.

server1 `/home`: 318208819200 available bytes; 82.25% used; 112474810 free inodes.

server1 `/tmp`: 318208819200 available bytes; 82.25% used; 112474810 free inodes.

server1 `/var/tmp`: 318208819200 available bytes; 82.25% used; 112474810 free inodes.

server1 `/mnt/raid5`: 218713030656 available bytes; 99.00% used; 337538112 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19843981312 available bytes; 98.89% used; 110384885 free inodes.

server2 `/home`: 19843981312 available bytes; 98.89% used; 110384885 free inodes.

server2 `/tmp`: 19843981312 available bytes; 98.89% used; 110384885 free inodes.

server2 `/var/tmp`: 19843981312 available bytes; 98.89% used; 110384885 free inodes.

server2 `/mnt/raid5`: 241694900224 available bytes; 98.33% used; 444978545 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82649550848 available bytes; 95.39% used; 114110817 free inodes.

server3 `/home`: 82649550848 available bytes; 95.39% used; 114110817 free inodes.

server3 `/data`: 123502297088 available bytes; 98.29% used; 225825657 free inodes.

server3 `/tmp`: 82649550848 available bytes; 95.39% used; 114110817 free inodes.

server3 `/var/tmp`: 82649550848 available bytes; 95.39% used; 114110817 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105909805056 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105909805056 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 88791277568 available bytes; 98.77% used; 224880332 free inodes.

server4 `/tmp`: 105909805056 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105909805056 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
