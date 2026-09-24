# V2R cluster inventory

2026-09-24T19:50:58.653732+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323988746240 available bytes; 81.93% used; 112481465 free inodes.

server1 `/home`: 323988746240 available bytes; 81.93% used; 112481465 free inodes.

server1 `/tmp`: 323988746240 available bytes; 81.93% used; 112481465 free inodes.

server1 `/var/tmp`: 323988746240 available bytes; 81.93% used; 112481465 free inodes.

server1 `/mnt/raid5`: 415572656128 available bytes; 98.09% used; 337629936 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 39890624512 available bytes; 97.77% used; 110411576 free inodes.

server2 `/home`: 39890624512 available bytes; 97.77% used; 110411576 free inodes.

server2 `/tmp`: 39890624512 available bytes; 97.77% used; 110411576 free inodes.

server2 `/var/tmp`: 39890624512 available bytes; 97.77% used; 110411576 free inodes.

server2 `/mnt/raid5`: 494227406848 available bytes; 96.59% used; 445158068 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84400390144 available bytes; 95.29% used; 114156137 free inodes.

server3 `/home`: 84400390144 available bytes; 95.29% used; 114156137 free inodes.

server3 `/data`: 152072294400 available bytes; 97.90% used; 225799113 free inodes.

server3 `/tmp`: 84400390144 available bytes; 95.29% used; 114156137 free inodes.

server3 `/var/tmp`: 84400390144 available bytes; 95.29% used; 114156137 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105642020864 available bytes; 94.10% used; 114348426 free inodes.

server4 `/home`: 105642020864 available bytes; 94.10% used; 114348426 free inodes.

server4 `/data`: 89840316416 available bytes; 98.76% used; 225266464 free inodes.

server4 `/tmp`: 105642020864 available bytes; 94.10% used; 114348426 free inodes.

server4 `/var/tmp`: 105642020864 available bytes; 94.10% used; 114348426 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
