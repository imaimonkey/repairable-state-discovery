# V2R cluster inventory

2026-09-27T05:13:25.262920+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314758877184 available bytes; 82.44% used; 112443004 free inodes.

server1 `/home`: 314758877184 available bytes; 82.44% used; 112443004 free inodes.

server1 `/tmp`: 314758877184 available bytes; 82.44% used; 112443004 free inodes.

server1 `/var/tmp`: 314758877184 available bytes; 82.44% used; 112443004 free inodes.

server1 `/mnt/raid5`: 634729832448 available bytes; 97.09% used; 337400246 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17629589504 available bytes; 99.02% used; 110364998 free inodes.

server2 `/home`: 17629589504 available bytes; 99.02% used; 110364998 free inodes.

server2 `/tmp`: 17629589504 available bytes; 99.02% used; 110364998 free inodes.

server2 `/var/tmp`: 17629589504 available bytes; 99.02% used; 110364998 free inodes.

server2 `/mnt/raid5`: 575045414912 available bytes; 96.03% used; 444878166 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78575439872 available bytes; 95.62% used; 114062914 free inodes.

server3 `/home`: 78575439872 available bytes; 95.62% used; 114062914 free inodes.

server3 `/data`: 1332936892416 available bytes; 81.58% used; 225758188 free inodes.

server3 `/tmp`: 78575439872 available bytes; 95.62% used; 114062914 free inodes.

server3 `/var/tmp`: 78575439872 available bytes; 95.62% used; 114062914 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111000145920 available bytes; 93.81% used; 114372913 free inodes.

server4 `/home`: 111000145920 available bytes; 93.81% used; 114372913 free inodes.

server4 `/data`: 382057267200 available bytes; 94.72% used; 224778038 free inodes.

server4 `/tmp`: 111000145920 available bytes; 93.81% used; 114372913 free inodes.

server4 `/var/tmp`: 111000145920 available bytes; 93.81% used; 114372913 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
