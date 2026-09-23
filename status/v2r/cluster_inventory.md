# V2R cluster inventory

2026-09-23T15:24:07.059974+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['7'] | [] |

server2 `/`: 41432293376 available bytes; 97.69% used; 110435179 free inodes.

server2 `/home`: 41432293376 available bytes; 97.69% used; 110435179 free inodes.

server2 `/tmp`: 41432293376 available bytes; 97.69% used; 110435179 free inodes.

server2 `/var/tmp`: 41432293376 available bytes; 97.69% used; 110435179 free inodes.

server2 `/mnt/raid5`: 550957858816 available bytes; 96.19% used; 445223873 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] |

server3 `/`: 377640124416 available bytes; 78.93% used; 114304776 free inodes.

server3 `/home`: 377640124416 available bytes; 78.93% used; 114304776 free inodes.

server3 `/data`: 124963545088 available bytes; 98.27% used; 225840936 free inodes.

server3 `/tmp`: 377640124416 available bytes; 78.93% used; 114304776 free inodes.

server3 `/var/tmp`: 377640124416 available bytes; 78.93% used; 114304776 free inodes.
| server4 | True | ['1', '2', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111672692736 available bytes; 93.77% used; 114378455 free inodes.

server4 `/home`: 111672692736 available bytes; 93.77% used; 114378455 free inodes.

server4 `/data`: 38929383424 available bytes; 99.46% used; 225495129 free inodes.

server4 `/tmp`: 111672692736 available bytes; 93.77% used; 114378455 free inodes.

server4 `/var/tmp`: 111672692736 available bytes; 93.77% used; 114378455 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
