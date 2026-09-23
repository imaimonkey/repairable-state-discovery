# V2R cluster inventory

2026-09-23T11:01:33.706187+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | [] | [] |

server2 `/`: 41843863552 available bytes; 97.67% used; 110436701 free inodes.

server2 `/home`: 41843863552 available bytes; 97.67% used; 110436701 free inodes.

server2 `/tmp`: 41843863552 available bytes; 97.67% used; 110436701 free inodes.

server2 `/var/tmp`: 41843863552 available bytes; 97.67% used; 110436701 free inodes.

server2 `/mnt/raid5`: 547494350848 available bytes; 96.22% used; 445238839 free inodes.
| server3 | True | ['1', '3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 380901089280 available bytes; 78.74% used; 114375137 free inodes.

server3 `/home`: 380901089280 available bytes; 78.74% used; 114375137 free inodes.

server3 `/data`: 140512980992 available bytes; 98.06% used; 225871522 free inodes.

server3 `/tmp`: 380901089280 available bytes; 78.74% used; 114375137 free inodes.

server3 `/var/tmp`: 380901089280 available bytes; 78.74% used; 114375137 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111605882880 available bytes; 93.77% used; 114379017 free inodes.

server4 `/home`: 111605882880 available bytes; 93.77% used; 114379017 free inodes.

server4 `/data`: 65495261184 available bytes; 99.09% used; 225403800 free inodes.

server4 `/tmp`: 111605882880 available bytes; 93.77% used; 114379017 free inodes.

server4 `/var/tmp`: 111605882880 available bytes; 93.77% used; 114379017 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
