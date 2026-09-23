# V2R cluster inventory

2026-09-23T12:05:09.207727+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['6'] | [] |

server2 `/`: 41818468352 available bytes; 97.67% used; 110436699 free inodes.

server2 `/home`: 41818468352 available bytes; 97.67% used; 110436699 free inodes.

server2 `/tmp`: 41818468352 available bytes; 97.67% used; 110436699 free inodes.

server2 `/var/tmp`: 41818468352 available bytes; 97.67% used; 110436699 free inodes.

server2 `/mnt/raid5`: 557502218240 available bytes; 96.15% used; 445231382 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 379971100672 available bytes; 78.80% used; 114343713 free inodes.

server3 `/home`: 379971100672 available bytes; 78.80% used; 114343713 free inodes.

server3 `/data`: 137469157376 available bytes; 98.10% used; 225864099 free inodes.

server3 `/tmp`: 379971100672 available bytes; 78.80% used; 114343713 free inodes.

server3 `/var/tmp`: 379971100672 available bytes; 78.80% used; 114343713 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111605006336 available bytes; 93.77% used; 114379002 free inodes.

server4 `/home`: 111605006336 available bytes; 93.77% used; 114379002 free inodes.

server4 `/data`: 65007243264 available bytes; 99.10% used; 225411494 free inodes.

server4 `/tmp`: 111605006336 available bytes; 93.77% used; 114379002 free inodes.

server4 `/var/tmp`: 111605006336 available bytes; 93.77% used; 114379002 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
