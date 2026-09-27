# V2R cluster inventory

2026-09-27T08:39:35.316948+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314465927168 available bytes; 82.46% used; 112440728 free inodes.

server1 `/home`: 314465927168 available bytes; 82.46% used; 112440728 free inodes.

server1 `/tmp`: 314465927168 available bytes; 82.46% used; 112440728 free inodes.

server1 `/var/tmp`: 314465927168 available bytes; 82.46% used; 112440728 free inodes.

server1 `/mnt/raid5`: 634590248960 available bytes; 97.09% used; 337400005 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 17611284480 available bytes; 99.02% used; 110364878 free inodes.

server2 `/home`: 17611284480 available bytes; 99.02% used; 110364878 free inodes.

server2 `/tmp`: 17611284480 available bytes; 99.02% used; 110364878 free inodes.

server2 `/var/tmp`: 17611284480 available bytes; 99.02% used; 110364878 free inodes.

server2 `/mnt/raid5`: 575804129280 available bytes; 96.02% used; 444751279 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78572036096 available bytes; 95.62% used; 114062865 free inodes.

server3 `/home`: 78572036096 available bytes; 95.62% used; 114062865 free inodes.

server3 `/data`: 1332624232448 available bytes; 81.58% used; 225763216 free inodes.

server3 `/tmp`: 78572036096 available bytes; 95.62% used; 114062865 free inodes.

server3 `/var/tmp`: 78572036096 available bytes; 95.62% used; 114062865 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111051927552 available bytes; 93.80% used; 114372882 free inodes.

server4 `/home`: 111051927552 available bytes; 93.80% used; 114372882 free inodes.

server4 `/data`: 366205939712 available bytes; 94.94% used; 224770160 free inodes.

server4 `/tmp`: 111051927552 available bytes; 93.80% used; 114372882 free inodes.

server4 `/var/tmp`: 111051927552 available bytes; 93.80% used; 114372882 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
