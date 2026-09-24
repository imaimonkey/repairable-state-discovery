# V2R cluster inventory

2026-09-24T18:29:17.918572+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324006756352 available bytes; 81.92% used; 112481439 free inodes.

server1 `/home`: 324006756352 available bytes; 81.92% used; 112481439 free inodes.

server1 `/tmp`: 324006756352 available bytes; 81.92% used; 112481439 free inodes.

server1 `/var/tmp`: 324006756352 available bytes; 81.92% used; 112481439 free inodes.

server1 `/mnt/raid5`: 416321441792 available bytes; 98.09% used; 337639491 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 54490157056 available bytes; 96.96% used; 110411982 free inodes.

server2 `/home`: 54490157056 available bytes; 96.96% used; 110411982 free inodes.

server2 `/tmp`: 54490157056 available bytes; 96.96% used; 110411982 free inodes.

server2 `/var/tmp`: 54490157056 available bytes; 96.96% used; 110411982 free inodes.

server2 `/mnt/raid5`: 496775548928 available bytes; 96.57% used; 445160918 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84411105280 available bytes; 95.29% used; 114156134 free inodes.

server3 `/home`: 84411105280 available bytes; 95.29% used; 114156134 free inodes.

server3 `/data`: 152885403648 available bytes; 97.89% used; 225800560 free inodes.

server3 `/tmp`: 84411105280 available bytes; 95.29% used; 114156134 free inodes.

server3 `/var/tmp`: 84411105280 available bytes; 95.29% used; 114156134 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105662349312 available bytes; 94.10% used; 114348506 free inodes.

server4 `/home`: 105662349312 available bytes; 94.10% used; 114348506 free inodes.

server4 `/data`: 90049622016 available bytes; 98.76% used; 225267997 free inodes.

server4 `/tmp`: 105662349312 available bytes; 94.10% used; 114348506 free inodes.

server4 `/var/tmp`: 105662349312 available bytes; 94.10% used; 114348506 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
