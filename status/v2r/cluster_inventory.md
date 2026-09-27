# V2R cluster inventory

2026-09-27T05:21:35.746010+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314754338816 available bytes; 82.44% used; 112442997 free inodes.

server1 `/home`: 314754338816 available bytes; 82.44% used; 112442997 free inodes.

server1 `/tmp`: 314754338816 available bytes; 82.44% used; 112442997 free inodes.

server1 `/var/tmp`: 314754338816 available bytes; 82.44% used; 112442997 free inodes.

server1 `/mnt/raid5`: 634728443904 available bytes; 97.09% used; 337400114 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17628041216 available bytes; 99.02% used; 110365000 free inodes.

server2 `/home`: 17628041216 available bytes; 99.02% used; 110365000 free inodes.

server2 `/tmp`: 17628041216 available bytes; 99.02% used; 110365000 free inodes.

server2 `/var/tmp`: 17628041216 available bytes; 99.02% used; 110365000 free inodes.

server2 `/mnt/raid5`: 574815916032 available bytes; 96.03% used; 444877939 free inodes.
| server3 | True | ['2'] | [] | reference_compatible=True |

server3 `/`: 78577614848 available bytes; 95.62% used; 114062912 free inodes.

server3 `/home`: 78577614848 available bytes; 95.62% used; 114062912 free inodes.

server3 `/data`: 1332918591488 available bytes; 81.58% used; 225758025 free inodes.

server3 `/tmp`: 78577614848 available bytes; 95.62% used; 114062912 free inodes.

server3 `/var/tmp`: 78577614848 available bytes; 95.62% used; 114062912 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110999875584 available bytes; 93.81% used; 114372908 free inodes.

server4 `/home`: 110999875584 available bytes; 93.81% used; 114372908 free inodes.

server4 `/data`: 378609180672 available bytes; 94.77% used; 224774964 free inodes.

server4 `/tmp`: 110999875584 available bytes; 93.81% used; 114372908 free inodes.

server4 `/var/tmp`: 110999875584 available bytes; 93.81% used; 114372908 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
