# V2R cluster inventory

2026-09-26T23:11:27.828482+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315467354112 available bytes; 82.40% used; 112445703 free inodes.

server1 `/home`: 315467354112 available bytes; 82.40% used; 112445703 free inodes.

server1 `/tmp`: 315467354112 available bytes; 82.40% used; 112445703 free inodes.

server1 `/var/tmp`: 315467354112 available bytes; 82.40% used; 112445703 free inodes.

server1 `/mnt/raid5`: 645838774272 available bytes; 97.04% used; 337467222 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 17948504064 available bytes; 99.00% used; 110367458 free inodes.

server2 `/home`: 17948504064 available bytes; 99.00% used; 110367458 free inodes.

server2 `/tmp`: 17948504064 available bytes; 99.00% used; 110367458 free inodes.

server2 `/var/tmp`: 17948504064 available bytes; 99.00% used; 110367458 free inodes.

server2 `/mnt/raid5`: 595074379776 available bytes; 95.89% used; 444960094 free inodes.
| server3 | True | ['2'] | [] | reference_compatible=True |

server3 `/`: 81085648896 available bytes; 95.48% used; 114069881 free inodes.

server3 `/home`: 81085648896 available bytes; 95.48% used; 114069881 free inodes.

server3 `/data`: 1349234384896 available bytes; 81.35% used; 225826606 free inodes.

server3 `/tmp`: 81085648896 available bytes; 95.48% used; 114069881 free inodes.

server3 `/var/tmp`: 81085648896 available bytes; 95.48% used; 114069881 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105898147840 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105898147840 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409609781248 available bytes; 94.34% used; 224823796 free inodes.

server4 `/tmp`: 105898147840 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105898147840 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
