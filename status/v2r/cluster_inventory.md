# V2R cluster inventory

2026-09-26T02:17:12.866592+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318419005440 available bytes; 82.24% used; 112476283 free inodes.

server1 `/home`: 318419005440 available bytes; 82.24% used; 112476283 free inodes.

server1 `/tmp`: 318419005440 available bytes; 82.24% used; 112476283 free inodes.

server1 `/var/tmp`: 318419005440 available bytes; 82.24% used; 112476283 free inodes.

server1 `/mnt/raid5`: 344994930688 available bytes; 98.42% used; 337546209 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22937829376 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22937829376 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22937829376 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22937829376 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 289338445824 available bytes; 98.00% used; 445054320 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84318019584 available bytes; 95.29% used; 114152370 free inodes.

server3 `/home`: 84318019584 available bytes; 95.29% used; 114152370 free inodes.

server3 `/data`: 124790198272 available bytes; 98.28% used; 225817219 free inodes.

server3 `/tmp`: 84318019584 available bytes; 95.29% used; 114152370 free inodes.

server3 `/var/tmp`: 84318019584 available bytes; 95.29% used; 114152370 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105433288704 available bytes; 94.12% used; 114348357 free inodes.

server4 `/home`: 105433288704 available bytes; 94.12% used; 114348357 free inodes.

server4 `/data`: 130902102016 available bytes; 98.19% used; 224915760 free inodes.

server4 `/tmp`: 105433288704 available bytes; 94.12% used; 114348357 free inodes.

server4 `/var/tmp`: 105433288704 available bytes; 94.12% used; 114348357 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
