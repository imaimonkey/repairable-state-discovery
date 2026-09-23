# V2R cluster inventory

2026-09-23T22:36:18.384694+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325696225280 available bytes; 81.83% used; 112501395 free inodes.

server1 `/home`: 325696225280 available bytes; 81.83% used; 112501395 free inodes.

server1 `/tmp`: 325696225280 available bytes; 81.83% used; 112501395 free inodes.

server1 `/var/tmp`: 325696225280 available bytes; 81.83% used; 112501395 free inodes.

server1 `/mnt/raid5`: 1388098289664 available bytes; 93.63% used; 337739821 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41083879424 available bytes; 97.71% used; 110432631 free inodes.

server2 `/home`: 41083879424 available bytes; 97.71% used; 110432631 free inodes.

server2 `/tmp`: 41083879424 available bytes; 97.71% used; 110432631 free inodes.

server2 `/var/tmp`: 41083879424 available bytes; 97.71% used; 110432631 free inodes.

server2 `/mnt/raid5`: 536446885888 available bytes; 96.29% used; 445206363 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292862083072 available bytes; 83.66% used; 114216381 free inodes.

server3 `/home`: 292862083072 available bytes; 83.66% used; 114216381 free inodes.

server3 `/data`: 82432110592 available bytes; 98.86% used; 225847245 free inodes.

server3 `/tmp`: 292862083072 available bytes; 83.66% used; 114216381 free inodes.

server3 `/var/tmp`: 292862083072 available bytes; 83.66% used; 114216381 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106359382016 available bytes; 94.06% used; 114354311 free inodes.

server4 `/home`: 106359382016 available bytes; 94.06% used; 114354311 free inodes.

server4 `/data`: 300066951168 available bytes; 95.85% used; 225436028 free inodes.

server4 `/tmp`: 106359382016 available bytes; 94.06% used; 114354311 free inodes.

server4 `/var/tmp`: 106359382016 available bytes; 94.06% used; 114354311 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
