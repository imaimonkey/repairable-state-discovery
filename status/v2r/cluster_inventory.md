# V2R cluster inventory

2026-09-23T13:49:31.397915+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['6', '7'] | [] |

server2 `/`: 41472000000 available bytes; 97.69% used; 110435076 free inodes.

server2 `/home`: 41472000000 available bytes; 97.69% used; 110435076 free inodes.

server2 `/tmp`: 41472000000 available bytes; 97.69% used; 110435076 free inodes.

server2 `/var/tmp`: 41472000000 available bytes; 97.69% used; 110435076 free inodes.

server2 `/mnt/raid5`: 554726506496 available bytes; 96.17% used; 445227078 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] |

server3 `/`: 378230644736 available bytes; 78.89% used; 114321841 free inodes.

server3 `/home`: 378230644736 available bytes; 78.89% used; 114321841 free inodes.

server3 `/data`: 133349634048 available bytes; 98.16% used; 225845015 free inodes.

server3 `/tmp`: 378230644736 available bytes; 78.89% used; 114321841 free inodes.

server3 `/var/tmp`: 378230644736 available bytes; 78.89% used; 114321841 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111676608512 available bytes; 93.77% used; 114378474 free inodes.

server4 `/home`: 111676608512 available bytes; 93.77% used; 114378474 free inodes.

server4 `/data`: 47195045888 available bytes; 99.35% used; 225444526 free inodes.

server4 `/tmp`: 111676608512 available bytes; 93.77% used; 114378474 free inodes.

server4 `/var/tmp`: 111676608512 available bytes; 93.77% used; 114378474 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
