# V2R cluster inventory

2026-09-27T03:33:26.903869+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315086409728 available bytes; 82.42% used; 112443053 free inodes.

server1 `/home`: 315086409728 available bytes; 82.42% used; 112443053 free inodes.

server1 `/tmp`: 315086409728 available bytes; 82.42% used; 112443053 free inodes.

server1 `/var/tmp`: 315086409728 available bytes; 82.42% used; 112443053 free inodes.

server1 `/mnt/raid5`: 636783783936 available bytes; 97.08% used; 337401379 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17633021952 available bytes; 99.02% used; 110365015 free inodes.

server2 `/home`: 17633021952 available bytes; 99.02% used; 110365015 free inodes.

server2 `/tmp`: 17633021952 available bytes; 99.02% used; 110365015 free inodes.

server2 `/var/tmp`: 17633021952 available bytes; 99.02% used; 110365015 free inodes.

server2 `/mnt/raid5`: 578508558336 available bytes; 96.00% used; 444882807 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78708330496 available bytes; 95.61% used; 114062950 free inodes.

server3 `/home`: 78708330496 available bytes; 95.61% used; 114062950 free inodes.

server3 `/data`: 1336437235712 available bytes; 81.53% used; 225761449 free inodes.

server3 `/tmp`: 78708330496 available bytes; 95.61% used; 114062950 free inodes.

server3 `/var/tmp`: 78708330496 available bytes; 95.61% used; 114062950 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111028080640 available bytes; 93.80% used; 114372980 free inodes.

server4 `/home`: 111028080640 available bytes; 93.80% used; 114372980 free inodes.

server4 `/data`: 385476419584 available bytes; 94.67% used; 224780882 free inodes.

server4 `/tmp`: 111028080640 available bytes; 93.80% used; 114372980 free inodes.

server4 `/var/tmp`: 111028080640 available bytes; 93.80% used; 114372980 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
