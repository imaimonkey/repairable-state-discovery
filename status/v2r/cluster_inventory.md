# V2R cluster inventory

2026-09-26T22:51:39.798296+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315472330752 available bytes; 82.40% used; 112445701 free inodes.

server1 `/home`: 315472330752 available bytes; 82.40% used; 112445701 free inodes.

server1 `/tmp`: 315472330752 available bytes; 82.40% used; 112445701 free inodes.

server1 `/var/tmp`: 315472330752 available bytes; 82.40% used; 112445701 free inodes.

server1 `/mnt/raid5`: 645834199040 available bytes; 97.04% used; 337467222 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 17947365376 available bytes; 99.00% used; 110367507 free inodes.

server2 `/home`: 17947365376 available bytes; 99.00% used; 110367507 free inodes.

server2 `/tmp`: 17947365376 available bytes; 99.00% used; 110367507 free inodes.

server2 `/var/tmp`: 17947365376 available bytes; 99.00% used; 110367507 free inodes.

server2 `/mnt/raid5`: 596453289984 available bytes; 95.88% used; 444960513 free inodes.
| server3 | True | ['2'] | [] | reference_compatible=True |

server3 `/`: 81084530688 available bytes; 95.48% used; 114069879 free inodes.

server3 `/home`: 81084530688 available bytes; 95.48% used; 114069879 free inodes.

server3 `/data`: 1349239541760 available bytes; 81.35% used; 225826808 free inodes.

server3 `/tmp`: 81084530688 available bytes; 95.48% used; 114069879 free inodes.

server3 `/var/tmp`: 81084530688 available bytes; 95.48% used; 114069879 free inodes.
| server4 | True | ['2', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105898659840 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105898659840 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409622085632 available bytes; 94.34% used; 224823835 free inodes.

server4 `/tmp`: 105898659840 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105898659840 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
