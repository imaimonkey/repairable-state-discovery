# V2R cluster inventory

2026-09-27T07:09:42.855389+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314480619520 available bytes; 82.46% used; 112440801 free inodes.

server1 `/home`: 314480619520 available bytes; 82.46% used; 112440801 free inodes.

server1 `/tmp`: 314480619520 available bytes; 82.46% used; 112440801 free inodes.

server1 `/var/tmp`: 314480619520 available bytes; 82.46% used; 112440801 free inodes.

server1 `/mnt/raid5`: 634663907328 available bytes; 97.09% used; 337400002 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17611231232 available bytes; 99.02% used; 110365011 free inodes.

server2 `/home`: 17611231232 available bytes; 99.02% used; 110365011 free inodes.

server2 `/tmp`: 17611231232 available bytes; 99.02% used; 110365011 free inodes.

server2 `/var/tmp`: 17611231232 available bytes; 99.02% used; 110365011 free inodes.

server2 `/mnt/raid5`: 571994984448 available bytes; 96.05% used; 444875059 free inodes.
| server3 | True | ['3'] | [] | reference_compatible=True |

server3 `/`: 78573633536 available bytes; 95.62% used; 114062900 free inodes.

server3 `/home`: 78573633536 available bytes; 95.62% used; 114062900 free inodes.

server3 `/data`: 1333228711936 available bytes; 81.57% used; 225764474 free inodes.

server3 `/tmp`: 78573633536 available bytes; 95.62% used; 114062900 free inodes.

server3 `/var/tmp`: 78573633536 available bytes; 95.62% used; 114062900 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111071047680 available bytes; 93.80% used; 114372892 free inodes.

server4 `/home`: 111071047680 available bytes; 93.80% used; 114372892 free inodes.

server4 `/data`: 374392565760 available bytes; 94.83% used; 224771211 free inodes.

server4 `/tmp`: 111071047680 available bytes; 93.80% used; 114372892 free inodes.

server4 `/var/tmp`: 111071047680 available bytes; 93.80% used; 114372892 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
