# V2R cluster inventory

2026-09-27T06:25:33.053221+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314496995328 available bytes; 82.46% used; 112440803 free inodes.

server1 `/home`: 314496995328 available bytes; 82.46% used; 112440803 free inodes.

server1 `/tmp`: 314496995328 available bytes; 82.46% used; 112440803 free inodes.

server1 `/var/tmp`: 314496995328 available bytes; 82.46% used; 112440803 free inodes.

server1 `/mnt/raid5`: 634687217664 available bytes; 97.09% used; 337400006 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17626476544 available bytes; 99.02% used; 110365006 free inodes.

server2 `/home`: 17626476544 available bytes; 99.02% used; 110365006 free inodes.

server2 `/tmp`: 17626476544 available bytes; 99.02% used; 110365006 free inodes.

server2 `/var/tmp`: 17626476544 available bytes; 99.02% used; 110365006 free inodes.

server2 `/mnt/raid5`: 573312471040 available bytes; 96.04% used; 444876192 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78579961856 available bytes; 95.61% used; 114062893 free inodes.

server3 `/home`: 78579961856 available bytes; 95.61% used; 114062893 free inodes.

server3 `/data`: 1333247811584 available bytes; 81.57% used; 225765231 free inodes.

server3 `/tmp`: 78579961856 available bytes; 95.61% used; 114062893 free inodes.

server3 `/var/tmp`: 78579961856 available bytes; 95.61% used; 114062893 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110998241280 available bytes; 93.81% used; 114372889 free inodes.

server4 `/home`: 110998241280 available bytes; 93.81% used; 114372889 free inodes.

server4 `/data`: 374466580480 available bytes; 94.82% used; 224771145 free inodes.

server4 `/tmp`: 110998241280 available bytes; 93.81% used; 114372889 free inodes.

server4 `/var/tmp`: 110998241280 available bytes; 93.81% used; 114372889 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
