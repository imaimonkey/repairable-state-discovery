# V2R cluster inventory

2026-09-23T11:17:42.170257+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | [] | [] |

server2 `/`: 41835802624 available bytes; 97.67% used; 110436701 free inodes.

server2 `/home`: 41835802624 available bytes; 97.67% used; 110436701 free inodes.

server2 `/tmp`: 41835802624 available bytes; 97.67% used; 110436701 free inodes.

server2 `/var/tmp`: 41835802624 available bytes; 97.67% used; 110436701 free inodes.

server2 `/mnt/raid5`: 545854853120 available bytes; 96.23% used; 445233931 free inodes.
| server3 | True | ['1', '3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 380543827968 available bytes; 78.76% used; 114364624 free inodes.

server3 `/home`: 380543827968 available bytes; 78.76% used; 114364624 free inodes.

server3 `/data`: 141564620800 available bytes; 98.04% used; 225885158 free inodes.

server3 `/tmp`: 380543827968 available bytes; 78.76% used; 114364624 free inodes.

server3 `/var/tmp`: 380543827968 available bytes; 78.76% used; 114364624 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111605731328 available bytes; 93.77% used; 114379012 free inodes.

server4 `/home`: 111605731328 available bytes; 93.77% used; 114379012 free inodes.

server4 `/data`: 62312321024 available bytes; 99.14% used; 225418127 free inodes.

server4 `/tmp`: 111605731328 available bytes; 93.77% used; 114379012 free inodes.

server4 `/var/tmp`: 111605731328 available bytes; 93.77% used; 114379012 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
