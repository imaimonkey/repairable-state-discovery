# V2R cluster inventory

2026-09-26T01:26:47.387357+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318650322944 available bytes; 82.22% used; 112476301 free inodes.

server1 `/home`: 318650322944 available bytes; 82.22% used; 112476301 free inodes.

server1 `/tmp`: 318650322944 available bytes; 82.22% used; 112476301 free inodes.

server1 `/var/tmp`: 318650322944 available bytes; 82.22% used; 112476301 free inodes.

server1 `/mnt/raid5`: 345507663872 available bytes; 98.42% used; 337546575 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22928986112 available bytes; 98.72% used; 110406220 free inodes.

server2 `/home`: 22928986112 available bytes; 98.72% used; 110406220 free inodes.

server2 `/tmp`: 22928986112 available bytes; 98.72% used; 110406220 free inodes.

server2 `/var/tmp`: 22928986112 available bytes; 98.72% used; 110406220 free inodes.

server2 `/mnt/raid5`: 290290479104 available bytes; 97.99% used; 445056097 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84336398336 available bytes; 95.29% used; 114152426 free inodes.

server3 `/home`: 84336398336 available bytes; 95.29% used; 114152426 free inodes.

server3 `/data`: 124866789376 available bytes; 98.27% used; 225818091 free inodes.

server3 `/tmp`: 84336398336 available bytes; 95.29% used; 114152426 free inodes.

server3 `/var/tmp`: 84336398336 available bytes; 95.29% used; 114152426 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105264218112 available bytes; 94.13% used; 114347079 free inodes.

server4 `/home`: 105264218112 available bytes; 94.13% used; 114347079 free inodes.

server4 `/data`: 141688872960 available bytes; 98.04% used; 224917301 free inodes.

server4 `/tmp`: 105264218112 available bytes; 94.13% used; 114347079 free inodes.

server4 `/var/tmp`: 105264218112 available bytes; 94.13% used; 114347079 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
