# V2R cluster inventory

2026-09-27T01:25:29.677680+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315146485760 available bytes; 82.42% used; 112443442 free inodes.

server1 `/home`: 315146485760 available bytes; 82.42% used; 112443442 free inodes.

server1 `/tmp`: 315146485760 available bytes; 82.42% used; 112443442 free inodes.

server1 `/var/tmp`: 315146485760 available bytes; 82.42% used; 112443442 free inodes.

server1 `/mnt/raid5`: 637521346560 available bytes; 97.08% used; 337405521 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17635061760 available bytes; 99.02% used; 110364998 free inodes.

server2 `/home`: 17635061760 available bytes; 99.02% used; 110364998 free inodes.

server2 `/tmp`: 17635061760 available bytes; 99.02% used; 110364998 free inodes.

server2 `/var/tmp`: 17635061760 available bytes; 99.02% used; 110364998 free inodes.

server2 `/mnt/raid5`: 582838358016 available bytes; 95.97% used; 444886637 free inodes.
| server3 | True | ['0', '3'] | [] | reference_compatible=True |

server3 `/`: 79500075008 available bytes; 95.56% used; 114068704 free inodes.

server3 `/home`: 79500075008 available bytes; 95.56% used; 114068704 free inodes.

server3 `/data`: 1342413602816 available bytes; 81.45% used; 225763647 free inodes.

server3 `/tmp`: 79500075008 available bytes; 95.56% used; 114068704 free inodes.

server3 `/var/tmp`: 79500075008 available bytes; 95.56% used; 114068704 free inodes.
| server4 | True | ['0', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105869553664 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105869553664 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 406543822848 available bytes; 94.38% used; 224782882 free inodes.

server4 `/tmp`: 105869553664 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105869553664 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
