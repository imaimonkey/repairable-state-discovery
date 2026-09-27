# V2R cluster inventory

2026-09-27T02:13:31.057382+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315159195648 available bytes; 82.42% used; 112443333 free inodes.

server1 `/home`: 315159195648 available bytes; 82.42% used; 112443333 free inodes.

server1 `/tmp`: 315159195648 available bytes; 82.42% used; 112443333 free inodes.

server1 `/var/tmp`: 315159195648 available bytes; 82.42% used; 112443333 free inodes.

server1 `/mnt/raid5`: 637261987840 available bytes; 97.08% used; 337401673 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17627525120 available bytes; 99.02% used; 110365000 free inodes.

server2 `/home`: 17627525120 available bytes; 99.02% used; 110365000 free inodes.

server2 `/tmp`: 17627525120 available bytes; 99.02% used; 110365000 free inodes.

server2 `/var/tmp`: 17627525120 available bytes; 99.02% used; 110365000 free inodes.

server2 `/mnt/raid5`: 580917047296 available bytes; 95.99% used; 444885249 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78706454528 available bytes; 95.61% used; 114062951 free inodes.

server3 `/home`: 78706454528 available bytes; 95.61% used; 114062951 free inodes.

server3 `/data`: 1337725034496 available bytes; 81.51% used; 225762564 free inodes.

server3 `/tmp`: 78706454528 available bytes; 95.61% used; 114062951 free inodes.

server3 `/var/tmp`: 78706454528 available bytes; 95.61% used; 114062951 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105810395136 available bytes; 94.10% used; 114347750 free inodes.

server4 `/home`: 105810395136 available bytes; 94.10% used; 114347750 free inodes.

server4 `/data`: 403609407488 available bytes; 94.42% used; 224781874 free inodes.

server4 `/tmp`: 105810395136 available bytes; 94.10% used; 114347750 free inodes.

server4 `/var/tmp`: 105810395136 available bytes; 94.10% used; 114347750 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
