# V2R cluster inventory

2026-09-25T13:34:20.967895+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319102038016 available bytes; 82.20% used; 112477540 free inodes.

server1 `/home`: 319102038016 available bytes; 82.20% used; 112477540 free inodes.

server1 `/tmp`: 319102038016 available bytes; 82.20% used; 112477540 free inodes.

server1 `/var/tmp`: 319102038016 available bytes; 82.20% used; 112477540 free inodes.

server1 `/mnt/raid5`: 364198363136 available bytes; 98.33% used; 337547753 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 15492534272 available bytes; 99.14% used; 110408597 free inodes.

server2 `/home`: 15492534272 available bytes; 99.14% used; 110408597 free inodes.

server2 `/tmp`: 15492534272 available bytes; 99.14% used; 110408597 free inodes.

server2 `/var/tmp`: 15492534272 available bytes; 99.14% used; 110408597 free inodes.

server2 `/mnt/raid5`: 323342585856 available bytes; 97.77% used; 445077345 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84199723008 available bytes; 95.30% used; 114154972 free inodes.

server3 `/home`: 84199723008 available bytes; 95.30% used; 114154972 free inodes.

server3 `/data`: 142348730368 available bytes; 98.03% used; 225809624 free inodes.

server3 `/tmp`: 84199723008 available bytes; 95.30% used; 114154972 free inodes.

server3 `/var/tmp`: 84199723008 available bytes; 95.30% used; 114154972 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105655861248 available bytes; 94.10% used; 114349714 free inodes.

server4 `/home`: 105655861248 available bytes; 94.10% used; 114349714 free inodes.

server4 `/data`: 231395315712 available bytes; 96.80% used; 224951410 free inodes.

server4 `/tmp`: 105655861248 available bytes; 94.10% used; 114349714 free inodes.

server4 `/var/tmp`: 105655861248 available bytes; 94.10% used; 114349714 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
