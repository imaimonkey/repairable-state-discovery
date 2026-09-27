# V2R cluster inventory

2026-09-27T08:35:01.088778+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314467278848 available bytes; 82.46% used; 112440729 free inodes.

server1 `/home`: 314467278848 available bytes; 82.46% used; 112440729 free inodes.

server1 `/tmp`: 314467278848 available bytes; 82.46% used; 112440729 free inodes.

server1 `/var/tmp`: 314467278848 available bytes; 82.46% used; 112440729 free inodes.

server1 `/mnt/raid5`: 634590244864 available bytes; 97.09% used; 337400003 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 17613815808 available bytes; 99.02% used; 110364880 free inodes.

server2 `/home`: 17613815808 available bytes; 99.02% used; 110364880 free inodes.

server2 `/tmp`: 17613815808 available bytes; 99.02% used; 110364880 free inodes.

server2 `/var/tmp`: 17613815808 available bytes; 99.02% used; 110364880 free inodes.

server2 `/mnt/raid5`: 575931691008 available bytes; 96.02% used; 444751422 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78572621824 available bytes; 95.62% used; 114062868 free inodes.

server3 `/home`: 78572621824 available bytes; 95.62% used; 114062868 free inodes.

server3 `/data`: 1332701450240 available bytes; 81.58% used; 225763305 free inodes.

server3 `/tmp`: 78572621824 available bytes; 95.62% used; 114062868 free inodes.

server3 `/var/tmp`: 78572621824 available bytes; 95.62% used; 114062868 free inodes.
| server4 | True | ['4'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111052038144 available bytes; 93.80% used; 114372882 free inodes.

server4 `/home`: 111052038144 available bytes; 93.80% used; 114372882 free inodes.

server4 `/data`: 367893061632 available bytes; 94.92% used; 224770664 free inodes.

server4 `/tmp`: 111052038144 available bytes; 93.80% used; 114372882 free inodes.

server4 `/var/tmp`: 111052038144 available bytes; 93.80% used; 114372882 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
