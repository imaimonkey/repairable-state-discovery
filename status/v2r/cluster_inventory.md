# V2R cluster inventory

2026-09-27T05:29:12.649248+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314523090944 available bytes; 82.45% used; 112441316 free inodes.

server1 `/home`: 314523090944 available bytes; 82.45% used; 112441316 free inodes.

server1 `/tmp`: 314523090944 available bytes; 82.45% used; 112441316 free inodes.

server1 `/var/tmp`: 314523090944 available bytes; 82.45% used; 112441316 free inodes.

server1 `/mnt/raid5`: 634738466816 available bytes; 97.09% used; 337400033 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17620672512 available bytes; 99.02% used; 110364998 free inodes.

server2 `/home`: 17620672512 available bytes; 99.02% used; 110364998 free inodes.

server2 `/tmp`: 17620672512 available bytes; 99.02% used; 110364998 free inodes.

server2 `/var/tmp`: 17620672512 available bytes; 99.02% used; 110364998 free inodes.

server2 `/mnt/raid5`: 575135809536 available bytes; 96.03% used; 444877606 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78574960640 available bytes; 95.62% used; 114062911 free inodes.

server3 `/home`: 78574960640 available bytes; 95.62% used; 114062911 free inodes.

server3 `/data`: 1333007269888 available bytes; 81.58% used; 225766339 free inodes.

server3 `/tmp`: 78574960640 available bytes; 95.62% used; 114062911 free inodes.

server3 `/var/tmp`: 78574960640 available bytes; 95.62% used; 114062911 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110999695360 available bytes; 93.81% used; 114372900 free inodes.

server4 `/home`: 110999695360 available bytes; 93.81% used; 114372900 free inodes.

server4 `/data`: 374583574528 available bytes; 94.82% used; 224771229 free inodes.

server4 `/tmp`: 110999695360 available bytes; 93.81% used; 114372900 free inodes.

server4 `/var/tmp`: 110999695360 available bytes; 93.81% used; 114372900 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
