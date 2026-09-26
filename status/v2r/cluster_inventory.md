# V2R cluster inventory

2026-09-26T21:55:18.373501+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315479662592 available bytes; 82.40% used; 112445682 free inodes.

server1 `/home`: 315479662592 available bytes; 82.40% used; 112445682 free inodes.

server1 `/tmp`: 315479662592 available bytes; 82.40% used; 112445682 free inodes.

server1 `/var/tmp`: 315479662592 available bytes; 82.40% used; 112445682 free inodes.

server1 `/mnt/raid5`: 645856571392 available bytes; 97.04% used; 337467241 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 17942695936 available bytes; 99.00% used; 110367513 free inodes.

server2 `/home`: 17942695936 available bytes; 99.00% used; 110367513 free inodes.

server2 `/tmp`: 17942695936 available bytes; 99.00% used; 110367513 free inodes.

server2 `/var/tmp`: 17942695936 available bytes; 99.00% used; 110367513 free inodes.

server2 `/mnt/raid5`: 598060941312 available bytes; 95.87% used; 444962186 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 81081229312 available bytes; 95.48% used; 114069851 free inodes.

server3 `/home`: 81081229312 available bytes; 95.48% used; 114069851 free inodes.

server3 `/data`: 1349623877632 available bytes; 81.35% used; 225827440 free inodes.

server3 `/tmp`: 81081229312 available bytes; 95.48% used; 114069851 free inodes.

server3 `/var/tmp`: 81081229312 available bytes; 95.48% used; 114069851 free inodes.
| server4 | True | ['2', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105900101632 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105900101632 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409660903424 available bytes; 94.34% used; 224823823 free inodes.

server4 `/tmp`: 105900101632 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105900101632 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
