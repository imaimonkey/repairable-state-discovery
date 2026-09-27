# V2R cluster inventory

2026-09-27T02:23:22.207736+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315154386944 available bytes; 82.42% used; 112443386 free inodes.

server1 `/home`: 315154386944 available bytes; 82.42% used; 112443386 free inodes.

server1 `/tmp`: 315154386944 available bytes; 82.42% used; 112443386 free inodes.

server1 `/var/tmp`: 315154386944 available bytes; 82.42% used; 112443386 free inodes.

server1 `/mnt/raid5`: 637263089664 available bytes; 97.08% used; 337401645 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17635782656 available bytes; 99.02% used; 110365000 free inodes.

server2 `/home`: 17635782656 available bytes; 99.02% used; 110365000 free inodes.

server2 `/tmp`: 17635782656 available bytes; 99.02% used; 110365000 free inodes.

server2 `/var/tmp`: 17635782656 available bytes; 99.02% used; 110365000 free inodes.

server2 `/mnt/raid5`: 581158494208 available bytes; 95.98% used; 444884967 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78709534720 available bytes; 95.61% used; 114062951 free inodes.

server3 `/home`: 78709534720 available bytes; 95.61% used; 114062951 free inodes.

server3 `/data`: 1337715642368 available bytes; 81.51% used; 225762423 free inodes.

server3 `/tmp`: 78709534720 available bytes; 95.61% used; 114062951 free inodes.

server3 `/var/tmp`: 78709534720 available bytes; 95.61% used; 114062951 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111036608512 available bytes; 93.80% used; 114373257 free inodes.

server4 `/home`: 111036608512 available bytes; 93.80% used; 114373257 free inodes.

server4 `/data`: 400316444672 available bytes; 94.47% used; 224781617 free inodes.

server4 `/tmp`: 111036608512 available bytes; 93.80% used; 114373257 free inodes.

server4 `/var/tmp`: 111036608512 available bytes; 93.80% used; 114373257 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
