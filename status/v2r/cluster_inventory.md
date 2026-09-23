# V2R cluster inventory

2026-09-23T13:04:34.810417+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['6'] | [] |

server2 `/`: 41322016768 available bytes; 97.69% used; 110436089 free inodes.

server2 `/home`: 41322016768 available bytes; 97.69% used; 110436089 free inodes.

server2 `/tmp`: 41322016768 available bytes; 97.69% used; 110436089 free inodes.

server2 `/var/tmp`: 41322016768 available bytes; 97.69% used; 110436089 free inodes.

server2 `/mnt/raid5`: 556310720512 available bytes; 96.16% used; 445228477 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 378392555520 available bytes; 78.88% used; 114326701 free inodes.

server3 `/home`: 378392555520 available bytes; 78.88% used; 114326701 free inodes.

server3 `/data`: 134910963712 available bytes; 98.14% used; 225862473 free inodes.

server3 `/tmp`: 378392555520 available bytes; 78.88% used; 114326701 free inodes.

server3 `/var/tmp`: 378392555520 available bytes; 78.88% used; 114326701 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111677313024 available bytes; 93.77% used; 114378481 free inodes.

server4 `/home`: 111677313024 available bytes; 93.77% used; 114378481 free inodes.

server4 `/data`: 53219090432 available bytes; 99.26% used; 225441408 free inodes.

server4 `/tmp`: 111677313024 available bytes; 93.77% used; 114378481 free inodes.

server4 `/var/tmp`: 111677313024 available bytes; 93.77% used; 114378481 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
