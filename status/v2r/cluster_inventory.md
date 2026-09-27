# V2R cluster inventory

2026-09-27T08:45:40.721989+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314469683200 available bytes; 82.46% used; 112440731 free inodes.

server1 `/home`: 314469683200 available bytes; 82.46% used; 112440731 free inodes.

server1 `/tmp`: 314469683200 available bytes; 82.46% used; 112440731 free inodes.

server1 `/var/tmp`: 314469683200 available bytes; 82.46% used; 112440731 free inodes.

server1 `/mnt/raid5`: 634582831104 available bytes; 97.09% used; 337400005 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 17602928640 available bytes; 99.02% used; 110364836 free inodes.

server2 `/home`: 17602928640 available bytes; 99.02% used; 110364836 free inodes.

server2 `/tmp`: 17602928640 available bytes; 99.02% used; 110364836 free inodes.

server2 `/var/tmp`: 17602928640 available bytes; 99.02% used; 110364836 free inodes.

server2 `/mnt/raid5`: 575640625152 available bytes; 96.02% used; 444750337 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78572191744 available bytes; 95.62% used; 114062869 free inodes.

server3 `/home`: 78572191744 available bytes; 95.62% used; 114062869 free inodes.

server3 `/data`: 1332614537216 available bytes; 81.58% used; 225763122 free inodes.

server3 `/tmp`: 78572191744 available bytes; 95.62% used; 114062869 free inodes.

server3 `/var/tmp`: 78572191744 available bytes; 95.62% used; 114062869 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111051743232 available bytes; 93.80% used; 114372882 free inodes.

server4 `/home`: 111051743232 available bytes; 93.80% used; 114372882 free inodes.

server4 `/data`: 366203645952 available bytes; 94.94% used; 224769719 free inodes.

server4 `/tmp`: 111051743232 available bytes; 93.80% used; 114372882 free inodes.

server4 `/var/tmp`: 111051743232 available bytes; 93.80% used; 114372882 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
