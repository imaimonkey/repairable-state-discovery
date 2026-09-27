# V2R cluster inventory

2026-09-27T00:47:24.394527+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315149172736 available bytes; 82.42% used; 112443459 free inodes.

server1 `/home`: 315149172736 available bytes; 82.42% used; 112443459 free inodes.

server1 `/tmp`: 315149172736 available bytes; 82.42% used; 112443459 free inodes.

server1 `/var/tmp`: 315149172736 available bytes; 82.42% used; 112443459 free inodes.

server1 `/mnt/raid5`: 637574553600 available bytes; 97.08% used; 337405841 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17639030784 available bytes; 99.02% used; 110365003 free inodes.

server2 `/home`: 17639030784 available bytes; 99.02% used; 110365003 free inodes.

server2 `/tmp`: 17639030784 available bytes; 99.02% used; 110365003 free inodes.

server2 `/var/tmp`: 17639030784 available bytes; 99.02% used; 110365003 free inodes.

server2 `/mnt/raid5`: 584486273024 available bytes; 95.96% used; 444887895 free inodes.
| server3 | True | ['0', '3'] | [] | reference_compatible=True |

server3 `/`: 79501393920 available bytes; 95.56% used; 114068710 free inodes.

server3 `/home`: 79501393920 available bytes; 95.56% used; 114068710 free inodes.

server3 `/data`: 1342505144320 available bytes; 81.45% used; 225764158 free inodes.

server3 `/tmp`: 79501393920 available bytes; 95.56% used; 114068710 free inodes.

server3 `/var/tmp`: 79501393920 available bytes; 95.56% used; 114068710 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105878876160 available bytes; 94.09% used; 114347835 free inodes.

server4 `/home`: 105878876160 available bytes; 94.09% used; 114347835 free inodes.

server4 `/data`: 406593871872 available bytes; 94.38% used; 224782992 free inodes.

server4 `/tmp`: 105878876160 available bytes; 94.09% used; 114347835 free inodes.

server4 `/var/tmp`: 105878876160 available bytes; 94.09% used; 114347835 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
