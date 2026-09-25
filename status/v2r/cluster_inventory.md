# V2R cluster inventory

2026-09-25T23:24:34.863296+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318676983808 available bytes; 82.22% used; 112476306 free inodes.

server1 `/home`: 318676983808 available bytes; 82.22% used; 112476306 free inodes.

server1 `/tmp`: 318676983808 available bytes; 82.22% used; 112476306 free inodes.

server1 `/var/tmp`: 318676983808 available bytes; 82.22% used; 112476306 free inodes.

server1 `/mnt/raid5`: 360124968960 available bytes; 98.35% used; 337538683 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22945697792 available bytes; 98.72% used; 110406230 free inodes.

server2 `/home`: 22945697792 available bytes; 98.72% used; 110406230 free inodes.

server2 `/tmp`: 22945697792 available bytes; 98.72% used; 110406230 free inodes.

server2 `/var/tmp`: 22945697792 available bytes; 98.72% used; 110406230 free inodes.

server2 `/mnt/raid5`: 296925421568 available bytes; 97.95% used; 445051091 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84348821504 available bytes; 95.29% used; 114152436 free inodes.

server3 `/home`: 84348821504 available bytes; 95.29% used; 114152436 free inodes.

server3 `/data`: 124751605760 available bytes; 98.28% used; 225805031 free inodes.

server3 `/tmp`: 84348821504 available bytes; 95.29% used; 114152436 free inodes.

server3 `/var/tmp`: 84348821504 available bytes; 95.29% used; 114152436 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105158852608 available bytes; 94.13% used; 114346790 free inodes.

server4 `/home`: 105158852608 available bytes; 94.13% used; 114346790 free inodes.

server4 `/data`: 185129820160 available bytes; 97.44% used; 224917627 free inodes.

server4 `/tmp`: 105158852608 available bytes; 94.13% used; 114346790 free inodes.

server4 `/var/tmp`: 105158852608 available bytes; 94.13% used; 114346790 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
