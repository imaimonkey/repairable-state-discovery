# V2R cluster inventory

2026-09-24T17:07:22.648219+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324024745984 available bytes; 81.92% used; 112481440 free inodes.

server1 `/home`: 324024745984 available bytes; 81.92% used; 112481440 free inodes.

server1 `/tmp`: 324024745984 available bytes; 81.92% used; 112481440 free inodes.

server1 `/var/tmp`: 324024745984 available bytes; 81.92% used; 112481440 free inodes.

server1 `/mnt/raid5`: 416500035584 available bytes; 98.09% used; 337649024 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57062449152 available bytes; 96.82% used; 110417938 free inodes.

server2 `/home`: 57062449152 available bytes; 96.82% used; 110417938 free inodes.

server2 `/tmp`: 57062449152 available bytes; 96.82% used; 110417938 free inodes.

server2 `/var/tmp`: 57062449152 available bytes; 96.82% used; 110417938 free inodes.

server2 `/mnt/raid5`: 499773837312 available bytes; 96.55% used; 445163134 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84417720320 available bytes; 95.29% used; 114156152 free inodes.

server3 `/home`: 84417720320 available bytes; 95.29% used; 114156152 free inodes.

server3 `/data`: 159092883456 available bytes; 97.80% used; 225787266 free inodes.

server3 `/tmp`: 84417720320 available bytes; 95.29% used; 114156152 free inodes.

server3 `/var/tmp`: 84417720320 available bytes; 95.29% used; 114156152 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105682223104 available bytes; 94.10% used; 114348569 free inodes.

server4 `/home`: 105682223104 available bytes; 94.10% used; 114348569 free inodes.

server4 `/data`: 89167974400 available bytes; 98.77% used; 225254677 free inodes.

server4 `/tmp`: 105682223104 available bytes; 94.10% used; 114348569 free inodes.

server4 `/var/tmp`: 105682223104 available bytes; 94.10% used; 114348569 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
