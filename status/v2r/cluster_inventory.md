# V2R cluster inventory

2026-09-23T11:21:12.474428+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | [] | [] |

server2 `/`: 41836429312 available bytes; 97.67% used; 110436703 free inodes.

server2 `/home`: 41836429312 available bytes; 97.67% used; 110436703 free inodes.

server2 `/tmp`: 41836429312 available bytes; 97.67% used; 110436703 free inodes.

server2 `/var/tmp`: 41836429312 available bytes; 97.67% used; 110436703 free inodes.

server2 `/mnt/raid5`: 545456865280 available bytes; 96.23% used; 445233674 free inodes.
| server3 | True | ['1', '3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 380474310656 available bytes; 78.77% used; 114362019 free inodes.

server3 `/home`: 380474310656 available bytes; 78.77% used; 114362019 free inodes.

server3 `/data`: 141540962304 available bytes; 98.04% used; 225884965 free inodes.

server3 `/tmp`: 380474310656 available bytes; 78.77% used; 114362019 free inodes.

server3 `/var/tmp`: 380474310656 available bytes; 78.77% used; 114362019 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111605669888 available bytes; 93.77% used; 114379012 free inodes.

server4 `/home`: 111605669888 available bytes; 93.77% used; 114379012 free inodes.

server4 `/data`: 61165400064 available bytes; 99.15% used; 225418039 free inodes.

server4 `/tmp`: 111605669888 available bytes; 93.77% used; 114379012 free inodes.

server4 `/var/tmp`: 111605669888 available bytes; 93.77% used; 114379012 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
