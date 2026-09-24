# V2R cluster inventory

2026-09-24T13:23:23.576827+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324024401920 available bytes; 81.92% used; 112481531 free inodes.

server1 `/home`: 324024401920 available bytes; 81.92% used; 112481531 free inodes.

server1 `/tmp`: 324024401920 available bytes; 81.92% used; 112481531 free inodes.

server1 `/var/tmp`: 324024401920 available bytes; 81.92% used; 112481531 free inodes.

server1 `/mnt/raid5`: 417045282816 available bytes; 98.09% used; 337675981 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57537404928 available bytes; 96.79% used; 110428781 free inodes.

server2 `/home`: 57537404928 available bytes; 96.79% used; 110428781 free inodes.

server2 `/tmp`: 57537404928 available bytes; 96.79% used; 110428781 free inodes.

server2 `/var/tmp`: 57537404928 available bytes; 96.79% used; 110428781 free inodes.

server2 `/mnt/raid5`: 506845519872 available bytes; 96.50% used; 445170007 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84704362496 available bytes; 95.27% used; 114165507 free inodes.

server3 `/home`: 84704362496 available bytes; 95.27% used; 114165507 free inodes.

server3 `/data`: 161386401792 available bytes; 97.77% used; 225809421 free inodes.

server3 `/tmp`: 84704362496 available bytes; 95.27% used; 114165507 free inodes.

server3 `/var/tmp`: 84704362496 available bytes; 95.27% used; 114165507 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105769996288 available bytes; 94.10% used; 114348744 free inodes.

server4 `/home`: 105769996288 available bytes; 94.10% used; 114348744 free inodes.

server4 `/data`: 90036150272 available bytes; 98.76% used; 225257183 free inodes.

server4 `/tmp`: 105769996288 available bytes; 94.10% used; 114348744 free inodes.

server4 `/var/tmp`: 105769996288 available bytes; 94.10% used; 114348744 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
