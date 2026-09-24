# V2R cluster inventory

2026-09-24T06:16:28.217972+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324514217984 available bytes; 81.90% used; 112491781 free inodes.

server1 `/home`: 324514217984 available bytes; 81.90% used; 112491781 free inodes.

server1 `/tmp`: 324514217984 available bytes; 81.90% used; 112491781 free inodes.

server1 `/var/tmp`: 324514217984 available bytes; 81.90% used; 112491781 free inodes.

server1 `/mnt/raid5`: 497716887552 available bytes; 97.72% used; 337723764 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57893376000 available bytes; 96.77% used; 110431243 free inodes.

server2 `/home`: 57893376000 available bytes; 96.77% used; 110431243 free inodes.

server2 `/tmp`: 57893376000 available bytes; 96.77% used; 110431243 free inodes.

server2 `/var/tmp`: 57893376000 available bytes; 96.77% used; 110431243 free inodes.

server2 `/mnt/raid5`: 520660221952 available bytes; 96.40% used; 445192352 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126776115200 available bytes; 92.93% used; 114173882 free inodes.

server3 `/home`: 126776115200 available bytes; 92.93% used; 114173882 free inodes.

server3 `/data`: 140618903552 available bytes; 98.06% used; 225836023 free inodes.

server3 `/tmp`: 126776115200 available bytes; 92.93% used; 114173882 free inodes.

server3 `/var/tmp`: 126776115200 available bytes; 92.93% used; 114173882 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105806368768 available bytes; 94.10% used; 114349319 free inodes.

server4 `/home`: 105806368768 available bytes; 94.10% used; 114349319 free inodes.

server4 `/data`: 338096365568 available bytes; 95.33% used; 225373731 free inodes.

server4 `/tmp`: 105806368768 available bytes; 94.10% used; 114349319 free inodes.

server4 `/var/tmp`: 105806368768 available bytes; 94.10% used; 114349319 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
