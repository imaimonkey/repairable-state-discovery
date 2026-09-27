# V2R cluster inventory

2026-09-27T10:15:38.157737+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314436513792 available bytes; 82.46% used; 112440680 free inodes.

server1 `/home`: 314436513792 available bytes; 82.46% used; 112440680 free inodes.

server1 `/tmp`: 314436513792 available bytes; 82.46% used; 112440680 free inodes.

server1 `/var/tmp`: 314436513792 available bytes; 82.46% used; 112440680 free inodes.

server1 `/mnt/raid5`: 635420909568 available bytes; 97.09% used; 337424412 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16504590336 available bytes; 99.08% used; 110356611 free inodes.

server2 `/home`: 16504590336 available bytes; 99.08% used; 110356611 free inodes.

server2 `/tmp`: 16504590336 available bytes; 99.08% used; 110356611 free inodes.

server2 `/var/tmp`: 16504590336 available bytes; 99.08% used; 110356611 free inodes.

server2 `/mnt/raid5`: 572205191168 available bytes; 96.05% used; 444739591 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78544609280 available bytes; 95.62% used; 114062830 free inodes.

server3 `/home`: 78544609280 available bytes; 95.62% used; 114062830 free inodes.

server3 `/data`: 1332211601408 available bytes; 81.59% used; 225761200 free inodes.

server3 `/tmp`: 78544609280 available bytes; 95.62% used; 114062830 free inodes.

server3 `/var/tmp`: 78544609280 available bytes; 95.62% used; 114062830 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111049068544 available bytes; 93.80% used; 114372831 free inodes.

server4 `/home`: 111049068544 available bytes; 93.80% used; 114372831 free inodes.

server4 `/data`: 363778375680 available bytes; 94.97% used; 224766938 free inodes.

server4 `/tmp`: 111049068544 available bytes; 93.80% used; 114372831 free inodes.

server4 `/var/tmp`: 111049068544 available bytes; 93.80% used; 114372831 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
