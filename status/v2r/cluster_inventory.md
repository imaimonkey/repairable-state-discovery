# V2R cluster inventory

2026-09-26T10:03:41.282495+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318612144128 available bytes; 82.23% used; 112475045 free inodes.

server1 `/home`: 318612144128 available bytes; 82.23% used; 112475045 free inodes.

server1 `/tmp`: 318612144128 available bytes; 82.23% used; 112475045 free inodes.

server1 `/var/tmp`: 318612144128 available bytes; 82.23% used; 112475045 free inodes.

server1 `/mnt/raid5`: 218891657216 available bytes; 99.00% used; 337538483 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22301302784 available bytes; 98.76% used; 110402877 free inodes.

server2 `/home`: 22301302784 available bytes; 98.76% used; 110402877 free inodes.

server2 `/tmp`: 22301302784 available bytes; 98.76% used; 110402877 free inodes.

server2 `/var/tmp`: 22301302784 available bytes; 98.76% used; 110402877 free inodes.

server2 `/mnt/raid5`: 251859505152 available bytes; 98.26% used; 445021566 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82661478400 available bytes; 95.39% used; 114110815 free inodes.

server3 `/home`: 82661478400 available bytes; 95.39% used; 114110815 free inodes.

server3 `/data`: 123589017600 available bytes; 98.29% used; 225827248 free inodes.

server3 `/tmp`: 82661478400 available bytes; 95.39% used; 114110815 free inodes.

server3 `/var/tmp`: 82661478400 available bytes; 95.39% used; 114110815 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105931173888 available bytes; 94.09% used; 114348027 free inodes.

server4 `/home`: 105931173888 available bytes; 94.09% used; 114348027 free inodes.

server4 `/data`: 89227370496 available bytes; 98.77% used; 224882256 free inodes.

server4 `/tmp`: 105931173888 available bytes; 94.09% used; 114348027 free inodes.

server4 `/var/tmp`: 105931173888 available bytes; 94.09% used; 114348027 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
