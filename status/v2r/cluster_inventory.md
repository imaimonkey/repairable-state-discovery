# V2R cluster inventory

2026-09-23T14:48:58.044908+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | False | [] | [] |
| server2 | True | ['7'] | [] |

server2 `/`: 41448435712 available bytes; 97.69% used; 110435187 free inodes.

server2 `/home`: 41448435712 available bytes; 97.69% used; 110435187 free inodes.

server2 `/tmp`: 41448435712 available bytes; 97.69% used; 110435187 free inodes.

server2 `/var/tmp`: 41448435712 available bytes; 97.69% used; 110435187 free inodes.

server2 `/mnt/raid5`: 551953793024 available bytes; 96.19% used; 445225141 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 377979449344 available bytes; 78.91% used; 114314311 free inodes.

server3 `/home`: 377979449344 available bytes; 78.91% used; 114314311 free inodes.

server3 `/data`: 125083353088 available bytes; 98.27% used; 225841599 free inodes.

server3 `/tmp`: 377979449344 available bytes; 78.91% used; 114314311 free inodes.

server3 `/var/tmp`: 377979449344 available bytes; 78.91% used; 114314311 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 111667216384 available bytes; 93.77% used; 114378461 free inodes.

server4 `/home`: 111667216384 available bytes; 93.77% used; 114378461 free inodes.

server4 `/data`: 39730339840 available bytes; 99.45% used; 225498425 free inodes.

server4 `/tmp`: 111667216384 available bytes; 93.77% used; 114378461 free inodes.

server4 `/var/tmp`: 111667216384 available bytes; 93.77% used; 114378461 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
