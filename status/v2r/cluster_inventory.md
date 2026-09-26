# V2R cluster inventory

2026-09-26T20:37:38.906247+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315482849280 available bytes; 82.40% used; 112444688 free inodes.

server1 `/home`: 315482849280 available bytes; 82.40% used; 112444688 free inodes.

server1 `/tmp`: 315482849280 available bytes; 82.40% used; 112444688 free inodes.

server1 `/var/tmp`: 315482849280 available bytes; 82.40% used; 112444688 free inodes.

server1 `/mnt/raid5`: 645854777344 available bytes; 97.04% used; 337467121 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 17975955456 available bytes; 99.00% used; 110367101 free inodes.

server2 `/home`: 17975955456 available bytes; 99.00% used; 110367101 free inodes.

server2 `/tmp`: 17975955456 available bytes; 99.00% used; 110367101 free inodes.

server2 `/var/tmp`: 17975955456 available bytes; 99.00% used; 110367101 free inodes.

server2 `/mnt/raid5`: 599936356352 available bytes; 95.85% used; 444964582 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 81264209920 available bytes; 95.47% used; 114065289 free inodes.

server3 `/home`: 81264209920 available bytes; 95.47% used; 114065289 free inodes.

server3 `/data`: 1348612136960 available bytes; 81.36% used; 225831622 free inodes.

server3 `/tmp`: 81264209920 available bytes; 95.47% used; 114065289 free inodes.

server3 `/var/tmp`: 81264209920 available bytes; 95.47% used; 114065289 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105918885888 available bytes; 94.09% used; 114347838 free inodes.

server4 `/home`: 105918885888 available bytes; 94.09% used; 114347838 free inodes.

server4 `/data`: 410086457344 available bytes; 94.33% used; 224823711 free inodes.

server4 `/tmp`: 105918885888 available bytes; 94.09% used; 114347838 free inodes.

server4 `/var/tmp`: 105918885888 available bytes; 94.09% used; 114347838 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
