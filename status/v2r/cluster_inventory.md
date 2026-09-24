# V2R cluster inventory

2026-09-24T08:14:37.777803+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324404965376 available bytes; 81.90% used; 112490627 free inodes.

server1 `/home`: 324404965376 available bytes; 81.90% used; 112490627 free inodes.

server1 `/tmp`: 324404965376 available bytes; 81.90% used; 112490627 free inodes.

server1 `/var/tmp`: 324404965376 available bytes; 81.90% used; 112490627 free inodes.

server1 `/mnt/raid5`: 496600350720 available bytes; 97.72% used; 337721360 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57817587712 available bytes; 96.77% used; 110431038 free inodes.

server2 `/home`: 57817587712 available bytes; 96.77% used; 110431038 free inodes.

server2 `/tmp`: 57817587712 available bytes; 96.77% used; 110431038 free inodes.

server2 `/var/tmp`: 57817587712 available bytes; 96.77% used; 110431038 free inodes.

server2 `/mnt/raid5`: 516638404608 available bytes; 96.43% used; 445180249 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85482729472 available bytes; 95.23% used; 114175164 free inodes.

server3 `/home`: 85482729472 available bytes; 95.23% used; 114175164 free inodes.

server3 `/data`: 175219023872 available bytes; 97.58% used; 225838108 free inodes.

server3 `/tmp`: 85482729472 available bytes; 95.23% used; 114175164 free inodes.

server3 `/var/tmp`: 85482729472 available bytes; 95.23% used; 114175164 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105778528256 available bytes; 94.10% used; 114349150 free inodes.

server4 `/home`: 105778528256 available bytes; 94.10% used; 114349150 free inodes.

server4 `/data`: 283889008640 available bytes; 96.08% used; 225365779 free inodes.

server4 `/tmp`: 105778528256 available bytes; 94.10% used; 114349150 free inodes.

server4 `/var/tmp`: 105778528256 available bytes; 94.10% used; 114349150 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
