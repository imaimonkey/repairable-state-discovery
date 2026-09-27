# V2R cluster inventory

2026-09-27T01:57:28.783038+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315161800704 available bytes; 82.42% used; 112443357 free inodes.

server1 `/home`: 315161800704 available bytes; 82.42% used; 112443357 free inodes.

server1 `/tmp`: 315161800704 available bytes; 82.42% used; 112443357 free inodes.

server1 `/var/tmp`: 315161800704 available bytes; 82.42% used; 112443357 free inodes.

server1 `/mnt/raid5`: 637479604224 available bytes; 97.08% used; 337405468 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17635921920 available bytes; 99.02% used; 110364998 free inodes.

server2 `/home`: 17635921920 available bytes; 99.02% used; 110364998 free inodes.

server2 `/tmp`: 17635921920 available bytes; 99.02% used; 110364998 free inodes.

server2 `/var/tmp`: 17635921920 available bytes; 99.02% used; 110364998 free inodes.

server2 `/mnt/raid5`: 581388853248 available bytes; 95.98% used; 444885870 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78715338752 available bytes; 95.61% used; 114062955 free inodes.

server3 `/home`: 78715338752 available bytes; 95.61% used; 114062955 free inodes.

server3 `/data`: 1338783748096 available bytes; 81.50% used; 225762787 free inodes.

server3 `/tmp`: 78715338752 available bytes; 95.61% used; 114062955 free inodes.

server3 `/var/tmp`: 78715338752 available bytes; 95.61% used; 114062955 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105860100096 available bytes; 94.09% used; 114347780 free inodes.

server4 `/home`: 105860100096 available bytes; 94.09% used; 114347780 free inodes.

server4 `/data`: 403700596736 available bytes; 94.42% used; 224782822 free inodes.

server4 `/tmp`: 105860100096 available bytes; 94.09% used; 114347780 free inodes.

server4 `/var/tmp`: 105860100096 available bytes; 94.09% used; 114347780 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
