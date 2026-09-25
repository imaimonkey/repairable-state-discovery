# V2R cluster inventory

2026-09-25T21:57:27.921110+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318695583744 available bytes; 82.22% used; 112476292 free inodes.

server1 `/home`: 318695583744 available bytes; 82.22% used; 112476292 free inodes.

server1 `/tmp`: 318695583744 available bytes; 82.22% used; 112476292 free inodes.

server1 `/var/tmp`: 318695583744 available bytes; 82.22% used; 112476292 free inodes.

server1 `/mnt/raid5`: 360312229888 available bytes; 98.35% used; 337539103 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22905077760 available bytes; 98.72% used; 110405684 free inodes.

server2 `/home`: 22905077760 available bytes; 98.72% used; 110405684 free inodes.

server2 `/tmp`: 22905077760 available bytes; 98.72% used; 110405684 free inodes.

server2 `/var/tmp`: 22905077760 available bytes; 98.72% used; 110405684 free inodes.

server2 `/mnt/raid5`: 279704420352 available bytes; 98.07% used; 445053767 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84366262272 available bytes; 95.29% used; 114152622 free inodes.

server3 `/home`: 84366262272 available bytes; 95.29% used; 114152622 free inodes.

server3 `/data`: 125884686336 available bytes; 98.26% used; 225806545 free inodes.

server3 `/tmp`: 84366262272 available bytes; 95.29% used; 114152622 free inodes.

server3 `/var/tmp`: 84366262272 available bytes; 95.29% used; 114152622 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105321017344 available bytes; 94.12% used; 114347146 free inodes.

server4 `/home`: 105321017344 available bytes; 94.12% used; 114347146 free inodes.

server4 `/data`: 208822824960 available bytes; 97.11% used; 224919167 free inodes.

server4 `/tmp`: 105321017344 available bytes; 94.12% used; 114347146 free inodes.

server4 `/var/tmp`: 105321017344 available bytes; 94.12% used; 114347146 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
