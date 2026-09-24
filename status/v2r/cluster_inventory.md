# V2R cluster inventory

2026-09-24T12:42:46.722259+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324042194944 available bytes; 81.92% used; 112481554 free inodes.

server1 `/home`: 324042194944 available bytes; 81.92% used; 112481554 free inodes.

server1 `/tmp`: 324042194944 available bytes; 81.92% used; 112481554 free inodes.

server1 `/var/tmp`: 324042194944 available bytes; 81.92% used; 112481554 free inodes.

server1 `/mnt/raid5`: 403374862336 available bytes; 98.15% used; 337680814 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57582215168 available bytes; 96.79% used; 110429209 free inodes.

server2 `/home`: 57582215168 available bytes; 96.79% used; 110429209 free inodes.

server2 `/tmp`: 57582215168 available bytes; 96.79% used; 110429209 free inodes.

server2 `/var/tmp`: 57582215168 available bytes; 96.79% used; 110429209 free inodes.

server2 `/mnt/raid5`: 508097630208 available bytes; 96.49% used; 445171253 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85703077888 available bytes; 95.22% used; 114197876 free inodes.

server3 `/home`: 85703077888 available bytes; 95.22% used; 114197876 free inodes.

server3 `/data`: 160452837376 available bytes; 97.78% used; 225814489 free inodes.

server3 `/tmp`: 85703077888 available bytes; 95.22% used; 114197876 free inodes.

server3 `/var/tmp`: 85703077888 available bytes; 95.22% used; 114197876 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780101120 available bytes; 94.10% used; 114348784 free inodes.

server4 `/home`: 105780101120 available bytes; 94.10% used; 114348784 free inodes.

server4 `/data`: 90050453504 available bytes; 98.76% used; 225257237 free inodes.

server4 `/tmp`: 105780101120 available bytes; 94.10% used; 114348784 free inodes.

server4 `/var/tmp`: 105780101120 available bytes; 94.10% used; 114348784 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
