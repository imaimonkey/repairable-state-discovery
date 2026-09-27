# V2R cluster inventory

2026-09-27T06:17:27.333643+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314498486272 available bytes; 82.46% used; 112440813 free inodes.

server1 `/home`: 314498486272 available bytes; 82.46% used; 112440813 free inodes.

server1 `/tmp`: 314498486272 available bytes; 82.46% used; 112440813 free inodes.

server1 `/var/tmp`: 314498486272 available bytes; 82.46% used; 112440813 free inodes.

server1 `/mnt/raid5`: 634702016512 available bytes; 97.09% used; 337400011 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17620885504 available bytes; 99.02% used; 110365006 free inodes.

server2 `/home`: 17620885504 available bytes; 99.02% used; 110365006 free inodes.

server2 `/tmp`: 17620885504 available bytes; 99.02% used; 110365006 free inodes.

server2 `/var/tmp`: 17620885504 available bytes; 99.02% used; 110365006 free inodes.

server2 `/mnt/raid5`: 573537525760 available bytes; 96.04% used; 444876414 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78577045504 available bytes; 95.62% used; 114062897 free inodes.

server3 `/home`: 78577045504 available bytes; 95.62% used; 114062897 free inodes.

server3 `/data`: 1333256478720 available bytes; 81.57% used; 225765479 free inodes.

server3 `/tmp`: 78577045504 available bytes; 95.62% used; 114062897 free inodes.

server3 `/var/tmp`: 78577045504 available bytes; 95.62% used; 114062897 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 110998466560 available bytes; 93.81% used; 114372891 free inodes.

server4 `/home`: 110998466560 available bytes; 93.81% used; 114372891 free inodes.

server4 `/data`: 374478147584 available bytes; 94.82% used; 224771174 free inodes.

server4 `/tmp`: 110998466560 available bytes; 93.81% used; 114372891 free inodes.

server4 `/var/tmp`: 110998466560 available bytes; 93.81% used; 114372891 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
