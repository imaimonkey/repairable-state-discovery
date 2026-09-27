# V2R cluster inventory

2026-09-27T08:37:44.482349+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314466328576 available bytes; 82.46% used; 112440728 free inodes.

server1 `/home`: 314466328576 available bytes; 82.46% used; 112440728 free inodes.

server1 `/tmp`: 314466328576 available bytes; 82.46% used; 112440728 free inodes.

server1 `/var/tmp`: 314466328576 available bytes; 82.46% used; 112440728 free inodes.

server1 `/mnt/raid5`: 634589442048 available bytes; 97.09% used; 337400005 free inodes.
| server2 | True | ['1', '2', '7'] | [] |

server2 `/`: 17611591680 available bytes; 99.02% used; 110364878 free inodes.

server2 `/home`: 17611591680 available bytes; 99.02% used; 110364878 free inodes.

server2 `/tmp`: 17611591680 available bytes; 99.02% used; 110364878 free inodes.

server2 `/var/tmp`: 17611591680 available bytes; 99.02% used; 110364878 free inodes.

server2 `/mnt/raid5`: 575868641280 available bytes; 96.02% used; 444751470 free inodes.
| server3 | True | ['0', '2'] | [] |

server3 `/`: 78572306432 available bytes; 95.62% used; 114062870 free inodes.

server3 `/home`: 78572306432 available bytes; 95.62% used; 114062870 free inodes.

server3 `/data`: 1332638945280 available bytes; 81.58% used; 225763253 free inodes.

server3 `/tmp`: 78572306432 available bytes; 95.62% used; 114062870 free inodes.

server3 `/var/tmp`: 78572306432 available bytes; 95.62% used; 114062870 free inodes.
| server4 | True | ['4', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111051984896 available bytes; 93.80% used; 114372882 free inodes.

server4 `/home`: 111051984896 available bytes; 93.80% used; 114372882 free inodes.

server4 `/data`: 367658004480 available bytes; 94.92% used; 224770305 free inodes.

server4 `/tmp`: 111051984896 available bytes; 93.80% used; 114372882 free inodes.

server4 `/var/tmp`: 111051984896 available bytes; 93.80% used; 114372882 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
