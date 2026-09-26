# V2R cluster inventory

2026-09-26T21:47:41.582456+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315481939968 available bytes; 82.40% used; 112445690 free inodes.

server1 `/home`: 315481939968 available bytes; 82.40% used; 112445690 free inodes.

server1 `/tmp`: 315481939968 available bytes; 82.40% used; 112445690 free inodes.

server1 `/var/tmp`: 315481939968 available bytes; 82.40% used; 112445690 free inodes.

server1 `/mnt/raid5`: 645857153024 available bytes; 97.04% used; 337467241 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 17943724032 available bytes; 99.00% used; 110367527 free inodes.

server2 `/home`: 17943724032 available bytes; 99.00% used; 110367527 free inodes.

server2 `/tmp`: 17943724032 available bytes; 99.00% used; 110367527 free inodes.

server2 `/var/tmp`: 17943724032 available bytes; 99.00% used; 110367527 free inodes.

server2 `/mnt/raid5`: 598268063744 available bytes; 95.87% used; 444962395 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 81084645376 available bytes; 95.48% used; 114069865 free inodes.

server3 `/home`: 81084645376 available bytes; 95.48% used; 114069865 free inodes.

server3 `/data`: 1349620445184 available bytes; 81.35% used; 225827512 free inodes.

server3 `/tmp`: 81084645376 available bytes; 95.48% used; 114069865 free inodes.

server3 `/var/tmp`: 81084645376 available bytes; 95.48% used; 114069865 free inodes.
| server4 | True | ['2', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105900290048 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105900290048 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409669685248 available bytes; 94.34% used; 224823837 free inodes.

server4 `/tmp`: 105900290048 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105900290048 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
