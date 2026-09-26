# V2R cluster inventory

2026-09-26T03:18:22.846489+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318417178624 available bytes; 82.24% used; 112476258 free inodes.

server1 `/home`: 318417178624 available bytes; 82.24% used; 112476258 free inodes.

server1 `/tmp`: 318417178624 available bytes; 82.24% used; 112476258 free inodes.

server1 `/var/tmp`: 318417178624 available bytes; 82.24% used; 112476258 free inodes.

server1 `/mnt/raid5`: 331041226752 available bytes; 98.48% used; 337545863 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22935228416 available bytes; 98.72% used; 110406210 free inodes.

server2 `/home`: 22935228416 available bytes; 98.72% used; 110406210 free inodes.

server2 `/tmp`: 22935228416 available bytes; 98.72% used; 110406210 free inodes.

server2 `/var/tmp`: 22935228416 available bytes; 98.72% used; 110406210 free inodes.

server2 `/mnt/raid5`: 287574847488 available bytes; 98.01% used; 445052771 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84309417984 available bytes; 95.30% used; 114152358 free inodes.

server3 `/home`: 84309417984 available bytes; 95.30% used; 114152358 free inodes.

server3 `/data`: 125433495552 available bytes; 98.27% used; 225830809 free inodes.

server3 `/tmp`: 84309417984 available bytes; 95.30% used; 114152358 free inodes.

server3 `/var/tmp`: 84309417984 available bytes; 95.30% used; 114152358 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105918152704 available bytes; 94.09% used; 114347133 free inodes.

server4 `/home`: 105918152704 available bytes; 94.09% used; 114347133 free inodes.

server4 `/data`: 109003370496 available bytes; 98.49% used; 224914836 free inodes.

server4 `/tmp`: 105918152704 available bytes; 94.09% used; 114347133 free inodes.

server4 `/var/tmp`: 105918152704 available bytes; 94.09% used; 114347133 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
