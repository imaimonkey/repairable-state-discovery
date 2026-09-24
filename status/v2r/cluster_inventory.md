# V2R cluster inventory

2026-09-24T17:43:01.027240+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324008050688 available bytes; 81.92% used; 112481440 free inodes.

server1 `/home`: 324008050688 available bytes; 81.92% used; 112481440 free inodes.

server1 `/tmp`: 324008050688 available bytes; 81.92% used; 112481440 free inodes.

server1 `/var/tmp`: 324008050688 available bytes; 81.92% used; 112481440 free inodes.

server1 `/mnt/raid5`: 416421056512 available bytes; 98.09% used; 337644872 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 56905609216 available bytes; 96.83% used; 110412385 free inodes.

server2 `/home`: 56905609216 available bytes; 96.83% used; 110412385 free inodes.

server2 `/tmp`: 56905609216 available bytes; 96.83% used; 110412385 free inodes.

server2 `/var/tmp`: 56905609216 available bytes; 96.83% used; 110412385 free inodes.

server2 `/mnt/raid5`: 497864097792 available bytes; 96.56% used; 445162070 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84408332288 available bytes; 95.29% used; 114156148 free inodes.

server3 `/home`: 84408332288 available bytes; 95.29% used; 114156148 free inodes.

server3 `/data`: 148739567616 available bytes; 97.94% used; 225786603 free inodes.

server3 `/tmp`: 84408332288 available bytes; 95.29% used; 114156148 free inodes.

server3 `/var/tmp`: 84408332288 available bytes; 95.29% used; 114156148 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105672634368 available bytes; 94.10% used; 114348559 free inodes.

server4 `/home`: 105672634368 available bytes; 94.10% used; 114348559 free inodes.

server4 `/data`: 89058578432 available bytes; 98.77% used; 225253753 free inodes.

server4 `/tmp`: 105672634368 available bytes; 94.10% used; 114348559 free inodes.

server4 `/var/tmp`: 105672634368 available bytes; 94.10% used; 114348559 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
