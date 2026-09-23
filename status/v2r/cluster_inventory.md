# V2R cluster inventory

2026-09-23T11:59:00.131750+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['6'] | [] |

server2 `/`: 41818505216 available bytes; 97.67% used; 110436695 free inodes.

server2 `/home`: 41818505216 available bytes; 97.67% used; 110436695 free inodes.

server2 `/tmp`: 41818505216 available bytes; 97.67% used; 110436695 free inodes.

server2 `/var/tmp`: 41818505216 available bytes; 97.67% used; 110436695 free inodes.

server2 `/mnt/raid5`: 558242750464 available bytes; 96.14% used; 445231590 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 380032270336 available bytes; 78.79% used; 114344977 free inodes.

server3 `/home`: 380032270336 available bytes; 78.79% used; 114344977 free inodes.

server3 `/data`: 137494618112 available bytes; 98.10% used; 225864293 free inodes.

server3 `/tmp`: 380032270336 available bytes; 78.79% used; 114344977 free inodes.

server3 `/var/tmp`: 380032270336 available bytes; 78.79% used; 114344977 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111605198848 available bytes; 93.77% used; 114379004 free inodes.

server4 `/home`: 111605198848 available bytes; 93.77% used; 114379004 free inodes.

server4 `/data`: 66320687104 available bytes; 99.08% used; 225411670 free inodes.

server4 `/tmp`: 111605198848 available bytes; 93.77% used; 114379004 free inodes.

server4 `/var/tmp`: 111605198848 available bytes; 93.77% used; 114379004 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
