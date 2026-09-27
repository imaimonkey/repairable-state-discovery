# V2R cluster inventory

2026-09-27T12:15:50.495169+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 304683888640 available bytes; 83.00% used; 112401434 free inodes.

server1 `/home`: 304683888640 available bytes; 83.00% used; 112401434 free inodes.

server1 `/tmp`: 304683888640 available bytes; 83.00% used; 112401434 free inodes.

server1 `/var/tmp`: 304683888640 available bytes; 83.00% used; 112401434 free inodes.

server1 `/mnt/raid5`: 634668470272 available bytes; 97.09% used; 337424351 free inodes.
| server2 | True | ['1', '2', '7'] | [] |

server2 `/`: 16405745664 available bytes; 99.08% used; 110352868 free inodes.

server2 `/home`: 16405745664 available bytes; 99.08% used; 110352868 free inodes.

server2 `/tmp`: 16405745664 available bytes; 99.08% used; 110352868 free inodes.

server2 `/var/tmp`: 16405745664 available bytes; 99.08% used; 110352868 free inodes.

server2 `/mnt/raid5`: 567765716992 available bytes; 96.08% used; 444735416 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 78543716352 available bytes; 95.62% used; 114062866 free inodes.

server3 `/home`: 78543716352 available bytes; 95.62% used; 114062866 free inodes.

server3 `/data`: 1331794096128 available bytes; 81.59% used; 225758486 free inodes.

server3 `/tmp`: 78543716352 available bytes; 95.62% used; 114062866 free inodes.

server3 `/var/tmp`: 78543716352 available bytes; 95.62% used; 114062866 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111028981760 available bytes; 93.80% used; 114372805 free inodes.

server4 `/home`: 111028981760 available bytes; 93.80% used; 114372805 free inodes.

server4 `/data`: 352513908736 available bytes; 95.13% used; 224727935 free inodes.

server4 `/tmp`: 111028981760 available bytes; 93.80% used; 114372805 free inodes.

server4 `/var/tmp`: 111028981760 available bytes; 93.80% used; 114372805 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
