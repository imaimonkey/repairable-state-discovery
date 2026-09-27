# V2R cluster inventory

2026-09-27T07:27:36.534883+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314479104000 available bytes; 82.46% used; 112440799 free inodes.

server1 `/home`: 314479104000 available bytes; 82.46% used; 112440799 free inodes.

server1 `/tmp`: 314479104000 available bytes; 82.46% used; 112440799 free inodes.

server1 `/var/tmp`: 314479104000 available bytes; 82.46% used; 112440799 free inodes.

server1 `/mnt/raid5`: 634659446784 available bytes; 97.09% used; 337400004 free inodes.
| server2 | True | ['0', '1'] | [] |

server2 `/`: 17616769024 available bytes; 99.02% used; 110365012 free inodes.

server2 `/home`: 17616769024 available bytes; 99.02% used; 110365012 free inodes.

server2 `/tmp`: 17616769024 available bytes; 99.02% used; 110365012 free inodes.

server2 `/var/tmp`: 17616769024 available bytes; 99.02% used; 110365012 free inodes.

server2 `/mnt/raid5`: 570926907392 available bytes; 96.06% used; 444874294 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 78574358528 available bytes; 95.62% used; 114062883 free inodes.

server3 `/home`: 78574358528 available bytes; 95.62% used; 114062883 free inodes.

server3 `/data`: 1333049171968 available bytes; 81.58% used; 225764131 free inodes.

server3 `/tmp`: 78574358528 available bytes; 95.62% used; 114062883 free inodes.

server3 `/var/tmp`: 78574358528 available bytes; 95.62% used; 114062883 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111070621696 available bytes; 93.80% used; 114372905 free inodes.

server4 `/home`: 111070621696 available bytes; 93.80% used; 114372905 free inodes.

server4 `/data`: 374344351744 available bytes; 94.83% used; 224771140 free inodes.

server4 `/tmp`: 111070621696 available bytes; 93.80% used; 114372905 free inodes.

server4 `/var/tmp`: 111070621696 available bytes; 93.80% used; 114372905 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
