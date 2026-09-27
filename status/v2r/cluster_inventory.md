# V2R cluster inventory

2026-09-27T12:17:30.621414+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304683458560 available bytes; 83.00% used; 112401422 free inodes.

server1 `/home`: 304683458560 available bytes; 83.00% used; 112401422 free inodes.

server1 `/tmp`: 304683458560 available bytes; 83.00% used; 112401422 free inodes.

server1 `/var/tmp`: 304683458560 available bytes; 83.00% used; 112401422 free inodes.

server1 `/mnt/raid5`: 634665058304 available bytes; 97.09% used; 337424239 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16413573120 available bytes; 99.08% used; 110352868 free inodes.

server2 `/home`: 16413573120 available bytes; 99.08% used; 110352868 free inodes.

server2 `/tmp`: 16413573120 available bytes; 99.08% used; 110352868 free inodes.

server2 `/var/tmp`: 16413573120 available bytes; 99.08% used; 110352868 free inodes.

server2 `/mnt/raid5`: 568254156800 available bytes; 96.07% used; 444735372 free inodes.
| server3 | True | ['0', '2'] | [] | reference_compatible=True |

server3 `/`: 78543712256 available bytes; 95.62% used; 114062865 free inodes.

server3 `/home`: 78543712256 available bytes; 95.62% used; 114062865 free inodes.

server3 `/data`: 1331773583360 available bytes; 81.59% used; 225758450 free inodes.

server3 `/tmp`: 78543712256 available bytes; 95.62% used; 114062865 free inodes.

server3 `/var/tmp`: 78543712256 available bytes; 95.62% used; 114062865 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111028928512 available bytes; 93.80% used; 114372805 free inodes.

server4 `/home`: 111028928512 available bytes; 93.80% used; 114372805 free inodes.

server4 `/data`: 352511782912 available bytes; 95.13% used; 224727923 free inodes.

server4 `/tmp`: 111028928512 available bytes; 93.80% used; 114372805 free inodes.

server4 `/var/tmp`: 111028928512 available bytes; 93.80% used; 114372805 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
