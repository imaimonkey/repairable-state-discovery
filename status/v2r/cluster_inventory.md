# V2R cluster inventory

2026-09-26T12:02:42.571354+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318193295360 available bytes; 82.25% used; 112474775 free inodes.

server1 `/home`: 318193295360 available bytes; 82.25% used; 112474775 free inodes.

server1 `/tmp`: 318193295360 available bytes; 82.25% used; 112474775 free inodes.

server1 `/var/tmp`: 318193295360 available bytes; 82.25% used; 112474775 free inodes.

server1 `/mnt/raid5`: 218621304832 available bytes; 99.00% used; 337537928 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19782045696 available bytes; 98.90% used; 110383636 free inodes.

server2 `/home`: 19782045696 available bytes; 98.90% used; 110383636 free inodes.

server2 `/tmp`: 19782045696 available bytes; 98.90% used; 110383636 free inodes.

server2 `/var/tmp`: 19782045696 available bytes; 98.90% used; 110383636 free inodes.

server2 `/mnt/raid5`: 241113931776 available bytes; 98.33% used; 444981313 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82652426240 available bytes; 95.39% used; 114110824 free inodes.

server3 `/home`: 82652426240 available bytes; 95.39% used; 114110824 free inodes.

server3 `/data`: 123426328576 available bytes; 98.29% used; 225824624 free inodes.

server3 `/tmp`: 82652426240 available bytes; 95.39% used; 114110824 free inodes.

server3 `/var/tmp`: 82652426240 available bytes; 95.39% used; 114110824 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105900433408 available bytes; 94.09% used; 114347938 free inodes.

server4 `/home`: 105900433408 available bytes; 94.09% used; 114347938 free inodes.

server4 `/data`: 88575795200 available bytes; 98.78% used; 224879221 free inodes.

server4 `/tmp`: 105900433408 available bytes; 94.09% used; 114347938 free inodes.

server4 `/var/tmp`: 105900433408 available bytes; 94.09% used; 114347938 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
