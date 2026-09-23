# V2R cluster inventory

2026-09-23T15:11:46.263879+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['7'] | [] |

server2 `/`: 41440976896 available bytes; 97.69% used; 110435185 free inodes.

server2 `/home`: 41440976896 available bytes; 97.69% used; 110435185 free inodes.

server2 `/tmp`: 41440976896 available bytes; 97.69% used; 110435185 free inodes.

server2 `/var/tmp`: 41440976896 available bytes; 97.69% used; 110435185 free inodes.

server2 `/mnt/raid5`: 551327006720 available bytes; 96.19% used; 445224572 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 377659682816 available bytes; 78.93% used; 114305062 free inodes.

server3 `/home`: 377659682816 available bytes; 78.93% used; 114305062 free inodes.

server3 `/data`: 124977172480 available bytes; 98.27% used; 225840953 free inodes.

server3 `/tmp`: 377659682816 available bytes; 78.93% used; 114305062 free inodes.

server3 `/var/tmp`: 377659682816 available bytes; 78.93% used; 114305062 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111673040896 available bytes; 93.77% used; 114378444 free inodes.

server4 `/home`: 111673040896 available bytes; 93.77% used; 114378444 free inodes.

server4 `/data`: 39052173312 available bytes; 99.46% used; 225495720 free inodes.

server4 `/tmp`: 111673040896 available bytes; 93.77% used; 114378444 free inodes.

server4 `/var/tmp`: 111673040896 available bytes; 93.77% used; 114378444 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
