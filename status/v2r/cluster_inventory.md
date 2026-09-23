# V2R cluster inventory

2026-09-23T22:41:21.649925+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325721382912 available bytes; 81.83% used; 112501558 free inodes.

server1 `/home`: 325721382912 available bytes; 81.83% used; 112501558 free inodes.

server1 `/tmp`: 325721382912 available bytes; 81.83% used; 112501558 free inodes.

server1 `/var/tmp`: 325721382912 available bytes; 81.83% used; 112501558 free inodes.

server1 `/mnt/raid5`: 1388120690688 available bytes; 93.63% used; 337739976 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41076318208 available bytes; 97.71% used; 110432622 free inodes.

server2 `/home`: 41076318208 available bytes; 97.71% used; 110432622 free inodes.

server2 `/tmp`: 41076318208 available bytes; 97.71% used; 110432622 free inodes.

server2 `/var/tmp`: 41076318208 available bytes; 97.71% used; 110432622 free inodes.

server2 `/mnt/raid5`: 536314003456 available bytes; 96.29% used; 445206523 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293044699136 available bytes; 83.65% used; 114223393 free inodes.

server3 `/home`: 293044699136 available bytes; 83.65% used; 114223393 free inodes.

server3 `/data`: 82451406848 available bytes; 98.86% used; 225847329 free inodes.

server3 `/tmp`: 293044699136 available bytes; 83.65% used; 114223393 free inodes.

server3 `/var/tmp`: 293044699136 available bytes; 83.65% used; 114223393 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106347831296 available bytes; 94.07% used; 114354127 free inodes.

server4 `/home`: 106347831296 available bytes; 94.07% used; 114354127 free inodes.

server4 `/data`: 300096294912 available bytes; 95.85% used; 225435449 free inodes.

server4 `/tmp`: 106347831296 available bytes; 94.07% used; 114354127 free inodes.

server4 `/var/tmp`: 106347831296 available bytes; 94.07% used; 114354127 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
