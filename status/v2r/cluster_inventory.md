# V2R cluster inventory

2026-09-26T04:27:07.209362+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318408073216 available bytes; 82.24% used; 112476260 free inodes.

server1 `/home`: 318408073216 available bytes; 82.24% used; 112476260 free inodes.

server1 `/tmp`: 318408073216 available bytes; 82.24% used; 112476260 free inodes.

server1 `/var/tmp`: 318408073216 available bytes; 82.24% used; 112476260 free inodes.

server1 `/mnt/raid5`: 330525650944 available bytes; 98.48% used; 337545476 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22932619264 available bytes; 98.72% used; 110406202 free inodes.

server2 `/home`: 22932619264 available bytes; 98.72% used; 110406202 free inodes.

server2 `/tmp`: 22932619264 available bytes; 98.72% used; 110406202 free inodes.

server2 `/var/tmp`: 22932619264 available bytes; 98.72% used; 110406202 free inodes.

server2 `/mnt/raid5`: 285579358208 available bytes; 98.03% used; 445050408 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84140396544 available bytes; 95.30% used; 114148305 free inodes.

server3 `/home`: 84140396544 available bytes; 95.30% used; 114148305 free inodes.

server3 `/data`: 124588494848 available bytes; 98.28% used; 225819585 free inodes.

server3 `/tmp`: 84140396544 available bytes; 95.30% used; 114148305 free inodes.

server3 `/var/tmp`: 84140396544 available bytes; 95.30% used; 114148305 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106002526208 available bytes; 94.08% used; 114348206 free inodes.

server4 `/home`: 106002526208 available bytes; 94.08% used; 114348206 free inodes.

server4 `/data`: 107085533184 available bytes; 98.52% used; 224929406 free inodes.

server4 `/tmp`: 106002526208 available bytes; 94.08% used; 114348206 free inodes.

server4 `/var/tmp`: 106002526208 available bytes; 94.08% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
