# V2R cluster inventory

2026-09-25T22:26:29.221301+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318695755776 available bytes; 82.22% used; 112476307 free inodes.

server1 `/home`: 318695755776 available bytes; 82.22% used; 112476307 free inodes.

server1 `/tmp`: 318695755776 available bytes; 82.22% used; 112476307 free inodes.

server1 `/var/tmp`: 318695755776 available bytes; 82.22% used; 112476307 free inodes.

server1 `/mnt/raid5`: 360252026880 available bytes; 98.35% used; 337538956 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22956163072 available bytes; 98.72% used; 110406240 free inodes.

server2 `/home`: 22956163072 available bytes; 98.72% used; 110406240 free inodes.

server2 `/tmp`: 22956163072 available bytes; 98.72% used; 110406240 free inodes.

server2 `/var/tmp`: 22956163072 available bytes; 98.72% used; 110406240 free inodes.

server2 `/mnt/raid5`: 299079725056 available bytes; 97.93% used; 445053033 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84355235840 available bytes; 95.29% used; 114152442 free inodes.

server3 `/home`: 84355235840 available bytes; 95.29% used; 114152442 free inodes.

server3 `/data`: 124828659712 available bytes; 98.27% used; 225806020 free inodes.

server3 `/tmp`: 84355235840 available bytes; 95.29% used; 114152442 free inodes.

server3 `/var/tmp`: 84355235840 available bytes; 95.29% used; 114152442 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105244561408 available bytes; 94.13% used; 114346967 free inodes.

server4 `/home`: 105244561408 available bytes; 94.13% used; 114346967 free inodes.

server4 `/data`: 193867718656 available bytes; 97.32% used; 224917765 free inodes.

server4 `/tmp`: 105244561408 available bytes; 94.13% used; 114346967 free inodes.

server4 `/var/tmp`: 105244561408 available bytes; 94.13% used; 114346967 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
