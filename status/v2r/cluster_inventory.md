# V2R cluster inventory

2026-09-24T06:26:54.829731+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324510892032 available bytes; 81.90% used; 112491696 free inodes.

server1 `/home`: 324510892032 available bytes; 81.90% used; 112491696 free inodes.

server1 `/tmp`: 324510892032 available bytes; 81.90% used; 112491696 free inodes.

server1 `/var/tmp`: 324510892032 available bytes; 81.90% used; 112491696 free inodes.

server1 `/mnt/raid5`: 517574131712 available bytes; 97.63% used; 337723765 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57882394624 available bytes; 96.77% used; 110431213 free inodes.

server2 `/home`: 57882394624 available bytes; 96.77% used; 110431213 free inodes.

server2 `/tmp`: 57882394624 available bytes; 96.77% used; 110431213 free inodes.

server2 `/var/tmp`: 57882394624 available bytes; 96.77% used; 110431213 free inodes.

server2 `/mnt/raid5`: 519814115328 available bytes; 96.41% used; 445192009 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 127210565632 available bytes; 92.90% used; 114199618 free inodes.

server3 `/home`: 127210565632 available bytes; 92.90% used; 114199618 free inodes.

server3 `/data`: 140535664640 available bytes; 98.06% used; 225835822 free inodes.

server3 `/tmp`: 127210565632 available bytes; 92.90% used; 114199618 free inodes.

server3 `/var/tmp`: 127210565632 available bytes; 92.90% used; 114199618 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105805631488 available bytes; 94.10% used; 114349280 free inodes.

server4 `/home`: 105805631488 available bytes; 94.10% used; 114349280 free inodes.

server4 `/data`: 330647691264 available bytes; 95.43% used; 225373143 free inodes.

server4 `/tmp`: 105805631488 available bytes; 94.10% used; 114349280 free inodes.

server4 `/var/tmp`: 105805631488 available bytes; 94.10% used; 114349280 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
