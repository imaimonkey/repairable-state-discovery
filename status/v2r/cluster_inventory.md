# V2R cluster inventory

2026-09-27T02:03:34.212153+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315160494080 available bytes; 82.42% used; 112443340 free inodes.

server1 `/home`: 315160494080 available bytes; 82.42% used; 112443340 free inodes.

server1 `/tmp`: 315160494080 available bytes; 82.42% used; 112443340 free inodes.

server1 `/var/tmp`: 315160494080 available bytes; 82.42% used; 112443340 free inodes.

server1 `/mnt/raid5`: 637477945344 available bytes; 97.08% used; 337405441 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17629659136 available bytes; 99.02% used; 110364994 free inodes.

server2 `/home`: 17629659136 available bytes; 99.02% used; 110364994 free inodes.

server2 `/tmp`: 17629659136 available bytes; 99.02% used; 110364994 free inodes.

server2 `/var/tmp`: 17629659136 available bytes; 99.02% used; 110364994 free inodes.

server2 `/mnt/raid5`: 581716152320 available bytes; 95.98% used; 444885416 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78715109376 available bytes; 95.61% used; 114062951 free inodes.

server3 `/home`: 78715109376 available bytes; 95.61% used; 114062951 free inodes.

server3 `/data`: 1338765307904 available bytes; 81.50% used; 225762697 free inodes.

server3 `/tmp`: 78715109376 available bytes; 95.61% used; 114062951 free inodes.

server3 `/var/tmp`: 78715109376 available bytes; 95.61% used; 114062951 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105859903488 available bytes; 94.09% used; 114347771 free inodes.

server4 `/home`: 105859903488 available bytes; 94.09% used; 114347771 free inodes.

server4 `/data`: 403668246528 available bytes; 94.42% used; 224782432 free inodes.

server4 `/tmp`: 105859903488 available bytes; 94.09% used; 114347771 free inodes.

server4 `/var/tmp`: 105859903488 available bytes; 94.09% used; 114347771 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
