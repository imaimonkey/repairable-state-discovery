# V2R cluster inventory

2026-09-27T13:21:34.149293+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304672489472 available bytes; 83.00% used; 112401381 free inodes.

server1 `/home`: 304672489472 available bytes; 83.00% used; 112401381 free inodes.

server1 `/tmp`: 304672489472 available bytes; 83.00% used; 112401381 free inodes.

server1 `/var/tmp`: 304672489472 available bytes; 83.00% used; 112401381 free inodes.

server1 `/mnt/raid5`: 634577166336 available bytes; 97.09% used; 337424233 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 13416333312 available bytes; 99.25% used; 110351833 free inodes.

server2 `/home`: 13416333312 available bytes; 99.25% used; 110351833 free inodes.

server2 `/tmp`: 13416333312 available bytes; 99.25% used; 110351833 free inodes.

server2 `/var/tmp`: 13416333312 available bytes; 99.25% used; 110351833 free inodes.

server2 `/mnt/raid5`: 528982384640 available bytes; 96.34% used; 444733569 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78568222720 available bytes; 95.62% used; 114062841 free inodes.

server3 `/home`: 78568222720 available bytes; 95.62% used; 114062841 free inodes.

server3 `/data`: 1331278278656 available bytes; 81.60% used; 225757606 free inodes.

server3 `/tmp`: 78568222720 available bytes; 95.62% used; 114062841 free inodes.

server3 `/var/tmp`: 78568222720 available bytes; 95.62% used; 114062841 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111010652160 available bytes; 93.81% used; 114372796 free inodes.

server4 `/home`: 111010652160 available bytes; 93.81% used; 114372796 free inodes.

server4 `/data`: 351397113856 available bytes; 95.14% used; 224727747 free inodes.

server4 `/tmp`: 111010652160 available bytes; 93.81% used; 114372796 free inodes.

server4 `/var/tmp`: 111010652160 available bytes; 93.81% used; 114372796 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
