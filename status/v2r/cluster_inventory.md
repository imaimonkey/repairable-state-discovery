# V2R cluster inventory

2026-09-26T06:08:06.238479+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318777573376 available bytes; 82.22% used; 112476284 free inodes.

server1 `/home`: 318777573376 available bytes; 82.22% used; 112476284 free inodes.

server1 `/tmp`: 318777573376 available bytes; 82.22% used; 112476284 free inodes.

server1 `/var/tmp`: 318777573376 available bytes; 82.22% used; 112476284 free inodes.

server1 `/mnt/raid5`: 224312299520 available bytes; 98.97% used; 337539920 free inodes.
| server2 | True | [] | [] |

server2 `/`: 21649551360 available bytes; 98.79% used; 110405045 free inodes.

server2 `/home`: 21649481728 available bytes; 98.79% used; 110405045 free inodes.

server2 `/tmp`: 21649416192 available bytes; 98.79% used; 110405045 free inodes.

server2 `/var/tmp`: 21649371136 available bytes; 98.79% used; 110405045 free inodes.

server2 `/mnt/raid5`: 274339418112 available bytes; 98.10% used; 445033373 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82430623744 available bytes; 95.40% used; 114110904 free inodes.

server3 `/home`: 82430623744 available bytes; 95.40% used; 114110904 free inodes.

server3 `/data`: 123994787840 available bytes; 98.29% used; 225822652 free inodes.

server3 `/tmp`: 82430623744 available bytes; 95.40% used; 114110904 free inodes.

server3 `/var/tmp`: 82430623744 available bytes; 95.40% used; 114110904 free inodes.
| server4 | True | ['1', '2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106093813760 available bytes; 94.08% used; 114348199 free inodes.

server4 `/home`: 106093813760 available bytes; 94.08% used; 114348199 free inodes.

server4 `/data`: 106917494784 available bytes; 98.52% used; 224929113 free inodes.

server4 `/tmp`: 106093813760 available bytes; 94.08% used; 114348199 free inodes.

server4 `/var/tmp`: 106093813760 available bytes; 94.08% used; 114348199 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
