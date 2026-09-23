# V2R cluster inventory

2026-09-23T21:04:18.973629+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325722972160 available bytes; 81.83% used; 112501612 free inodes.

server1 `/home`: 325722972160 available bytes; 81.83% used; 112501612 free inodes.

server1 `/tmp`: 325722972160 available bytes; 81.83% used; 112501612 free inodes.

server1 `/var/tmp`: 325722972160 available bytes; 81.83% used; 112501612 free inodes.

server1 `/mnt/raid5`: 1388139040768 available bytes; 93.63% used; 337739996 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41122418688 available bytes; 97.71% used; 110432717 free inodes.

server2 `/home`: 41122418688 available bytes; 97.71% used; 110432717 free inodes.

server2 `/tmp`: 41122418688 available bytes; 97.71% used; 110432717 free inodes.

server2 `/var/tmp`: 41122418688 available bytes; 97.71% used; 110432717 free inodes.

server2 `/mnt/raid5`: 539305959424 available bytes; 96.27% used; 445209669 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293462544384 available bytes; 83.62% used; 114236957 free inodes.

server3 `/home`: 293462544384 available bytes; 83.62% used; 114236957 free inodes.

server3 `/data`: 52320251904 available bytes; 99.28% used; 225849705 free inodes.

server3 `/tmp`: 293462544384 available bytes; 83.62% used; 114236957 free inodes.

server3 `/var/tmp`: 293462544384 available bytes; 83.62% used; 114236957 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106497335296 available bytes; 94.06% used; 114356055 free inodes.

server4 `/home`: 106497335296 available bytes; 94.06% used; 114356055 free inodes.

server4 `/data`: 300540784640 available bytes; 95.85% used; 225456191 free inodes.

server4 `/tmp`: 106497335296 available bytes; 94.06% used; 114356055 free inodes.

server4 `/var/tmp`: 106497335296 available bytes; 94.06% used; 114356055 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
