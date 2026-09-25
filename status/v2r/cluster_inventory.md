# V2R cluster inventory

2026-09-25T22:58:34.338290+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318694584320 available bytes; 82.22% used; 112476299 free inodes.

server1 `/home`: 318694584320 available bytes; 82.22% used; 112476299 free inodes.

server1 `/tmp`: 318694584320 available bytes; 82.22% used; 112476299 free inodes.

server1 `/var/tmp`: 318694584320 available bytes; 82.22% used; 112476299 free inodes.

server1 `/mnt/raid5`: 360185233408 available bytes; 98.35% used; 337538806 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22946299904 available bytes; 98.72% used; 110406228 free inodes.

server2 `/home`: 22946299904 available bytes; 98.72% used; 110406228 free inodes.

server2 `/tmp`: 22946299904 available bytes; 98.72% used; 110406228 free inodes.

server2 `/var/tmp`: 22946299904 available bytes; 98.72% used; 110406228 free inodes.

server2 `/mnt/raid5`: 298149601280 available bytes; 97.94% used; 445051942 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84351279104 available bytes; 95.29% used; 114152432 free inodes.

server3 `/home`: 84351279104 available bytes; 95.29% used; 114152432 free inodes.

server3 `/data`: 124822220800 available bytes; 98.27% used; 225805479 free inodes.

server3 `/tmp`: 84351279104 available bytes; 95.29% used; 114152432 free inodes.

server3 `/var/tmp`: 84351279104 available bytes; 95.29% used; 114152432 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105159688192 available bytes; 94.13% used; 114346790 free inodes.

server4 `/home`: 105159688192 available bytes; 94.13% used; 114346790 free inodes.

server4 `/data`: 185232121856 available bytes; 97.44% used; 224917659 free inodes.

server4 `/tmp`: 105159688192 available bytes; 94.13% used; 114346790 free inodes.

server4 `/var/tmp`: 105159688192 available bytes; 94.13% used; 114346790 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
