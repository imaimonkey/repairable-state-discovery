# V2R cluster inventory

2026-09-23T23:02:55.038656+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325742043136 available bytes; 81.83% used; 112501689 free inodes.

server1 `/home`: 325742043136 available bytes; 81.83% used; 112501689 free inodes.

server1 `/tmp`: 325742043136 available bytes; 81.83% used; 112501689 free inodes.

server1 `/var/tmp`: 325742043136 available bytes; 81.83% used; 112501689 free inodes.

server1 `/mnt/raid5`: 1379579457536 available bytes; 93.67% used; 337739787 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41059774464 available bytes; 97.71% used; 110432609 free inodes.

server2 `/home`: 41059774464 available bytes; 97.71% used; 110432609 free inodes.

server2 `/tmp`: 41059774464 available bytes; 97.71% used; 110432609 free inodes.

server2 `/var/tmp`: 41059774464 available bytes; 97.71% used; 110432609 free inodes.

server2 `/mnt/raid5`: 535306121216 available bytes; 96.30% used; 445205911 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292833083392 available bytes; 83.66% used; 114210815 free inodes.

server3 `/home`: 292833083392 available bytes; 83.66% used; 114210815 free inodes.

server3 `/data`: 82345271296 available bytes; 98.86% used; 225846618 free inodes.

server3 `/tmp`: 292833083392 available bytes; 83.66% used; 114210815 free inodes.

server3 `/var/tmp`: 292833083392 available bytes; 83.66% used; 114210815 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106290618368 available bytes; 94.07% used; 114353347 free inodes.

server4 `/home`: 106290618368 available bytes; 94.07% used; 114353347 free inodes.

server4 `/data`: 300066017280 available bytes; 95.85% used; 225431526 free inodes.

server4 `/tmp`: 106290618368 available bytes; 94.07% used; 114353347 free inodes.

server4 `/var/tmp`: 106290618368 available bytes; 94.07% used; 114353347 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
