# V2R cluster inventory

2026-09-26T01:46:38.959597+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318647840768 available bytes; 82.22% used; 112476293 free inodes.

server1 `/home`: 318647840768 available bytes; 82.22% used; 112476293 free inodes.

server1 `/tmp`: 318647840768 available bytes; 82.22% used; 112476293 free inodes.

server1 `/var/tmp`: 318647840768 available bytes; 82.22% used; 112476293 free inodes.

server1 `/mnt/raid5`: 345462730752 available bytes; 98.42% used; 337546408 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22938611712 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22938611712 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22938611712 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22938611712 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 290232119296 available bytes; 97.99% used; 445055250 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84326289408 available bytes; 95.29% used; 114152364 free inodes.

server3 `/home`: 84326289408 available bytes; 95.29% used; 114152364 free inodes.

server3 `/data`: 124795346944 available bytes; 98.28% used; 225817726 free inodes.

server3 `/tmp`: 84326289408 available bytes; 95.29% used; 114152364 free inodes.

server3 `/var/tmp`: 84326289408 available bytes; 95.29% used; 114152364 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105196486656 available bytes; 94.13% used; 114346901 free inodes.

server4 `/home`: 105196486656 available bytes; 94.13% used; 114346901 free inodes.

server4 `/data`: 131301679104 available bytes; 98.19% used; 224915838 free inodes.

server4 `/tmp`: 105196486656 available bytes; 94.13% used; 114346901 free inodes.

server4 `/var/tmp`: 105196486656 available bytes; 94.13% used; 114346901 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
