# V2R cluster inventory

2026-09-26T09:33:10.408432+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318628024320 available bytes; 82.22% used; 112475101 free inodes.

server1 `/home`: 318628024320 available bytes; 82.22% used; 112475101 free inodes.

server1 `/tmp`: 318628024320 available bytes; 82.22% used; 112475101 free inodes.

server1 `/var/tmp`: 318628024320 available bytes; 82.22% used; 112475101 free inodes.

server1 `/mnt/raid5`: 218958053376 available bytes; 99.00% used; 337538630 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22313906176 available bytes; 98.76% used; 110403908 free inodes.

server2 `/home`: 22313906176 available bytes; 98.76% used; 110403908 free inodes.

server2 `/tmp`: 22313906176 available bytes; 98.76% used; 110403908 free inodes.

server2 `/var/tmp`: 22313906176 available bytes; 98.76% used; 110403908 free inodes.

server2 `/mnt/raid5`: 254106669056 available bytes; 98.24% used; 445022945 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82660757504 available bytes; 95.39% used; 114110809 free inodes.

server3 `/home`: 82660757504 available bytes; 95.39% used; 114110809 free inodes.

server3 `/data`: 123655704576 available bytes; 98.29% used; 225827785 free inodes.

server3 `/tmp`: 82660757504 available bytes; 95.39% used; 114110809 free inodes.

server3 `/var/tmp`: 82660757504 available bytes; 95.39% used; 114110809 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105942773760 available bytes; 94.09% used; 114348052 free inodes.

server4 `/home`: 105942773760 available bytes; 94.09% used; 114348052 free inodes.

server4 `/data`: 89293385728 available bytes; 98.77% used; 224882745 free inodes.

server4 `/tmp`: 105942773760 available bytes; 94.09% used; 114348052 free inodes.

server4 `/var/tmp`: 105942773760 available bytes; 94.09% used; 114348052 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
