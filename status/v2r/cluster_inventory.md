# V2R cluster inventory

2026-09-26T10:05:12.820757+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318611566592 available bytes; 82.23% used; 112475049 free inodes.

server1 `/home`: 318611566592 available bytes; 82.23% used; 112475049 free inodes.

server1 `/tmp`: 318611566592 available bytes; 82.23% used; 112475049 free inodes.

server1 `/var/tmp`: 318611566592 available bytes; 82.23% used; 112475049 free inodes.

server1 `/mnt/raid5`: 218886914048 available bytes; 99.00% used; 337538475 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22302490624 available bytes; 98.76% used; 110402883 free inodes.

server2 `/home`: 22302490624 available bytes; 98.76% used; 110402883 free inodes.

server2 `/tmp`: 22302490624 available bytes; 98.76% used; 110402883 free inodes.

server2 `/var/tmp`: 22302490624 available bytes; 98.76% used; 110402883 free inodes.

server2 `/mnt/raid5`: 252362436608 available bytes; 98.26% used; 445021779 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82658172928 available bytes; 95.39% used; 114110817 free inodes.

server3 `/home`: 82658172928 available bytes; 95.39% used; 114110817 free inodes.

server3 `/data`: 123588677632 available bytes; 98.29% used; 225827219 free inodes.

server3 `/tmp`: 82658172928 available bytes; 95.39% used; 114110817 free inodes.

server3 `/var/tmp`: 82658172928 available bytes; 95.39% used; 114110817 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105931116544 available bytes; 94.09% used; 114348027 free inodes.

server4 `/home`: 105931116544 available bytes; 94.09% used; 114348027 free inodes.

server4 `/data`: 89220988928 available bytes; 98.77% used; 224882049 free inodes.

server4 `/tmp`: 105931116544 available bytes; 94.09% used; 114348027 free inodes.

server4 `/var/tmp`: 105931116544 available bytes; 94.09% used; 114348027 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
