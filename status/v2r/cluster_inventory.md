# V2R cluster inventory

2026-09-24T12:25:31.443622+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324056768512 available bytes; 81.92% used; 112481548 free inodes.

server1 `/home`: 324056768512 available bytes; 81.92% used; 112481548 free inodes.

server1 `/tmp`: 324056768512 available bytes; 81.92% used; 112481548 free inodes.

server1 `/var/tmp`: 324056768512 available bytes; 81.92% used; 112481548 free inodes.

server1 `/mnt/raid5`: 405201973248 available bytes; 98.14% used; 337682915 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57600020480 available bytes; 96.79% used; 110429452 free inodes.

server2 `/home`: 57600020480 available bytes; 96.79% used; 110429452 free inodes.

server2 `/tmp`: 57600020480 available bytes; 96.79% used; 110429452 free inodes.

server2 `/var/tmp`: 57600020480 available bytes; 96.79% used; 110429452 free inodes.

server2 `/mnt/raid5`: 508653006848 available bytes; 96.49% used; 445171901 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85718994944 available bytes; 95.22% used; 114197120 free inodes.

server3 `/home`: 85718994944 available bytes; 95.22% used; 114197120 free inodes.

server3 `/data`: 163407982592 available bytes; 97.74% used; 225814837 free inodes.

server3 `/tmp`: 85718994944 available bytes; 95.22% used; 114197120 free inodes.

server3 `/var/tmp`: 85718994944 available bytes; 95.22% used; 114197120 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780809728 available bytes; 94.10% used; 114348797 free inodes.

server4 `/home`: 105780809728 available bytes; 94.10% used; 114348797 free inodes.

server4 `/data`: 90076581888 available bytes; 98.76% used; 225257276 free inodes.

server4 `/tmp`: 105780809728 available bytes; 94.10% used; 114348797 free inodes.

server4 `/var/tmp`: 105780809728 available bytes; 94.10% used; 114348797 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
