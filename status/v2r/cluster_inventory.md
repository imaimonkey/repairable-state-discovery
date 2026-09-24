# V2R cluster inventory

2026-09-24T08:08:23.940609+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324409716736 available bytes; 81.90% used; 112490680 free inodes.

server1 `/home`: 324409716736 available bytes; 81.90% used; 112490680 free inodes.

server1 `/tmp`: 324409716736 available bytes; 81.90% used; 112490680 free inodes.

server1 `/var/tmp`: 324409716736 available bytes; 81.90% used; 112490680 free inodes.

server1 `/mnt/raid5`: 499505467392 available bytes; 97.71% used; 337721446 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57818480640 available bytes; 96.77% used; 110431050 free inodes.

server2 `/home`: 57818480640 available bytes; 96.77% used; 110431050 free inodes.

server2 `/tmp`: 57818480640 available bytes; 96.77% used; 110431050 free inodes.

server2 `/var/tmp`: 57818480640 available bytes; 96.77% used; 110431050 free inodes.

server2 `/mnt/raid5`: 517089464320 available bytes; 96.43% used; 445180194 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85483941888 available bytes; 95.23% used; 114175168 free inodes.

server3 `/home`: 85483941888 available bytes; 95.23% used; 114175168 free inodes.

server3 `/data`: 177692196864 available bytes; 97.54% used; 225838347 free inodes.

server3 `/tmp`: 85483941888 available bytes; 95.23% used; 114175168 free inodes.

server3 `/var/tmp`: 85483941888 available bytes; 95.23% used; 114175168 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105778851840 available bytes; 94.10% used; 114349157 free inodes.

server4 `/home`: 105778851840 available bytes; 94.10% used; 114349157 free inodes.

server4 `/data`: 284229316608 available bytes; 96.07% used; 225365952 free inodes.

server4 `/tmp`: 105778851840 available bytes; 94.10% used; 114349157 free inodes.

server4 `/var/tmp`: 105778851840 available bytes; 94.10% used; 114349157 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
