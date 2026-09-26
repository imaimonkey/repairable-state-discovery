# V2R cluster inventory

2026-09-26T21:29:25.138594+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315480469504 available bytes; 82.40% used; 112445687 free inodes.

server1 `/home`: 315480469504 available bytes; 82.40% used; 112445687 free inodes.

server1 `/tmp`: 315480469504 available bytes; 82.40% used; 112445687 free inodes.

server1 `/var/tmp`: 315480469504 available bytes; 82.40% used; 112445687 free inodes.

server1 `/mnt/raid5`: 645854797824 available bytes; 97.04% used; 337467239 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 17951412224 available bytes; 99.00% used; 110367529 free inodes.

server2 `/home`: 17951412224 available bytes; 99.00% used; 110367529 free inodes.

server2 `/tmp`: 17951412224 available bytes; 99.00% used; 110367529 free inodes.

server2 `/var/tmp`: 17951412224 available bytes; 99.00% used; 110367529 free inodes.

server2 `/mnt/raid5`: 598790025216 available bytes; 95.86% used; 444962762 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 81371246592 available bytes; 95.46% used; 114079981 free inodes.

server3 `/home`: 81371246592 available bytes; 95.46% used; 114079981 free inodes.

server3 `/data`: 1349671817216 available bytes; 81.35% used; 225828558 free inodes.

server3 `/tmp`: 81371246592 available bytes; 95.46% used; 114079981 free inodes.

server3 `/var/tmp`: 81371246592 available bytes; 95.46% used; 114079981 free inodes.
| server4 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105909137408 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105909137408 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 409900527616 available bytes; 94.34% used; 224823843 free inodes.

server4 `/tmp`: 105909137408 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105909137408 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
