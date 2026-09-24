# V2R cluster inventory

2026-09-24T08:02:09.777933+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324413374464 available bytes; 81.90% used; 112490746 free inodes.

server1 `/home`: 324413374464 available bytes; 81.90% used; 112490746 free inodes.

server1 `/tmp`: 324413374464 available bytes; 81.90% used; 112490746 free inodes.

server1 `/var/tmp`: 324413374464 available bytes; 81.90% used; 112490746 free inodes.

server1 `/mnt/raid5`: 503976787968 available bytes; 97.69% used; 337721967 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57826635776 available bytes; 96.77% used; 110431068 free inodes.

server2 `/home`: 57826635776 available bytes; 96.77% used; 110431068 free inodes.

server2 `/tmp`: 57826635776 available bytes; 96.77% used; 110431068 free inodes.

server2 `/var/tmp`: 57826635776 available bytes; 96.77% used; 110431068 free inodes.

server2 `/mnt/raid5`: 517280788480 available bytes; 96.43% used; 445180494 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85483900928 available bytes; 95.23% used; 114175159 free inodes.

server3 `/home`: 85483900928 available bytes; 95.23% used; 114175159 free inodes.

server3 `/data`: 177823248384 available bytes; 97.54% used; 225838867 free inodes.

server3 `/tmp`: 85483900928 available bytes; 95.23% used; 114175159 free inodes.

server3 `/var/tmp`: 85483900928 available bytes; 95.23% used; 114175159 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779105792 available bytes; 94.10% used; 114349157 free inodes.

server4 `/home`: 105779105792 available bytes; 94.10% used; 114349157 free inodes.

server4 `/data`: 284233326592 available bytes; 96.07% used; 225366050 free inodes.

server4 `/tmp`: 105779105792 available bytes; 94.10% used; 114349157 free inodes.

server4 `/var/tmp`: 105779105792 available bytes; 94.10% used; 114349157 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
