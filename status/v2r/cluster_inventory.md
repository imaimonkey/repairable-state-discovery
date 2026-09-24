# V2R cluster inventory

2026-09-24T10:12:45.493675+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324423229440 available bytes; 81.90% used; 112489416 free inodes.

server1 `/home`: 324423229440 available bytes; 81.90% used; 112489416 free inodes.

server1 `/tmp`: 324423229440 available bytes; 81.90% used; 112489416 free inodes.

server1 `/var/tmp`: 324423229440 available bytes; 81.90% used; 112489416 free inodes.

server1 `/mnt/raid5`: 500656173056 available bytes; 97.70% used; 337699874 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57744183296 available bytes; 96.78% used; 110430705 free inodes.

server2 `/home`: 57744183296 available bytes; 96.78% used; 110430705 free inodes.

server2 `/tmp`: 57744183296 available bytes; 96.78% used; 110430705 free inodes.

server2 `/var/tmp`: 57744183296 available bytes; 96.78% used; 110430705 free inodes.

server2 `/mnt/raid5`: 513255579648 available bytes; 96.45% used; 445175882 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85368832000 available bytes; 95.24% used; 114173537 free inodes.

server3 `/home`: 85368832000 available bytes; 95.24% used; 114173537 free inodes.

server3 `/data`: 164427927552 available bytes; 97.73% used; 225819011 free inodes.

server3 `/tmp`: 85368832000 available bytes; 95.24% used; 114173537 free inodes.

server3 `/var/tmp`: 85368832000 available bytes; 95.24% used; 114173537 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105747410944 available bytes; 94.10% used; 114349000 free inodes.

server4 `/home`: 105747410944 available bytes; 94.10% used; 114349000 free inodes.

server4 `/data`: 153493979136 available bytes; 97.88% used; 225258622 free inodes.

server4 `/tmp`: 105747410944 available bytes; 94.10% used; 114349000 free inodes.

server4 `/var/tmp`: 105747410944 available bytes; 94.10% used; 114349000 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
