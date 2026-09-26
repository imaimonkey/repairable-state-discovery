# V2R cluster inventory

2026-09-26T11:07:46.614192+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318212997120 available bytes; 82.25% used; 112474827 free inodes.

server1 `/home`: 318212997120 available bytes; 82.25% used; 112474827 free inodes.

server1 `/tmp`: 318212997120 available bytes; 82.25% used; 112474827 free inodes.

server1 `/var/tmp`: 318212997120 available bytes; 82.25% used; 112474827 free inodes.

server1 `/mnt/raid5`: 218748395520 available bytes; 99.00% used; 337538188 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19848396800 available bytes; 98.89% used; 110384881 free inodes.

server2 `/home`: 19848396800 available bytes; 98.89% used; 110384881 free inodes.

server2 `/tmp`: 19848396800 available bytes; 98.89% used; 110384881 free inodes.

server2 `/var/tmp`: 19848396800 available bytes; 98.89% used; 110384881 free inodes.

server2 `/mnt/raid5`: 242095927296 available bytes; 98.33% used; 444978813 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82650021888 available bytes; 95.39% used; 114110815 free inodes.

server3 `/home`: 82650021888 available bytes; 95.39% used; 114110815 free inodes.

server3 `/data`: 123564236800 available bytes; 98.29% used; 225825875 free inodes.

server3 `/tmp`: 82650021888 available bytes; 95.39% used; 114110815 free inodes.

server3 `/var/tmp`: 82650021888 available bytes; 95.39% used; 114110815 free inodes.
| server4 | True | ['3', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105926410240 available bytes; 94.09% used; 114347959 free inodes.

server4 `/home`: 105926410240 available bytes; 94.09% used; 114347959 free inodes.

server4 `/data`: 88884662272 available bytes; 98.77% used; 224880522 free inodes.

server4 `/tmp`: 105926410240 available bytes; 94.09% used; 114347959 free inodes.

server4 `/var/tmp`: 105926410240 available bytes; 94.09% used; 114347959 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
