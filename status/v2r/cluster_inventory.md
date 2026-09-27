# V2R cluster inventory

2026-09-27T05:33:46.829674+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314491920384 available bytes; 82.46% used; 112440818 free inodes.

server1 `/home`: 314491920384 available bytes; 82.46% used; 112440818 free inodes.

server1 `/tmp`: 314491920384 available bytes; 82.46% used; 112440818 free inodes.

server1 `/var/tmp`: 314491920384 available bytes; 82.46% used; 112440818 free inodes.

server1 `/mnt/raid5`: 634736246784 available bytes; 97.09% used; 337400017 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17621102592 available bytes; 99.02% used; 110365000 free inodes.

server2 `/home`: 17621102592 available bytes; 99.02% used; 110365000 free inodes.

server2 `/tmp`: 17621102592 available bytes; 99.02% used; 110365000 free inodes.

server2 `/var/tmp`: 17621102592 available bytes; 99.02% used; 110365000 free inodes.

server2 `/mnt/raid5`: 574462541824 available bytes; 96.03% used; 444877742 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78575304704 available bytes; 95.62% used; 114062913 free inodes.

server3 `/home`: 78575304704 available bytes; 95.62% used; 114062913 free inodes.

server3 `/data`: 1333006757888 available bytes; 81.58% used; 225766262 free inodes.

server3 `/tmp`: 78575304704 available bytes; 95.62% used; 114062913 free inodes.

server3 `/var/tmp`: 78575304704 available bytes; 95.62% used; 114062913 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110999568384 available bytes; 93.81% used; 114372900 free inodes.

server4 `/home`: 110999568384 available bytes; 93.81% used; 114372900 free inodes.

server4 `/data`: 374581510144 available bytes; 94.82% used; 224771221 free inodes.

server4 `/tmp`: 110999568384 available bytes; 93.81% used; 114372900 free inodes.

server4 `/var/tmp`: 110999568384 available bytes; 93.81% used; 114372900 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
