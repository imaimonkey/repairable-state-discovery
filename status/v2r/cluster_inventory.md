# V2R cluster inventory

2026-09-26T21:15:42.953984+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315482435584 available bytes; 82.40% used; 112445685 free inodes.

server1 `/home`: 315482435584 available bytes; 82.40% used; 112445685 free inodes.

server1 `/tmp`: 315482435584 available bytes; 82.40% used; 112445685 free inodes.

server1 `/var/tmp`: 315482435584 available bytes; 82.40% used; 112445685 free inodes.

server1 `/mnt/raid5`: 645854949376 available bytes; 97.04% used; 337467121 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 17931481088 available bytes; 99.00% used; 110367523 free inodes.

server2 `/home`: 17931481088 available bytes; 99.00% used; 110367523 free inodes.

server2 `/tmp`: 17931481088 available bytes; 99.00% used; 110367523 free inodes.

server2 `/var/tmp`: 17931481088 available bytes; 99.00% used; 110367523 free inodes.

server2 `/mnt/raid5`: 599107670016 available bytes; 95.86% used; 444963144 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 80704073728 available bytes; 95.50% used; 114043684 free inodes.

server3 `/home`: 80704073728 available bytes; 95.50% used; 114043684 free inodes.

server3 `/data`: 1351107653632 available bytes; 81.33% used; 225830897 free inodes.

server3 `/tmp`: 80704073728 available bytes; 95.50% used; 114043684 free inodes.

server3 `/var/tmp`: 80704073728 available bytes; 95.50% used; 114043684 free inodes.
| server4 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105909481472 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105909481472 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 409913425920 available bytes; 94.33% used; 224823845 free inodes.

server4 `/tmp`: 105909481472 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105909481472 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
