# V2R cluster inventory

2026-09-24T04:35:55.398628+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324629569536 available bytes; 81.89% used; 112492944 free inodes.

server1 `/home`: 324629569536 available bytes; 81.89% used; 112492944 free inodes.

server1 `/tmp`: 324629569536 available bytes; 81.89% used; 112492944 free inodes.

server1 `/var/tmp`: 324629569536 available bytes; 81.89% used; 112492944 free inodes.

server1 `/mnt/raid5`: 455315566592 available bytes; 97.91% used; 337724645 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40779034624 available bytes; 97.73% used; 110430506 free inodes.

server2 `/home`: 40779034624 available bytes; 97.73% used; 110430506 free inodes.

server2 `/tmp`: 40779034624 available bytes; 97.73% used; 110430506 free inodes.

server2 `/var/tmp`: 40779034624 available bytes; 97.73% used; 110430506 free inodes.

server2 `/mnt/raid5`: 524896096256 available bytes; 96.37% used; 445195748 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292002816000 available bytes; 83.71% used; 114176138 free inodes.

server3 `/home`: 292002816000 available bytes; 83.71% used; 114176138 free inodes.

server3 `/data`: 24376029184 available bytes; 99.66% used; 225840823 free inodes.

server3 `/tmp`: 292002816000 available bytes; 83.71% used; 114176138 free inodes.

server3 `/var/tmp`: 292002816000 available bytes; 83.71% used; 114176138 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105844228096 available bytes; 94.09% used; 114349416 free inodes.

server4 `/home`: 105844228096 available bytes; 94.09% used; 114349416 free inodes.

server4 `/data`: 253400317952 available bytes; 96.50% used; 225366885 free inodes.

server4 `/tmp`: 105844228096 available bytes; 94.09% used; 114349416 free inodes.

server4 `/var/tmp`: 105844228096 available bytes; 94.09% used; 114349416 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
