# V2R cluster inventory

2026-09-27T01:05:41.281136+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315149938688 available bytes; 82.42% used; 112443432 free inodes.

server1 `/home`: 315149938688 available bytes; 82.42% used; 112443432 free inodes.

server1 `/tmp`: 315149938688 available bytes; 82.42% used; 112443432 free inodes.

server1 `/var/tmp`: 315149938688 available bytes; 82.42% used; 112443432 free inodes.

server1 `/mnt/raid5`: 637561724928 available bytes; 97.08% used; 337405752 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17630253056 available bytes; 99.02% used; 110364994 free inodes.

server2 `/home`: 17630253056 available bytes; 99.02% used; 110364994 free inodes.

server2 `/tmp`: 17630253056 available bytes; 99.02% used; 110364994 free inodes.

server2 `/var/tmp`: 17630253056 available bytes; 99.02% used; 110364994 free inodes.

server2 `/mnt/raid5`: 583945637888 available bytes; 95.97% used; 444887260 free inodes.
| server3 | True | ['0', '3'] | [] | reference_compatible=True |

server3 `/`: 79497977856 available bytes; 95.56% used; 114068698 free inodes.

server3 `/home`: 79497977856 available bytes; 95.56% used; 114068698 free inodes.

server3 `/data`: 1342475751424 available bytes; 81.45% used; 225763968 free inodes.

server3 `/tmp`: 79497977856 available bytes; 95.56% used; 114068698 free inodes.

server3 `/var/tmp`: 79497977856 available bytes; 95.56% used; 114068698 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105878409216 available bytes; 94.09% used; 114347835 free inodes.

server4 `/home`: 105878409216 available bytes; 94.09% used; 114347835 free inodes.

server4 `/data`: 406583586816 available bytes; 94.38% used; 224782986 free inodes.

server4 `/tmp`: 105878409216 available bytes; 94.09% used; 114347835 free inodes.

server4 `/var/tmp`: 105878409216 available bytes; 94.09% used; 114347835 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
