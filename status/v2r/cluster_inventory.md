# V2R cluster inventory

2026-09-24T03:57:50.012273+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324731998208 available bytes; 81.88% used; 112493612 free inodes.

server1 `/home`: 324731998208 available bytes; 81.88% used; 112493612 free inodes.

server1 `/tmp`: 324731998208 available bytes; 81.88% used; 112493612 free inodes.

server1 `/var/tmp`: 324731998208 available bytes; 81.88% used; 112493612 free inodes.

server1 `/mnt/raid5`: 416641425408 available bytes; 98.09% used; 337724788 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40813744128 available bytes; 97.72% used; 110430892 free inodes.

server2 `/home`: 40813744128 available bytes; 97.72% used; 110430892 free inodes.

server2 `/tmp`: 40813744128 available bytes; 97.72% used; 110430892 free inodes.

server2 `/var/tmp`: 40813744128 available bytes; 97.72% used; 110430892 free inodes.

server2 `/mnt/raid5`: 525844357120 available bytes; 96.37% used; 445197204 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292382887936 available bytes; 83.68% used; 114201257 free inodes.

server3 `/home`: 292382887936 available bytes; 83.68% used; 114201257 free inodes.

server3 `/data`: 33866772480 available bytes; 99.53% used; 225842438 free inodes.

server3 `/tmp`: 292382887936 available bytes; 83.68% used; 114201257 free inodes.

server3 `/var/tmp`: 292382887936 available bytes; 83.68% used; 114201257 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105791504384 available bytes; 94.10% used; 114349507 free inodes.

server4 `/home`: 105791504384 available bytes; 94.10% used; 114349507 free inodes.

server4 `/data`: 258348433408 available bytes; 96.43% used; 225382433 free inodes.

server4 `/tmp`: 105791504384 available bytes; 94.10% used; 114349507 free inodes.

server4 `/var/tmp`: 105791504384 available bytes; 94.10% used; 114349507 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
