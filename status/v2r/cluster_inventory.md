# V2R cluster inventory

2026-09-24T12:33:24.065224+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324050563072 available bytes; 81.92% used; 112481538 free inodes.

server1 `/home`: 324050563072 available bytes; 81.92% used; 112481538 free inodes.

server1 `/tmp`: 324050563072 available bytes; 81.92% used; 112481538 free inodes.

server1 `/var/tmp`: 324050563072 available bytes; 81.92% used; 112481538 free inodes.

server1 `/mnt/raid5`: 405172486144 available bytes; 98.14% used; 337681978 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57592614912 available bytes; 96.79% used; 110429364 free inodes.

server2 `/home`: 57592614912 available bytes; 96.79% used; 110429364 free inodes.

server2 `/tmp`: 57592614912 available bytes; 96.79% used; 110429364 free inodes.

server2 `/var/tmp`: 57592614912 available bytes; 96.79% used; 110429364 free inodes.

server2 `/mnt/raid5`: 504690356224 available bytes; 96.51% used; 445171787 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85713289216 available bytes; 95.22% used; 114198044 free inodes.

server3 `/home`: 85713289216 available bytes; 95.22% used; 114198044 free inodes.

server3 `/data`: 163282223104 available bytes; 97.74% used; 225814684 free inodes.

server3 `/tmp`: 85713289216 available bytes; 95.22% used; 114198044 free inodes.

server3 `/var/tmp`: 85713289216 available bytes; 95.22% used; 114198044 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780518912 available bytes; 94.10% used; 114348793 free inodes.

server4 `/home`: 105780518912 available bytes; 94.10% used; 114348793 free inodes.

server4 `/data`: 90076237824 available bytes; 98.76% used; 225257243 free inodes.

server4 `/tmp`: 105780518912 available bytes; 94.10% used; 114348793 free inodes.

server4 `/var/tmp`: 105780518912 available bytes; 94.10% used; 114348793 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
