# V2R cluster inventory

2026-09-27T06:31:38.503026+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314497662976 available bytes; 82.46% used; 112440810 free inodes.

server1 `/home`: 314497662976 available bytes; 82.46% used; 112440810 free inodes.

server1 `/tmp`: 314497662976 available bytes; 82.46% used; 112440810 free inodes.

server1 `/var/tmp`: 314497662976 available bytes; 82.46% used; 112440810 free inodes.

server1 `/mnt/raid5`: 634693718016 available bytes; 97.09% used; 337400010 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17625194496 available bytes; 99.02% used; 110365003 free inodes.

server2 `/home`: 17625194496 available bytes; 99.02% used; 110365003 free inodes.

server2 `/tmp`: 17625194496 available bytes; 99.02% used; 110365003 free inodes.

server2 `/var/tmp`: 17625194496 available bytes; 99.02% used; 110365003 free inodes.

server2 `/mnt/raid5`: 573053140992 available bytes; 96.04% used; 444875831 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78578679808 available bytes; 95.62% used; 114062889 free inodes.

server3 `/home`: 78578679808 available bytes; 95.62% used; 114062889 free inodes.

server3 `/data`: 1333175672832 available bytes; 81.57% used; 225765161 free inodes.

server3 `/tmp`: 78578679808 available bytes; 95.62% used; 114062889 free inodes.

server3 `/var/tmp`: 78578679808 available bytes; 95.62% used; 114062889 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110998097920 available bytes; 93.81% used; 114372898 free inodes.

server4 `/home`: 110998097920 available bytes; 93.81% used; 114372898 free inodes.

server4 `/data`: 374468116480 available bytes; 94.82% used; 224771155 free inodes.

server4 `/tmp`: 110998097920 available bytes; 93.81% used; 114372898 free inodes.

server4 `/var/tmp`: 110998097920 available bytes; 93.81% used; 114372898 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
