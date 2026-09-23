# V2R cluster inventory

2026-09-23T15:37:47.821214+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['7'] | [] |

server2 `/`: 41428062208 available bytes; 97.69% used; 110435188 free inodes.

server2 `/home`: 41428062208 available bytes; 97.69% used; 110435188 free inodes.

server2 `/tmp`: 41428062208 available bytes; 97.69% used; 110435188 free inodes.

server2 `/var/tmp`: 41428062208 available bytes; 97.69% used; 110435188 free inodes.

server2 `/mnt/raid5`: 550550405120 available bytes; 96.20% used; 445223529 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] |

server3 `/`: 377602224128 available bytes; 78.93% used; 114304096 free inodes.

server3 `/home`: 377602224128 available bytes; 78.93% used; 114304096 free inodes.

server3 `/data`: 125631623168 available bytes; 98.26% used; 225855634 free inodes.

server3 `/tmp`: 377602224128 available bytes; 78.93% used; 114304096 free inodes.

server3 `/var/tmp`: 377602224128 available bytes; 78.93% used; 114304096 free inodes.
| server4 | True | ['1', '2', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111499550720 available bytes; 93.78% used; 114375780 free inodes.

server4 `/home`: 111499550720 available bytes; 93.78% used; 114375780 free inodes.

server4 `/data`: 38808981504 available bytes; 99.46% used; 225495032 free inodes.

server4 `/tmp`: 111499550720 available bytes; 93.78% used; 114375780 free inodes.

server4 `/var/tmp`: 111499550720 available bytes; 93.78% used; 114375780 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
