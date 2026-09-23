# V2R cluster inventory

2026-09-23T15:08:46.512303+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['7'] | [] |

server2 `/`: 41441767424 available bytes; 97.69% used; 110435185 free inodes.

server2 `/home`: 41441767424 available bytes; 97.69% used; 110435185 free inodes.

server2 `/tmp`: 41441767424 available bytes; 97.69% used; 110435185 free inodes.

server2 `/var/tmp`: 41441767424 available bytes; 97.69% used; 110435185 free inodes.

server2 `/mnt/raid5`: 551401136128 available bytes; 96.19% used; 445224353 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 377662857216 available bytes; 78.93% used; 114305223 free inodes.

server3 `/home`: 377662857216 available bytes; 78.93% used; 114305223 free inodes.

server3 `/data`: 124980563968 available bytes; 98.27% used; 225841006 free inodes.

server3 `/tmp`: 377662857216 available bytes; 78.93% used; 114305223 free inodes.

server3 `/var/tmp`: 377662857216 available bytes; 78.93% used; 114305223 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111673184256 available bytes; 93.77% used; 114378461 free inodes.

server4 `/home`: 111673184256 available bytes; 93.77% used; 114378461 free inodes.

server4 `/data`: 39153590272 available bytes; 99.46% used; 225495954 free inodes.

server4 `/tmp`: 111673184256 available bytes; 93.77% used; 114378461 free inodes.

server4 `/var/tmp`: 111673184256 available bytes; 93.77% used; 114378461 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
