# V2R cluster inventory

2026-09-26T23:55:37.462404+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315446484992 available bytes; 82.40% used; 112445732 free inodes.

server1 `/home`: 315446484992 available bytes; 82.40% used; 112445732 free inodes.

server1 `/tmp`: 315446484992 available bytes; 82.40% used; 112445732 free inodes.

server1 `/var/tmp`: 315446484992 available bytes; 82.40% used; 112445732 free inodes.

server1 `/mnt/raid5`: 637713981440 available bytes; 97.07% used; 337408378 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 17945313280 available bytes; 99.00% used; 110367452 free inodes.

server2 `/home`: 17945313280 available bytes; 99.00% used; 110367452 free inodes.

server2 `/tmp`: 17945313280 available bytes; 99.00% used; 110367452 free inodes.

server2 `/var/tmp`: 17945313280 available bytes; 99.00% used; 110367452 free inodes.

server2 `/mnt/raid5`: 594350411776 available bytes; 95.89% used; 444958810 free inodes.
| server3 | True | ['2', '3'] | [] | reference_compatible=True |

server3 `/`: 81081675776 available bytes; 95.48% used; 114069888 free inodes.

server3 `/home`: 81081675776 available bytes; 95.48% used; 114069888 free inodes.

server3 `/data`: 1349116841984 available bytes; 81.35% used; 225826117 free inodes.

server3 `/tmp`: 81081675776 available bytes; 95.48% used; 114069888 free inodes.

server3 `/var/tmp`: 81081675776 available bytes; 95.48% used; 114069888 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105880276992 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105880276992 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409580871680 available bytes; 94.34% used; 224823790 free inodes.

server4 `/tmp`: 105880276992 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105880276992 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
