# V2R cluster inventory

2026-09-27T00:07:48.461544+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315431137280 available bytes; 82.40% used; 112445714 free inodes.

server1 `/home`: 315431137280 available bytes; 82.40% used; 112445714 free inodes.

server1 `/tmp`: 315431137280 available bytes; 82.40% used; 112445714 free inodes.

server1 `/var/tmp`: 315431137280 available bytes; 82.40% used; 112445714 free inodes.

server1 `/mnt/raid5`: 637711683584 available bytes; 97.07% used; 337408131 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 17938182144 available bytes; 99.00% used; 110367426 free inodes.

server2 `/home`: 17938182144 available bytes; 99.00% used; 110367426 free inodes.

server2 `/tmp`: 17938182144 available bytes; 99.00% used; 110367426 free inodes.

server2 `/var/tmp`: 17938182144 available bytes; 99.00% used; 110367426 free inodes.

server2 `/mnt/raid5`: 593741762560 available bytes; 95.90% used; 444957941 free inodes.
| server3 | True | ['2', '3'] | [] | reference_compatible=True |

server3 `/`: 81071767552 available bytes; 95.48% used; 114069881 free inodes.

server3 `/home`: 81071767552 available bytes; 95.48% used; 114069881 free inodes.

server3 `/data`: 1349116796928 available bytes; 81.35% used; 225825942 free inodes.

server3 `/tmp`: 81071767552 available bytes; 95.48% used; 114069881 free inodes.

server3 `/var/tmp`: 81071767552 available bytes; 95.48% used; 114069881 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105879961600 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105879961600 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409570398208 available bytes; 94.34% used; 224823739 free inodes.

server4 `/tmp`: 105879961600 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105879961600 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
