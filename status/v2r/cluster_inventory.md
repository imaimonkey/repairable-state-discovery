# V2R cluster inventory

2026-09-27T10:59:48.744036+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314430234624 available bytes; 82.46% used; 112440693 free inodes.

server1 `/home`: 314430234624 available bytes; 82.46% used; 112440693 free inodes.

server1 `/tmp`: 314430234624 available bytes; 82.46% used; 112440693 free inodes.

server1 `/var/tmp`: 314430234624 available bytes; 82.46% used; 112440693 free inodes.

server1 `/mnt/raid5`: 635401547776 available bytes; 97.09% used; 337424412 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16490627072 available bytes; 99.08% used; 110355928 free inodes.

server2 `/home`: 16490627072 available bytes; 99.08% used; 110355928 free inodes.

server2 `/tmp`: 16490627072 available bytes; 99.08% used; 110355928 free inodes.

server2 `/var/tmp`: 16490627072 available bytes; 99.08% used; 110355928 free inodes.

server2 `/mnt/raid5`: 570953732096 available bytes; 96.05% used; 444737925 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78543544320 available bytes; 95.62% used; 114062818 free inodes.

server3 `/home`: 78543544320 available bytes; 95.62% used; 114062818 free inodes.

server3 `/data`: 1332031131648 available bytes; 81.59% used; 225760504 free inodes.

server3 `/tmp`: 78543544320 available bytes; 95.62% used; 114062818 free inodes.

server3 `/var/tmp`: 78543544320 available bytes; 95.62% used; 114062818 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111031074816 available bytes; 93.80% used; 114372822 free inodes.

server4 `/home`: 111031074816 available bytes; 93.80% used; 114372822 free inodes.

server4 `/data`: 362972413952 available bytes; 94.98% used; 224766823 free inodes.

server4 `/tmp`: 111031074816 available bytes; 93.80% used; 114372822 free inodes.

server4 `/var/tmp`: 111031074816 available bytes; 93.80% used; 114372822 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
