# V2R cluster inventory

2026-09-24T22:33:02.994151+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 323946164224 available bytes; 81.93% used; 112481422 free inodes.

server1 `/home`: 323946164224 available bytes; 81.93% used; 112481422 free inodes.

server1 `/tmp`: 323946164224 available bytes; 81.93% used; 112481422 free inodes.

server1 `/var/tmp`: 323946164224 available bytes; 81.93% used; 112481422 free inodes.

server1 `/mnt/raid5`: 415370788864 available bytes; 98.09% used; 337619991 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23189925888 available bytes; 98.71% used; 110410928 free inodes.

server2 `/home`: 23189925888 available bytes; 98.71% used; 110410928 free inodes.

server2 `/tmp`: 23189925888 available bytes; 98.71% used; 110410928 free inodes.

server2 `/var/tmp`: 23189925888 available bytes; 98.71% used; 110410928 free inodes.

server2 `/mnt/raid5`: 488451510272 available bytes; 96.62% used; 445152952 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84379365376 available bytes; 95.29% used; 114156083 free inodes.

server3 `/home`: 84379365376 available bytes; 95.29% used; 114156083 free inodes.

server3 `/data`: 149254078464 available bytes; 97.94% used; 225802025 free inodes.

server3 `/tmp`: 84379365376 available bytes; 95.29% used; 114156083 free inodes.

server3 `/var/tmp`: 84379365376 available bytes; 95.29% used; 114156083 free inodes.
| server4 | True | ['0', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105801826304 available bytes; 94.10% used; 114348327 free inodes.

server4 `/home`: 105801826304 available bytes; 94.10% used; 114348327 free inodes.

server4 `/data`: 73258823680 available bytes; 98.99% used; 225224785 free inodes.

server4 `/tmp`: 105801826304 available bytes; 94.10% used; 114348327 free inodes.

server4 `/var/tmp`: 105801826304 available bytes; 94.10% used; 114348327 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
