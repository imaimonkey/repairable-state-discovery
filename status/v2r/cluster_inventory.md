# V2R cluster inventory

2026-09-24T12:27:10.974499+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324055506944 available bytes; 81.92% used; 112481551 free inodes.

server1 `/home`: 324055506944 available bytes; 81.92% used; 112481551 free inodes.

server1 `/tmp`: 324055506944 available bytes; 81.92% used; 112481551 free inodes.

server1 `/var/tmp`: 324055506944 available bytes; 81.92% used; 112481551 free inodes.

server1 `/mnt/raid5`: 405192491008 available bytes; 98.14% used; 337682717 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57598578688 available bytes; 96.79% used; 110429436 free inodes.

server2 `/home`: 57598578688 available bytes; 96.79% used; 110429436 free inodes.

server2 `/tmp`: 57598578688 available bytes; 96.79% used; 110429436 free inodes.

server2 `/var/tmp`: 57598578688 available bytes; 96.79% used; 110429436 free inodes.

server2 `/mnt/raid5`: 487950237696 available bytes; 96.63% used; 445171712 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85714956288 available bytes; 95.22% used; 114196881 free inodes.

server3 `/home`: 85714956288 available bytes; 95.22% used; 114196881 free inodes.

server3 `/data`: 163391123456 available bytes; 97.74% used; 225814808 free inodes.

server3 `/tmp`: 85714956288 available bytes; 95.22% used; 114196881 free inodes.

server3 `/var/tmp`: 85714956288 available bytes; 95.22% used; 114196881 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780764672 available bytes; 94.10% used; 114348797 free inodes.

server4 `/home`: 105780764672 available bytes; 94.10% used; 114348797 free inodes.

server4 `/data`: 90074877952 available bytes; 98.76% used; 225257261 free inodes.

server4 `/tmp`: 105780764672 available bytes; 94.10% used; 114348797 free inodes.

server4 `/var/tmp`: 105780764672 available bytes; 94.10% used; 114348797 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
