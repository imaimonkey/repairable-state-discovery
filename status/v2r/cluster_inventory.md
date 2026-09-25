# V2R cluster inventory

2026-09-25T04:34:31.429740+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318929555456 available bytes; 82.21% used; 112480368 free inodes.

server1 `/home`: 318929555456 available bytes; 82.21% used; 112480368 free inodes.

server1 `/tmp`: 318929555456 available bytes; 82.21% used; 112480368 free inodes.

server1 `/var/tmp`: 318929555456 available bytes; 82.21% used; 112480368 free inodes.

server1 `/mnt/raid5`: 408724348928 available bytes; 98.13% used; 337591179 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22947364864 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22947364864 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22947364864 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22947364864 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 462359867392 available bytes; 96.81% used; 445109807 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84340830208 available bytes; 95.29% used; 114156078 free inodes.

server3 `/home`: 84340830208 available bytes; 95.29% used; 114156078 free inodes.

server3 `/data`: 143445807104 available bytes; 98.02% used; 225816066 free inodes.

server3 `/tmp`: 84340830208 available bytes; 95.29% used; 114156078 free inodes.

server3 `/var/tmp`: 84340830208 available bytes; 95.29% used; 114156078 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105671299072 available bytes; 94.10% used; 114350865 free inodes.

server4 `/home`: 105671299072 available bytes; 94.10% used; 114350865 free inodes.

server4 `/data`: 32789020672 available bytes; 99.55% used; 224962734 free inodes.

server4 `/tmp`: 105671299072 available bytes; 94.10% used; 114350865 free inodes.

server4 `/var/tmp`: 105671299072 available bytes; 94.10% used; 114350865 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
