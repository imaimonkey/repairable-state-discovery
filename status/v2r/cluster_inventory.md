# V2R cluster inventory

2026-09-24T23:26:49.088992+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319014023168 available bytes; 82.20% used; 112480779 free inodes.

server1 `/home`: 319014023168 available bytes; 82.20% used; 112480779 free inodes.

server1 `/tmp`: 319014023168 available bytes; 82.20% used; 112480779 free inodes.

server1 `/var/tmp`: 319014023168 available bytes; 82.20% used; 112480779 free inodes.

server1 `/mnt/raid5`: 415239647232 available bytes; 98.10% used; 337613600 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23110963200 available bytes; 98.71% used; 110410804 free inodes.

server2 `/home`: 23110963200 available bytes; 98.71% used; 110410804 free inodes.

server2 `/tmp`: 23110963200 available bytes; 98.71% used; 110410804 free inodes.

server2 `/var/tmp`: 23110963200 available bytes; 98.71% used; 110410804 free inodes.

server2 `/mnt/raid5`: 485974831104 available bytes; 96.64% used; 445151423 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84369752064 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84369752064 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 148331028480 available bytes; 97.95% used; 225800980 free inodes.

server3 `/tmp`: 84369752064 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84369752064 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105799671808 available bytes; 94.10% used; 114348305 free inodes.

server4 `/home`: 105799671808 available bytes; 94.10% used; 114348305 free inodes.

server4 `/data`: 61393526784 available bytes; 99.15% used; 225152061 free inodes.

server4 `/tmp`: 105799671808 available bytes; 94.10% used; 114348305 free inodes.

server4 `/var/tmp`: 105799671808 available bytes; 94.10% used; 114348305 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
