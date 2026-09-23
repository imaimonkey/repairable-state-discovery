# V2R cluster inventory

2026-09-23T23:35:16.200704+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325615849472 available bytes; 81.84% used; 112501265 free inodes.

server1 `/home`: 325615849472 available bytes; 81.84% used; 112501265 free inodes.

server1 `/tmp`: 325615849472 available bytes; 81.84% used; 112501265 free inodes.

server1 `/var/tmp`: 325615849472 available bytes; 81.84% used; 112501265 free inodes.

server1 `/mnt/raid5`: 1367401160704 available bytes; 93.73% used; 337736319 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41034121216 available bytes; 97.71% used; 110432551 free inodes.

server2 `/home`: 41034121216 available bytes; 97.71% used; 110432551 free inodes.

server2 `/tmp`: 41034121216 available bytes; 97.71% used; 110432551 free inodes.

server2 `/var/tmp`: 41034121216 available bytes; 97.71% used; 110432551 free inodes.

server2 `/mnt/raid5`: 534291980288 available bytes; 96.31% used; 445205135 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292842201088 available bytes; 83.66% used; 114214316 free inodes.

server3 `/home`: 292842201088 available bytes; 83.66% used; 114214316 free inodes.

server3 `/data`: 82304884736 available bytes; 98.86% used; 225845668 free inodes.

server3 `/tmp`: 292842201088 available bytes; 83.66% used; 114214316 free inodes.

server3 `/var/tmp`: 292842201088 available bytes; 83.66% used; 114214316 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106209382400 available bytes; 94.07% used; 114352175 free inodes.

server4 `/home`: 106209382400 available bytes; 94.07% used; 114352175 free inodes.

server4 `/data`: 293028880384 available bytes; 95.95% used; 225422323 free inodes.

server4 `/tmp`: 106209382400 available bytes; 94.07% used; 114352175 free inodes.

server4 `/var/tmp`: 106209382400 available bytes; 94.07% used; 114352175 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
