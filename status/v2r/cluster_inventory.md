# V2R cluster inventory

2026-09-26T10:12:50.555549+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318606557184 available bytes; 82.23% used; 112474984 free inodes.

server1 `/home`: 318606557184 available bytes; 82.23% used; 112474984 free inodes.

server1 `/tmp`: 318606557184 available bytes; 82.23% used; 112474984 free inodes.

server1 `/var/tmp`: 318606557184 available bytes; 82.23% used; 112474984 free inodes.

server1 `/mnt/raid5`: 218870923264 available bytes; 99.00% used; 337538442 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 20150931456 available bytes; 98.88% used; 110384947 free inodes.

server2 `/home`: 20150931456 available bytes; 98.88% used; 110384947 free inodes.

server2 `/tmp`: 20150931456 available bytes; 98.88% used; 110384947 free inodes.

server2 `/var/tmp`: 20150931456 available bytes; 98.88% used; 110384947 free inodes.

server2 `/mnt/raid5`: 252124401664 available bytes; 98.26% used; 445021171 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82657038336 available bytes; 95.39% used; 114110823 free inodes.

server3 `/home`: 82657038336 available bytes; 95.39% used; 114110823 free inodes.

server3 `/data`: 123586670592 available bytes; 98.29% used; 225827077 free inodes.

server3 `/tmp`: 82657038336 available bytes; 95.39% used; 114110823 free inodes.

server3 `/var/tmp`: 82657038336 available bytes; 95.39% used; 114110823 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105930883072 available bytes; 94.09% used; 114348032 free inodes.

server4 `/home`: 105930883072 available bytes; 94.09% used; 114348032 free inodes.

server4 `/data`: 89125548032 available bytes; 98.77% used; 224882033 free inodes.

server4 `/tmp`: 105930883072 available bytes; 94.09% used; 114348032 free inodes.

server4 `/var/tmp`: 105930883072 available bytes; 94.09% used; 114348032 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
