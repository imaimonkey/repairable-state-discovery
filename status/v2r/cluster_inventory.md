# V2R cluster inventory

2026-09-27T06:39:15.321269+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314498043904 available bytes; 82.46% used; 112440812 free inodes.

server1 `/home`: 314498043904 available bytes; 82.46% used; 112440812 free inodes.

server1 `/tmp`: 314498043904 available bytes; 82.46% used; 112440812 free inodes.

server1 `/var/tmp`: 314498043904 available bytes; 82.46% used; 112440812 free inodes.

server1 `/mnt/raid5`: 634674257920 available bytes; 97.09% used; 337400004 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17619427328 available bytes; 99.02% used; 110365003 free inodes.

server2 `/home`: 17619427328 available bytes; 99.02% used; 110365003 free inodes.

server2 `/tmp`: 17619427328 available bytes; 99.02% used; 110365003 free inodes.

server2 `/var/tmp`: 17619427328 available bytes; 99.02% used; 110365003 free inodes.

server2 `/mnt/raid5`: 572847652864 available bytes; 96.04% used; 444875760 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78575357952 available bytes; 95.62% used; 114062897 free inodes.

server3 `/home`: 78575357952 available bytes; 95.62% used; 114062897 free inodes.

server3 `/data`: 1333275406336 available bytes; 81.57% used; 225765225 free inodes.

server3 `/tmp`: 78575357952 available bytes; 95.62% used; 114062897 free inodes.

server3 `/var/tmp`: 78575357952 available bytes; 95.62% used; 114062897 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110997913600 available bytes; 93.81% used; 114372899 free inodes.

server4 `/home`: 110997913600 available bytes; 93.81% used; 114372899 free inodes.

server4 `/data`: 374453956608 available bytes; 94.82% used; 224771187 free inodes.

server4 `/tmp`: 110997913600 available bytes; 93.81% used; 114372899 free inodes.

server4 `/var/tmp`: 110997913600 available bytes; 93.81% used; 114372899 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
