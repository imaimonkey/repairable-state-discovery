# V2R cluster inventory

2026-09-25T22:00:31.114144+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318694998016 available bytes; 82.22% used; 112476292 free inodes.

server1 `/home`: 318694998016 available bytes; 82.22% used; 112476292 free inodes.

server1 `/tmp`: 318694998016 available bytes; 82.22% used; 112476292 free inodes.

server1 `/var/tmp`: 318694998016 available bytes; 82.22% used; 112476292 free inodes.

server1 `/mnt/raid5`: 360310247424 available bytes; 98.35% used; 337539089 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22904504320 available bytes; 98.72% used; 110405686 free inodes.

server2 `/home`: 22904504320 available bytes; 98.72% used; 110405686 free inodes.

server2 `/tmp`: 22904504320 available bytes; 98.72% used; 110405686 free inodes.

server2 `/var/tmp`: 22904504320 available bytes; 98.72% used; 110405686 free inodes.

server2 `/mnt/raid5`: 299701252096 available bytes; 97.93% used; 445053446 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84365602816 available bytes; 95.29% used; 114152622 free inodes.

server3 `/home`: 84365602816 available bytes; 95.29% used; 114152622 free inodes.

server3 `/data`: 125882220544 available bytes; 98.26% used; 225806468 free inodes.

server3 `/tmp`: 84365602816 available bytes; 95.29% used; 114152622 free inodes.

server3 `/var/tmp`: 84365602816 available bytes; 95.29% used; 114152622 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105320906752 available bytes; 94.12% used; 114347146 free inodes.

server4 `/home`: 105320906752 available bytes; 94.12% used; 114347146 free inodes.

server4 `/data`: 208755875840 available bytes; 97.11% used; 224919086 free inodes.

server4 `/tmp`: 105320906752 available bytes; 94.12% used; 114347146 free inodes.

server4 `/var/tmp`: 105320906752 available bytes; 94.12% used; 114347146 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
