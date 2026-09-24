# V2R cluster inventory

2026-09-24T14:17:51.240631+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324057149440 available bytes; 81.92% used; 112481459 free inodes.

server1 `/home`: 324057149440 available bytes; 81.92% used; 112481459 free inodes.

server1 `/tmp`: 324057149440 available bytes; 81.92% used; 112481459 free inodes.

server1 `/var/tmp`: 324057149440 available bytes; 81.92% used; 112481459 free inodes.

server1 `/mnt/raid5`: 416926826496 available bytes; 98.09% used; 337669644 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57469317120 available bytes; 96.79% used; 110428243 free inodes.

server2 `/home`: 57469317120 available bytes; 96.79% used; 110428243 free inodes.

server2 `/tmp`: 57469317120 available bytes; 96.79% used; 110428243 free inodes.

server2 `/var/tmp`: 57469317120 available bytes; 96.79% used; 110428243 free inodes.

server2 `/mnt/raid5`: 504873152512 available bytes; 96.51% used; 445168449 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85049786368 available bytes; 95.25% used; 114188756 free inodes.

server3 `/home`: 85049786368 available bytes; 95.25% used; 114188756 free inodes.

server3 `/data`: 160999735296 available bytes; 97.77% used; 225808893 free inodes.

server3 `/tmp`: 85049786368 available bytes; 95.25% used; 114188756 free inodes.

server3 `/var/tmp`: 85049786368 available bytes; 95.25% used; 114188756 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759481856 available bytes; 94.10% used; 114348703 free inodes.

server4 `/home`: 105759481856 available bytes; 94.10% used; 114348703 free inodes.

server4 `/data`: 69364359168 available bytes; 99.04% used; 225257070 free inodes.

server4 `/tmp`: 105759481856 available bytes; 94.10% used; 114348703 free inodes.

server4 `/var/tmp`: 105759481856 available bytes; 94.10% used; 114348703 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
