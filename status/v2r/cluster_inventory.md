# V2R cluster inventory

2026-09-24T05:37:20.264320+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324533477376 available bytes; 81.90% used; 112492194 free inodes.

server1 `/home`: 324533477376 available bytes; 81.90% used; 112492194 free inodes.

server1 `/tmp`: 324533477376 available bytes; 81.90% used; 112492194 free inodes.

server1 `/var/tmp`: 324533477376 available bytes; 81.90% used; 112492194 free inodes.

server1 `/mnt/raid5`: 517632626688 available bytes; 97.63% used; 337723980 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57915179008 available bytes; 96.77% used; 110431350 free inodes.

server2 `/home`: 57915179008 available bytes; 96.77% used; 110431350 free inodes.

server2 `/tmp`: 57915179008 available bytes; 96.77% used; 110431350 free inodes.

server2 `/var/tmp`: 57915179008 available bytes; 96.77% used; 110431350 free inodes.

server2 `/mnt/raid5`: 522160402432 available bytes; 96.39% used; 445193917 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126963908608 available bytes; 92.91% used; 114191092 free inodes.

server3 `/home`: 126963908608 available bytes; 92.91% used; 114191092 free inodes.

server3 `/data`: 185260957696 available bytes; 97.44% used; 225839260 free inodes.

server3 `/tmp`: 126963908608 available bytes; 92.91% used; 114191092 free inodes.

server3 `/var/tmp`: 126963908608 available bytes; 92.91% used; 114191092 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105816764416 available bytes; 94.10% used; 114349365 free inodes.

server4 `/home`: 105816764416 available bytes; 94.10% used; 114349365 free inodes.

server4 `/data`: 251509063680 available bytes; 96.52% used; 225358067 free inodes.

server4 `/tmp`: 105816764416 available bytes; 94.10% used; 114349365 free inodes.

server4 `/var/tmp`: 105816764416 available bytes; 94.10% used; 114349365 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
