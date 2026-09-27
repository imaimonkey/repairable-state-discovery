# V2R cluster inventory

2026-09-27T07:56:56.062631+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314469941248 available bytes; 82.46% used; 112440784 free inodes.

server1 `/home`: 314469941248 available bytes; 82.46% used; 112440784 free inodes.

server1 `/tmp`: 314469941248 available bytes; 82.46% used; 112440784 free inodes.

server1 `/var/tmp`: 314469941248 available bytes; 82.46% used; 112440784 free inodes.

server1 `/mnt/raid5`: 634649694208 available bytes; 97.09% used; 337400004 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 17609646080 available bytes; 99.02% used; 110365015 free inodes.

server2 `/home`: 17609646080 available bytes; 99.02% used; 110365015 free inodes.

server2 `/tmp`: 17609646080 available bytes; 99.02% used; 110365015 free inodes.

server2 `/var/tmp`: 17609646080 available bytes; 99.02% used; 110365015 free inodes.

server2 `/mnt/raid5`: 570604384256 available bytes; 96.06% used; 444873239 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78573854720 available bytes; 95.62% used; 114062880 free inodes.

server3 `/home`: 78573854720 available bytes; 95.62% used; 114062880 free inodes.

server3 `/data`: 1332959653888 available bytes; 81.58% used; 225763784 free inodes.

server3 `/tmp`: 78573854720 available bytes; 95.62% used; 114062880 free inodes.

server3 `/var/tmp`: 78573854720 available bytes; 95.62% used; 114062880 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111069806592 available bytes; 93.80% used; 114372877 free inodes.

server4 `/home`: 111069806592 available bytes; 93.80% used; 114372877 free inodes.

server4 `/data`: 374271418368 available bytes; 94.83% used; 224770935 free inodes.

server4 `/tmp`: 111069806592 available bytes; 93.80% used; 114372877 free inodes.

server4 `/var/tmp`: 111069806592 available bytes; 93.80% used; 114372877 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
