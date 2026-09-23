# V2R cluster inventory

2026-09-23T23:11:40.724710+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325671899136 available bytes; 81.83% used; 112501634 free inodes.

server1 `/home`: 325671899136 available bytes; 81.83% used; 112501634 free inodes.

server1 `/tmp`: 325671899136 available bytes; 81.83% used; 112501634 free inodes.

server1 `/var/tmp`: 325671899136 available bytes; 81.83% used; 112501634 free inodes.

server1 `/mnt/raid5`: 1387992842240 available bytes; 93.63% used; 337739774 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41059999744 available bytes; 97.71% used; 110432611 free inodes.

server2 `/home`: 41059999744 available bytes; 97.71% used; 110432611 free inodes.

server2 `/tmp`: 41059999744 available bytes; 97.71% used; 110432611 free inodes.

server2 `/var/tmp`: 41059999744 available bytes; 97.71% used; 110432611 free inodes.

server2 `/mnt/raid5`: 535062896640 available bytes; 96.30% used; 445206290 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292243681280 available bytes; 83.69% used; 114168235 free inodes.

server3 `/home`: 292243681280 available bytes; 83.69% used; 114168235 free inodes.

server3 `/data`: 82340286464 available bytes; 98.86% used; 225846418 free inodes.

server3 `/tmp`: 292243681280 available bytes; 83.69% used; 114168235 free inodes.

server3 `/var/tmp`: 292243681280 available bytes; 83.69% used; 114168235 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106270785536 available bytes; 94.07% used; 114353031 free inodes.

server4 `/home`: 106270785536 available bytes; 94.07% used; 114353031 free inodes.

server4 `/data`: 300040482816 available bytes; 95.85% used; 225429959 free inodes.

server4 `/tmp`: 106270785536 available bytes; 94.07% used; 114353031 free inodes.

server4 `/var/tmp`: 106270785536 available bytes; 94.07% used; 114353031 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
