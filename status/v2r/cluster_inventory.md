# V2R cluster inventory

2026-09-27T07:43:13.775762+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314470985728 available bytes; 82.46% used; 112440791 free inodes.

server1 `/home`: 314470985728 available bytes; 82.46% used; 112440791 free inodes.

server1 `/tmp`: 314470985728 available bytes; 82.46% used; 112440791 free inodes.

server1 `/var/tmp`: 314470985728 available bytes; 82.46% used; 112440791 free inodes.

server1 `/mnt/raid5`: 634657255424 available bytes; 97.09% used; 337400006 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 17610514432 available bytes; 99.02% used; 110365019 free inodes.

server2 `/home`: 17610514432 available bytes; 99.02% used; 110365019 free inodes.

server2 `/tmp`: 17610514432 available bytes; 99.02% used; 110365019 free inodes.

server2 `/var/tmp`: 17610514432 available bytes; 99.02% used; 110365019 free inodes.

server2 `/mnt/raid5`: 571003088896 available bytes; 96.05% used; 444873867 free inodes.
| server3 | True | ['3'] | [] | reference_compatible=True |

server3 `/`: 78572150784 available bytes; 95.62% used; 114062874 free inodes.

server3 `/home`: 78572150784 available bytes; 95.62% used; 114062874 free inodes.

server3 `/data`: 1333017997312 available bytes; 81.58% used; 225763949 free inodes.

server3 `/tmp`: 78572150784 available bytes; 95.62% used; 114062874 free inodes.

server3 `/var/tmp`: 78572150784 available bytes; 95.62% used; 114062874 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111070162944 available bytes; 93.80% used; 114372883 free inodes.

server4 `/home`: 111070162944 available bytes; 93.80% used; 114372883 free inodes.

server4 `/data`: 374299578368 available bytes; 94.83% used; 224770983 free inodes.

server4 `/tmp`: 111070162944 available bytes; 93.80% used; 114372883 free inodes.

server4 `/var/tmp`: 111070162944 available bytes; 93.80% used; 114372883 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
