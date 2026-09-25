# V2R cluster inventory

2026-09-25T12:54:15.682327+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319110983680 available bytes; 82.20% used; 112477578 free inodes.

server1 `/home`: 319110983680 available bytes; 82.20% used; 112477578 free inodes.

server1 `/tmp`: 319110983680 available bytes; 82.20% used; 112477578 free inodes.

server1 `/var/tmp`: 319110983680 available bytes; 82.20% used; 112477578 free inodes.

server1 `/mnt/raid5`: 364476932096 available bytes; 98.33% used; 337547954 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] |

server2 `/`: 9277399040 available bytes; 99.48% used; 110408847 free inodes.

server2 `/home`: 9277399040 available bytes; 99.48% used; 110408847 free inodes.

server2 `/tmp`: 9277399040 available bytes; 99.48% used; 110408847 free inodes.

server2 `/var/tmp`: 9277399040 available bytes; 99.48% used; 110408847 free inodes.

server2 `/mnt/raid5`: 324506361856 available bytes; 97.76% used; 445078132 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84208377856 available bytes; 95.30% used; 114154974 free inodes.

server3 `/home`: 84208377856 available bytes; 95.30% used; 114154974 free inodes.

server3 `/data`: 142271983616 available bytes; 98.03% used; 225810825 free inodes.

server3 `/tmp`: 84208377856 available bytes; 95.30% used; 114154974 free inodes.

server3 `/var/tmp`: 84208377856 available bytes; 95.30% used; 114154974 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105665380352 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105665380352 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 232003833856 available bytes; 96.79% used; 224960873 free inodes.

server4 `/tmp`: 105665380352 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105665380352 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
