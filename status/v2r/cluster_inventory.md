# V2R cluster inventory

2026-09-26T00:04:18.010207+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318671966208 available bytes; 82.22% used; 112476311 free inodes.

server1 `/home`: 318671966208 available bytes; 82.22% used; 112476311 free inodes.

server1 `/tmp`: 318671966208 available bytes; 82.22% used; 112476311 free inodes.

server1 `/var/tmp`: 318671966208 available bytes; 82.22% used; 112476311 free inodes.

server1 `/mnt/raid5`: 359435149312 available bytes; 98.35% used; 337538407 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22943559680 available bytes; 98.72% used; 110406226 free inodes.

server2 `/home`: 22943559680 available bytes; 98.72% used; 110406226 free inodes.

server2 `/tmp`: 22943559680 available bytes; 98.72% used; 110406226 free inodes.

server2 `/var/tmp`: 22943559680 available bytes; 98.72% used; 110406226 free inodes.

server2 `/mnt/raid5`: 296089178112 available bytes; 97.95% used; 445049727 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84347027456 available bytes; 95.29% used; 114152438 free inodes.

server3 `/home`: 84347027456 available bytes; 95.29% used; 114152438 free inodes.

server3 `/data`: 124801011712 available bytes; 98.28% used; 225810828 free inodes.

server3 `/tmp`: 84347027456 available bytes; 95.29% used; 114152438 free inodes.

server3 `/var/tmp`: 84347027456 available bytes; 95.29% used; 114152438 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105454018560 available bytes; 94.12% used; 114348398 free inodes.

server4 `/home`: 105454018560 available bytes; 94.12% used; 114348398 free inodes.

server4 `/data`: 178051506176 available bytes; 97.54% used; 224917553 free inodes.

server4 `/tmp`: 105454018560 available bytes; 94.12% used; 114348398 free inodes.

server4 `/var/tmp`: 105454018560 available bytes; 94.12% used; 114348398 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
