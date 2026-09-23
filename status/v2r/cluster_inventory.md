# V2R cluster inventory

2026-09-23T15:36:16.213186+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['7'] | [] |

server2 `/`: 41428123648 available bytes; 97.69% used; 110435189 free inodes.

server2 `/home`: 41428123648 available bytes; 97.69% used; 110435189 free inodes.

server2 `/tmp`: 41428123648 available bytes; 97.69% used; 110435189 free inodes.

server2 `/var/tmp`: 41428123648 available bytes; 97.69% used; 110435189 free inodes.

server2 `/mnt/raid5`: 550578552832 available bytes; 96.20% used; 445223463 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] |

server3 `/`: 377603465216 available bytes; 78.93% used; 114304115 free inodes.

server3 `/home`: 377603465216 available bytes; 78.93% used; 114304115 free inodes.

server3 `/data`: 125635026944 available bytes; 98.26% used; 225855676 free inodes.

server3 `/tmp`: 377603465216 available bytes; 78.93% used; 114304115 free inodes.

server3 `/var/tmp`: 377603465216 available bytes; 78.93% used; 114304115 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111499542528 available bytes; 93.78% used; 114375768 free inodes.

server4 `/home`: 111499542528 available bytes; 93.78% used; 114375768 free inodes.

server4 `/data`: 38844203008 available bytes; 99.46% used; 225495049 free inodes.

server4 `/tmp`: 111499542528 available bytes; 93.78% used; 114375768 free inodes.

server4 `/var/tmp`: 111499542528 available bytes; 93.78% used; 114375768 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
