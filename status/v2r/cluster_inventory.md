# V2R cluster inventory

2026-09-27T08:31:38.313979+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314468503552 available bytes; 82.46% used; 112440796 free inodes.

server1 `/home`: 314468503552 available bytes; 82.46% used; 112440796 free inodes.

server1 `/tmp`: 314468503552 available bytes; 82.46% used; 112440796 free inodes.

server1 `/var/tmp`: 314468503552 available bytes; 82.46% used; 112440796 free inodes.

server1 `/mnt/raid5`: 634589716480 available bytes; 97.09% used; 337400003 free inodes.
| server2 | True | ['1', '2', '7'] | [] |

server2 `/`: 17608908800 available bytes; 99.02% used; 110365012 free inodes.

server2 `/home`: 17608908800 available bytes; 99.02% used; 110365012 free inodes.

server2 `/tmp`: 17608908800 available bytes; 99.02% used; 110365012 free inodes.

server2 `/var/tmp`: 17608908800 available bytes; 99.02% used; 110365012 free inodes.

server2 `/mnt/raid5`: 575616544768 available bytes; 96.02% used; 444753254 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 78573572096 available bytes; 95.62% used; 114062872 free inodes.

server3 `/home`: 78573572096 available bytes; 95.62% used; 114062872 free inodes.

server3 `/data`: 1332704432128 available bytes; 81.58% used; 225763348 free inodes.

server3 `/tmp`: 78573572096 available bytes; 95.62% used; 114062872 free inodes.

server3 `/var/tmp`: 78573572096 available bytes; 95.62% used; 114062872 free inodes.
| server4 | True | ['4', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111052124160 available bytes; 93.80% used; 114372886 free inodes.

server4 `/home`: 111052124160 available bytes; 93.80% used; 114372886 free inodes.

server4 `/data`: 367893819392 available bytes; 94.92% used; 224770783 free inodes.

server4 `/tmp`: 111052124160 available bytes; 93.80% used; 114372886 free inodes.

server4 `/var/tmp`: 111052124160 available bytes; 93.80% used; 114372886 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
