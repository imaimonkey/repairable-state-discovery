# V2R cluster inventory

2026-09-27T02:25:42.897621+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315091562496 available bytes; 82.42% used; 112443387 free inodes.

server1 `/home`: 315091562496 available bytes; 82.42% used; 112443387 free inodes.

server1 `/tmp`: 315091562496 available bytes; 82.42% used; 112443387 free inodes.

server1 `/var/tmp`: 315091562496 available bytes; 82.42% used; 112443387 free inodes.

server1 `/mnt/raid5`: 637263851520 available bytes; 97.08% used; 337401647 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17635598336 available bytes; 99.02% used; 110365000 free inodes.

server2 `/home`: 17635598336 available bytes; 99.02% used; 110365000 free inodes.

server2 `/tmp`: 17635598336 available bytes; 99.02% used; 110365000 free inodes.

server2 `/var/tmp`: 17635598336 available bytes; 99.02% used; 110365000 free inodes.

server2 `/mnt/raid5`: 581097320448 available bytes; 95.98% used; 444884905 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78709010432 available bytes; 95.61% used; 114062953 free inodes.

server3 `/home`: 78709010432 available bytes; 95.61% used; 114062953 free inodes.

server3 `/data`: 1337714552832 available bytes; 81.51% used; 225762405 free inodes.

server3 `/tmp`: 78709010432 available bytes; 95.61% used; 114062953 free inodes.

server3 `/var/tmp`: 78709010432 available bytes; 95.61% used; 114062953 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111036514304 available bytes; 93.80% used; 114373257 free inodes.

server4 `/home`: 111036514304 available bytes; 93.80% used; 114373257 free inodes.

server4 `/data`: 400312733696 available bytes; 94.47% used; 224781619 free inodes.

server4 `/tmp`: 111036514304 available bytes; 93.80% used; 114373257 free inodes.

server4 `/var/tmp`: 111036514304 available bytes; 93.80% used; 114373257 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
