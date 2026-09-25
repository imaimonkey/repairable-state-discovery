# V2R cluster inventory

2026-09-25T21:08:33.638374+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318697672704 available bytes; 82.22% used; 112476323 free inodes.

server1 `/home`: 318697672704 available bytes; 82.22% used; 112476323 free inodes.

server1 `/tmp`: 318697672704 available bytes; 82.22% used; 112476323 free inodes.

server1 `/var/tmp`: 318697672704 available bytes; 82.22% used; 112476323 free inodes.

server1 `/mnt/raid5`: 368603471872 available bytes; 98.31% used; 337539494 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22889447424 available bytes; 98.72% used; 110405680 free inodes.

server2 `/home`: 22889447424 available bytes; 98.72% used; 110405680 free inodes.

server2 `/tmp`: 22889447424 available bytes; 98.72% used; 110405680 free inodes.

server2 `/var/tmp`: 22889447424 available bytes; 98.72% used; 110405680 free inodes.

server2 `/mnt/raid5`: 302164779008 available bytes; 97.91% used; 445055716 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84366163968 available bytes; 95.29% used; 114152624 free inodes.

server3 `/home`: 84366163968 available bytes; 95.29% used; 114152624 free inodes.

server3 `/data`: 125906051072 available bytes; 98.26% used; 225807339 free inodes.

server3 `/tmp`: 84366163968 available bytes; 95.29% used; 114152624 free inodes.

server3 `/var/tmp`: 84366163968 available bytes; 95.29% used; 114152624 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105388175360 available bytes; 94.12% used; 114347327 free inodes.

server4 `/home`: 105388175360 available bytes; 94.12% used; 114347327 free inodes.

server4 `/data`: 218508275712 available bytes; 96.98% used; 224920839 free inodes.

server4 `/tmp`: 105388175360 available bytes; 94.12% used; 114347327 free inodes.

server4 `/var/tmp`: 105388175360 available bytes; 94.12% used; 114347327 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
