# V2R cluster inventory

2026-09-27T04:31:20.482288+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314905726976 available bytes; 82.43% used; 112443031 free inodes.

server1 `/home`: 314905726976 available bytes; 82.43% used; 112443031 free inodes.

server1 `/tmp`: 314905726976 available bytes; 82.43% used; 112443031 free inodes.

server1 `/var/tmp`: 314905726976 available bytes; 82.43% used; 112443031 free inodes.

server1 `/mnt/raid5`: 636063903744 available bytes; 97.08% used; 337400343 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17622937600 available bytes; 99.02% used; 110365001 free inodes.

server2 `/home`: 17622937600 available bytes; 99.02% used; 110365001 free inodes.

server2 `/tmp`: 17622937600 available bytes; 99.02% used; 110365001 free inodes.

server2 `/var/tmp`: 17622937600 available bytes; 99.02% used; 110365001 free inodes.

server2 `/mnt/raid5`: 576258207744 available bytes; 96.02% used; 444879584 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78695862272 available bytes; 95.61% used; 114062929 free inodes.

server3 `/home`: 78695862272 available bytes; 95.61% used; 114062929 free inodes.

server3 `/data`: 1335096381440 available bytes; 81.55% used; 225759179 free inodes.

server3 `/tmp`: 78695862272 available bytes; 95.61% used; 114062929 free inodes.

server3 `/var/tmp`: 78695862272 available bytes; 95.61% used; 114062929 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111018098688 available bytes; 93.80% used; 114372937 free inodes.

server4 `/home`: 111018098688 available bytes; 93.80% used; 114372937 free inodes.

server4 `/data`: 382133563392 available bytes; 94.72% used; 224780561 free inodes.

server4 `/tmp`: 111018098688 available bytes; 93.80% used; 114372937 free inodes.

server4 `/var/tmp`: 111018098688 available bytes; 93.80% used; 114372937 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
