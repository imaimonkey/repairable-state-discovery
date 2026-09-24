# V2R cluster inventory

2026-09-24T12:34:58.102120+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324047740928 available bytes; 81.92% used; 112481547 free inodes.

server1 `/home`: 324047740928 available bytes; 81.92% used; 112481547 free inodes.

server1 `/tmp`: 324047740928 available bytes; 81.92% used; 112481547 free inodes.

server1 `/var/tmp`: 324047740928 available bytes; 81.92% used; 112481547 free inodes.

server1 `/mnt/raid5`: 405169844224 available bytes; 98.14% used; 337681802 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57592397824 available bytes; 96.79% used; 110429352 free inodes.

server2 `/home`: 57592397824 available bytes; 96.79% used; 110429352 free inodes.

server2 `/tmp`: 57592397824 available bytes; 96.79% used; 110429352 free inodes.

server2 `/var/tmp`: 57592397824 available bytes; 96.79% used; 110429352 free inodes.

server2 `/mnt/raid5`: 486636802048 available bytes; 96.64% used; 445171615 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85710045184 available bytes; 95.22% used; 114197985 free inodes.

server3 `/home`: 85710045184 available bytes; 95.22% used; 114197985 free inodes.

server3 `/data`: 163273543680 available bytes; 97.74% used; 225814660 free inodes.

server3 `/tmp`: 85710045184 available bytes; 95.22% used; 114197985 free inodes.

server3 `/var/tmp`: 85710045184 available bytes; 95.22% used; 114197985 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780494336 available bytes; 94.10% used; 114348793 free inodes.

server4 `/home`: 105780494336 available bytes; 94.10% used; 114348793 free inodes.

server4 `/data`: 90072723456 available bytes; 98.76% used; 225257242 free inodes.

server4 `/tmp`: 105780494336 available bytes; 94.10% used; 114348793 free inodes.

server4 `/var/tmp`: 105780494336 available bytes; 94.10% used; 114348793 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
