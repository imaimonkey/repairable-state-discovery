# V2R cluster inventory

2026-09-27T08:47:12.177283+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314469466112 available bytes; 82.46% used; 112440731 free inodes.

server1 `/home`: 314469466112 available bytes; 82.46% used; 112440731 free inodes.

server1 `/tmp`: 314469466112 available bytes; 82.46% used; 112440731 free inodes.

server1 `/var/tmp`: 314469466112 available bytes; 82.46% used; 112440731 free inodes.

server1 `/mnt/raid5`: 634583326720 available bytes; 97.09% used; 337400007 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 17602744320 available bytes; 99.02% used; 110364836 free inodes.

server2 `/home`: 17602744320 available bytes; 99.02% used; 110364836 free inodes.

server2 `/tmp`: 17602744320 available bytes; 99.02% used; 110364836 free inodes.

server2 `/var/tmp`: 17602744320 available bytes; 99.02% used; 110364836 free inodes.

server2 `/mnt/raid5`: 575051132928 available bytes; 96.03% used; 444750138 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78572044288 available bytes; 95.62% used; 114062864 free inodes.

server3 `/home`: 78572044288 available bytes; 95.62% used; 114062864 free inodes.

server3 `/data`: 1332593938432 available bytes; 81.58% used; 225763103 free inodes.

server3 `/tmp`: 78572044288 available bytes; 95.62% used; 114062864 free inodes.

server3 `/var/tmp`: 78572044288 available bytes; 95.62% used; 114062864 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111051698176 available bytes; 93.80% used; 114372880 free inodes.

server4 `/home`: 111051698176 available bytes; 93.80% used; 114372880 free inodes.

server4 `/data`: 366145249280 available bytes; 94.94% used; 224769526 free inodes.

server4 `/tmp`: 111051698176 available bytes; 93.80% used; 114372880 free inodes.

server4 `/var/tmp`: 111051698176 available bytes; 93.80% used; 114372880 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
