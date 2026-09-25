# V2R cluster inventory

2026-09-25T23:49:01.378387+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318672494592 available bytes; 82.22% used; 112476305 free inodes.

server1 `/home`: 318672494592 available bytes; 82.22% used; 112476305 free inodes.

server1 `/tmp`: 318672494592 available bytes; 82.22% used; 112476305 free inodes.

server1 `/var/tmp`: 318672494592 available bytes; 82.22% used; 112476305 free inodes.

server1 `/mnt/raid5`: 360068763648 available bytes; 98.35% used; 337538555 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22950526976 available bytes; 98.72% used; 110406240 free inodes.

server2 `/home`: 22950526976 available bytes; 98.72% used; 110406240 free inodes.

server2 `/tmp`: 22950526976 available bytes; 98.72% used; 110406240 free inodes.

server2 `/var/tmp`: 22950526976 available bytes; 98.72% used; 110406240 free inodes.

server2 `/mnt/raid5`: 296469778432 available bytes; 97.95% used; 445050418 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84350058496 available bytes; 95.29% used; 114152442 free inodes.

server3 `/home`: 84350058496 available bytes; 95.29% used; 114152442 free inodes.

server3 `/data`: 124800548864 available bytes; 98.28% used; 225811142 free inodes.

server3 `/tmp`: 84350058496 available bytes; 95.29% used; 114152442 free inodes.

server3 `/var/tmp`: 84350058496 available bytes; 95.29% used; 114152442 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105082568704 available bytes; 94.14% used; 114346616 free inodes.

server4 `/home`: 105082568704 available bytes; 94.14% used; 114346616 free inodes.

server4 `/data`: 178218471424 available bytes; 97.54% used; 224917594 free inodes.

server4 `/tmp`: 105082568704 available bytes; 94.14% used; 114346616 free inodes.

server4 `/var/tmp`: 105082568704 available bytes; 94.14% used; 114346616 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
