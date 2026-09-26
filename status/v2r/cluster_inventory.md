# V2R cluster inventory

2026-09-26T01:51:13.927369+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318528212992 available bytes; 82.23% used; 112476288 free inodes.

server1 `/home`: 318528212992 available bytes; 82.23% used; 112476288 free inodes.

server1 `/tmp`: 318528212992 available bytes; 82.23% used; 112476288 free inodes.

server1 `/var/tmp`: 318528212992 available bytes; 82.23% used; 112476288 free inodes.

server1 `/mnt/raid5`: 345246724096 available bytes; 98.42% used; 337546346 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22932316160 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22932316160 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22932316160 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22932316160 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 289574412288 available bytes; 98.00% used; 445055352 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84326858752 available bytes; 95.29% used; 114152366 free inodes.

server3 `/home`: 84326858752 available bytes; 95.29% used; 114152366 free inodes.

server3 `/data`: 124793520128 available bytes; 98.28% used; 225817657 free inodes.

server3 `/tmp`: 84326858752 available bytes; 95.29% used; 114152366 free inodes.

server3 `/var/tmp`: 84326858752 available bytes; 95.29% used; 114152366 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105434001408 available bytes; 94.12% used; 114348357 free inodes.

server4 `/home`: 105434001408 available bytes; 94.12% used; 114348357 free inodes.

server4 `/data`: 130903351296 available bytes; 98.19% used; 224915770 free inodes.

server4 `/tmp`: 105434001408 available bytes; 94.12% used; 114348357 free inodes.

server4 `/var/tmp`: 105434001408 available bytes; 94.12% used; 114348357 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
