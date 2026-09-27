# V2R cluster inventory

2026-09-27T08:53:18.672979+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314468683776 available bytes; 82.46% used; 112440726 free inodes.

server1 `/home`: 314468683776 available bytes; 82.46% used; 112440726 free inodes.

server1 `/tmp`: 314468683776 available bytes; 82.46% used; 112440726 free inodes.

server1 `/var/tmp`: 314468683776 available bytes; 82.46% used; 112440726 free inodes.

server1 `/mnt/raid5`: 634580930560 available bytes; 97.09% used; 337400005 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 17576955904 available bytes; 99.02% used; 110364378 free inodes.

server2 `/home`: 17576955904 available bytes; 99.02% used; 110364378 free inodes.

server2 `/tmp`: 17576955904 available bytes; 99.02% used; 110364378 free inodes.

server2 `/var/tmp`: 17576955904 available bytes; 99.02% used; 110364378 free inodes.

server2 `/mnt/raid5`: 575698423808 available bytes; 96.02% used; 444749905 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78557151232 available bytes; 95.62% used; 114062861 free inodes.

server3 `/home`: 78557151232 available bytes; 95.62% used; 114062861 free inodes.

server3 `/data`: 1332586192896 available bytes; 81.58% used; 225763015 free inodes.

server3 `/tmp`: 78557151232 available bytes; 95.62% used; 114062861 free inodes.

server3 `/var/tmp`: 78557151232 available bytes; 95.62% used; 114062861 free inodes.
| server4 | True | ['4', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111051526144 available bytes; 93.80% used; 114372883 free inodes.

server4 `/home`: 111051526144 available bytes; 93.80% used; 114372883 free inodes.

server4 `/data`: 366091468800 available bytes; 94.94% used; 224769343 free inodes.

server4 `/tmp`: 111051526144 available bytes; 93.80% used; 114372883 free inodes.

server4 `/var/tmp`: 111051526144 available bytes; 93.80% used; 114372883 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
