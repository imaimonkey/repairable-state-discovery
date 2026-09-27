# V2R cluster inventory

2026-09-27T10:07:44.018281+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314436489216 available bytes; 82.46% used; 112440699 free inodes.

server1 `/home`: 314436489216 available bytes; 82.46% used; 112440699 free inodes.

server1 `/tmp`: 314436489216 available bytes; 82.46% used; 112440699 free inodes.

server1 `/var/tmp`: 314436489216 available bytes; 82.46% used; 112440699 free inodes.

server1 `/mnt/raid5`: 635425959936 available bytes; 97.09% used; 337424412 free inodes.
| server2 | True | ['1', '2', '7'] | [] |

server2 `/`: 16507568128 available bytes; 99.08% used; 110356830 free inodes.

server2 `/home`: 16507568128 available bytes; 99.08% used; 110356830 free inodes.

server2 `/tmp`: 16507568128 available bytes; 99.08% used; 110356830 free inodes.

server2 `/var/tmp`: 16507568128 available bytes; 99.08% used; 110356830 free inodes.

server2 `/mnt/raid5`: 572501803008 available bytes; 96.04% used; 444740397 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 78543835136 available bytes; 95.62% used; 114062831 free inodes.

server3 `/home`: 78543835136 available bytes; 95.62% used; 114062831 free inodes.

server3 `/data`: 1332241281024 available bytes; 81.59% used; 225761430 free inodes.

server3 `/tmp`: 78543835136 available bytes; 95.62% used; 114062831 free inodes.

server3 `/var/tmp`: 78543835136 available bytes; 95.62% used; 114062831 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111049318400 available bytes; 93.80% used; 114372831 free inodes.

server4 `/home`: 111049318400 available bytes; 93.80% used; 114372831 free inodes.

server4 `/data`: 363918299136 available bytes; 94.97% used; 224767028 free inodes.

server4 `/tmp`: 111049318400 available bytes; 93.80% used; 114372831 free inodes.

server4 `/var/tmp`: 111049318400 available bytes; 93.80% used; 114372831 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
