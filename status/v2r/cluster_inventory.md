# V2R cluster inventory

2026-09-23T15:05:43.713432+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['7'] | [] |

server2 `/`: 41442455552 available bytes; 97.69% used; 110435185 free inodes.

server2 `/home`: 41442455552 available bytes; 97.69% used; 110435185 free inodes.

server2 `/tmp`: 41442455552 available bytes; 97.69% used; 110435185 free inodes.

server2 `/var/tmp`: 41442455552 available bytes; 97.69% used; 110435185 free inodes.

server2 `/mnt/raid5`: 551497424896 available bytes; 96.19% used; 445224614 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 377668124672 available bytes; 78.92% used; 114305345 free inodes.

server3 `/home`: 377668124672 available bytes; 78.92% used; 114305345 free inodes.

server3 `/data`: 124988411904 available bytes; 98.27% used; 225841079 free inodes.

server3 `/tmp`: 377668124672 available bytes; 78.92% used; 114305345 free inodes.

server3 `/var/tmp`: 377668124672 available bytes; 78.92% used; 114305345 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111666921472 available bytes; 93.77% used; 114378460 free inodes.

server4 `/home`: 111666921472 available bytes; 93.77% used; 114378460 free inodes.

server4 `/data`: 39208206336 available bytes; 99.46% used; 225497068 free inodes.

server4 `/tmp`: 111666921472 available bytes; 93.77% used; 114378460 free inodes.

server4 `/var/tmp`: 111666921472 available bytes; 93.77% used; 114378460 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
