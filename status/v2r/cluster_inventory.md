# V2R cluster inventory

2026-09-23T12:03:37.755031+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['6'] | [] |

server2 `/`: 41818898432 available bytes; 97.67% used; 110436699 free inodes.

server2 `/home`: 41818898432 available bytes; 97.67% used; 110436699 free inodes.

server2 `/tmp`: 41818898432 available bytes; 97.67% used; 110436699 free inodes.

server2 `/var/tmp`: 41818898432 available bytes; 97.67% used; 110436699 free inodes.

server2 `/mnt/raid5`: 558082072576 available bytes; 96.14% used; 445231306 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 379965980672 available bytes; 78.80% used; 114342443 free inodes.

server3 `/home`: 379965980672 available bytes; 78.80% used; 114342443 free inodes.

server3 `/data`: 137474715648 available bytes; 98.10% used; 225864120 free inodes.

server3 `/tmp`: 379965980672 available bytes; 78.80% used; 114342443 free inodes.

server3 `/var/tmp`: 379965980672 available bytes; 78.80% used; 114342443 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111605116928 available bytes; 93.77% used; 114379003 free inodes.

server4 `/home`: 111605116928 available bytes; 93.77% used; 114379003 free inodes.

server4 `/data`: 65232146432 available bytes; 99.10% used; 225411531 free inodes.

server4 `/tmp`: 111605116928 available bytes; 93.77% used; 114379003 free inodes.

server4 `/var/tmp`: 111605116928 available bytes; 93.77% used; 114379003 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
