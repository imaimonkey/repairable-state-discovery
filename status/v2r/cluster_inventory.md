# V2R cluster inventory

2026-09-26T23:01:25.747025+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315468468224 available bytes; 82.40% used; 112445685 free inodes.

server1 `/home`: 315468468224 available bytes; 82.40% used; 112445685 free inodes.

server1 `/tmp`: 315468468224 available bytes; 82.40% used; 112445685 free inodes.

server1 `/var/tmp`: 315468468224 available bytes; 82.40% used; 112445685 free inodes.

server1 `/mnt/raid5`: 645833793536 available bytes; 97.04% used; 337467216 free inodes.
| server2 | True | ['2', '7'] | [] |

server2 `/`: 17941544960 available bytes; 99.00% used; 110367493 free inodes.

server2 `/home`: 17941544960 available bytes; 99.00% used; 110367493 free inodes.

server2 `/tmp`: 17941544960 available bytes; 99.00% used; 110367493 free inodes.

server2 `/var/tmp`: 17941544960 available bytes; 99.00% used; 110367493 free inodes.

server2 `/mnt/raid5`: 596168855552 available bytes; 95.88% used; 444960372 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 81080541184 available bytes; 95.48% used; 114069865 free inodes.

server3 `/home`: 81080541184 available bytes; 95.48% used; 114069865 free inodes.

server3 `/data`: 1349238849536 available bytes; 81.35% used; 225826706 free inodes.

server3 `/tmp`: 81080541184 available bytes; 95.48% used; 114069865 free inodes.

server3 `/var/tmp`: 81080541184 available bytes; 95.48% used; 114069865 free inodes.
| server4 | True | ['2', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105898418176 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105898418176 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409614032896 available bytes; 94.34% used; 224823821 free inodes.

server4 `/tmp`: 105898418176 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105898418176 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
