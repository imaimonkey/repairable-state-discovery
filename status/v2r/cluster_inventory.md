# V2R cluster inventory

2026-09-24T12:28:45.077097+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324055162880 available bytes; 81.92% used; 112481554 free inodes.

server1 `/home`: 324055162880 available bytes; 81.92% used; 112481554 free inodes.

server1 `/tmp`: 324055162880 available bytes; 81.92% used; 112481554 free inodes.

server1 `/var/tmp`: 324055162880 available bytes; 81.92% used; 112481554 free inodes.

server1 `/mnt/raid5`: 405193707520 available bytes; 98.14% used; 337682542 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57597018112 available bytes; 96.79% used; 110429417 free inodes.

server2 `/home`: 57597018112 available bytes; 96.79% used; 110429417 free inodes.

server2 `/tmp`: 57597018112 available bytes; 96.79% used; 110429417 free inodes.

server2 `/var/tmp`: 57597018112 available bytes; 96.79% used; 110429417 free inodes.

server2 `/mnt/raid5`: 508545454080 available bytes; 96.49% used; 445171628 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85719494656 available bytes; 95.22% used; 114197769 free inodes.

server3 `/home`: 85719494656 available bytes; 95.22% used; 114197769 free inodes.

server3 `/data`: 163348185088 available bytes; 97.74% used; 225814769 free inodes.

server3 `/tmp`: 85719494656 available bytes; 95.22% used; 114197769 free inodes.

server3 `/var/tmp`: 85719494656 available bytes; 95.22% used; 114197769 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780649984 available bytes; 94.10% used; 114348793 free inodes.

server4 `/home`: 105780649984 available bytes; 94.10% used; 114348793 free inodes.

server4 `/data`: 90073841664 available bytes; 98.76% used; 225257248 free inodes.

server4 `/tmp`: 105780649984 available bytes; 94.10% used; 114348793 free inodes.

server4 `/var/tmp`: 105780649984 available bytes; 94.10% used; 114348793 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
