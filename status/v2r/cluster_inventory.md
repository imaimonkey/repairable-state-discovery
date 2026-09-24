# V2R cluster inventory

2026-09-24T09:52:33.573413+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324443832320 available bytes; 81.90% used; 112489606 free inodes.

server1 `/home`: 324443832320 available bytes; 81.90% used; 112489606 free inodes.

server1 `/tmp`: 324443832320 available bytes; 81.90% used; 112489606 free inodes.

server1 `/var/tmp`: 324443832320 available bytes; 81.90% used; 112489606 free inodes.

server1 `/mnt/raid5`: 500738273280 available bytes; 97.70% used; 337702304 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57757454336 available bytes; 96.78% used; 110430763 free inodes.

server2 `/home`: 57757454336 available bytes; 96.78% used; 110430763 free inodes.

server2 `/tmp`: 57757454336 available bytes; 96.78% used; 110430763 free inodes.

server2 `/var/tmp`: 57757454336 available bytes; 96.78% used; 110430763 free inodes.

server2 `/mnt/raid5`: 513917390848 available bytes; 96.45% used; 445177122 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85829722112 available bytes; 95.21% used; 114199311 free inodes.

server3 `/home`: 85829722112 available bytes; 95.21% used; 114199311 free inodes.

server3 `/data`: 165612658688 available bytes; 97.71% used; 225819759 free inodes.

server3 `/tmp`: 85829722112 available bytes; 95.21% used; 114199311 free inodes.

server3 `/var/tmp`: 85829722112 available bytes; 95.21% used; 114199311 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105748328448 available bytes; 94.10% used; 114349034 free inodes.

server4 `/home`: 105748328448 available bytes; 94.10% used; 114349034 free inodes.

server4 `/data`: 154552922112 available bytes; 97.86% used; 225273203 free inodes.

server4 `/tmp`: 105748328448 available bytes; 94.10% used; 114349034 free inodes.

server4 `/var/tmp`: 105748328448 available bytes; 94.10% used; 114349034 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
