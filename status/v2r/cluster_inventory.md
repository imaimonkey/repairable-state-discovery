# V2R cluster inventory

2026-09-24T12:36:33.972192+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324046598144 available bytes; 81.92% used; 112481553 free inodes.

server1 `/home`: 324046598144 available bytes; 81.92% used; 112481553 free inodes.

server1 `/tmp`: 324046598144 available bytes; 81.92% used; 112481553 free inodes.

server1 `/var/tmp`: 324046598144 available bytes; 81.92% used; 112481553 free inodes.

server1 `/mnt/raid5`: 405167951872 available bytes; 98.14% used; 337681617 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57586712576 available bytes; 96.79% used; 110429338 free inodes.

server2 `/home`: 57586712576 available bytes; 96.79% used; 110429338 free inodes.

server2 `/tmp`: 57586712576 available bytes; 96.79% used; 110429338 free inodes.

server2 `/var/tmp`: 57586712576 available bytes; 96.79% used; 110429338 free inodes.

server2 `/mnt/raid5`: 507752865792 available bytes; 96.49% used; 445171476 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85708673024 available bytes; 95.22% used; 114197908 free inodes.

server3 `/home`: 85708673024 available bytes; 95.22% used; 114197908 free inodes.

server3 `/data`: 163256127488 available bytes; 97.74% used; 225814625 free inodes.

server3 `/tmp`: 85708673024 available bytes; 95.22% used; 114197908 free inodes.

server3 `/var/tmp`: 85708673024 available bytes; 95.22% used; 114197908 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780375552 available bytes; 94.10% used; 114348789 free inodes.

server4 `/home`: 105780375552 available bytes; 94.10% used; 114348789 free inodes.

server4 `/data`: 90060570624 available bytes; 98.76% used; 225257236 free inodes.

server4 `/tmp`: 105780375552 available bytes; 94.10% used; 114348789 free inodes.

server4 `/var/tmp`: 105780375552 available bytes; 94.10% used; 114348789 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
