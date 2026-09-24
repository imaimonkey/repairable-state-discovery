# V2R cluster inventory

2026-09-24T10:31:23.586914+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324409069568 available bytes; 81.90% used; 112489257 free inodes.

server1 `/home`: 324409069568 available bytes; 81.90% used; 112489257 free inodes.

server1 `/tmp`: 324409069568 available bytes; 81.90% used; 112489257 free inodes.

server1 `/var/tmp`: 324409069568 available bytes; 81.90% used; 112489257 free inodes.

server1 `/mnt/raid5`: 500156387328 available bytes; 97.71% used; 337697682 free inodes.
| server2 | True | ['5'] | [] |

server2 `/`: 57732575232 available bytes; 96.78% used; 110430609 free inodes.

server2 `/home`: 57732575232 available bytes; 96.78% used; 110430609 free inodes.

server2 `/tmp`: 57732575232 available bytes; 96.78% used; 110430609 free inodes.

server2 `/var/tmp`: 57732575232 available bytes; 96.78% used; 110430609 free inodes.

server2 `/mnt/raid5`: 512748240896 available bytes; 96.46% used; 445175389 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85295284224 available bytes; 95.24% used; 114170280 free inodes.

server3 `/home`: 85295284224 available bytes; 95.24% used; 114170280 free inodes.

server3 `/data`: 164287655936 available bytes; 97.73% used; 225818222 free inodes.

server3 `/tmp`: 85295284224 available bytes; 95.24% used; 114170280 free inodes.

server3 `/var/tmp`: 85295284224 available bytes; 95.24% used; 114170280 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105744437248 available bytes; 94.10% used; 114348961 free inodes.

server4 `/home`: 105744437248 available bytes; 94.10% used; 114348961 free inodes.

server4 `/data`: 153476435968 available bytes; 97.88% used; 225258405 free inodes.

server4 `/tmp`: 105744437248 available bytes; 94.10% used; 114348961 free inodes.

server4 `/var/tmp`: 105744437248 available bytes; 94.10% used; 114348961 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
