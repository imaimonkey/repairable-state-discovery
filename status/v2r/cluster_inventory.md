# V2R cluster inventory

2026-09-27T10:55:14.558748+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314432131072 available bytes; 82.46% used; 112440701 free inodes.

server1 `/home`: 314432131072 available bytes; 82.46% used; 112440701 free inodes.

server1 `/tmp`: 314432131072 available bytes; 82.46% used; 112440701 free inodes.

server1 `/var/tmp`: 314432131072 available bytes; 82.46% used; 112440701 free inodes.

server1 `/mnt/raid5`: 635403534336 available bytes; 97.09% used; 337424412 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16491565056 available bytes; 99.08% used; 110355934 free inodes.

server2 `/home`: 16491565056 available bytes; 99.08% used; 110355934 free inodes.

server2 `/tmp`: 16491565056 available bytes; 99.08% used; 110355934 free inodes.

server2 `/var/tmp`: 16491565056 available bytes; 99.08% used; 110355934 free inodes.

server2 `/mnt/raid5`: 571079356416 available bytes; 96.05% used; 444738176 free inodes.
| server3 | True | ['0', '2'] | [] | reference_compatible=True |

server3 `/`: 78545616896 available bytes; 95.62% used; 114062820 free inodes.

server3 `/home`: 78545616896 available bytes; 95.62% used; 114062820 free inodes.

server3 `/data`: 1332032983040 available bytes; 81.59% used; 225760569 free inodes.

server3 `/tmp`: 78545616896 available bytes; 95.62% used; 114062820 free inodes.

server3 `/var/tmp`: 78545616896 available bytes; 95.62% used; 114062820 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111031214080 available bytes; 93.80% used; 114372822 free inodes.

server4 `/home`: 111031214080 available bytes; 93.80% used; 114372822 free inodes.

server4 `/data`: 363066986496 available bytes; 94.98% used; 224766834 free inodes.

server4 `/tmp`: 111031214080 available bytes; 93.80% used; 114372822 free inodes.

server4 `/var/tmp`: 111031214080 available bytes; 93.80% used; 114372822 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
