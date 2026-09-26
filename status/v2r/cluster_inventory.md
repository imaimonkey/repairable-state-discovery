# V2R cluster inventory

2026-09-26T23:37:21.220734+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315460747264 available bytes; 82.40% used; 112445651 free inodes.

server1 `/home`: 315460747264 available bytes; 82.40% used; 112445651 free inodes.

server1 `/tmp`: 315460747264 available bytes; 82.40% used; 112445651 free inodes.

server1 `/var/tmp`: 315460747264 available bytes; 82.40% used; 112445651 free inodes.

server1 `/mnt/raid5`: 645840158720 available bytes; 97.04% used; 337467027 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 17939628032 available bytes; 99.00% used; 110367448 free inodes.

server2 `/home`: 17939628032 available bytes; 99.00% used; 110367448 free inodes.

server2 `/tmp`: 17939628032 available bytes; 99.00% used; 110367448 free inodes.

server2 `/var/tmp`: 17939628032 available bytes; 99.00% used; 110367448 free inodes.

server2 `/mnt/raid5`: 593789079552 available bytes; 95.90% used; 444959087 free inodes.
| server3 | True | ['2'] | [] | reference_compatible=True |

server3 `/`: 81080147968 available bytes; 95.48% used; 114069879 free inodes.

server3 `/home`: 81080147968 available bytes; 95.48% used; 114069879 free inodes.

server3 `/data`: 1349232242688 available bytes; 81.35% used; 225826325 free inodes.

server3 `/tmp`: 81080147968 available bytes; 95.48% used; 114069879 free inodes.

server3 `/var/tmp`: 81080147968 available bytes; 95.48% used; 114069879 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105889124352 available bytes; 94.09% used; 114347853 free inodes.

server4 `/home`: 105889124352 available bytes; 94.09% used; 114347853 free inodes.

server4 `/data`: 409590538240 available bytes; 94.34% used; 224823790 free inodes.

server4 `/tmp`: 105889124352 available bytes; 94.09% used; 114347853 free inodes.

server4 `/var/tmp`: 105889124352 available bytes; 94.09% used; 114347853 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
