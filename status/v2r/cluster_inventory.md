# V2R cluster inventory

2026-09-25T21:05:30.337513+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318698115072 available bytes; 82.22% used; 112476316 free inodes.

server1 `/home`: 318698115072 available bytes; 82.22% used; 112476316 free inodes.

server1 `/tmp`: 318698115072 available bytes; 82.22% used; 112476316 free inodes.

server1 `/var/tmp`: 318698115072 available bytes; 82.22% used; 112476316 free inodes.

server1 `/mnt/raid5`: 368609345536 available bytes; 98.31% used; 337539504 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22890008576 available bytes; 98.72% used; 110405684 free inodes.

server2 `/home`: 22890008576 available bytes; 98.72% used; 110405684 free inodes.

server2 `/tmp`: 22890008576 available bytes; 98.72% used; 110405684 free inodes.

server2 `/var/tmp`: 22890008576 available bytes; 98.72% used; 110405684 free inodes.

server2 `/mnt/raid5`: 302261260288 available bytes; 97.91% used; 445056019 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84366708736 available bytes; 95.29% used; 114152624 free inodes.

server3 `/home`: 84366708736 available bytes; 95.29% used; 114152624 free inodes.

server3 `/data`: 126046646272 available bytes; 98.26% used; 225807420 free inodes.

server3 `/tmp`: 84366708736 available bytes; 95.29% used; 114152624 free inodes.

server3 `/var/tmp`: 84366708736 available bytes; 95.29% used; 114152624 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105447657472 available bytes; 94.12% used; 114347376 free inodes.

server4 `/home`: 105447657472 available bytes; 94.12% used; 114347376 free inodes.

server4 `/data`: 218521157632 available bytes; 96.98% used; 224921618 free inodes.

server4 `/tmp`: 105447657472 available bytes; 94.12% used; 114347376 free inodes.

server4 `/var/tmp`: 105447657472 available bytes; 94.12% used; 114347376 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
