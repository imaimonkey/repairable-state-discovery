# V2R cluster inventory

2026-09-25T21:37:35.925519+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318701522944 available bytes; 82.22% used; 112476316 free inodes.

server1 `/home`: 318701522944 available bytes; 82.22% used; 112476316 free inodes.

server1 `/tmp`: 318701522944 available bytes; 82.22% used; 112476316 free inodes.

server1 `/var/tmp`: 318701522944 available bytes; 82.22% used; 112476316 free inodes.

server1 `/mnt/raid5`: 360509243392 available bytes; 98.35% used; 337539237 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22900146176 available bytes; 98.72% used; 110405684 free inodes.

server2 `/home`: 22900146176 available bytes; 98.72% used; 110405684 free inodes.

server2 `/tmp`: 22900146176 available bytes; 98.72% used; 110405684 free inodes.

server2 `/var/tmp`: 22900146176 available bytes; 98.72% used; 110405684 free inodes.

server2 `/mnt/raid5`: 301033562112 available bytes; 97.92% used; 445054509 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84367220736 available bytes; 95.29% used; 114152626 free inodes.

server3 `/home`: 84367220736 available bytes; 95.29% used; 114152626 free inodes.

server3 `/data`: 125890682880 available bytes; 98.26% used; 225806847 free inodes.

server3 `/tmp`: 84367220736 available bytes; 95.29% used; 114152626 free inodes.

server3 `/var/tmp`: 84367220736 available bytes; 95.29% used; 114152626 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105388810240 available bytes; 94.12% used; 114347331 free inodes.

server4 `/home`: 105388810240 available bytes; 94.12% used; 114347331 free inodes.

server4 `/data`: 216841048064 available bytes; 97.00% used; 224919915 free inodes.

server4 `/tmp`: 105388810240 available bytes; 94.12% used; 114347331 free inodes.

server4 `/var/tmp`: 105388810240 available bytes; 94.12% used; 114347331 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
