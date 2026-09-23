# V2R cluster inventory

2026-09-23T12:52:23.623672+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['6'] | [] |

server2 `/`: 41322446848 available bytes; 97.69% used; 110436095 free inodes.

server2 `/home`: 41322446848 available bytes; 97.69% used; 110436095 free inodes.

server2 `/tmp`: 41322446848 available bytes; 97.69% used; 110436095 free inodes.

server2 `/var/tmp`: 41322446848 available bytes; 97.69% used; 110436095 free inodes.

server2 `/mnt/raid5`: 556683505664 available bytes; 96.15% used; 445228725 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 378449539072 available bytes; 78.88% used; 114329020 free inodes.

server3 `/home`: 378449539072 available bytes; 78.88% used; 114329020 free inodes.

server3 `/data`: 134985838592 available bytes; 98.13% used; 225862655 free inodes.

server3 `/tmp`: 378449539072 available bytes; 78.88% used; 114329020 free inodes.

server3 `/var/tmp`: 378449539072 available bytes; 78.88% used; 114329020 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111677546496 available bytes; 93.77% used; 114378483 free inodes.

server4 `/home`: 111677546496 available bytes; 93.77% used; 114378483 free inodes.

server4 `/data`: 54258749440 available bytes; 99.25% used; 225404065 free inodes.

server4 `/tmp`: 111677546496 available bytes; 93.77% used; 114378483 free inodes.

server4 `/var/tmp`: 111677546496 available bytes; 93.77% used; 114378483 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
